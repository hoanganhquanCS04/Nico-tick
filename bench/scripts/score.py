"""Chấm output thô và dựng bảng benchmark (việc 2.5 + chuẩn bị 2.6, spec P0-2).

Đọc bench/results/raw/<model>__seed<k>.jsonl, chạy validator v0 trên raw_output (không tin phần parse
lúc chạy), rồi tổng hợp.

Chỉ số chính là HỢP LỆ / YÊU CẦU: số công thức hợp lệ chia cho số công thức đã yêu cầu
(3 / lượt gọi). Lượt hỏng JSON tính là 0 công thức hợp lệ, không bị loại khỏi mẫu số -
nếu chia cho "số công thức đọc được" thì mô hình càng hỏng format càng được lợi.

Chấm hai lần:
    strict  : parse đúng một mảng/object JSON như yêu cầu -> đo cái pipeline nhận được thật
    lenient : cứu JSON bị vỡ vỏ (nhiều mảng nối nhau, thừa ngoặc) -> đo năng lực viết công thức,
              tách khỏi lỗi định dạng mà giải mã ràng buộc (GCD) sẽ loại bỏ

Phạm vi khử trùng (C3): trong cùng một lượt chạy (mô hình x seed), duyệt prompt theo đúng thứ tự
của eval/prompts.jsonl để kết quả không phụ thuộc thứ tự chạy thực tế. Với prompt F3, công thức
chép lại ví dụ mẫu cũng tính là trùng. Dòng gộp 3 seed lấy TRUNG BÌNH tỷ lệ trùng của từng seed
(gộp rồi mới đếm thì 3 seed sinh cùng một công thức bị tính là trùng - sai).

VRAM: bộ cấp phát của PyTorch giữ lại bộ nhớ đã dùng (không trả cho card), nên đỉnh NVML trên T4
16GB phình theo prompt dài nhất và KHÔNG phản ánh mức tối thiểu cần có. Ước tính card cần =
đỉnh torch.cuda.max_memory_allocated + phần ngữ cảnh CUDA đo lúc nạp (trung vị giữa các mô hình).

Đầu ra:
    bench/results/metrics.csv   một dòng / (mô hình, seed, cách parse) + dòng gộp
    bench/results/table.md      bảng cho tờ trình + bảng phụ
    bench/results/formulas.csv  toàn bộ công thức (parse lenient) đã chấm
    eval/c4_blind.csv           (--c4-sample) 20 công thức hợp lệ / mô hình, GIẤU tên mô hình (việc 2.6)
    eval/c4_key.csv             khoá giải mã, không mở khi đang chấm

Chạy:
    python bench/scripts/score.py
    python bench/scripts/score.py --raw D:/hf_cache/bench_smoke --c4-sample
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
from validator import Validator, canonical, extract_json, extract_json_lenient, reason_kind  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VARIABLES = Path("config/variables.yaml")
PROMPTS = Path("eval/prompts.jsonl")
MODELS = Path(__file__).parent.parent / "config" / "models.yaml"
RAW_NAME = re.compile(r"^(?P<model>.+)__seed(?P<seed>\d+)\.jsonl$")
TS_FUNCS = {"lag", "delta", "growth", "mean", "std"}
SCALE_FREE_FUNCS = {"safe_div", "growth", "rank", "zscore", "log"}
FUNC_RE = re.compile(r"[a-z_]+(?=\()")


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


def scale_free(formula: str, variables: list[str], catalog: dict[str, dict]) -> bool:
    """Công thức có chuẩn hoá quy mô (tỷ số, tăng trưởng, xếp hạng...) mới so sánh được giữa các
    công ty. `total_assets + total_liabilities` hợp lệ cú pháp nhưng chỉ là thước đo quy mô."""
    uses_vnd = any(catalog.get(v, {}).get("unit") == "VND" for v in variables)
    return bool(set(FUNC_RE.findall(formula)) & SCALE_FREE_FUNCS) or not uses_vnd


def score_run(recs: dict[str, dict], prompts: list[dict], validator: Validator,
              catalog: dict[str, dict], lenient: bool) -> tuple[list[dict], list[dict]]:
    """Trả (dòng theo lượt gọi, dòng theo công thức)."""
    seen: set[str] = set()
    calls, formulas = [], []
    for p in prompts:
        r = recs.get(p["id"])
        if r is None:
            continue
        raw = r.get("raw_output", "")
        strict_items, err = (None, r.get("error")) if r.get("error") else extract_json(raw)
        if lenient and not r.get("error"):
            items, mode = extract_json_lenient(raw)
        else:
            items, mode = strict_items, ("strict" if strict_items is not None else "fail")
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
            formula = obj.get("formula") if isinstance(obj, dict) else None
            funcs = set(FUNC_RE.findall(formula)) if isinstance(formula, str) else set()
            formulas.append({
                "prompt_id": p["id"], "family": p["family"], "pair_id": p["pair_id"],
                "is_financial": p["is_financial"], "idx": i, "parse_mode": mode,
                "name": obj.get("name") if isinstance(obj, dict) else None,
                "formula": formula,
                "rationale": obj.get("rationale") if isinstance(obj, dict) else None,
                "source_type": src_type, "source_ref": ref,
                "quote_found": bool(ref) and src_type == "note" and _norm(ref) in _norm(p.get("context", "")),
                "valid": res["valid"], "reasons": "|".join(res["reasons"]),
                "warnings": "|".join(res["warnings"]), "canonical": res["canonical"],
                "depth": res["depth"], "n_vars": res["n_vars"],
                "scale_free": res["valid"] and scale_free(formula, res["vars"], catalog),
                "uses_ts": bool(funcs & TS_FUNCS),
                "uses_note_var": any(catalog.get(v, {}).get("statement") == "notes" for v in res["vars"]),
            })
        used_vars = {v for res in results for v in (res["vars"] or [])}
        calls.append({
            "prompt_id": p["id"], "family": p["family"], "is_financial": p["is_financial"],
            "error": r.get("error"), "json_ok": strict_items is not None, "json_error": err,
            "parse_mode": mode, "n_requested": p["n_formulas"],
            "n_formulas": len(items or []), "count_ok": len(strict_items or []) == p["n_formulas"],
            "n_valid": min(sum(x["valid"] for x in results), p["n_formulas"]),
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
    n_req = sum(c["n_requested"] for c in calls)
    n_f = len(formulas)
    n_valid = sum(c["n_valid"] for c in calls)
    valid = [f for f in formulas if f["valid"]]
    c1c2 = [f for f in formulas if f["canonical"] and not (set(f["reasons"].split("|")) - {"", "duplicate", "copied_fewshot"})]
    uniq = len({f["canonical"] for f in c1c2})
    gen_tok = sum(c["n_gen_tokens"] for c in calls)
    lat = sum(c["latency_s"] for c in calls)
    return {
        "n_calls": n_calls,
        "n_errors": sum(bool(c["error"]) for c in calls),
        "json_rate": _ratio(sum(c["json_ok"] for c in calls), n_calls),
        "recovered_rate": _ratio(sum(c["parse_mode"] == "recovered" for c in calls), n_calls),
        "count_ok_rate": _ratio(sum(c["count_ok"] for c in calls), n_calls),
        "n_requested": n_req,
        "n_formulas": n_f,
        "n_valid": n_valid,
        "yield": _ratio(n_valid, n_req),
        "valid_of_parsed": _ratio(sum(f["valid"] for f in formulas), n_f),
        "usable_yield": _ratio(sum(f["scale_free"] for f in valid), n_req),
        "dup_rate": _ratio(len(c1c2) - uniq, len(c1c2)),
        "must_ok_rate": _ratio(sum(c["must_ok"] for c in calls), n_calls),
        "truncated_rate": _ratio(sum(bool(c["hit_max_tokens"]) for c in calls), n_calls),
        "tok_per_s": round(gen_tok / lat, 2) if lat else None,
        "s_per_valid": round(lat / n_valid, 1) if n_valid else None,
        "latency_mean_s": round(lat / n_calls, 1) if n_calls else None,
        "vram_nvml_peak_mb": max((c["vram_nvml_peak_mb"] or 0 for c in calls), default=None),
        "vram_torch_peak_mb": max((c["vram_torch_peak_mb"] or 0 for c in calls), default=None),
        "prompt_tokens_max": max((c["n_prompt_tokens"] or 0 for c in calls), default=None),
        # chất lượng trong số công thức hợp lệ
        "q_n_valid": len(valid),
        "q_unique_valid": len({f["canonical"] for f in valid}),
        "q_scale_free": _ratio(sum(f["scale_free"] for f in valid), len(valid)),
        "q_single_var": _ratio(sum(f["n_vars"] == 1 for f in valid), len(valid)),
        "q_uses_ts": _ratio(sum(f["uses_ts"] for f in valid), len(valid)),
        "q_uses_note_var": _ratio(sum(f["uses_note_var"] for f in valid), len(valid)),
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
    ap.add_argument("--raw", default="bench/results/raw")
    ap.add_argument("--out", default="bench/results")
    ap.add_argument("--c4-sample", action="store_true", help="xuất mẫu chấm tay mù (việc 2.6)")
    ap.add_argument("--c4-n", type=int, default=20)
    args = ap.parse_args()

    raw_dir, out_dir = Path(args.raw), Path(args.out)
    catalog = {v["name"]: v for v in yaml.safe_load(VARIABLES.read_text(encoding="utf-8"))["variables"]}
    prompts = [json.loads(ln) for ln in PROMPTS.read_text(encoding="utf-8").splitlines() if ln.strip()]
    models_doc = yaml.safe_load(MODELS.read_text(encoding="utf-8"))
    info = {m["key"]: m for m in models_doc["models"]}
    runs, meta = load_raw(raw_dir), load_meta(raw_dir)
    if not runs:
        sys.exit(f"Không có file *__seed*.jsonl trong {raw_dir}")
    validator = Validator(set(catalog))

    per = {mode: {k: score_run(v, prompts, validator, catalog, mode == "lenient") for k, v in runs.items()}
           for mode in ("strict", "lenient")}
    models = sorted({m for m, _ in runs}, key=lambda k: (info.get(k.split("+")[0], {}).get("slot", 9), k))

    def pooled(mode: str, model: str, pred=lambda x: True) -> dict:
        calls = [c for (m, _), (cs, _) in per[mode].items() if m == model for c in cs if pred(c)]
        forms = [f for (m, _), (_, fs) in per[mode].items() if m == model for f in fs if pred(f)]
        out = summarize(calls, forms)
        seeds = [summarize([c for c in cs if pred(c)], [f for f in fs if pred(f)])
                 for (m, _), (cs, fs) in per[mode].items() if m == model]
        dups = [s["dup_rate"] for s in seeds if s["dup_rate"] is not None]
        out["dup_rate"] = round(st.mean(dups), 4) if dups else None
        return out

    def seed_vals(mode: str, model: str, field: str) -> list:
        return [summarize(cs, fs)[field] for (m, _), (cs, fs) in sorted(per[mode].items()) if m == model]

    # ---------------------------------------------------------------- results.csv
    rows = []
    for mode in ("strict", "lenient"):
        for (model, seed), (calls, forms) in sorted(per[mode].items()):
            rows.append({"parse": mode, "model": model, "seed": seed, **summarize(calls, forms)})
        for model in models:
            rows.append({"parse": mode, "model": model, "seed": "all", **pooled(mode, model)})
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "metrics.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ---------------------------------------------------------------- formulas.csv (lenient)
    all_forms = [{"model": m, "seed": s, **f} for (m, s), (_, fs) in sorted(per["lenient"].items()) for f in fs]
    if all_forms:
        with (out_dir / "formulas.csv").open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(all_forms[0].keys()))
            w.writeheader()
            w.writerows(all_forms)

    # ---------------------------------------------------------------- VRAM ước tính
    ctx = [me["vram_after_load_mb"] - me["cuda_allocated_mb"] for me in meta.values()
           if me.get("vram_after_load_mb") and me.get("cuda_allocated_mb") is not None]
    ctx_mb = st.median(ctx) if ctx else 0.0

    # ---------------------------------------------------------------- table.md
    S = {m: pooled("strict", m) for m in models}
    Lx = {m: pooled("lenient", m) for m in models}
    L = ["# Kết quả benchmark P0", "",
         f"Sinh bởi `bench/scripts/score.py` từ `{raw_dir.as_posix()}`. Định nghĩa chỉ số: `bench/README.md`.", "",
         "## Bảng chính (đưa vào tờ trình)", "",
         "| Mô hình | Tham số | **Hợp lệ / yêu cầu (%)** | Nếu cứu JSON (%) | Hợp lệ & chuẩn hoá quy mô (%) "
         "| VRAM ước tính cần (MB) | s / công thức hợp lệ | tok/s | JSON đúng (%) | Trùng (%) | Lượt |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for model in models:
        s, l, base = S[model], Lx[model], info.get(model.split("+")[0], {})
        need = f'{s["vram_torch_peak_mb"] + ctx_mb:.0f}' if s["vram_torch_peak_mb"] else "-"
        L.append(f'| {model}{" *" if base.get("reference_only") else ""} | {base.get("params", "?")} '
                 f'| **{spread(seed_vals("strict", model, "yield"))}** | {pct(l["yield"])} | {pct(l["usable_yield"])} '
                 f'| {need} | {s["s_per_valid"] or "-"} | {s["tok_per_s"] or "-"} | {pct(s["json_rate"])} '
                 f'| {pct(s["dup_rate"])} | {s["n_calls"]} |')
    L += ["",
          "- **Hợp lệ / yêu cầu** = số công thức qua C1∧C2∧C3 / số công thức đã yêu cầu (3 × số lượt). "
          "Lượt hỏng JSON = 0 công thức hợp lệ. `a ± b` = trung bình ± độ lệch chuẩn giữa các seed.",
          "- **Nếu cứu JSON** = như trên nhưng gom lại công thức từ output vỡ vỏ JSON (ước lượng cận trên khi có GCD).",
          "- **Chuẩn hoá quy mô** = công thức hợp lệ có tỷ số/tăng trưởng/xếp hạng, so sánh được giữa công ty lớn và nhỏ "
          "(parse lenient).",
          f"- **VRAM ước tính cần** = đỉnh `torch.cuda.max_memory_allocated` + {ctx_mb:.0f} MB ngữ cảnh CUDA "
          "(trung vị đo lúc nạp). Không dùng đỉnh NVML: trên T4 16GB bộ cấp phát giữ lại bộ nhớ nên con số đó phình to.",
          "- **Trùng** = trung bình tỷ lệ trùng của từng seed. `*` = dòng tham chiếu, chỉ chạy 10 prompt × 1 seed.",
          "", "## Theo họ prompt (hợp lệ / yêu cầu %, strict · cứu JSON)", "",
          "| Mô hình | F1 chỉ biến | F2 + thuyết minh | F3 + ví dụ | F4 ép format | F2: có công thức lấy từ thuyết minh | F2: trích dẫn đúng nguyên văn |",
          "|---|---|---|---|---|---|---|"]
    for model in models:
        cells = []
        for f in ("F1", "F2", "F3", "F4"):
            a = pooled("strict", model, lambda x, f=f: x["family"] == f)["yield"]
            b = pooled("lenient", model, lambda x, f=f: x["family"] == f)["yield"]
            cells.append(f"{pct(a)} · {pct(b)}")
        f2_calls = [c for (m, _), (cs, _) in per["lenient"].items() if m == model for c in cs if c["family"] == "F2"]
        f2_notes = [f for (m, _), (_, fs) in per["lenient"].items() if m == model for f in fs
                    if f["family"] == "F2" and f["source_type"] == "note"]
        L.append(f'| {model} | ' + " | ".join(cells)
                 + f' | {pct(_ratio(sum(c["note_used"] for c in f2_calls), len(f2_calls)))}'
                 + f' | {pct(_ratio(sum(f["quote_found"] for f in f2_notes), len(f2_notes)))} |')
    L += ["", "## Theo nhóm doanh nghiệp và tuân thủ yêu cầu (strict)", "",
          "| Mô hình | Phi tài chính (%) | Ngân hàng / chứng khoán (%) | Đúng 3 công thức (%) | Dùng biến bắt buộc (%, cứu JSON) | Chạm trần 512 token (%) | Độ trễ TB / lượt (s) |",
          "|---|---|---|---|---|---|---|"]
    for model in models:
        s = S[model]
        L.append(f'| {model} | {pct(pooled("strict", model, lambda x: not x["is_financial"])["yield"])} '
                 f'| {pct(pooled("strict", model, lambda x: x["is_financial"])["yield"])} '
                 f'| {pct(s["count_ok_rate"])} | {pct(pooled("lenient", model)["must_ok_rate"])} '
                 f'| {pct(s["truncated_rate"])} | {s["latency_mean_s"]} |')
    L += ["", "## Chất lượng trong số công thức hợp lệ (cứu JSON)", "",
          "| Mô hình | Số hợp lệ | Khác nhau (3 seed gộp) | Chuẩn hoá quy mô (%) | Chỉ 1 biến (%) | Có hàm chuỗi thời gian (%) | Dùng biến thuyết minh (%) |",
          "|---|---|---|---|---|---|---|"]
    for model in models:
        l = Lx[model]
        L.append(f'| {model} | {l["q_n_valid"]} | {l["q_unique_valid"]} | {pct(l["q_scale_free"])} | {pct(l["q_single_var"])} '
                 f'| {pct(l["q_uses_ts"])} | {pct(l["q_uses_note_var"])} |')
    L += ["", "## Lỗi hay gặp", "", "| Mô hình | Lượt hỏng JSON (strict) | Cứu được | 6 lỗi công thức nhiều nhất (cứu JSON) |",
          "|---|---|---|---|"]
    for model in models:
        cnt = Counter(x if x.split(":")[0] in ("bad_arity", "unknown_func") else reason_kind(x)
                      for (m, _), (_, fs) in per["lenient"].items() if m == model
                      for f in fs for x in f["reasons"].split("|") if x)
        s = S[model]
        L.append(f'| {model} | {s["n_calls"] - round((s["json_rate"] or 0) * s["n_calls"])} '
                 f'| {round((Lx[model]["recovered_rate"] or 0) * s["n_calls"])} | '
                 + ", ".join(f"{k} {v}" for k, v in cnt.most_common(6)) + " |")
    L += ["", "## Điều kiện đo", "",
          "| Mô hình | GPU | Lượng tử | dtype | Nạp (s) | torch sau nạp (MB) | Đỉnh torch (MB) | Đỉnh NVML (MB, tham khảo) | Module đưa ra CPU | transformers | bitsandbytes |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for model in models:
        me, s = meta.get(model, {}), S[model]
        cpu = "; ".join(x.split(":")[0].split(".")[-1] for x in me.get("cpu_modules", []) if "CPU" in x) or "-"
        L.append(f'| {model} | {me.get("gpu", "-")} | {me.get("quant", "-")} | {me.get("compute_dtype", "-")} '
                 f'| {me.get("load_s", "-")} | {me.get("cuda_allocated_mb", "-")} | {s["vram_torch_peak_mb"]} '
                 f'| {s["vram_nvml_peak_mb"]} | {cpu} '
                 f'| {me.get("versions", {}).get("transformers", "-")} | {me.get("versions", {}).get("bitsandbytes", "-")} |')
    (out_dir / "table.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))

    # ---------------------------------------------------------------- mẫu chấm tay mù (việc 2.6)
    if args.c4_sample:
        rng = random.Random(2026)
        blind = []
        for model in models:
            if info.get(model.split("+")[0], {}).get("reference_only"):
                continue
            pool = [f for f in all_forms if f["model"] == model and f["valid"]]
            blind += rng.sample(pool, min(args.c4_n, len(pool)))
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
