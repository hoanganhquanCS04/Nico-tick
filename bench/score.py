"""Chấm output thô và dựng bảng benchmark (việc 2.5 + chuẩn bị 2.6, spec P0-2).

Đọc bench/raw/<model>__seed<k>.jsonl, chạy validator v0 trên raw_output (không tin phần parse
lúc chạy), rồi tổng hợp.

Phạm vi khử trùng (C3): trong cùng một lượt chạy (mô hình x seed), duyệt prompt theo đúng thứ tự
của eval/prompts.jsonl để kết quả không phụ thuộc thứ tự chạy thực tế. Với prompt F3, công thức
chép lại ví dụ mẫu cũng tính là trùng.

Đầu ra:
    bench/results.csv     một dòng / (mô hình, seed) + dòng tổng hợp / mô hình
    bench/table.md        bảng cho tờ trình + bảng phụ (theo họ, theo nhóm ngành, lỗi hay gặp)
    bench/formulas.csv    toàn bộ công thức đã chấm - để soi và lấy mẫu chấm tay
    eval/c4_blind.csv     (--c4-sample) 20 công thức hợp lệ / mô hình, GIẤU tên mô hình (việc 2.6)
    eval/c4_key.csv       khoá giải mã, không mở khi đang chấm

Chạy:
    python bench/score.py
    python bench/score.py --raw D:/hf_cache/bench_smoke --c4-sample
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import random
import re
import statistics as st
import sys
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from validator import Validator, canonical, extract_json, reason_kind  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VARIABLES = Path("config/variables.yaml")
PROMPTS = Path("eval/prompts.jsonl")
MODELS = Path(__file__).parent / "models.yaml"
RAW_NAME = re.compile(r"^(?P<model>.+)__seed(?P<seed>\d+)\.jsonl$")


def load_raw(raw_dir: Path) -> dict[tuple[str, int], dict[str, dict]]:
    runs: dict[tuple[str, int], dict[str, dict]] = {}
    for path in sorted(raw_dir.glob("*__seed*.jsonl")):
        m = RAW_NAME.match(path.name)
        recs = {}
        for ln in path.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                continue
            recs[r["prompt_id"]] = r                   # chạy lại -> giữ bản mới nhất
        runs[(m["model"], int(m["seed"]))] = recs
    return runs


def load_meta(raw_dir: Path) -> dict[str, dict]:
    return {p.name.split("__meta")[0]: json.loads(p.read_text(encoding="utf-8"))
            for p in raw_dir.glob("*__meta.json")}


def score_run(recs: dict[str, dict], prompts: list[dict], validator: Validator) -> tuple[list[dict], list[dict]]:
    """Trả (dòng theo lượt gọi, dòng theo công thức)."""
    seen: set[str] = set()
    calls, formulas = [], []
    for p in prompts:
        r = recs.get(p["id"])
        if r is None:
            continue
        items, err = (None, r.get("error")) if r.get("error") else extract_json(r.get("raw_output", ""))
        shots = {canonical(ast.parse(s["formula"], mode="eval")) for s in p.get("fewshot", [])}
        allowed = set(p["allowed_vars"])
        results, src_types = [], []
        for i, obj in enumerate(items or []):
            res = validator.check(obj, seen | shots, allowed)
            if res["canonical"] in shots and "duplicate" in res["reasons"]:
                res["reasons"] = [x if x != "duplicate" else "copied_fewshot" for x in res["reasons"]]
            if res["canonical"] and not {"syntax_error", "missing_field:formula"} & set(res["reasons"]):
                seen.add(res["canonical"])
            results.append(res)
            src = obj.get("source") if isinstance(obj, dict) else None
            src_type = src.get("type") if isinstance(src, dict) else None
            ref = str(src.get("ref", "")) if isinstance(src, dict) else ""
            src_types.append(src_type)
            formulas.append({
                "prompt_id": p["id"], "family": p["family"], "pair_id": p["pair_id"],
                "is_financial": p["is_financial"], "idx": i,
                "name": obj.get("name") if isinstance(obj, dict) else None,
                "formula": obj.get("formula") if isinstance(obj, dict) else None,
                "rationale": obj.get("rationale") if isinstance(obj, dict) else None,
                "source_type": src_type, "source_ref": ref,
                "quote_found": bool(ref) and src_type == "note" and _norm(ref) in _norm(p.get("context", "")),
                "valid": res["valid"], "reasons": "|".join(res["reasons"]),
                "warnings": "|".join(res["warnings"]), "canonical": res["canonical"],
                "depth": res["depth"], "n_vars": res["n_vars"],
            })
        used_vars = {v for res in results for v in (res["vars"] or [])}
        calls.append({
            "prompt_id": p["id"], "family": p["family"], "is_financial": p["is_financial"],
            "error": r.get("error"), "json_ok": items is not None, "json_error": err,
            "n_formulas": len(items or []), "count_ok": len(items or []) == p["n_formulas"],
            "n_valid": sum(x["valid"] for x in results),
            "must_ok": set(p["must_reference"]) <= used_vars,
            "note_used": "note" in src_types,
            "hit_max_tokens": r.get("hit_max_tokens"), "n_prompt_tokens": r.get("n_prompt_tokens"),
            "n_gen_tokens": r.get("n_gen_tokens") or 0, "latency_s": r.get("latency_s") or 0.0,
            "vram_torch_peak_mb": r.get("vram_torch_peak_mb"), "vram_nvml_peak_mb": r.get("vram_nvml_peak_mb"),
        })
    return calls, formulas


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def summarize(calls: list[dict], formulas: list[dict]) -> dict:
    n_calls = len(calls)
    n_f = len(formulas)
    n_valid = sum(f["valid"] for f in formulas)
    c1c2 = [f for f in formulas if f["canonical"] and not (set(f["reasons"].split("|")) - {"", "duplicate", "copied_fewshot"})]
    uniq = len({f["canonical"] for f in c1c2})
    gen_tok = sum(c["n_gen_tokens"] for c in calls)
    lat = sum(c["latency_s"] for c in calls)
    return {
        "n_calls": n_calls,
        "n_errors": sum(bool(c["error"]) for c in calls),
        "json_rate": _ratio(sum(c["json_ok"] for c in calls), n_calls),
        "count_ok_rate": _ratio(sum(c["count_ok"] for c in calls), n_calls),
        "n_formulas": n_f,
        "valid_rate": _ratio(n_valid, n_f),
        "dup_rate": _ratio(len(c1c2) - uniq, len(c1c2)),
        "must_ok_rate": _ratio(sum(c["must_ok"] for c in calls), n_calls),
        "truncated_rate": _ratio(sum(bool(c["hit_max_tokens"]) for c in calls), n_calls),
        "tok_per_s": round(gen_tok / lat, 2) if lat else None,
        "s_per_valid": round(lat / n_valid, 2) if n_valid else None,
        "vram_nvml_peak_mb": max((c["vram_nvml_peak_mb"] or 0 for c in calls), default=None),
        "vram_torch_peak_mb": max((c["vram_torch_peak_mb"] or 0 for c in calls), default=None),
        "prompt_tokens_max": max((c["n_prompt_tokens"] or 0 for c in calls), default=None),
    }


def _ratio(a: int, b: int) -> float | None:
    return round(a / b, 4) if b else None


def pct(x: float | None) -> str:
    return "-" if x is None else f"{100 * x:.1f}"


def spread(values: list[float]) -> str:
    vals = [v for v in values if v is not None]
    if not vals:
        return "-"
    if len(vals) == 1:
        return f"{100 * vals[0]:.1f}"
    return f"{100 * st.mean(vals):.1f} ± {100 * st.stdev(vals):.1f}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="bench/raw")
    ap.add_argument("--out", default="bench")
    ap.add_argument("--c4-sample", action="store_true", help="xuất mẫu chấm tay mù (việc 2.6)")
    ap.add_argument("--c4-n", type=int, default=20)
    args = ap.parse_args()

    raw_dir, out_dir = Path(args.raw), Path(args.out)
    catalog = {v["name"] for v in yaml.safe_load(VARIABLES.read_text(encoding="utf-8"))["variables"]}
    prompts = [json.loads(ln) for ln in PROMPTS.read_text(encoding="utf-8").splitlines() if ln.strip()]
    models_doc = yaml.safe_load(MODELS.read_text(encoding="utf-8"))
    info = {m["key"]: m for m in models_doc["models"]}
    runs, meta = load_raw(raw_dir), load_meta(raw_dir)
    if not runs:
        sys.exit(f"Không có file *__seed*.jsonl trong {raw_dir}")
    validator = Validator(catalog)

    per_run: dict[tuple[str, int], tuple[list, list]] = {k: score_run(v, prompts, validator) for k, v in runs.items()}
    models = sorted({m for m, _ in per_run}, key=lambda k: (info.get(k.split("+")[0], {}).get("slot", 9), k))

    # ---------------------------------------------------------------- results.csv
    rows = []
    for (model, seed), (calls, forms) in sorted(per_run.items()):
        rows.append({"model": model, "seed": seed, **summarize(calls, forms)})
    for model in models:
        calls = [c for (m, _), (cs, _) in per_run.items() if m == model for c in cs]
        forms = [f for (m, _), (_, fs) in per_run.items() if m == model for f in fs]
        rows.append({"model": model, "seed": "all", **summarize(calls, forms)})
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "results.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ---------------------------------------------------------------- formulas.csv
    all_forms = [{"model": m, "seed": s, **f} for (m, s), (_, fs) in sorted(per_run.items()) for f in fs]
    if all_forms:
        with (out_dir / "formulas.csv").open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(all_forms[0].keys()))
            w.writeheader()
            w.writerows(all_forms)

    # ---------------------------------------------------------------- table.md
    def agg(model: str) -> dict:
        return next(r for r in rows if r["model"] == model and r["seed"] == "all")

    def seed_vals(model: str, field: str) -> list:
        return [r[field] for r in rows if r["model"] == model and r["seed"] != "all"]

    def subset(model: str, pred) -> dict:
        calls = [c for (m, _), (cs, _) in per_run.items() if m == model for c in cs if pred(c)]
        forms = [f for (m, _), (_, fs) in per_run.items() if m == model for f in fs if pred(f)]
        return summarize(calls, forms)

    L = ["# Kết quả benchmark P0", "",
         f"Sinh bởi `bench/score.py` từ `{raw_dir.as_posix()}`. Định nghĩa chỉ số: `bench/README.md`.", "",
         "## Bảng chính (đưa vào tờ trình)", "",
         "| Mô hình | Tham số | VRAM đỉnh card (MB) | VRAM torch (MB) | tok/s | s/công thức hợp lệ "
         "| Hợp lệ (%) | Trùng (%) | JSON (%) | Seed | Lượt |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for model in models:
        a, base = agg(model), info.get(model.split("+")[0], {})
        me = meta.get(model, {})
        idle = me.get("vram_idle_mb")
        vram = a["vram_nvml_peak_mb"]
        vram_txt = f"{vram:.0f}" + (f" (nền {idle:.0f})" if idle and idle > 300 else "") if vram else "-"
        L.append(f'| {model}{" *" if base.get("reference_only") else ""} | {base.get("params", "?")} | {vram_txt} '
                 f'| {a["vram_torch_peak_mb"] or "-"} | {a["tok_per_s"] or "-"} | {a["s_per_valid"] or "-"} '
                 f'| {spread(seed_vals(model, "valid_rate"))} | {pct(a["dup_rate"])} | {pct(a["json_rate"])} '
                 f'| {len(seed_vals(model, "valid_rate"))} | {a["n_calls"]} |')
    L += ["", "Hợp lệ = parse được theo DSL ∧ mọi biến có trong danh mục ∧ không trùng (dạng chuẩn hoá). "
          "Giá trị `a ± b` = trung bình ± độ lệch chuẩn giữa các seed. `*` = dòng tham chiếu VRAM, không chạy đủ bộ thử.",
          "", "## Theo họ prompt (tỷ lệ hợp lệ %, gộp seed)", "",
          "| Mô hình | F1 chỉ biến | F2 + thuyết minh | F3 + ví dụ | F4 ép format | F2: có dùng thuyết minh | F2: trích dẫn đúng nguyên văn |",
          "|---|---|---|---|---|---|---|"]
    for model in models:
        fam = {f: subset(model, lambda x, f=f: x["family"] == f)["valid_rate"] for f in ("F1", "F2", "F3", "F4")}
        f2_calls = [c for (m, _), (cs, _) in per_run.items() if m == model for c in cs if c["family"] == "F2"]
        f2_forms = [f for (m, _), (_, fs) in per_run.items() if m == model for f in fs
                    if f["family"] == "F2" and f["source_type"] == "note"]
        L.append(f'| {model} | ' + " | ".join(pct(fam[f]) for f in ("F1", "F2", "F3", "F4"))
                 + f' | {pct(_ratio(sum(c["note_used"] for c in f2_calls), len(f2_calls)))}'
                 + f' | {pct(_ratio(sum(f["quote_found"] for f in f2_forms), len(f2_forms)))} |')
    L += ["", "## Theo nhóm doanh nghiệp (tỷ lệ hợp lệ %)", "",
          "| Mô hình | Phi tài chính | Ngân hàng / chứng khoán | Đúng số công thức (%) | Dùng biến bắt buộc (%) | Chạm trần 512 token (%) |",
          "|---|---|---|---|---|---|"]
    for model in models:
        a = agg(model)
        L.append(f'| {model} | {pct(subset(model, lambda x: not x["is_financial"])["valid_rate"])} '
                 f'| {pct(subset(model, lambda x: x["is_financial"])["valid_rate"])} '
                 f'| {pct(a["count_ok_rate"])} | {pct(a["must_ok_rate"])} | {pct(a["truncated_rate"])} |')
    L += ["", "## Lỗi hay gặp (số công thức)", "", "| Mô hình | 5 lỗi nhiều nhất |", "|---|---|"]
    for model in models:
        cnt = Counter(reason_kind(x) for (m, _), (_, fs) in per_run.items() if m == model
                      for f in fs for x in f["reasons"].split("|") if x)
        cnt.update(c["json_error"] or c["error"] for (m, _), (cs, _) in per_run.items() if m == model
                   for c in cs if not c["json_ok"])
        L.append(f'| {model} | ' + ", ".join(f"{k} {v}" for k, v in cnt.most_common(5)) + " |")
    L += ["", "## Điều kiện đo", "", "| Mô hình | GPU | Lượng tử | dtype | Nạp (s) | VRAM sau nạp (MB) | Module đưa ra CPU | transformers | bitsandbytes |",
          "|---|---|---|---|---|---|---|---|---|"]
    for model in models:
        me = meta.get(model, {})
        cpu = "; ".join(x.split(":")[0].split(".")[-1] for x in me.get("cpu_modules", []) if "CPU" in x) or "-"
        L.append(f'| {model} | {me.get("gpu", "-")} | {me.get("quant", "-")} | {me.get("compute_dtype", "-")} '
                 f'| {me.get("load_s", "-")} | {me.get("vram_after_load_mb", "-")} | {cpu} '
                 f'| {me.get("versions", {}).get("transformers", "-")} | {me.get("versions", {}).get("bitsandbytes", "-")} |')
    (out_dir / "table.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))

    # ---------------------------------------------------------------- mẫu chấm tay mù (việc 2.6)
    if args.c4_sample:
        rng = random.Random(2026)
        blind, key = [], []
        for model in models:
            if info.get(model.split("+")[0], {}).get("reference_only"):
                continue
            pool = [f for f in all_forms if f["model"] == model and f["valid"]]
            for f in rng.sample(pool, min(args.c4_n, len(pool))):
                blind.append(f)
        rng.shuffle(blind)
        rows_b, rows_k = [], []
        for i, f in enumerate(blind, start=1):
            fid = f"C{i:03d}"
            rows_b.append({"formula_id": fid, "prompt_id": f["prompt_id"], "name": f["name"],
                           "formula": f["formula"], "rationale": f["rationale"],
                           "rater": "", "c4_score": "", "comment": ""})
            rows_k.append({"formula_id": fid, "model": f["model"], "seed": f["seed"]})
        for name, data in (("c4_blind.csv", rows_b), ("c4_key.csv", rows_k)):
            if data:
                with (Path("eval") / name).open("w", encoding="utf-8", newline="") as fh:
                    w = csv.DictWriter(fh, fieldnames=list(data[0].keys()))
                    w.writeheader()
                    w.writerows(data)
        print(f"\nĐã xuất {len(rows_b)} công thức chấm mù -> eval/c4_blind.csv (khoá: eval/c4_key.csv)")


if __name__ == "__main__":
    main()
