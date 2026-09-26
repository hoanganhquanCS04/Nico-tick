"""Validator v0 - kiểm tra công thức mô hình sinh ra (việc 2.3, spec P0-2 mục 4).

Bản tối giản của task #15. P4 chỉ NÂNG CẤP (thay bước 10 bằng khử trùng theo tương quan
trên dữ liệu thật), không viết lại.

Công thức "hợp lệ" = C1 ∧ C2 ∧ C3 (rubric):
    C1  parse được theo DSL    : bước 1-3, 5-9
    C2  mọi biến có trong danh mục config/variables.yaml : bước 4
    C3  không trùng công thức đã sinh (dạng chuẩn hoá)   : bước 10

Không dùng eval: parse bằng ast.parse rồi duyệt cây với danh sách node được phép.

Dùng như thư viện:
    from validator import extract_json, Validator
    formulas, err = extract_json(raw_output)
    v = Validator(catalog_names)
    res = v.check(formula_obj, seen=set_of_canonical)
"""

from __future__ import annotations

import ast
import json
import re

FUNCS = {"lag": 2, "delta": 2, "growth": 2, "mean": 2, "std": 2,
         "rank": 1, "zscore": 1, "log": 1, "abs": 1, "safe_div": 2}
TS_FUNCS = {"lag", "delta", "growth", "mean", "std"}
LAGS = {1, 2, 4, 8}
MAX_DEPTH, MAX_VARS = 6, 6
REQUIRED = ("name", "formula", "rationale", "source")

ALLOWED_NODES = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Call, ast.Name, ast.Constant, ast.Load,
                 ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)

THINK_RE = re.compile(r"<think>.*?(</think>|$)", re.S)
FENCE_RE = re.compile(r"```(?:json)?", re.I)


# ============================================================================ bước 1-2: JSON

def extract_json(raw: str) -> tuple[list | None, str | None]:
    """Lấy mảng công thức từ output thô. Trả (danh sách, None) hoặc (None, mã lỗi).

    Chấp nhận các lệch format hay gặp ở mô hình nhỏ mà không làm sai nội dung: khối <think>,
    bọc ```json, văn bản thừa trước/sau mảng, trả một object thay vì mảng.
    """
    text = FENCE_RE.sub("", THINK_RE.sub("", raw)).strip()
    start, end = text.find("["), text.rfind("]")
    if start != -1 and end > start:
        try:
            data = json.loads(text[start:end + 1])
            if isinstance(data, list):
                return data, None
        except json.JSONDecodeError:
            pass
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        try:
            data = json.loads(text[start:end + 1])
            return ([data] if isinstance(data, dict) else None), (None if isinstance(data, dict) else "json_parse_error")
        except json.JSONDecodeError:
            pass
    return None, "json_parse_error"


def extract_json_lenient(raw: str) -> tuple[list | None, str]:
    """Như extract_json, nhưng nếu hỏng thì gom mọi object có khoá 'formula' từ các giá trị JSON
    nối tiếp nhau. Dùng để tách LỖI VỎ (Qwen3.5-2B hay trả `[{..}]} [{..}]} [{..}]}`) khỏi năng lực
    viết công thức. Trả (danh sách, 'strict' | 'recovered') hoặc (None, 'fail')."""
    items, _ = extract_json(raw)
    if items is not None:
        return items, "strict"
    text = FENCE_RE.sub("", THINK_RE.sub("", raw))
    dec, out, i = json.JSONDecoder(), [], 0
    while i < len(text):
        if text[i] in "[{":
            try:
                val, j = dec.raw_decode(text, i)
            except json.JSONDecodeError:
                i += 1
                continue
            stack = [val]
            while stack:
                x = stack.pop(0)
                if isinstance(x, list):
                    stack = x + stack
                elif isinstance(x, dict) and "formula" in x:
                    out.append(x)
            i = j
            continue
        i += 1
    return (out, "recovered") if out else (None, "fail")


# ============================================================================ bước 3-10: công thức

def depth(node: ast.AST) -> int:
    kids = [c for c in ast.iter_child_nodes(node)
            if not isinstance(c, (ast.Load, ast.operator, ast.unaryop))]
    if isinstance(node, ast.Call):
        kids = list(node.args)
    return 1 + max((depth(k) for k in kids), default=0)


