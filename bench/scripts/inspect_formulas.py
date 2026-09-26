"""Soi công thức một mô hình đã sinh: phân loại, gắn họ nhân tố, bắt lỗi ngữ nghĩa, xuất file đọc được.

validator.py chỉ trả lời "đúng cú pháp chưa". Script này trả lời câu tiếp theo: công thức hợp lệ
đó có NGHĨA không - trước khi người duyệt chấm C4 bằng tay.

Đọc bench/results/formulas.csv (do score.py sinh), ghi bench/results/formulas_<model>.md.

Chạy:
    python bench/scripts/inspect_formulas.py --model gemma4-e2b-plecpu
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FORMULAS = Path("bench/results/formulas.csv")
PROMPTS = Path("eval/prompts.jsonl")
VARIABLES = Path("config/variables.yaml")
TS = {"lag", "delta", "growth", "mean", "std"}
MONO = {"rank", "zscore", "abs", "log", "lag"}          # biến đổi giữ thứ tự (gần đúng)

# Họ nhân tố kinh điển, nhận diện theo biến dùng (heuristic - để định hướng, không thay chấm tay)
FAMILIES = [
    ("Chất lượng lợi nhuận (dồn tích)", lambda v, f: {"net_income", "cfo"} <= v),
    ("Định giá", lambda v, f: "market_cap" in v or "close_price" in v),
    ("Dự phòng / chất lượng tài sản", lambda v, f: bool(v & {"provision_doubtful_debt", "inventory_writedown"})),
    ("Sinh lời", lambda v, f: bool(v & {"gross_profit", "net_income", "operating_profit", "pretax_profit",
                                        "net_income_parent"}) and "safe_div" in f),
    ("Đầu tư / tăng trưởng tài sản", lambda v, f: bool(v & {"capex", "construction_in_progress", "fixed_assets",
                                                            "tangible_fixed_assets", "long_term_assets"})
                                                   or ("total_assets" in v and "growth" in f)),
    ("Đòn bẩy / thanh khoản", lambda v, f: bool(v & {"short_term_debt", "long_term_debt", "total_liabilities",
                                                     "current_liabilities", "interest_expense", "cash_and_equivalents"})),
    ("Vốn lưu động", lambda v, f: bool(v & {"receivables_customers", "short_term_receivables", "inventory",
                                            "inventory_gross", "payables_suppliers", "customer_advances",
                                            "prepaid_to_suppliers"})),
    ("Liên kết / đầu tư tài chính", lambda v, f: bool(v & {"share_of_associates", "investments_associates",
                                                           "long_term_investments", "financial_income"})),
    ("Cờ thuyết minh", lambda v, f: bool(v & {"related_party_disclosed", "audit_opinion_qualified",
                                              "going_concern_flag", "contingent_liabilities_disclosed",
                                              "segment_disclosed"})),
]


def name_of(n: ast.AST) -> str | None:
    return n.func.id if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) else None


def strip_mono(n: ast.AST) -> ast.AST:
    while isinstance(n, ast.Call) and name_of(n) in MONO and n.args:
        n = n.args[0]
    return n


def shape(tree: ast.AST, n_vars: int) -> str:
    body = tree.body
    if n_vars == 1:
        return "1 biến"
    if name_of(body) == "safe_div":
        return "tỷ số"
    if name_of(body) in TS | {"rank", "zscore", "abs", "log"} and name_of(body.args[0]) == "safe_div":
        return "biến đổi của tỷ số"
    return "tổ hợp"


def smells(tree: ast.AST, catalog: dict) -> list[str]:
    """Lỗi ngữ nghĩa mà validator không bắt."""
    out = []
    vnd = lambda n: isinstance(strip_mono(n), ast.Name) and catalog.get(strip_mono(n).id, {}).get("unit") == "VND"
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult):
            for a, b in ((n.left, n.right), (n.right, n.left)):
                # x * safe_div(y, x)  ->  rút gọn còn y
                if name_of(b) == "safe_div" and ast.dump(strip_mono(b.args[1])) == ast.dump(strip_mono(a)):
                    out.append("tự triệt tiêu (x · y/x = y)")
                # nhân với một chỉ tiêu VND trần -> điểm số phụ thuộc quy mô công ty
                if vnd(a) and not isinstance(strip_mono(b), ast.Constant):
                    out.append("nhân với quy mô công ty")
            # zscore(x) * rank(x): hai biến đổi của cùng một biến
            l, r = strip_mono(n.left), strip_mono(n.right)
            if isinstance(l, ast.Name) and isinstance(r, ast.Name) and l.id == r.id:
                out.append("lặp một biến hai lần")
        if isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Add, ast.Sub)):
            kinds = set()
            for side in (n.left, n.right):
                s = strip_mono(side)
                if isinstance(s, ast.Name) and s.id in catalog and catalog[s.id]["statement"] not in ("notes", "market"):
                    kinds.add("kỳ" if catalog[s.id]["is_flow"] else "thời điểm")
            if kinds == {"kỳ", "thời điểm"}:
                out.append("cộng/trừ chỉ tiêu kỳ với thời điểm")
        if isinstance(n, ast.Name) and catalog.get(n.id, {}).get("statement") == "notes":
            out.append("dùng cờ thuyết minh (chỉ là số lần nhắc tới)")
        # lag(1, 2), zscore(0.5): hàm áp lên hằng số - validator cho qua vì công thức vẫn có biến ở chỗ khác
        if isinstance(n, ast.Call) and n.args and isinstance(n.args[0], ast.Constant):
            out.append("hàm áp lên hằng số")
    if tree.body and name_of(tree.body) in {"lag", "abs"} and isinstance(strip_mono(tree.body), ast.Name) \
            and catalog.get(strip_mono(tree.body).id, {}).get("unit") == "VND":
        out.append("chỉ là quy mô (không chuẩn hoá)")
    return sorted(set(out))


def families(vars_: set[str], formula: str) -> list[str]:
    return [name for name, pred in FAMILIES if pred(vars_, formula)] or ["Khác"]


DIRECTION = re.compile(r"(cao|thấp|tăng|giảm|lớn|nhỏ|mạnh|yếu)", re.I)
RETURN = re.compile(r"(lợi suất|giá cổ phiếu|cổ phiếu|lợi nhuận kỳ tới|hiệu suất)", re.I)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    args = ap.parse_args()

    catalog = {v["name"]: v for v in yaml.safe_load(VARIABLES.read_text(encoding="utf-8"))["variables"]}
    prompts = {json.loads(l)["id"]: json.loads(l) for l in PROMPTS.read_text(encoding="utf-8").splitlines() if l}
    rows = [r for r in csv.DictReader(FORMULAS.open(encoding="utf-8")) if r["model"] == args.model]
    if not rows:
        sys.exit(f"Không có công thức của '{args.model}' trong {FORMULAS} - chạy bench/scripts/score.py trước.")

    valid = []
    for r in rows:
        r["theme"] = prompts[r["prompt_id"]]["theme"]
        if r["valid"] != "True":
            continue
        tree = ast.parse(r["formula"], mode="eval")
        vars_ = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)} & set(catalog)
        r["shape"] = shape(tree, int(r["n_vars"]))
        r["smells"] = smells(tree, catalog)
        r["families"] = families(vars_, r["formula"])
        r["directional"] = bool(DIRECTION.search(r["rationale"] or "") and RETURN.search(r["rationale"] or ""))
        valid.append(r)

    uniq: dict[str, list[dict]] = defaultdict(list)
    for r in valid:
        uniq[r["canonical"]].append(r)

    # ---------------------------------------------------------------- tóm tắt ra màn hình
    n = len(valid)
    clean = [r for r in valid if not r["smells"] and r["shape"] != "1 biến"]
    print(f"{args.model}: {len(rows)} công thức sinh ra, {n} hợp lệ, {len(uniq)} khác nhau")
    print("dạng:", Counter(r["shape"] for r in valid).most_common())
    print("lỗi ngữ nghĩa:", Counter(s for r in valid for s in r["smells"]).most_common())
    print(f"sạch (≥2 biến, không lỗi ngữ nghĩa): {len(clean)} ({len(clean) / n:.0%}), khác nhau {len({r['canonical'] for r in clean})}")
    print("họ nhân tố:", Counter(f for r in valid for f in r["families"]).most_common())
    print(f"rationale nêu chiều tác động tới lợi suất: {sum(r['directional'] for r in valid) / n:.0%}")
    note = [r for r in rows if r["family"] in ("F2", "F3")]
    nsrc = [r for r in note if r["source_type"] == "note"]
    print(f"F2/F3: {len(nsrc)}/{len(note)} công thức ghi nguồn là thuyết minh, trích đúng nguyên văn {sum(r['quote_found'] == 'True' for r in nsrc)}")

    # ---------------------------------------------------------------- file đọc được
    L = [f"# Công thức do `{args.model}` sinh ra", "",
         f"Sinh bởi `bench/scripts/inspect_formulas.py` từ `bench/results/formulas.csv`. Nguồn gốc: `bench/results/raw/{args.model}__seed*.jsonl`.", "",
         f"- **{len(rows)}** công thức sinh ra (76 prompt × 3 seed × ~3), **{n}** hợp lệ, **{len(uniq)}** công thức khác nhau",
         f"- Sạch (≥ 2 biến, không lỗi ngữ nghĩa): **{len(clean)}**, trong đó {len({r['canonical'] for r in clean})} khác nhau",
         "- Cột *lặp* = số lần cùng công thức (dạng chuẩn hoá) xuất hiện qua các prompt và seed", "",
         "## Công thức hợp lệ, theo chủ đề prompt", ""]
    themes = sorted({r["theme"] for r in rows})
    for t in themes:
        items = [(c, rs) for c, rs in uniq.items() if rs[0]["theme"] == t]
        if not items:
            continue
        items.sort(key=lambda x: (-len(x[1]), x[0]))
        L += [f"### {t}", "", "| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |", "|---|---|---|---|---|---|"]
        for c, rs in items:
            r = rs[0]
            why = (r["rationale"] or "").replace("|", "/").replace("\n", " ")
            L.append(f'| {len(rs)} | `{r["formula"]}` | {r["shape"]} | {", ".join(r["families"])} '
                     f'| {"; ".join(r["smells"]) or "—"} | {why[:160]} |')
        L.append("")
    L += ["## Công thức KHÔNG hợp lệ, theo lỗi", ""]
    bad = defaultdict(list)
    for r in rows:
        if r["valid"] != "True":
            bad[r["reasons"].split("|")[0].split(":")[0]].append(r)
    for reason, rs in sorted(bad.items(), key=lambda x: -len(x[1])):
        L += [f"### {reason} — {len(rs)} công thức", ""]
        for r in rs[:12]:
            L.append(f'- `{r["formula"]}` — {r["prompt_id"]} · {r["reasons"]}')
        if len(rs) > 12:
            L.append(f"- … và {len(rs) - 12} công thức khác (xem `bench/results/formulas.csv`)")
        L.append("")
    out = Path(f"bench/results/formulas_{args.model}.md")
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"\n-> {out}")


if __name__ == "__main__":
    main()
