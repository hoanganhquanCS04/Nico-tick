"""Gộp điểm chấm tay C4 (việc 2.6): đo đồng thuận giữa người chấm, rồi mới mở khoá tên mô hình.

Mỗi người chấm một file riêng, chấm độc lập theo eval/rubric.md:
    eval/c4_scores_<tên>.csv    bản sao eval/c4_blind.csv đã điền c4_score (1-5) và comment

Công thức lệch từ 2 điểm trở lên đem ra bàn; điểm thống nhất ghi vào (tuỳ chọn)
    eval/c4_consensus.csv       formula_id,c4_score,comment
KHÔNG sửa file điểm của từng người sau khi bàn - số đồng thuận báo cáo phải là số trước khi bàn.

Điểm cuối mỗi công thức = điểm trọng tài nếu có, không thì trung bình các người chấm.
Tên mô hình (eval/c4_key.csv) chỉ được mở khi MỌI công thức đã có điểm cuối, để không lộ mô hình
giữa chừng - nếu lộ, người chấm sẽ thiên vị mô hình mình muốn chọn ở các công thức còn lại.

Đồng thuận: tỷ lệ trùng khít, tỷ lệ lệch ≤1, và kappa có trọng số bậc hai (thước đo chuẩn cho thang
thứ bậc: lệch 1 điểm bị phạt nhẹ, lệch 4 điểm bị phạt nặng; 1 = hoàn toàn khớp, 0 = khớp như đoán bừa).

Đầu ra:
    eval/manual_scores.csv      dạng dài theo spec P0-1: formula_id,model,seed,prompt_id,formula,rater,c4_score,comment
                                (rater = "final" là điểm cuối)
    bench/results/c4.md         đồng thuận + điểm C4 theo mô hình, cho tờ trình

Chạy:
    python bench/scripts/c4_merge.py --only C001-C010    # vòng hiệu chỉnh 10 mẫu đầu
    python bench/scripts/c4_merge.py                     # sau khi chấm xong
"""

from __future__ import annotations

import argparse
import csv
import itertools
import statistics as st
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EVAL = Path("eval")
BLIND = EVAL / "c4_blind.csv"
KEY = EVAL / "c4_key.csv"
CONSENSUS = EVAL / "c4_consensus.csv"
OUT_LONG = EVAL / "manual_scores.csv"
OUT_MD = Path("bench/results/c4.md")
SCALE = range(1, 6)


def read_csv(path: Path) -> list[dict]:
    """Đọc CSV từ Google Sheet hoặc Excel: có/không BOM, phân cách ',' hoặc ';'."""
    text = path.read_text(encoding="utf-8-sig")
    try:
        dialect = csv.Sniffer().sniff(text.split("\n", 1)[0], delimiters=",;")
    except csv.Error:
        dialect = csv.excel
    return [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(text.splitlines(), dialect=dialect)]


def parse_score(raw: str, where: str) -> int | None:
    if raw == "":
        return None
    try:
        s = float(raw.replace(",", "."))
    except ValueError:
        raise SystemExit(f"{where}: điểm '{raw}' không phải số")
    if not s.is_integer() or int(s) not in SCALE:
        raise SystemExit(f"{where}: điểm '{raw}' phải là số nguyên 1-5")
    return int(s)


def parse_only(spec: str | None, ids: list[str]) -> list[str]:
    if not spec:
        return ids
    lo, _, hi = spec.upper().partition("-")
    return [i for i in ids if lo <= i <= (hi or lo)]


def weighted_kappa(a: list[int], b: list[int]) -> float | None:
    n, k = len(a), len(SCALE)
    if n == 0:
        return None
    obs = [[0] * k for _ in SCALE]
    for x, y in zip(a, b):
        obs[x - 1][y - 1] += 1
    row = [sum(r) for r in obs]
    col = [sum(obs[i][j] for i in range(k)) for j in range(k)]
    w = lambda i, j: (i - j) ** 2 / (k - 1) ** 2
    o = sum(w(i, j) * obs[i][j] for i in range(k) for j in range(k))
    e = sum(w(i, j) * row[i] * col[j] / n for i in range(k) for j in range(k))
    return None if e == 0 else 1 - o / e


def agreement(scores: dict[str, dict[str, int]], ids: list[str]) -> tuple[list[dict], list[tuple]]:
    """Đồng thuận từng cặp người chấm + danh sách công thức lệch ≥2 điểm."""
    stats, gaps = [], {}
    for r1, r2 in itertools.combinations(sorted(scores), 2):
        both = [i for i in ids if i in scores[r1] and i in scores[r2]]
        a, b = [scores[r1][i] for i in both], [scores[r2][i] for i in both]
        diff = [abs(x - y) for x, y in zip(a, b)]
        stats.append({"pair": f"{r1} – {r2}", "n": len(both),
                      "exact": sum(d == 0 for d in diff) / len(both) if both else None,
                      "within1": sum(d <= 1 for d in diff) / len(both) if both else None,
                      "gap2": sum(d >= 2 for d in diff), "mad": st.mean(diff) if diff else None,
                      "kappa": weighted_kappa(a, b)})
        for i, d in zip(both, diff):
            if d >= 2:
                gaps[i] = max(gaps.get(i, 0), d)
    return stats, sorted(gaps.items())


def pct(x: float | None) -> str:
    return "-" if x is None else f"{100 * x:.0f}%"


