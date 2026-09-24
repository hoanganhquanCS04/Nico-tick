"""Khảo sát cấu trúc kho dữ liệu HuggingFace trước khi tải.

Kho `tinixai/ocr_annual_financials` nặng 194GB. Đoán sai `allow_patterns` là tải nhầm
cả kho, nên bước bắt buộc trước mọi lần tải là liệt kê danh sách file và hiểu cây thư mục.

Chạy:
    python src/data/hf_explore.py                 # liệt kê, lưu cache, in tóm tắt
    python src/data/hf_explore.py --ticker HPG    # xem toàn bộ file của một mã
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from huggingface_hub import HfApi

# Console Windows mặc định cp1252, in tiếng Việt sẽ nổ UnicodeEncodeError.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ID = "tinixai/ocr_annual_financials"
REPO_TYPE = "dataset"
CACHE = Path("data/meta/repo_files.json")

YEAR_RE = re.compile(r"(?<!\d)(19|20)\d{2}(?!\d)")
TICKER_RE = re.compile(r"^[A-Z]{3}$")


def fetch_file_list(force: bool = False) -> list[str]:
    """Lấy danh sách file trong kho, cache lại để không gọi API nhiều lần."""
    if CACHE.exists() and not force:
        return json.loads(CACHE.read_text(encoding="utf-8"))

    api = HfApi()
    files = api.list_repo_files(repo_id=REPO_ID, repo_type=REPO_TYPE)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(files, ensure_ascii=False), encoding="utf-8")
    return files


def summarize(files: list[str]) -> None:
    print(f"Tổng số file: {len(files):,}")

    print("\n--- 30 đường dẫn đầu ---")
    for f in files[:30]:
        print(" ", f)

    depths = Counter(f.count("/") + 1 for f in files)
    print("\n--- Độ sâu đường dẫn ---")
    for d, n in sorted(depths.items()):
        print(f"  {d} cấp: {n:,} file")

    exts = Counter(Path(f).suffix.lower() for f in files)
    print("\n--- Phần mở rộng ---")
    for e, n in exts.most_common(15):
        print(f"  {e or '(không có)':10s} {n:,}")

    roots = Counter(f.split("/")[0] for f in files)
    print(f"\n--- Thư mục gốc ({len(roots)} mục, 20 mục nhiều file nhất) ---")
    for r, n in roots.most_common(20):
        print(f"  {r:20s} {n:,}")

    # Đoán vị trí mã chứng khoán trong đường dẫn: đoạn nào khớp 3 chữ in hoa nhiều nhất
    seg_hits: Counter[int] = Counter()
    for f in files:
        for i, seg in enumerate(f.split("/")):
            if TICKER_RE.match(seg):
                seg_hits[i] += 1
    print("\n--- Đoạn đường dẫn trông giống mã CK (3 chữ in hoa) ---")
    for i, n in seg_hits.most_common():
        print(f"  đoạn thứ {i}: {n:,} lần")

    years = Counter()
    for f in files:
        years.update(m.group(0) for m in YEAR_RE.finditer(f))
    print("\n--- Năm xuất hiện trong đường dẫn ---")
    for y, n in sorted(years.items()):
        print(f"  {y}: {n:,}")


def tickers_index(files: list[str], seg: int = 0) -> dict[str, list[str]]:
    """Gom file theo mã CK, lấy theo đoạn thứ `seg` của đường dẫn."""
    idx: dict[str, list[str]] = defaultdict(list)
    for f in files:
        parts = f.split("/")
        if len(parts) > seg and TICKER_RE.match(parts[seg]):
            idx[parts[seg]].append(f)
    return dict(idx)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="gọi lại API, bỏ cache")
    ap.add_argument("--ticker", help="in toàn bộ file của một mã")
    ap.add_argument("--seg", type=int, default=0, help="đoạn đường dẫn chứa mã CK")
    args = ap.parse_args()

    files = fetch_file_list(force=args.force)

    if args.ticker:
        idx = tickers_index(files, seg=args.seg)
        hits = idx.get(args.ticker.upper(), [])
        print(f"{args.ticker.upper()}: {len(hits)} file")
        for f in sorted(hits):
            print(" ", f)
        return

    summarize(files)
    idx = tickers_index(files, seg=args.seg)
    if idx:
        print(f"\n--- Số mã nhận diện được ở đoạn {args.seg}: {len(idx)} ---")
        sample = sorted(idx)[:20]
        print("  ví dụ:", ", ".join(sample))


if __name__ == "__main__":
    main()
