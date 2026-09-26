"""Sinh các file markdown trong docs/pm/ từ Google Sheet quản lý dự án.

Google Sheet là bản cập nhật hằng ngày (ai cũng sửa được). Các file .md ở đây là bản chụp để giữ
lịch sử trong git và để lấy làm tư liệu viết báo cáo (nhật ký quyết định, biên bản HITL...).
Đừng sửa tay các file sinh ra - sửa trên Sheet rồi chạy lại script.

Mỗi tab là một bảng, dòng 1 là tiêu đề cột. Cột tính bằng công thức (Trễ?, Điểm) được tính lại ở
đây thay vì đọc giá trị trong file, vì file xuất từ openpyxl không có giá trị đã tính.

Đầu ra:
    docs/pm/viec.md         tab Việc, nhóm theo pha, kèm bảng đếm theo người
    docs/pm/phan_cong.md    tab Phân công + Ma trận
    docs/pm/rui_ro.md       tab Rủi ro, xếp theo điểm giảm dần
    docs/pm/quyet_dinh.md   tab Quyết định, "Chờ quyết" lên đầu
    docs/pm/hop.md          tab Họp

Chạy (chỉ cần thư viện chuẩn):
    Google Sheet -> Tệp -> Tải xuống -> Microsoft Excel (.xlsx)
    python docs/pm/xlsx_to_md.py <file.xlsx>
"""

from __future__ import annotations

import argparse
import datetime as dt
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

OUT = Path(__file__).resolve().parent

M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PKG = "{http://schemas.openxmlformats.org/package/2006/relationships}"

DATE_COLS = {"Bắt đầu", "Hạn", "Hạn mới", "Ngày", "Cập nhật"}
EXCEL_EPOCH = dt.date(1899, 12, 30)
STATUS_ICON = {"Xong": "✅", "Đang làm": "🔄", "Chờ duyệt": "👀", "Kẹt": "⛔", "Cần làm": "⬜", "Huỷ": "➖"}
STATUS_ORDER = ["Cần làm", "Đang làm", "Chờ duyệt", "Kẹt", "Xong"]
TEAM = ["Quân", "Thắng", "Trung"]


# ------------------------------------------------------------------ đọc xlsx

def _text(el) -> str:
    return "" if el is None else "".join(t.text or "" for t in el.iter(M + "t"))


def _col_index(ref: str) -> int:
    n = 0
    for ch in ref:
        if not ch.isalpha():
            break
        n = n * 26 + ord(ch.upper()) - 64
    return n - 1


def read_workbook(path: Path) -> dict[str, list[list]]:
    """Trả về {tên tab: danh sách dòng}, mỗi dòng là list giá trị (str / float / None)."""
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        shared = [_text(si) for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall(M + "si")]
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels")).iter(PKG + "Relationship")}
    sheets = {}
    for s in ET.fromstring(z.read("xl/workbook.xml")).iter(M + "sheet"):
        target = rels[s.get(R + "id")].lstrip("/")
        target = target if target.startswith("xl/") else "xl/" + target
        rows = []
        for row in ET.fromstring(z.read(target)).iter(M + "row"):
            vals: dict[int, object] = {}
            for c in row.findall(M + "c"):
                t, v = c.get("t"), c.find(M + "v")
                if t == "inlineStr":
                    val = _text(c.find(M + "is"))
                elif v is None or v.text is None:
                    val = None
                elif t == "s":
                    val = shared[int(v.text)]
                elif t in ("str", "e"):
                    val = v.text
                elif t == "b":
                    val = v.text == "1"
                else:
                    val = float(v.text)
                vals[_col_index(c.get("r"))] = val
            if vals:
                rows.append([vals.get(i) for i in range(max(vals) + 1)])
        sheets[s.get("name")] = rows
    return sheets


def records(rows: list[list], key: str) -> list[dict]:
    """Dòng 1 là tiêu đề. Bỏ dòng trống ở cột `key` (dòng chỉ có công thức dựng sẵn) và dòng chỉ có
    1 ô (dòng chú thích dưới bảng)."""
    if not rows:
        return []
    header = [str(h).strip() if h is not None else "" for h in rows[0]]
    out = []
    for row in rows[1:]:
        rec = {h: (row[i] if i < len(row) else None) for i, h in enumerate(header) if h}
        if rec.get(key) in (None, "") or sum(v not in (None, "") for v in rec.values()) < 2:
            continue
        for h in DATE_COLS & rec.keys():
            if isinstance(rec[h], float):
                rec[h] = EXCEL_EPOCH + dt.timedelta(days=int(rec[h]))
        out.append(rec)
    return out