def canonical(node: ast.AST) -> str:
    """Dựng lại chuỗi từ AST; phép + và * được làm phẳng và sắp xếp toán hạng -> a+b == b+a."""
    if isinstance(node, ast.Expression):
        return canonical(node.body)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Constant):
        v = node.value
        return str(int(v)) if isinstance(v, float) and v.is_integer() else str(v)
    if isinstance(node, ast.UnaryOp):
        inner = canonical(node.operand)
        return f"-{inner}" if isinstance(node.op, ast.USub) else inner
    if isinstance(node, ast.Call):
        return f'{node.func.id}({",".join(canonical(a) for a in node.args)})'
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, (ast.Add, ast.Mult)):
            op = type(node.op)
            terms: list[str] = []

            def flatten(n: ast.AST) -> None:
                if isinstance(n, ast.BinOp) and isinstance(n.op, op):
                    flatten(n.left)
                    flatten(n.right)
                else:
                    terms.append(canonical(n))

            flatten(node)
            sym = "+" if op is ast.Add else "*"
            return "(" + sym.join(sorted(terms)) + ")"
        sym = "-" if isinstance(node.op, ast.Sub) else "/"
        return f"({canonical(node.left)}{sym}{canonical(node.right)})"
    return "?"


class Validator:
    def __init__(self, catalog: set[str]):
        self.catalog = catalog

    def check(self, obj: object, seen: set[str], allowed: set[str] | None = None) -> dict:
        """Kiểm tra một phần tử. Không tự thêm vào `seen` - người gọi quyết định phạm vi khử trùng."""
        res = {"valid": False, "reasons": [], "warnings": [], "canonical": None,
               "depth": None, "n_vars": None, "vars": []}
        if not isinstance(obj, dict):
            res["reasons"].append("not_object")
            return res
        res["reasons"] += [f"missing_field:{k}" for k in REQUIRED if k not in obj]
        formula = obj.get("formula")
        if not isinstance(formula, str) or not formula.strip():
            if "missing_field:formula" not in res["reasons"]:
                res["reasons"].append("missing_field:formula")
            return res

        try:
            tree = ast.parse(formula.strip(), mode="eval")
        except SyntaxError:
            res["reasons"].append("syntax_error")
            return res
        bad = {type(n).__name__ for n in ast.walk(tree) if not isinstance(n, ALLOWED_NODES)}
        if bad:
            res["reasons"].append("syntax_error:" + ",".join(sorted(bad)))
            return res

        names: set[str] = set()
        for n in ast.walk(tree):
            if isinstance(n, ast.Call):
                fname = n.func.id if isinstance(n.func, ast.Name) else None
                if fname not in FUNCS:
                    res["reasons"].append(f"unknown_func:{fname or '?'}")
                    continue
                if n.keywords or len(n.args) != FUNCS[fname]:
                    res["reasons"].append(f"bad_arity:{fname}")
                    continue
                if fname in TS_FUNCS:
                    k = n.args[1]
                    if not (isinstance(k, ast.Constant) and isinstance(k.value, (int, float))
                            and k.value in LAGS):
                        res["reasons"].append(f"bad_lag:{fname}")
            elif isinstance(n, ast.Name):
                names.add(n.id)
            elif isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div):
                res["reasons"].append("raw_division")
        callees = {n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
        variables = sorted(names - callees)
        res["reasons"] += [f"unknown_var:{v}" for v in variables if v not in self.catalog]
        if allowed is not None:
            res["warnings"] += [f"outside_allowed:{v}" for v in variables
                                if v in self.catalog and v not in allowed]

        res["vars"] = variables
        res["n_vars"] = len(variables)
        res["depth"] = depth(tree.body)
        if res["depth"] > MAX_DEPTH or res["n_vars"] > MAX_VARS:
            res["reasons"].append("too_complex")
        if not variables:
            res["reasons"].append("constant_only")

        res["canonical"] = canonical(tree)
        if res["canonical"] in seen:
            res["reasons"].append("duplicate")

        res["reasons"] = sorted(set(res["reasons"]), key=res["reasons"].index)
        res["valid"] = not res["reasons"]
        return res


def reason_kind(reason: str) -> str:
    """'unknown_var:ebitda' -> 'unknown_var' để đếm lỗi hay gặp."""
    return reason.split(":")[0]


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    v = Validator({"net_income", "cfo", "total_assets", "inventory", "revenue"})
    seen = {"(cfo+net_income)"}
    cases = [
        "safe_div(net_income - cfo, total_assets)",
        "net_income / total_assets",
        "cfo + net_income",
        "growth(inventory, 3)",
        "safe_div(ebitda, total_assets)",
        "zscore(safe_div(delta(inventory, 4), mean(total_assets, 4)))",
        "42",
        "__import__('os')",
        "safe_div(revenue, total_assets, 1)",
    ]
    for c in cases:
        r = v.check({"name": "x", "formula": c, "rationale": "r", "source": {}}, seen)
        print(f"{c:62s} valid={r['valid']!s:5s} depth={r['depth']} {r['reasons']} {r['canonical']}")
    print(extract_json('Đây là kết quả:\n```json\n[{"name": "a", "formula": "cfo"}]\n```'))
    print(extract_json('<think>\n\n</think>\n\n{"name": "a", "formula": "cfo"}'))
    print(extract_json('[{"name": "a", "formula": "cfo"'))