def num(x: float | None, nd: int = 2) -> str:
    return "-" if x is None else f"{x:.{nd}f}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="chỉ xét một khoảng formula_id, ví dụ C001-C010 (vòng hiệu chỉnh)")
    args = ap.parse_args()

    blind = {r["formula_id"]: r for r in read_csv(BLIND)}
    ids = parse_only(args.only, sorted(blind))
    files = sorted(EVAL.glob("c4_scores_*.csv"))
    if len(files) < 2:
        raise SystemExit(f"Cần ít nhất 2 file eval/c4_scores_<tên>.csv, đang có {len(files)}")

    scores: dict[str, dict[str, int]] = {}
    comments: dict[tuple[str, str], str] = {}
    for f in files:
        rater = f.stem.removeprefix("c4_scores_")
        scores[rater] = {}
        for r in read_csv(f):
            fid = r.get("formula_id", "")
            if fid not in blind:
                continue
            s = parse_score(r.get("c4_score", ""), f"{f.name} {fid}")
            if s is not None:
                scores[rater][fid] = s
                comments[(rater, fid)] = r.get("comment", "")

    print(f"Xét {len(ids)} công thức ({args.only or 'tất cả'}), {len(files)} người chấm")
    for rater, sc in scores.items():
        missing = [i for i in ids if i not in sc]
        print(f"  {rater}: đã chấm {len(ids) - len(missing)}/{len(ids)}" + (f", thiếu {', '.join(missing[:10])}{' …' if len(missing) > 10 else ''}" if missing else ""))

    stats, gaps = agreement(scores, ids)
    print("\nĐồng thuận (trước khi bàn):")
    for s in stats:
        print(f"  {s['pair']}: n={s['n']}, khớp {pct(s['exact'])}, lệch ≤1 {pct(s['within1'])}, "
              f"lệch ≥2: {s['gap2']}, lệch TB {num(s['mad'])}, kappa {num(s['kappa'])}")
        if args.only and s["n"] and s["gap2"] / s["n"] > 0.3:
            print("  ⚠️  Quá 30% công thức lệch ≥2 điểm: bàn lại, làm rõ rubric rồi chấm lại vòng này.")

    consensus = {}
    if CONSENSUS.exists():
        for r in read_csv(CONSENSUS):
            s = parse_score(r.get("c4_score", ""), f"{CONSENSUS.name} {r.get('formula_id')}")
            if s is not None:
                consensus[r["formula_id"]] = (s, r.get("comment", ""))
    pending = [(i, d) for i, d in gaps if i not in consensus]
    if pending:
        print(f"\nCần bàn ({len(pending)} công thức lệch ≥2, chưa có trong {CONSENSUS.name}):")
        for i, _ in pending:
            given = ", ".join(f"{r}={scores[r][i]}" for r in sorted(scores) if i in scores[r])
            print(f"  {i}  {blind[i]['formula']}\n        {given}")

    pending_ids = {i for i, _ in pending}
    final: dict[str, float] = {}
    for i in ids:
        if i in consensus:
            final[i] = consensus[i][0]
        else:
            given = [scores[r][i] for r in scores if i in scores[r]]
            if len(given) >= 2 and i not in pending_ids:
                final[i] = st.mean(given)

    done = len(final) == len(blind) and not args.only
    if not done:
        print(f"\nĐiểm cuối: {len(final)}/{len(blind)} công thức. Chưa đủ nên CHƯA mở khoá tên mô hình.")
        return

    key = {r["formula_id"]: r for r in read_csv(KEY)}
    long_rows = []
    for i in sorted(blind):
        b, k = blind[i], key.get(i, {})
        base = {"formula_id": i, "model": k.get("model", ""), "seed": k.get("seed", ""),
                "prompt_id": b["prompt_id"], "formula": b["formula"]}
        for r in sorted(scores):
            if i in scores[r]:
                long_rows.append({**base, "rater": r, "c4_score": scores[r][i], "comment": comments.get((r, i), "")})
        long_rows.append({**base, "rater": "final", "c4_score": f"{final[i]:g}", "comment": consensus.get(i, (0, ""))[1]})
    with OUT_LONG.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(long_rows[0]))
        w.writeheader()
        w.writerows(long_rows)

    by_model: dict[str, list[float]] = {}
    for i, s in final.items():
        by_model.setdefault(key[i]["model"], []).append(s)
    L = ["# Chấm tay C4 — ý nghĩa kinh tế", "",
         f"Sinh bởi `bench/scripts/c4_merge.py`. Thang và quy trình: `eval/rubric.md`. "
         f"{len(files)} người chấm độc lập, mù tên mô hình; {len(consensus)} công thức lệch ≥2 điểm được trọng tài thống nhất.", "",
         "## Điểm theo mô hình", "",
         "| Mô hình | n | **C4 trung bình** | ± sd | Tốt (≥4) | Vô nghĩa (≤2) |", "|---|---|---|---|---|---|"]
    for m, v in sorted(by_model.items(), key=lambda kv: -st.mean(kv[1])):
        L.append(f"| {m} | {len(v)} | **{st.mean(v):.2f}** | {st.stdev(v) if len(v) > 1 else 0:.2f} "
                 f"| {pct(sum(x >= 4 for x in v) / len(v))} | {pct(sum(x <= 2 for x in v) / len(v))} |")
    L += ["", "## Đồng thuận giữa người chấm (trước khi bàn)", "",
          "| Cặp | n | Khớp | Lệch ≤1 | Lệch ≥2 | Lệch TB | Kappa trọng số |", "|---|---|---|---|---|---|---|"]
    L += [f"| {s['pair']} | {s['n']} | {pct(s['exact'])} | {pct(s['within1'])} | {s['gap2']} | {num(s['mad'])} | {num(s['kappa'])} |" for s in stats]
    L += ["", "Kappa trọng số bậc hai: 1 = khớp hoàn toàn, 0 = khớp như đoán bừa. Trên 0,6 thường coi là đồng thuận khá."]
    OUT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n" + "\n".join(L))
    print(f"\nĐã ghi {OUT_LONG} và {OUT_MD}")


if __name__ == "__main__":
    main()
