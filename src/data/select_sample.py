"""Chọn mẫu 15-20 mã cho bộ thử P0 (task 1.1).

Chọn phân tầng theo ngành x vốn hoá x sàn, chỉ giữ mã thực sự có dữ liệu trong kho
HuggingFace ở CẢ hai mốc thời gian (một năm xa, một năm gần). Thuật toán tất định:
chạy lại cho ra đúng kết quả cũ, không dùng random.

Đầu vào : config/sample_universe.csv, data/meta/repo_files.json (hf_explore.py tạo)
Đầu ra  : data/sample/tickers.csv

Chạy:
    python src/data/select_sample.py
    python src/data/select_sample.py --n 20 --explain
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

UNIVERSE = Path("config/sample_universe.csv")
REPO_FILES = Path("data/meta/repo_files.json")
OUT = Path("data/sample/tickers.csv")

# Hai mốc thời gian: năm xa để thấy mẫu biểu cũ + OCR kém hơn, năm gần để thấy hiện trạng.
FAR_YEARS = ["2017", "2018", "2016", "2015"]   # thứ tự ưu tiên
NEAR_YEARS = ["2024", "2023", "2025"]

# Hạn ngạch ngành, tổng = 20 (spec P0-1 mục 3)
SECTOR_QUOTA = {
    "manufacturing": 4,
    "retail_consumer": 3,
    "real_estate": 3,
    "construction_materials": 2,
    "utilities_energy": 2,
    "logistics": 2,
    "bank": 2,
    "securities": 1,
    "agri_fishery": 1,
}

# Ràng buộc tối thiểu, kiểm tra sau khi chọn
MIN_CAP = {"large": 6, "mid": 7, "small": 5}
MIN_HNX = 4


def load_universe() -> list[dict]:
    rows = []
    with UNIVERSE.open(encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            rows = list(csv.DictReader([line] + fh.readlines()))
            break
    return rows


def coverage_index() -> dict[str, dict[str, list[str]]]:
    """Gom file OCR theo mã -> năm -> danh sách thư mục báo cáo."""
    files = json.loads(REPO_FILES.read_text(encoding="utf-8"))
    idx: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for f in files:
        if not f.startswith("ocr_results/"):
            continue
        parts = f.split("/")
        if len(parts) < 5:
            continue
        idx[parts[1]][parts[2]].append(parts[3])
    return {t: dict(y) for t, y in idx.items()}


def pick_year(available: list[str], preference: list[str]) -> str | None:
    for y in preference:
        if y in available:
            return y
    return None


def select(universe: list[dict], cov: dict, n_target: int, explain: bool) -> list[dict]:
    # Bước 1: loại mã không đủ dữ liệu ở cả hai mốc
    eligible: list[dict] = []
    for row in universe:
        t = row["ticker"]
        years = sorted(cov.get(t, {}))
        if not years:
            if explain:
                print(f"  loại {t}: không có trong kho")
            continue
        far = pick_year(years, FAR_YEARS)
        near = pick_year(years, NEAR_YEARS)
        if not far or not near:
            if explain:
                print(f"  loại {t}: thiếu mốc (xa={far}, gần={near}, có {len(years)} năm)")
            continue
        eligible.append({**row, "far_year": far, "near_year": near, "n_years": len(years)})

    # Bước 2: điền theo hạn ngạch ngành, ưu tiên ứng viên bù được ràng buộc còn thiếu
    by_sector: dict[str, list[dict]] = defaultdict(list)
    for r in eligible:
        by_sector[r["sector"]].append(r)

    chosen: list[dict] = []
    cap_count = {k: 0 for k in MIN_CAP}
    hnx_count = 0

    def score(cand: dict) -> tuple:
        remaining = n_target - len(chosen)
        cap_deficit = max(0, MIN_CAP[cand["cap_tier"]] - cap_count[cand["cap_tier"]])
        hnx_deficit = max(0, MIN_HNX - hnx_count)
        s = 0
        # càng gấp (thiếu nhiều so với số suất còn lại) thì điểm càng cao
        if cap_deficit:
            s += 3 if cap_deficit >= remaining / 3 else 1
        if cand["exchange"] == "HNX" and hnx_deficit:
            s += 3 if hnx_deficit >= remaining / 4 else 1
        return (s, cand["n_years"], cand["ticker"])   # tie-break tất định

    for sector, quota in SECTOR_QUOTA.items():
        pool = list(by_sector.get(sector, []))
        if len(pool) < quota:
            print(f"  ! ngành {sector}: chỉ có {len(pool)} ứng viên đủ điều kiện / cần {quota}")
        for _ in range(min(quota, len(pool))):
            pool.sort(key=score, reverse=True)
            best = pool.pop(0)
            chosen.append(best)
            cap_count[best["cap_tier"]] += 1
            hnx_count += 1 if best["exchange"] == "HNX" else 0

    return chosen


def check(chosen: list[dict]) -> None:
    cap = defaultdict(int)
    ex = defaultdict(int)
    fin = 0
    for r in chosen:
        cap[r["cap_tier"]] += 1
        ex[r["exchange"]] += 1
        fin += r["is_financial"].strip().lower() == "true"

    print(f"\nĐã chọn {len(chosen)} mã")
    print("  vốn hoá:", dict(cap), "| yêu cầu tối thiểu:", MIN_CAP)
    print("  sàn    :", dict(ex), f"| yêu cầu HNX >= {MIN_HNX}")
    print(f"  nhóm tài chính (ngân hàng/CK/BH): {fin}")

    problems = [f"{k}={cap[k]} < {v}" for k, v in MIN_CAP.items() if cap[k] < v]
    if ex["HNX"] < MIN_HNX:
        problems.append(f"HNX={ex['HNX']} < {MIN_HNX}")
    if problems:
        print("  ! CHƯA THOẢ:", "; ".join(problems))
        print("    -> bổ sung ứng viên vào config/sample_universe.csv rồi chạy lại,")
        print("       hoặc chỉnh SECTOR_QUOTA nếu quyết định đổi cơ cấu mẫu.")
    else:
        print("  -> thoả toàn bộ ràng buộc phân tầng")


def write(chosen: list[dict]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    cols = ["ticker", "exchange", "sector", "cap_tier", "years", "is_financial",
            "ocr_quality", "n_years_available", "reason"]
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in sorted(chosen, key=lambda x: (x["sector"], x["ticker"])):
            w.writerow({
                "ticker": r["ticker"],
                "exchange": r["exchange"],
                "sector": r["sector"],
                "cap_tier": r["cap_tier"],
                "years": f'{r["far_year"]},{r["near_year"]}',
                "is_financial": r["is_financial"],
                "ocr_quality": "",           # điền sau khi tải, xem download_sample.py --report
                "n_years_available": r["n_years"],
                "reason": r["note"],
            })
    print(f"\nĐã ghi {OUT}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=sum(SECTOR_QUOTA.values()))
    ap.add_argument("--explain", action="store_true", help="in lý do loại từng mã")
    args = ap.parse_args()

    if not REPO_FILES.exists():
        sys.exit("Chưa có data/meta/repo_files.json — chạy src/data/hf_explore.py trước.")

    universe = load_universe()
    cov = coverage_index()
    print(f"Pool ứng viên: {len(universe)} mã | kho có {len(cov)} mã")

    chosen = select(universe, cov, args.n, args.explain)
    check(chosen)
    write(chosen)

    print("\nMẫu đã chọn:")
    for r in sorted(chosen, key=lambda x: (x["sector"], x["ticker"])):
        fin = " [TC]" if r["is_financial"].strip().lower() == "true" else ""
        print(f"  {r['ticker']:5s} {r['exchange']:5s} {r['sector']:24s} "
              f"{r['cap_tier']:6s} {r['far_year']}+{r['near_year']}{fin}")


if __name__ == "__main__":
    main()
