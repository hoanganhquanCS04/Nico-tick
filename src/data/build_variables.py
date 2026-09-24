"""Chạy parser trên toàn bộ mẫu, đo độ phủ từng biến, điền lại config/variables.yaml.

Đây là bước nghiệm thu của việc 1.3 (spec P0-1): mỗi biến phải map được về >=12/20 doanh
nghiệp mẫu, nếu không thì hoặc mã số sai, hoặc biến đó không tồn tại trong mẫu biểu Việt Nam.

Đầu vào : config/variables.yaml, data/sample/manifest.csv
Đầu ra  : data/sample/extracted.json  (giá trị đã trích, nguyên liệu cho prompt)
          config/variables.yaml       (điền lại trường coverage, giữ nguyên chú thích)
          data/sample/coverage.csv    (bảng độ phủ để soi nhanh)

Chạy:
    python src/data/build_variables.py
    python src/data/build_variables.py --no-write     # chỉ in, không sửa yaml
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from parse_statements import narrative_text, parse_document   # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VARIABLES = Path("config/variables.yaml")
MANIFEST = Path("data/sample/manifest.csv")
EXTRACTED = Path("data/sample/extracted.json")
COVERAGE = Path("data/sample/coverage.csv")

MIN_COVERAGE = 12          # ngưỡng spec P0-1: >=12/20 doanh nghiệp


def load_variables() -> list[dict]:
    doc = yaml.safe_load(VARIABLES.read_text(encoding="utf-8"))
    return doc["variables"]


def extract_all(variables: list[dict]) -> dict:
    by_code = defaultdict(dict)          # statement -> code -> tên biến
    for v in variables:
        if v.get("vas_code"):
            by_code[v["statement"]][str(v["vas_code"])] = v["name"]

    text_vars = [v for v in variables if v.get("extract") == "text"]

    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8")))
    out = {}
    for r in rows:
        path = Path(r["local_path"])
        if not path.exists():                       # manifest ghi đường dẫn tương đối
            path = Path(*Path(r["local_path"]).parts)
        text = path.read_text(encoding="utf-8", errors="replace")
        doc = parse_document(text)
        narrative = narrative_text(text)
        narrative_low = narrative.lower()

        values = {}
        for statement, items in doc.items():
            for code, item in items.items():
                name = by_code[statement].get(code)
                if name:
                    values[name] = {
                        "statement": statement, "code": code, "label": item["label"],
                        "note_ref": item["note_ref"],
                        "current": item["current"], "previous": item["previous"],
                    }
        for v in text_vars:
            hits = sum(narrative_low.count(p.lower()) for p in v.get("patterns", []))
            if hits:
                values[v["name"]] = {"statement": "notes", "code": None, "label": v["vi_label"],
                                     "note_ref": "", "current": float(hits), "previous": None}

        out[f'{r["ticker"]}_{r["year"]}'] = {
            "ticker": r["ticker"], "year": r["year"], "sector": r["sector"],
            "is_financial": r["is_financial"].strip().lower() == "true",
            "doc_class": r["doc_class"], "local_path": path.as_posix(),
            "n_codes": {s: len(items) for s, items in doc.items()},
            "narrative_chars": len(narrative),
            "values": values,
        }
    return out


def coverage_report(variables: list[dict], extracted: dict) -> list[dict]:
    """Độ phủ tính theo SỐ DOANH NGHIỆP có biến ở ít nhất một năm."""
    nonfin = {d["ticker"] for d in extracted.values() if not d["is_financial"]}
    fin = {d["ticker"] for d in extracted.values() if d["is_financial"]}

    have_nonfin = defaultdict(set)
    have_fin = defaultdict(set)
    signs = defaultdict(lambda: [0, 0])          # tên biến -> [số dương, số âm]
    for d in extracted.values():
        target = have_fin if d["is_financial"] else have_nonfin
        for name, item in d["values"].items():
            target[name].add(d["ticker"])
            if item["current"] is not None and item["statement"] != "notes":
                signs[name][0 if item["current"] >= 0 else 1] += 1

    rows = []
    for v in variables:
        name = v["name"]
        pos, neg = signs[name]
        rows.append({
            "name": name,
            "statement": v["statement"],
            "vas_code": v.get("vas_code") or "",
            "declared_sign": v.get("sign", ""),
            "n_nonfinancial": len(have_nonfin[name]),
            "of_nonfinancial": len(nonfin),
            "n_financial": len(have_fin[name]),
            "of_financial": len(fin),
            "obs_positive": pos,
            "obs_negative": neg,
        })
    return rows


def write_coverage_into_yaml(rows: list[dict]) -> None:
    """Điền trường coverage bằng sửa văn bản, để không mất chú thích trong file."""
    cov = {r["name"]: f'{r["n_nonfinancial"]}/{r["of_nonfinancial"]}' for r in rows}
    lines = VARIABLES.read_text(encoding="utf-8").splitlines()

    out: list[str] = []
    current: str | None = None
    block: list[str] = []

    def flush() -> None:
        """Đẩy block của biến hiện tại ra, chèn/cập nhật dòng coverage ở cuối block."""
        if current is None:
            out.extend(block)
            return
        body = [ln for ln in block if not re.match(r"^\s{4}coverage:", ln)]
        while body and not body[-1].strip():
            body.pop()
        body.append(f"    coverage: {cov.get(current, '')}")
        out.extend(body)
        out.append("")

    for line in lines:
        m = re.match(r"^  - name:\s*(\S+)", line)
        if m:
            flush()
            current, block = m.group(1), [line]
            continue
        if current is None:
            out.append(line)
        else:
            block.append(line)
    flush()

    VARIABLES.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-write", action="store_true", help="không sửa config/variables.yaml")
    args = ap.parse_args()

    variables = load_variables()
    print(f"Danh mục: {len(variables)} biến")

    extracted = extract_all(variables)
    EXTRACTED.write_text(json.dumps(extracted, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Đã trích {len(extracted)} báo cáo -> {EXTRACTED}")

    rows = coverage_report(variables, extracted)
    with COVERAGE.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"\n{'biến':32s}{'báo cáo':16s}{'mã':>5s}  phi TC   TC   dấu quan sát")
    weak = []
    for r in rows:
        if r["statement"] == "market":
            continue
        flag = "" if r["n_nonfinancial"] >= MIN_COVERAGE else "  <-- THẤP"
        if flag:
            weak.append(r["name"])
        sign = f'+{r["obs_positive"]}/-{r["obs_negative"]}'
        print(f'  {r["name"]:30s}{r["statement"]:16s}{str(r["vas_code"]):>5s}'
              f'  {r["n_nonfinancial"]:2d}/{r["of_nonfinancial"]:<5d}'
              f'{r["n_financial"]:2d}/{r["of_financial"]:<5d}{sign:>10s}{flag}')

    # cảnh báo dấu trái với khai báo
    mismatch = [r for r in rows
                if r["declared_sign"] == "negative" and r["obs_positive"] > r["obs_negative"]]
    if mismatch:
        print("\nDấu quan sát trái với khai báo (báo cáo ghi trị tuyệt đối, không đóng ngoặc):")
        for r in mismatch:
            print(f'  {r["name"]:30s} khai báo negative nhưng +{r["obs_positive"]}/-{r["obs_negative"]}')
        print("  -> chuẩn hoá dấu ở P5 trước khi tính công thức, đừng để mô hình tự đoán.")

    n_ok = sum(1 for r in rows if r["statement"] != "market" and r["n_nonfinancial"] >= MIN_COVERAGE)
    n_total = sum(1 for r in rows if r["statement"] != "market")
    print(f"\nĐạt ngưỡng >={MIN_COVERAGE}/20: {n_ok}/{n_total} biến")
    if weak:
        print("Biến dưới ngưỡng:", ", ".join(weak))

    if not args.no_write:
        write_coverage_into_yaml(rows)
        print(f"Đã điền coverage vào {VARIABLES}")


if __name__ == "__main__":
    main()