# ------------------------------------------------------------------ định dạng

def fmt(v) -> str:
    if v is None:
        return ""
    if isinstance(v, dt.date):
        return v.strftime("%d/%m")
    if isinstance(v, float):
        return str(int(v)) if v.is_integer() else f"{v:g}"
    return str(v).replace("|", "\\|").replace("\r", "").replace("\n", "<br>").strip()


def md_table(headers: list[str], rows: list[list]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    lines += ["| " + " | ".join(fmt(v) for v in r) + " |" for r in rows]
    return "\n".join(lines)


def banner(title: str, today: dt.date) -> str:
    return (f"# {title}\n\n"
            f"> Sinh tự động từ Google Sheet bằng `docs/pm/xlsx_to_md.py` ngày {today:%d/%m/%Y}. "
            f"**Đừng sửa tay** — sửa trên Sheet rồi chạy lại script.\n")


def due_of(t: dict):
    return t.get("Hạn mới") or t.get("Hạn")


def late_flag(t: dict, today: dt.date) -> str:
    """Giống cột Trễ? trên Sheet: quá hạn hiện hành -> TRỄ, còn ≤2 ngày -> Sắp hạn."""
    due = due_of(t)
    if t.get("Trạng thái") in ("Xong", "Huỷ") or not isinstance(due, dt.date):
        return ""
    if due < today:
        return "TRỄ"
    return "Sắp hạn" if (due - today).days <= 2 else ""


# ------------------------------------------------------------------ từng file

def write_viec(tasks: list[dict], today: dt.date) -> str:
    people = sorted({t.get("Phụ trách") for t in tasks} - {None, ""},
                    key=lambda p: (TEAM.index(p) if p in TEAM else len(TEAM), p))
    count_rows = []
    for p in people:
        mine = [t for t in tasks if t.get("Phụ trách") == p]
        counts = [sum(t.get("Trạng thái") == s for t in mine) for s in STATUS_ORDER]
        count_rows.append([p, *counts, sum(late_flag(t, today) == "TRỄ" for t in mine), sum(counts)])

    parts = [banner("Bảng việc", today),
             "## Theo người\n",
             md_table(["Người", *STATUS_ORDER, "Trễ", "Tổng"], count_rows), ""]

    late = [t for t in tasks if late_flag(t, today) == "TRỄ"]
    if late:
        parts += ["## ⚠️ Đang trễ\n",
                  md_table(["ID", "Việc", "Phụ trách", "Hạn"], [[t["ID"], t.get("Việc"), t.get("Phụ trách"), due_of(t)] for t in late]), ""]

    for phase in dict.fromkeys(t.get("Pha") or "Khác" for t in tasks):
        rows = []
        for t in (t for t in tasks if (t.get("Pha") or "Khác") == phase):
            due = fmt(t.get("Hạn"))
            if t.get("Hạn mới"):
                due = f"~~{due}~~ → {fmt(t['Hạn mới'])}"
            status = f"{STATUS_ICON.get(t.get('Trạng thái'), '')} {fmt(t.get('Trạng thái'))}".strip()
            flag = late_flag(t, today)
            if flag:
                status += " · ⚠️ TRỄ" if flag == "TRỄ" else " · ⏰ sắp hạn"
            rows.append([t["ID"], t.get("Việc"), t.get("Phụ trách"), t.get("Hỗ trợ"), t.get("Bắt đầu"), due,
                         status, t.get("Xong khi (đầu ra)"), t.get("Phụ thuộc"), t.get("Ghi chú")])
        parts += [f"## {phase}\n",
                  md_table(["ID", "Việc", "Phụ trách", "Hỗ trợ", "Bắt đầu", "Hạn", "Trạng thái", "Xong khi", "Phụ thuộc", "Ghi chú"], rows), ""]
    return "\n".join(parts)


def write_phan_cong(people: list[dict], matrix: list[dict], today: dt.date) -> str:
    cols_p = ["Người", "Vai chính", "Vai phụ", "Phụ trách chính (pha)", "Hỗ trợ (pha)", "Trách nhiệm cụ thể"]
    cols_m = ["Pha", "Nội dung", "Hạn", "Quân", "Thắng", "Trung", "Ghi chú"]
    return "\n".join([
        banner("Phân công", today),
        "## Ai làm gì\n",
        md_table(cols_p, [[p.get(c) for c in cols_p] for p in people]), "",
        "## Ma trận theo pha\n",
        "**Chính** = chịu trách nhiệm kết quả của pha · **Hỗ trợ** = làm một phần theo yêu cầu người Chính · "
        "**Duyệt** = xem và đồng ý đầu ra trước khi đóng pha. Ở mức từng việc, mỗi việc chỉ có 1 người phụ trách.\n",
        md_table(cols_m, [[m.get(c) for c in cols_m] for m in matrix]), "",
    ])


def write_rui_ro(risks: list[dict], today: dt.date) -> str:
    def score(r):
        try:
            return int(float(r.get("Khả năng (1–3)"))) * int(float(r.get("Ảnh hưởng (1–3)")))
        except (TypeError, ValueError):
            return 0

    def level(s):
        return "🔴" if s >= 6 else "🟡" if s >= 3 else "🟢"

    open_ = sorted((r for r in risks if r.get("Trạng thái") != "Đã đóng"), key=score, reverse=True)
    closed = [r for r in risks if r.get("Trạng thái") == "Đã đóng"]
    cols = ["ID", "Điểm", "Rủi ro", "Nhóm", "Dấu hiệu sớm", "Cách phòng", "Nếu xảy ra thì", "Người theo dõi", "Trạng thái", "Cập nhật"]
    to_row = lambda r: [r["ID"], f"{level(score(r))} {score(r)}", *[r.get(c) for c in cols[2:]]]
    parts = [banner("Sổ rủi ro", today),
             "Điểm = Khả năng × Ảnh hưởng (mỗi thứ 1–3). 🔴 ≥6: bàn mỗi buổi họp tuần · 🟡 3–5: theo dõi · 🟢 ≤2.\n",
             "## Đang mở\n", md_table(cols, [to_row(r) for r in open_]), ""]
    if closed:
        parts += ["## Đã đóng\n", md_table(cols, [to_row(r) for r in closed]), ""]
    return "\n".join(parts)


def write_quyet_dinh(decisions: list[dict], today: dt.date) -> str:
    cols = ["ID", "Ngày", "Quyết định", "Lý do", "Ai quyết", "Phương án đã bỏ", "Ảnh hưởng tới", "Nguồn"]
    parts = [banner("Nhật ký quyết định", today),
             "Đổi ý thì không xoá dòng cũ: đặt nó \"Đã thay đổi\" và thêm dòng mới.\n"]
    for status, title in [("Chờ quyết", "⏳ Chờ quyết"), ("Đã chốt", "✅ Đã chốt"), ("Đã thay đổi", "↩️ Đã thay đổi")]:
        group = [q for q in decisions if q.get("Trạng thái") == status]
        if group:
            parts += [f"## {title}\n", md_table(cols, [[q.get(c) for c in cols] for q in group]), ""]
    return "\n".join(parts)


def write_hop(meetings: list[dict], today: dt.date) -> str:
    cols = ["Ngày", "Loại", "Người dự", "Người ghi", "Đã xong từ lần trước", "Đang kẹt", "Quyết định (ID)", "Việc mới / đổi (ID)", "Ghi chú / link biên bản"]
    return "\n".join([
        banner("Nhật ký họp", today),
        "Biên bản chi tiết: [bien_ban/](bien_ban/). Mẫu biên bản: [bien_ban/_mau.md](bien_ban/_mau.md).\n",
        md_table(cols, [[m.get(c) for c in cols] for m in meetings]), "",
    ])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx", type=Path, help="file .xlsx tải về từ Google Sheet")
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today(), help="ngày dùng để tính trễ hạn (YYYY-MM-DD)")
    args = ap.parse_args()

    wb = read_workbook(args.xlsx)
    missing = {"Việc", "Phân công", "Ma trận", "Rủi ro", "Quyết định", "Họp"} - wb.keys()
    if missing:
        raise SystemExit(f"Thiếu tab: {', '.join(sorted(missing))}")

    files = {
        "viec.md": write_viec(records(wb["Việc"], "ID"), args.today),
        "phan_cong.md": write_phan_cong(records(wb["Phân công"], "Người"), records(wb["Ma trận"], "Pha"), args.today),
        "rui_ro.md": write_rui_ro(records(wb["Rủi ro"], "ID"), args.today),
        "quyet_dinh.md": write_quyet_dinh(records(wb["Quyết định"], "ID"), args.today),
        "hop.md": write_hop(records(wb["Họp"], "Ngày"), args.today),
    }
    for name, text in files.items():
        (OUT / name).write_text(text, encoding="utf-8")
        print(f"ghi {OUT / name}")


if __name__ == "__main__":
    main()
