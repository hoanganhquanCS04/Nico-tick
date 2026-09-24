"""Trích chỉ tiêu tài chính từ file OCR của kho HuggingFace.

File `_extracted.txt` không phải text thuần mà trộn giữa văn xuôi và bảng HTML:

    ===== PAGE 6 =====
    <table><tr><td></td><td>Mã số</td><td>Thuyết minh</td><td>31/12/2024 VND</td><td>1/1/2024 VND</td></tr>
    <tr><td>Hàng tồn kho</td><td>140</td><td>10.1</td><td>46.091.222.189.472</td><td>34.504.487.406.261</td></tr>
    ...</table>

Vì vậy trích biến theo MÃ SỐ CHỈ TIÊU, không dò khớp tên tiếng Việt - miễn nhiễm với
sai chính tả OCR.

Điểm khó: mã số va nhau giữa ba báo cáo (mã 20 = lợi nhuận gộp ở KQKD nhưng = lưu chuyển
tiền thuần từ HĐKD ở LCTT). Phải xác định bảng thuộc báo cáo nào trước. Tiêu đề báo cáo
xuất hiện nhan nhản trong văn xuôi nên không dùng làm mốc được; thay vào đó nhận diện
bằng DÒNG NEO (mã 270/440 -> cân đối, "lưu chuyển tiền thuần" -> LCTT, ...) và cho bảng
không có dòng neo kế thừa phân loại của bảng liền trước - đúng với thực tế báo cáo bị
cắt ngang trang.

Dùng như thư viện:
    from parse_statements import parse_document
    doc = parse_document(text)          # -> {"balance_sheet": {"270": {...}}, ...}

Chạy trực tiếp để soi một file:
    python src/data/parse_statements.py data/sample/raw/.../XXX_extracted.txt
"""

from __future__ import annotations

import re
import sys
import unicodedata

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TABLE_RE = re.compile(r"<table.*?</table>", re.S)
ROW_RE = re.compile(r"<tr>(.*?)</tr>", re.S)
CELL_RE = re.compile(r"<t[dh]>(.*?)</t[dh]>", re.S)
TAG_RE = re.compile(r"<[^>]+>")
PAGE_RE = re.compile(r"=====\s*PAGE\s+\d+\s*=====")

# Dòng neo nhận diện báo cáo: (báo cáo, mẫu khớp trên nhãn đã chuẩn hoá)
ANCHORS = [
    ("balance_sheet", ("tongcongtaisan", "tongcongnguonvon", "tongtaisan", "tongnguonvon")),
    ("cash_flow", ("luuchuyentienthuan", "khauhaotaisancodinh", "tienvatuongduongtiencuoiky")),
    ("income_statement", ("doanhthuthuanve", "loinhuangop", "loinhuansauthuethunhapdoanhnghiep",
                          "tongloinhuanketoantruocthue", "giavonhangban")),
]

# Mã số chỉ có ở một báo cáo duy nhất -> dùng để phân loại khi không có dòng neo
BS_ONLY_CODES = {"100", "110", "130", "140", "200", "220", "270", "300", "310", "400", "440"}


