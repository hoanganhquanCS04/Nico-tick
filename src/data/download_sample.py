"""Tải BCTC mẫu từ HuggingFace về máy (task 1.2).

Kho `tinixai/ocr_annual_financials` nặng 194GB / 36.472 file. Script này CHỈ tải đúng
các file ứng với mẫu đã chọn trong data/sample/tickers.csv — mặc định vài chục file text,
tổng dưới 100MB.

Cấu trúc kho (đã xác minh bằng hf_explore.py):
    ocr_results/<MÃ>/<NĂM>/<TÊN_BÁO_CÁO>/<TÊN_BÁO_CÁO>_extracted.txt   (5 cấp)
    pdf_files/<MÃ>/<NĂM>/<TÊN_BÁO_CÁO>.pdf                            (4 cấp)

CẢNH BÁO về đặt tên: kho có hai lối đặt tên song song.
    - Chuẩn hoá:  HPG_Baocaotaichinh_2024_Kiemtoan_Hopnhat
    - Thô, theo file gốc doanh nghiệp công bố:
          bao-cao-tai-chinh-hop-nhat-nam-2024-da-kiem-toan-1
          1.HUT_2018.3.28_b31e4fa_BCTC_HN_2017_signed
Xếp hạng theo hậu tố sẽ chọn nhầm bản công ty mẹ trong khi bản hợp nhất vẫn có.
Vì vậy phân loại bằng từ khoá trên tên đã khử dấu, không bằng hậu tố.

Mô hình nhân tố làm việc trên số liệu HỢP NHẤT, nên thứ tự ưu tiên là:
    hợp nhất > không ghi rõ (thường là DN không có công ty con) > riêng/công ty mẹ

Chạy:
    python src/data/download_sample.py --dry-run     # xem sẽ tải gì, bao nhiêu MB
    python src/data/download_sample.py               # tải text
    python src/data/download_sample.py --with-pdf 5  # tải thêm PDF gốc để đối chiếu OCR
    python src/data/download_sample.py --report      # chấm chất lượng OCR, điền vào tickers.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

from huggingface_hub import HfApi, hf_hub_download

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ID = "tinixai/ocr_annual_financials"
REPO_TYPE = "dataset"

REPO_FILES = Path("data/meta/repo_files.json")
TICKERS = Path("data/sample/tickers.csv")
RAW_DIR = Path("data/sample/raw")
MANIFEST = Path("data/sample/manifest.csv")

SAFETY_LIMIT_MB = 2000          # chặn tay trượt kéo cả kho về

# Từ khoá nhận diện loại báo cáo, xét trên tên đã khử dấu và bỏ ký tự phân cách
CONSOLIDATED = ("hopnhat", "bctchn", "bchn", "consolidated")
SEPARATE = ("congtyme", "rieng", "separate", "bctcrieng", "bctcme")
CLASS_RANK = {"consolidated": 0, "generic": 1, "separate": 2}


# ----------------------------------------------------------------------------- phân loại

def normalize(name: str) -> str:
    """Khử dấu, bỏ mọi ký tự không phải chữ/số, hạ chữ thường."""
    nfd = unicodedata.normalize("NFD", name)
    plain = "".join(c for c in nfd if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", plain.lower())


def classify_doc(doc_name: str) -> str:
    n = normalize(doc_name)
    if any(k in n for k in CONSOLIDATED):
        return "consolidated"
    if any(k in n for k in SEPARATE):
        return "separate"
    return "generic"


def txt_to_pdf(txt_path: str) -> str:
    """ocr_results/T/Y/DOC/DOC_extracted.txt -> pdf_files/T/Y/DOC.pdf"""
    p = txt_path.split("/")
    return f"pdf_files/{p[1]}/{p[2]}/{p[3]}.pdf"


# ----------------------------------------------------------------------------- chọn file

def build_index() -> dict[tuple[str, str], list[str]]:
    """(mã, năm) -> danh sách file .txt trong kho."""
    files = json.loads(REPO_FILES.read_text(encoding="utf-8"))
    idx: dict[tuple[str, str], list[str]] = defaultdict(list)
    for f in files:
        if f.startswith("ocr_results/") and f.endswith("_extracted.txt"):
            p = f.split("/")
            if len(p) == 5:
                idx[(p[1], p[2])].append(f)
    return idx


def collect_candidates(rows: list[dict], idx: dict) -> list[dict]:
    groups = []
    for row in rows:
        for year in (y.strip() for y in row["years"].split(",")):
            cands = sorted(idx.get((row["ticker"], year), []))
            if not cands:
                print(f"  ! {row['ticker']} {year}: không có file trong kho")
                continue
            groups.append({"row": row, "year": year, "candidates": cands})
    return groups


def resolve(groups: list[dict], sizes: dict[str, int]) -> list[dict]:
    """Chọn 1 file cho mỗi (mã, năm): ưu tiên hợp nhất, cùng hạng thì lấy bản dài hơn."""
    jobs = []
    for g in groups:
        ranked = sorted(
            g["candidates"],
            key=lambda p: (CLASS_RANK[classify_doc(p.split("/")[3])], -sizes.get(p, 0), p),
        )
        chosen = ranked[0]
        row = g["row"]
        jobs.append({
            "ticker": row["ticker"],
            "year": g["year"],
            "sector": row["sector"],
            "is_financial": row["is_financial"],
            "repo_path": chosen,
            "doc_name": chosen.split("/")[3],
            "doc_class": classify_doc(chosen.split("/")[3]),
            "n_candidates": len(ranked),
            "other_candidates": " | ".join(
                f'{c.split("/")[3]}[{classify_doc(c.split("/")[3])}]' for c in ranked[1:]
            ),
        })
    return jobs


# ----------------------------------------------------------------------------- chất lượng OCR

def ocr_stats(text: str) -> dict:
    n = len(text)
    letters = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)
    # dấu tiếng Việt: chữ cái tách được thành nhiều ký tự ở dạng NFD
    diacritics = sum(1 for c in text if c.isalpha() and len(unicodedata.normalize("NFD", c)) > 1)
    lines = text.splitlines()
    return {
        "n_chars": n,
        "digit_ratio": round(digits / n, 4) if n else 0.0,
        "diacritic_ratio": round(diacritics / letters, 4) if letters else 0.0,
        "replacement_chars": text.count("�"),
        "n_lines": len(lines),
        "avg_line_len": round(n / len(lines), 1) if lines else 0.0,
    }


def grade(st: dict) -> str:
    """Xếp loại thô để lọc nhanh. Vẫn phải người mở file xem lại trước khi chốt."""
    if st["n_chars"] < 10_000 or st["diacritic_ratio"] < 0.02 or st["replacement_chars"] > 50:
        return "poor"
    if st["n_chars"] < 40_000 or st["diacritic_ratio"] < 0.05 or st["digit_ratio"] < 0.05:
        return "fair"
    return "good"


# ----------------------------------------------------------------------------- tải

def fetch_sizes(api: HfApi, paths: list[str]) -> dict[str, int]:
    """Hỏi kích thước trước khi tải — vừa để ước lượng, vừa để tie-break chọn bản dài hơn."""
    sizes: dict[str, int] = {}
    uniq = sorted(set(paths))
    for i in range(0, len(uniq), 100):
        for info in api.get_paths_info(REPO_ID, uniq[i:i + 100], repo_type=REPO_TYPE):
            sizes[info.path] = getattr(info, "size", 0) or 0
    return sizes


def run(rows: list[dict], with_pdf: int, dry_run: bool) -> list[dict]:
    api = HfApi()
    groups = collect_candidates(rows, build_index())
    all_cands = [p for g in groups for p in g["candidates"]]

    print(f"Mẫu: {len(rows)} mã -> {len(groups)} kỳ báo cáo, {len(all_cands)} file ứng viên")
    sizes = fetch_sizes(api, all_cands)
    jobs = resolve(groups, sizes)

    by_class = defaultdict(int)
    for j in jobs:
        by_class[j["doc_class"]] += 1
    print("Loại báo cáo đã chọn:", dict(by_class))
    if by_class["separate"]:
        print("  ! có kỳ chỉ lấy được báo cáo riêng/công ty mẹ — ghi rõ trong phần hạn chế,")
        print("    và không trộn lẫn với số hợp nhất khi tính biến ở P1.")

    pdf_tickers = sorted({j["ticker"] for j in jobs})[:with_pdf] if with_pdf else []
    pdf_paths = [txt_to_pdf(j["repo_path"]) for j in jobs if j["ticker"] in pdf_tickers]
    if pdf_paths:
        sizes |= fetch_sizes(api, pdf_paths)

    targets = [j["repo_path"] for j in jobs] + pdf_paths
    total_mb = sum(sizes.get(t, 0) for t in targets) / 1e6
    print(f"\nSẽ tải {len(targets)} file, tổng {total_mb:.1f} MB")
    if pdf_tickers:
        print(f"  gồm PDF gốc của: {', '.join(pdf_tickers)}")

    if dry_run:
        for j in jobs:
            flag = "" if j["n_candidates"] == 1 else f"  (bỏ qua: {j['other_candidates']})"
            print(f"  {sizes.get(j['repo_path'], 0)/1e6:6.2f} MB  {j['ticker']:5s} {j['year']}"
                  f"  [{j['doc_class']:12s}] {j['doc_name']}{flag}")
        for p in pdf_paths:
            print(f"  {sizes.get(p, 0)/1e6:6.2f} MB  {p}")
        return []

    if total_mb > SAFETY_LIMIT_MB:
        sys.exit(f"DỪNG: {total_mb:.0f} MB vượt ngưỡng an toàn {SAFETY_LIMIT_MB} MB. Kiểm tra lại bộ lọc.")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []
    for i, job in enumerate(jobs, 1):
        local = hf_hub_download(repo_id=REPO_ID, repo_type=REPO_TYPE,
                                filename=job["repo_path"], local_dir=RAW_DIR)
        text = Path(local).read_text(encoding="utf-8", errors="replace")
        st = ocr_stats(text)
        rec = {**job, "local_path": Path(local).as_posix(),
               "size_bytes": sizes.get(job["repo_path"], 0), **st, "ocr_grade": grade(st),
               "pdf_path": ""}

        if job["ticker"] in pdf_tickers:
            rec["pdf_path"] = txt_to_pdf(job["repo_path"])
            hf_hub_download(repo_id=REPO_ID, repo_type=REPO_TYPE,
                            filename=rec["pdf_path"], local_dir=RAW_DIR)

        manifest.append(rec)
        print(f"  [{i:2d}/{len(jobs)}] {job['ticker']:5s} {job['year']}  "
              f"{st['n_chars']:>8,} ký tự  {rec['ocr_grade']:5s}  {job['doc_class']}")

    return manifest


def write_manifest(manifest: list[dict]) -> None:
    if not manifest:
        return
    cols = list(manifest[0].keys())
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(manifest)
    print(f"\nĐã ghi {MANIFEST} ({len(manifest)} dòng)")


def report() -> None:
    """Điền cột ocr_quality trong tickers.csv, lấy mức xấu nhất trong các kỳ của mã."""
    if not MANIFEST.exists():
        sys.exit("Chưa có manifest — chạy tải trước.")
    order = {"poor": 0, "fair": 1, "good": 2}
    worst: dict[str, str] = {}
    with MANIFEST.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            g = r["ocr_grade"]
            if r["ticker"] not in worst or order[g] < order[worst[r["ticker"]]]:
                worst[r["ticker"]] = g

    with TICKERS.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
        cols = list(rows[0].keys())
    for r in rows:
        r["ocr_quality"] = worst.get(r["ticker"], "")
    with TICKERS.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    dist: dict[str, int] = defaultdict(int)
    for g in worst.values():
        dist[g] += 1
    print(f"Đã cập nhật ocr_quality trong {TICKERS}: {dict(dist)}")
    if dist["poor"] + dist["fair"] < 3:
        print("  ! Spec P0-1 yêu cầu giữ >=3 mã OCR kém để biết mô hình gãy ở đâu.")
        print("    Hiện chưa đủ — thêm mã vốn hoá nhỏ vào config/sample_universe.csv rồi chọn lại.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="chỉ in kế hoạch tải và dung lượng")
    ap.add_argument("--with-pdf", type=int, default=0, metavar="N",
                    help="tải kèm PDF gốc của N mã đầu tiên để đối chiếu OCR")
    ap.add_argument("--report", action="store_true", help="chấm chất lượng OCR, cập nhật tickers.csv")
    args = ap.parse_args()

    if args.report:
        return report()
    if not TICKERS.exists():
        sys.exit("Chưa có data/sample/tickers.csv — chạy src/data/select_sample.py trước.")

    rows = list(csv.DictReader(TICKERS.open(encoding="utf-8")))
    manifest = run(rows, args.with_pdf, args.dry_run)
    write_manifest(manifest)
    if manifest:
        print("\nBước tiếp: python src/data/download_sample.py --report")


if __name__ == "__main__":
    main()