def normalize(s: str) -> str:
    """Khử dấu, bỏ ký tự không phải chữ số, hạ chữ thường."""
    nfd = unicodedata.normalize("NFD", s)
    plain = "".join(c for c in nfd if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", plain.lower())


def parse_number(raw: str) -> float | None:
    """'46.091.222.189.472' -> 46091222189472 ; '(101.069.892.341)' -> số âm."""
    s = raw.strip().replace(" ", " ")
    if not s or s in {"-", "–", "—"}:
        return None
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()").strip()
    # bỏ dấu phân cách hàng nghìn (dấu chấm kiểu Việt Nam, hoặc dấu phẩy)
    s = re.sub(r"[.,\s](?=\d{3}\b)", "", s)
    s = s.replace(" ", "")
    if not re.fullmatch(r"-?\d+(?:[.,]\d+)?", s):
        return None
    val = float(s.replace(",", "."))
    return -val if neg else val


def cells_of(row_html: str) -> list[str]:
    return [TAG_RE.sub("", c).strip() for c in CELL_RE.findall(row_html)]


def is_code(s: str) -> bool:
    return bool(re.fullmatch(r"\d{1,3}", s.strip()))


def locate_columns(rows: list[list[str]]) -> tuple[int, int | None, list[int]] | None:
    """Tìm cột mã số, cột thuyết minh và các cột giá trị.

    Ưu tiên hàng tiêu đề ('Mã số'); không có thì suy từ dữ liệu: cột nào phần lớn ô là
    số 1-3 chữ số thì là cột mã, các cột còn lại chứa số lớn là cột giá trị.
    """
    width = max((len(r) for r in rows), default=0)
    if width < 3:
        return None

    for r in rows[:4]:
        norm = [normalize(c) for c in r]
        if "maso" in norm:
            code_col = norm.index("maso")
            note_col = norm.index("thuyetminh") if "thuyetminh" in norm else None
            val_cols = [i for i in range(len(r)) if i not in {0, code_col, note_col}]
            return code_col, note_col, val_cols

    # không có tiêu đề: đoán từ dữ liệu
    code_hits = [0] * width
    num_hits = [0] * width
    for r in rows:
        for i, c in enumerate(r):
            if i >= width:
                continue
            if is_code(c):
                code_hits[i] += 1
            v = parse_number(c)
            if v is not None and abs(v) >= 1000:
                num_hits[i] += 1
    if max(code_hits[1:], default=0) < 3:
        return None
    code_col = 1 + code_hits[1:].index(max(code_hits[1:]))
    val_cols = [i for i in range(width) if i != code_col and num_hits[i] >= 3]
    if not val_cols:
        return None
    return code_col, None, val_cols


def classify_table(rows: list[list[str]], code_col: int) -> str | None:
    labels = [normalize(r[0]) for r in rows if r]
    for statement, keys in ANCHORS:
        for lab in labels:
            if any(k in lab for k in keys):
                return statement
    codes = {r[code_col].strip() for r in rows if len(r) > code_col and is_code(r[code_col])}
    if codes & BS_ONLY_CODES:
        return "balance_sheet"
    return None


def parse_document(text: str) -> dict[str, dict[str, dict]]:
    """Trả về {báo cáo: {mã số: {label, note_ref, current, previous}}}.

    Gặp mã số trùng trong cùng báo cáo thì giữ lần xuất hiện ĐẦU: bảng chính nằm trước,
    các bảng thuyết minh phía sau hay lặp lại mã số với ý nghĩa khác.
    """
    out: dict[str, dict[str, dict]] = {"balance_sheet": {}, "income_statement": {}, "cash_flow": {}}
    last_statement: str | None = None

    for tb in TABLE_RE.finditer(text):
        rows = [cells_of(r) for r in ROW_RE.findall(tb.group(0))]
        rows = [r for r in rows if r]
        if len(rows) < 3:
            continue

        cols = locate_columns(rows)
        if cols is None:
            continue
        code_col, note_col, val_cols = cols

        statement = classify_table(rows, code_col) or last_statement
        if statement is None:
            continue
        last_statement = statement

        for r in rows:
            if len(r) <= code_col or not is_code(r[code_col]):
                continue
            code = r[code_col].strip().lstrip("0") or "0"
            code = code.zfill(2) if len(code) < 2 else code
            if code in out[statement]:
                continue
            values = [parse_number(r[i]) for i in val_cols if i < len(r)]
            values = [v for v in values if v is not None]
            if not values:
                continue
            out[statement][code] = {
                "label": r[0],
                "note_ref": r[note_col].strip() if note_col is not None and len(r) > note_col else "",
                "current": values[0],
                "previous": values[1] if len(values) > 1 else None,
            }

    return out


def narrative_text(text: str) -> str:
    """Phần văn xuôi ngoài bảng - nguyên liệu cho prompt họ F2 và cho RAG ở P3."""
    without_tables = TABLE_RE.sub(" ", text)
    return TAG_RE.sub(" ", without_tables)


def split_pages(text: str) -> list[str]:
    parts = PAGE_RE.split(text)
    return [p for p in parts if p.strip()]


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    text = open(sys.argv[1], encoding="utf-8", errors="replace").read()
    doc = parse_document(text)
    for statement, items in doc.items():
        print(f"\n=== {statement}: {len(items)} mã số ===")
        for code in sorted(items, key=lambda c: (len(c), c)):
            it = items[code]
            cur = f'{it["current"]:,.0f}' if it["current"] is not None else "-"
            print(f'  {code:>4s}  {it["label"][:52]:52s} tm={it["note_ref"]:>5s}  {cur:>22s}')
    print(f"\nvăn xuôi ngoài bảng: {len(narrative_text(text)):,} ký tự")


if __name__ == "__main__":
    main()
