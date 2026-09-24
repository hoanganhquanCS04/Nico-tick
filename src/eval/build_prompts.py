"""Sinh bộ thử eval/prompts.jsonl (việc 1.4, spec P0-1 mục 6).

Bộ thử thiết kế theo CẶP để so sánh giữa các họ không bị lẫn với khác biệt doanh nghiệp:

    F2 notes-augmented   tập gốc: mỗi dòng = (mã, năm, chủ đề, đoạn thuyết minh thật)
    F1 structured-only   = dòng gốc BỎ đoạn thuyết minh          -> F2 vs F1 đo giá trị thuyết minh (H2)
    F3 few-shot          = dòng gốc THÊM 3 công thức mẫu          -> F3 vs F2 đo tác dụng của ví dụ
    F4 constrained       = như F1, ép JSON schema + nhắc ngữ pháp -> F4 vs F1 đo lỗi format (cứu CHỐT 2)

Các prompt cùng `pair_id` chỉ khác nhau đúng một yếu tố.

Đoạn thuyết minh cắt tự động từ file OCR theo tiêu đề mục riêng của doanh nghiệp
(`10. Hàng tồn kho`), không lấy mục chính sách kế toán (`3.6 Hàng tồn kho` - văn mẫu,
công ty nào cũng giống nhau) trừ khi mục riêng ngắn hơn 300 từ thì ghép thêm làm đoạn thứ hai.

Đầu vào : config/variables.yaml, data/sample/tickers.csv, data/sample/manifest.csv
Đầu ra  : eval/prompts.jsonl, eval/prompts_preview.md, bench/system_prompt.txt

Chạy:
    python src/eval/build_prompts.py --scan     # soi mục thuyết minh nào có trong báo cáo nào
    python src/eval/build_prompts.py            # sinh bộ thử
    python src/eval/build_prompts.py --check    # kiểm tra lại file đã sinh
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "data"))
from parse_statements import CELL_RE, PAGE_RE, ROW_RE, TABLE_RE, TAG_RE, normalize  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VARIABLES = Path("config/variables.yaml")
TICKERS = Path("data/sample/tickers.csv")
MANIFEST = Path("data/sample/manifest.csv")
RAW_ROOT = Path("data/sample/raw")
PROMPTS = Path("eval/prompts.jsonl")
PREVIEW = Path("eval/prompts_preview.md")
SYSTEM_PROMPT = Path("bench/system_prompt.txt")

N_FORMULAS = 3
MIN_WORDS, MAX_WORDS = 300, 800          # độ dài đoạn thuyết minh, spec P0-1 mục 6.2
LAGS = {1, 2, 4, 8}
FUNCS = {"lag": 2, "delta": 2, "growth": 2, "mean": 2, "std": 2,
         "rank": 1, "zscore": 1, "log": 1, "abs": 1, "safe_div": 2}

# ============================================================================ system prompt
# Một bản duy nhất cho mọi mô hình, mọi họ (spec P0-2 mục 5). Sửa ở đây, không sửa file .txt.

SYSTEM_TEXT = """\
Bạn là chuyên viên phân tích định lượng, chuyên xây dựng đặc trưng (factor) từ báo cáo tài chính \
của doanh nghiệp niêm yết Việt Nam lập theo chuẩn mực kế toán Việt Nam (VAS).

Nhiệm vụ: đề xuất công thức đặc trưng tường minh dùng để xếp hạng cổ phiếu theo lát cắt ngang, \
dữ liệu theo quý. Công thức phải áp dụng được cho mọi doanh nghiệp, không chỉ riêng doanh nghiệp được nêu.

Ngôn ngữ công thức:
- Toán tử: + - * và dấu ngoặc ( ). KHÔNG dùng dấu /. Mọi phép chia viết safe_div(a, b).
- Hàm chuỗi thời gian, k là số quý và chỉ nhận 1, 2, 4 hoặc 8:
  lag(x, k), delta(x, k), growth(x, k), mean(x, k), std(x, k)
- Hàm lát cắt ngang (chuẩn hoá trên toàn bộ cổ phiếu trong cùng kỳ): rank(x), zscore(x)
- Hàm khác: log(x), abs(x), safe_div(a, b)
- Chỉ dùng tên biến có trong danh sách được cung cấp. Không tự đặt tên biến mới.
- Tối đa 6 biến khác nhau, độ sâu lồng tối đa 6, không được là hằng số thuần.
- Không cộng trừ trực tiếp chỉ tiêu phát sinh trong kỳ với chỉ tiêu số dư cuối kỳ.

Mỗi công thức là một đối tượng JSON:
{"name": "<tên snake_case>", "formula": "<biểu thức>", \
"rationale": "<1-2 câu tiếng Việt: ý nghĩa kinh tế và chiều tác động dự kiến tới lợi suất>", \
"source": {"type": "line_item" hoặc "note", "ref": "<các biến đã dùng, hoặc trích dẫn ngắn từ thuyết minh>"}}

Trả về một mảng JSON gồm đúng số công thức được yêu cầu, không kèm văn bản nào khác.
"""

# ============================================================================ chủ đề
# heading: cụm từ tiếng Việt khớp với tiêu đề mục thuyết minh (so sau khi khử dấu, vì OCR hay
# sai dấu: "HÀNG TÔN KHO", "NỘ' XÂU"). Tiền tố "^" = tiêu đề phải BẮT ĐẦU bằng cụm đó
# (tránh "Phải thu về cho vay ngắn hạn" khớp nhầm chủ đề vay nợ).
# vars: biến riêng của chủ đề; mọi prompt phi tài chính còn được thêm CORE_VARS.

CORE_VARS = ["total_assets", "equity", "revenue", "net_income", "market_cap"]

THEMES = {
    "inventory": {
        "topic": "hàng tồn kho và dự phòng giảm giá hàng tồn kho",
        "heading": ["hàng tồn kho"],
        "vars": ["inventory", "inventory_gross", "inventory_writedown", "cogs", "gross_profit",
                 "current_assets", "current_liabilities", "payables_suppliers", "customer_advances", "cfo"],
        "must": ["inventory_writedown"],
    },
    "receivables": {
        "topic": "phải thu khách hàng và nợ khó đòi",
        "heading": ["phải thu khách hàng", "phải thu ngắn hạn của khách hàng", "nợ xấu"],
        "vars": ["receivables_customers", "short_term_receivables", "provision_doubtful_debt",
                 "prepaid_to_suppliers", "customer_advances", "current_assets", "cfo", "gross_profit"],
        "must": ["receivables_customers"],
    },
    "debt": {
        "topic": "vay nợ, trái phiếu và chi phí lãi vay",
        "heading": ["^vay", "^các khoản vay"],
        "vars": ["short_term_debt", "long_term_debt", "interest_expense", "financial_expense",
                 "total_liabilities", "current_liabilities", "cash_and_equivalents", "operating_profit",
                 "pretax_profit", "depreciation", "cfo"],
        "must": ["interest_expense"],
    },
    "fixed_assets": {
        "topic": "tài sản cố định, khấu hao và đầu tư mới",
        "heading": ["tài sản cố định hữu hình"],
        "vars": ["fixed_assets", "tangible_fixed_assets", "accumulated_depreciation", "depreciation",
                 "capex", "construction_in_progress", "long_term_assets", "cfo"],
        "must": ["capex"],
    },
    "cip": {
        "topic": "xây dựng cơ bản dở dang và chu kỳ đầu tư",
        "heading": ["xây dựng cơ bản dở dang"],
        "vars": ["construction_in_progress", "fixed_assets", "tangible_fixed_assets", "depreciation",
                 "capex", "long_term_debt", "long_term_assets", "cfo"],
        "must": ["construction_in_progress"],
    },
    "customer_advances": {
        "topic": "người mua trả tiền trước, doanh thu chưa thực hiện và doanh thu tương lai",
        "heading": ["người mua trả tiền trước", "doanh thu chưa thực hiện"],
        "vars": ["customer_advances", "inventory", "short_term_receivables", "gross_profit",
                 "current_liabilities", "cash_and_equivalents", "cfo"],
        "must": ["customer_advances"],
    },
    "associates": {
        "topic": "đầu tư vào công ty liên doanh, liên kết",
        "heading": ["liên doanh, liên kết", "công ty liên kết"],
        "vars": ["investments_associates", "long_term_investments", "share_of_associates",
                 "financial_income", "pretax_profit", "net_income_parent", "minority_interest", "cfi"],
        "must": ["share_of_associates"],
    },
    "related_party": {
        "topic": "giao dịch và số dư với các bên liên quan",
        "heading": ["bên liên quan"],
        "vars": ["related_party_disclosed", "receivables_customers", "short_term_receivables",
                 "prepaid_to_suppliers", "payables_suppliers", "cogs", "cfo"],
        "must": ["related_party_disclosed"],
    },
    "commitments": {
        "topic": "cam kết, nợ tiềm tàng và khoản mục ngoài bảng",
        "heading": ["cam kết", "nợ tiềm", "ngoài bảng cân đối"],
        "vars": ["contingent_liabilities_disclosed", "construction_in_progress", "capex",
                 "total_liabilities", "long_term_debt", "cash_and_equivalents", "cfo"],
        "must": ["contingent_liabilities_disclosed"],
    },
    "segment": {
        "topic": "cơ cấu doanh thu và lợi nhuận theo bộ phận",
        "heading": ["bộ phận"],
        "vars": ["segment_disclosed", "gross_revenue", "cogs", "gross_profit", "selling_expense",
                 "admin_expense", "operating_profit", "long_term_assets"],
        "must": ["gross_profit"],
    },
    "tax": {
        "topic": "thuế thu nhập doanh nghiệp và chất lượng lợi nhuận",
        "heading": ["thuế thu nhập doanh nghiệp"],
        "vars": ["pretax_profit", "current_tax_expense", "other_income", "operating_profit",
                 "depreciation", "cfo", "retained_earnings"],
        "must": ["current_tax_expense"],
    },
    # ---- nhóm tài chính: danh mục biến chỉ có 15 biến áp dụng được (xem applies_to), nên
    # không ép must_reference. Đây là phép thử mô hình có bịa biến ngoài danh mục không.
    "bank_loans": {
        "topic": "chất lượng danh mục cho vay và dự phòng rủi ro tín dụng",
        "heading": ["^cho vay khách hàng", "dự phòng rủi ro"],
        "vars": [], "must": [],
    },
    "fin_assets": {
        "topic": "danh mục tài sản tài chính của công ty chứng khoán",
        "heading": ["tài sản tài chính"],
        "vars": [], "must": [],
    },
}

# ============================================================================ kế hoạch bộ thử
# (mã, năm, chủ đề, các họ dùng dòng gốc này). F2 dùng mọi dòng; F1/F3/F4 lấy tập con.
# Chọn theo: chủ đề khớp đặc thù ngành (tồn kho cho sản xuất/bán lẻ, người mua trả trước cho BĐS),
# cân bằng 2017/2024, mỗi mã >=2 prompt, mã tài chính >=3.

# Đã soi bằng --scan: chỉ chọn cặp (báo cáo, chủ đề) cắt được >=180 từ thuyết minh riêng.
# Loại có chủ đích: CTD phải thu (126 từ), NLG 2017 người mua trả trước (53 từ),
# VGC liên kết (không có mục riêng).

PLAN = [
    ("ANV", 2017, "inventory",         "F1 F2 F3 F4"),
    ("HPG", 2024, "inventory",         "F1 F2 F3"),
    ("PNJ", 2024, "inventory",         "F1 F2 F4"),
    ("GAS", 2024, "receivables",       "F1 F2 F3 F4"),
    ("HUT", 2024, "receivables",       "F2 F3"),
    ("TNG", 2024, "debt",              "F1 F2 F4"),
    ("NLG", 2017, "debt",              "F1 F2 F3 F4"),
    ("POW", 2017, "debt",              "F2 F3"),
    ("HAH", 2024, "fixed_assets",      "F1 F2 F3 F4"),
    ("TNG", 2017, "fixed_assets",      "F2 F3"),
    ("HPG", 2017, "cip",               "F2 F4"),
    ("VGC", 2024, "cip",               "F1 F2 F3 F4"),
    ("NLG", 2024, "customer_advances", "F2 F3"),
    ("IDC", 2024, "customer_advances", "F1 F2 F3 F4"),
    ("CTD", 2017, "associates",        "F1 F2 F3 F4"),
    ("PVT", 2017, "associates",        "F1 F2 F3"),
    ("NTP", 2017, "related_party",     "F1 F2 F3"),
    ("MWG", 2024, "related_party",     "F2 F4"),
    ("GAS", 2017, "commitments",       "F1 F2 F3 F4"),
    ("VNM", 2024, "segment",           "F1 F2 F3"),
    ("PC1", 2024, "segment",           "F2 F4"),
    ("PNJ", 2017, "tax",               "F2 F3"),
    ("VCB", 2024, "bank_loans",        "F1 F2 F3 F4"),
    ("SHB", 2017, "bank_loans",        "F1 F2 F3"),
    ("BVS", 2024, "fin_assets",        "F1 F2 F4"),
]

# ============================================================================ công thức mẫu (F3)
# Lấy từ nhân tố đã công bố để ví dụ có nghĩa kinh tế thật. `themes` quyết định ví dụ nào được
# đưa vào prompt nào; ví dụ chỉ được chọn khi mọi biến của nó nằm trong allowed_vars của prompt.

FEWSHOT = [
    {"themes": ["*"], "name": "accruals_to_assets",
     "formula": "safe_div(net_income - cfo, total_assets)",
     "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).",
     "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
    {"themes": ["*"], "name": "earnings_yield",
     "formula": "safe_div(net_income, market_cap)",
     "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.",
     "source": {"type": "line_item", "ref": "net_income, market_cap"}},
    {"themes": ["*"], "name": "asset_growth",
     "formula": "growth(total_assets, 4)",
     "rationale": "Doanh nghiệp mở rộng tài sản quá nhanh thường có lợi suất sau đó thấp hơn (Cooper, Gulen, Schill 2008).",
     "source": {"type": "line_item", "ref": "total_assets"}},
    {"themes": ["inventory"], "name": "inventory_change_to_assets",
     "formula": "safe_div(delta(inventory, 4), mean(total_assets, 4))",
     "rationale": "Tồn kho tăng nhanh hơn quy mô tài sản báo hiệu hàng bán chậm, dự báo lợi suất thấp hơn (Thomas & Zhang 2002).",
     "source": {"type": "line_item", "ref": "inventory, total_assets"}},
    {"themes": ["inventory"], "name": "inventory_writedown_ratio",
     "formula": "safe_div(abs(inventory_writedown), inventory_gross)",
     "rationale": "Tỷ lệ dự phòng giảm giá trên giá gốc hàng tồn kho cao cho thấy rủi ro hàng lỗi thời hoặc giá bán giảm.",
     "source": {"type": "note", "ref": "dự phòng giảm giá hàng tồn kho"}},
    {"themes": ["receivables"], "name": "receivable_revenue_gap",
     "formula": "growth(receivables_customers, 4) - growth(revenue, 4)",
     "rationale": "Phải thu tăng nhanh hơn doanh thu gợi ý nới lỏng tín dụng để đẩy doanh số, lợi nhuận kém bền vững.",
     "source": {"type": "line_item", "ref": "receivables_customers, revenue"}},
    {"themes": ["receivables"], "name": "doubtful_debt_coverage",
     "formula": "safe_div(abs(provision_doubtful_debt), receivables_customers)",
     "rationale": "Mức trích lập dự phòng trên phải thu phản ánh chất lượng khách hàng và mức độ thận trọng kế toán.",
     "source": {"type": "note", "ref": "dự phòng phải thu ngắn hạn khó đòi"}},
    {"themes": ["receivables"], "name": "receivables_accrual",
     "formula": "safe_div(delta(short_term_receivables, 4), mean(total_assets, 4))",
     "rationale": "Phải thu ngắn hạn phình ra là phần dồn tích chưa thành tiền, thường đi trước lợi suất kém.",
     "source": {"type": "line_item", "ref": "short_term_receivables, total_assets"}},
    {"themes": ["customer_advances", "debt"], "name": "cash_to_current_liabilities",
     "formula": "safe_div(cash_and_equivalents, current_liabilities)",
     "rationale": "Tiền mặt so với nợ ngắn hạn đo khả năng thanh toán; thấp làm tăng rủi ro khi dòng tiền bán hàng chậm lại.",
     "source": {"type": "line_item", "ref": "cash_and_equivalents, current_liabilities"}},
    {"themes": ["associates"], "name": "financial_income_share",
     "formula": "safe_div(financial_income, pretax_profit)",
     "rationale": "Lợi nhuận dựa nhiều vào thu nhập tài chính thay vì hoạt động cốt lõi thì kém bền vững.",
     "source": {"type": "line_item", "ref": "financial_income, pretax_profit"}},
    {"themes": ["segment"], "name": "sga_intensity",
     "formula": "safe_div(selling_expense + admin_expense, gross_revenue)",
     "rationale": "Chi phí bán hàng và quản lý trên doanh thu cao làm biên lợi nhuận nhạy với biến động doanh số.",
     "source": {"type": "line_item", "ref": "selling_expense, admin_expense, gross_revenue"}},
    {"themes": ["tax"], "name": "other_income_share",
     "formula": "safe_div(other_income, pretax_profit)",
     "rationale": "Tỷ trọng thu nhập khác lớn cho thấy lợi nhuận kỳ này có phần không lặp lại.",
     "source": {"type": "line_item", "ref": "other_income, pretax_profit"}},
    {"themes": ["debt"], "name": "net_debt_to_equity",
     "formula": "safe_div(short_term_debt + long_term_debt - cash_and_equivalents, equity)",
     "rationale": "Đòn bẩy ròng cao làm tăng rủi ro tài chính, cổ phiếu nhạy hơn với lãi suất.",
     "source": {"type": "line_item", "ref": "short_term_debt, long_term_debt, cash_and_equivalents, equity"}},
    {"themes": ["debt"], "name": "interest_coverage",
     "formula": "safe_div(pretax_profit + interest_expense, interest_expense)",
     "rationale": "Khả năng trả lãi từ lợi nhuận trước lãi vay và thuế; thấp nghĩa là dễ tổn thương khi lãi suất tăng.",
     "source": {"type": "line_item", "ref": "pretax_profit, interest_expense"}},
    {"themes": ["fixed_assets", "cip"], "name": "capex_to_depreciation",
     "formula": "safe_div(abs(capex), depreciation)",
     "rationale": "Chi đầu tư vượt xa khấu hao cho thấy doanh nghiệp đang mở rộng năng lực, lợi suất ngắn hạn thường thấp hơn (Titman, Wei, Xie 2004).",
     "source": {"type": "line_item", "ref": "capex, depreciation"}},
    {"themes": ["fixed_assets", "cip"], "name": "cip_to_fixed_assets",
     "formula": "safe_div(construction_in_progress, fixed_assets)",
     "rationale": "Tỷ trọng công trình dở dang lớn báo hiệu năng lực mới sắp đưa vào khai thác, kèm rủi ro chậm tiến độ.",
     "source": {"type": "note", "ref": "chi phí xây dựng cơ bản dở dang"}},
    {"themes": ["customer_advances"], "name": "advances_to_inventory",
     "formula": "safe_div(customer_advances, inventory)",
     "rationale": "Với doanh nghiệp bất động sản, tiền khách trả trước so với quỹ hàng tồn kho là chỉ báo doanh thu sẽ ghi nhận khi bàn giao.",
     "source": {"type": "note", "ref": "người mua trả tiền trước"}},
    {"themes": ["associates"], "name": "associates_profit_share",
     "formula": "safe_div(share_of_associates, pretax_profit)",
     "rationale": "Lợi nhuận phụ thuộc nhiều vào công ty liên kết thì khó dự báo và ít chịu kiểm soát của ban điều hành.",
     "source": {"type": "line_item", "ref": "share_of_associates, pretax_profit"}},
    {"themes": ["related_party", "commitments", "segment", "tax"], "name": "gross_profitability",
     "formula": "safe_div(gross_profit, total_assets)",
     "rationale": "Lợi nhuận gộp trên tổng tài sản là thước đo khả năng sinh lời cốt lõi, dự báo lợi suất tốt (Novy-Marx 2013).",
     "source": {"type": "line_item", "ref": "gross_profit, total_assets"}},
    {"themes": ["tax"], "name": "cash_tax_rate",
     "formula": "safe_div(current_tax_expense, pretax_profit)",
     "rationale": "Thuế suất hiệu dụng thấp bất thường so với lợi nhuận kế toán có thể là dấu hiệu lợi nhuận bị thổi phồng.",
     "source": {"type": "line_item", "ref": "current_tax_expense, pretax_profit"}},
    {"themes": ["bank_loans", "fin_assets"], "name": "roe_change",
     "formula": "delta(safe_div(net_income, mean(equity, 4)), 4)",
     "rationale": "Cải thiện tỷ suất sinh lời trên vốn chủ so với cùng kỳ năm trước báo hiệu chất lượng hoạt động đi lên.",
     "source": {"type": "line_item", "ref": "net_income, equity"}},
    {"themes": ["bank_loans", "fin_assets"], "name": "book_to_market",
     "formula": "safe_div(equity, market_cap)",
     "rationale": "Giá trị sổ sách cao so với vốn hoá là nhân tố giá trị kinh điển (Fama & French 1992).",
     "source": {"type": "line_item", "ref": "equity, market_cap"}},
]

SECTOR_VI = {
    "agri_fishery": "nông nghiệp - thuỷ sản", "bank": "ngân hàng", "securities": "chứng khoán",
    "construction_materials": "xây dựng - vật liệu", "logistics": "logistics - vận tải",
    "manufacturing": "sản xuất công nghiệp", "real_estate": "bất động sản",
    "retail_consumer": "bán lẻ - tiêu dùng", "utilities_energy": "tiện ích - năng lượng",
}

# ============================================================================ cắt thuyết minh

# Ba kiểu đánh số gặp trong mẫu:
#   "10. Hàng tồn kho"  (KPMG, EY)          -> cấp 1
#   "18 VAY"            (PwC, không dấu chấm) -> cấp 1, bắt buộc chữ đầu viết hoa để không
#                                              nhầm với dòng ngày tháng "31 tháng 12 năm 2024"
#   "5.7 Hàng tồn kho"  (mẫu VAS cũ: mục V. Thông tin bổ sung, chính sách không đánh số) -> cấp 2
#   "IV. CÁC CHÍNH SÁCH KẾ TOÁN ÁP DỤNG" -> cấp 0, chỉ dùng để biết mục cấp 1 bên dưới là văn mẫu
HEADING_RE = re.compile(r"^\s*(\d{1,2})(\.?)\s+(\S.{2,110})$")
SUBHEADING_RE = re.compile(r"^\s*(\d{1,2}\.\d{1,2})\.?\s+(\S.{2,110})$")
SECTION_RE = re.compile(r"^\s*([IVX]{1,4})\.\s+(\S.{2,110})$")
POLICY_WORDS = ("chính sách", "nguyên tắc")


def phrase_matcher(phrases: list[str]):
    keys = [(p.startswith("^"), normalize(p.lstrip("^"))) for p in phrases]
    return lambda norm: any(norm.startswith(k) if anchored else k in norm for anchored, k in keys)


def is_policy(norm: str) -> bool:
    return any(normalize(w) in norm for w in POLICY_WORDS)


def heading_of(line: str) -> tuple[int, str, str] | None:
    """(cấp, số hiệu, tiêu đề) nếu dòng là tiêu đề mục thuyết minh."""
    m = SUBHEADING_RE.match(line)
    if m:
        level, num, title = 2, m.group(1), m.group(2).strip()
    elif m := SECTION_RE.match(line):
        level, num, title = 0, m.group(1), m.group(2).strip()
        if not title[0].isupper():
            return None
    else:
        m = HEADING_RE.match(line)
        if not m:
            return None
        level, num, title = 1, m.group(1), m.group(3).strip()
        if not m.group(2) and not title[0].isupper():
            return None
    if not title[0].isalpha() or title[-1] in ".;:,":
        return None
    return level, num, title


def find_headings(lines: list[str]) -> list[dict]:
    """Liệt kê tiêu đề và đánh dấu `in_policy` = nằm trong phần tóm tắt chính sách kế toán.

    Ranh giới phần lớn là tiêu đề cấp 0 (số La Mã), HOẶC số mục cấp 1 quay về nhỏ hơn -
    OCR hay làm rơi tiêu đề 'V. Thông tin bổ sung...' nên không thể chỉ dựa vào cấp 0.
    """
    out = []
    section_policy, last_num, parent_policy = False, None, False
    for i, ln in enumerate(lines):
        h = heading_of(ln)
        if h is None:
            continue
        level, num, title = h
        norm = normalize(title)
        cont = "tieptheo" in norm
        norm = norm.replace("tieptheo", "")
        if level == 0:
            section_policy, last_num = is_policy(norm), None
            in_policy = section_policy
        elif level == 1:
            if not cont:
                if last_num is not None and int(num) < last_num:
                    section_policy = False
                last_num = int(num)
            in_policy = section_policy
            parent_policy = section_policy or is_policy(norm)
        else:
            in_policy = parent_policy
        out.append({"line": i, "level": level, "num": num, "title": title,
                    "cont": cont, "norm": norm, "in_policy": in_policy})
    return out


def note_end(heads: list[dict], k: int, n_lines: int) -> int:
    """Mục cấp 1 kết thúc ở tiêu đề cấp 0/1 kế tiếp; mục cấp 2 ở tiêu đề bất kỳ kế tiếp.
    Tiêu đề '(tiếp theo)' cùng số hiệu thì gộp vào, không cắt."""
    me = heads[k]
    for h in heads[k + 1:]:
        if h["cont"] and h["num"] == me["num"]:
            continue
        if me["level"] == 1 and h["level"] == 2:
            continue
        return h["line"]
    return n_lines


def furniture(lines: list[str]) -> set[str]:
    """Dòng lặp >=3 lần trong tài liệu = tiêu đề/chân trang (tên công ty, 'Mẫu B09-DN'...)."""
    seen: dict[str, int] = {}
    for ln in lines:
        s = ln.strip()
        if s and len(s) < 300 and not s.startswith("<table"):
            seen[s] = seen.get(s, 0) + 1
    return {s for s, c in seen.items() if c >= 3}


def is_noise(s: str) -> bool:
    """Chữ OCR từ con dấu, chữ ký ('ÔNG', 'OÁN VÀ', '1-C-7.1.N.H.H + MINH', tên người ký)."""
    words = s.split()
    return len(words) <= 3 and not s.endswith(":")


def units_of(lines: list[str], start: int, end: int, skip: set[str]) -> list[tuple[int, str]]:
    """Tách đoạn [start, end) thành đơn vị (số dòng gốc, text): mỗi dòng văn xuôi hoặc mỗi hàng bảng."""
    out = []
    for i in range(start, end):
        s = lines[i].strip()
        if not s or s in skip or PAGE_RE.fullmatch(s) or re.fullmatch(r"[\d\s.\-–]+", s):
            continue
        if i != start and heading_of(s) and "tieptheo" in normalize(s):
            continue
        if i != start and "<table" not in s and not heading_of(s) and is_noise(s):
            continue
        if "<table" in s:
            for tb in TABLE_RE.findall(s):
                for row in ROW_RE.findall(tb):
                    cells = [TAG_RE.sub("", c).strip() for c in CELL_RE.findall(row)]
                    if any(cells):
                        out.append((i, " | ".join(cells)))
            continue
        out.append((i, TAG_RE.sub("", s)))
    return out


def take_words(units: list[tuple[int, str]], budget: int) -> tuple[list[tuple[int, str]], bool]:
    kept, used = [], 0
    for i, text in units:
        n = len(text.split())
        if used + n > budget:
            if budget - used >= 30:                      # còn đủ chỗ thì cắt dở câu cuối
                kept.append((i, " ".join(text.split()[: budget - used]) + " [...]"))
            return kept, True
        kept.append((i, text))
        used += n
    return kept, False


def best_note(lines: list[str], heads: list[dict], match) -> dict | None:
    """Mục riêng (không phải chính sách) khớp chủ đề và dài nhất."""
    skip = furniture(lines)
    best = None
    for k, h in enumerate(heads):
        if h["level"] == 0 or h["cont"] or h["in_policy"] or is_policy(h["norm"]) or not match(h["norm"]):
            continue
        units = units_of(lines, h["line"], note_end(heads, k, len(lines)), skip)
        words = sum(len(t.split()) for _, t in units)
        if best is None or words > best["words"]:
            best = {"head": h, "units": units, "words": words}
    return best


def policy_note(lines: list[str], heads: list[dict], match, before: int) -> list[tuple[int, str]]:
    """Mục chính sách kế toán cùng chủ đề (3.6 Hàng tồn kho, hoặc 7. dưới IV. Chính sách), nằm trước mục riêng."""
    for k, h in enumerate(heads):
        if h["line"] >= before:
            break
        if h["in_policy"] and h["level"] > 0 and match(h["norm"]):
            end = heads[k + 1]["line"] if k + 1 < len(heads) else before
            return units_of(lines, h["line"], min(end, before), furniture(lines))
    return []


def extract_context(path: Path, theme: str) -> dict | None:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    match = phrase_matcher(THEMES[theme]["heading"])
    heads = find_headings(lines)
    note = best_note(lines, heads, match)
    if note is None:
        return None

    main, truncated = take_words(note["units"], MAX_WORDS)
    parts = [main]
    used = sum(len(t.split()) for _, t in main)
    if used < MIN_WORDS:
        extra, _ = take_words(policy_note(lines, heads, match, note["head"]["line"]), MAX_WORDS - used)
        if extra:
            parts.append(extra)

    rel = path.relative_to(RAW_ROOT.parent.parent.parent).as_posix()
    text = "\n\n".join("\n".join(t for _, t in p) for p in parts)
    return {
        "text": text,
        "words": len(text.split()),
        "note_title": note["head"]["title"],
        "note_no": note["head"]["num"],
        "with_policy": len(parts) > 1,
        "truncated": truncated,
        "source": ";".join(f"{rel}#L{p[0][0] + 1}-L{p[-1][0] + 1}" for p in parts),
    }


# ============================================================================ dựng prompt

def load_catalog() -> dict[str, dict]:
    doc = yaml.safe_load(VARIABLES.read_text(encoding="utf-8"))
    return {v["name"]: v for v in doc["variables"]}


def load_docs() -> dict[tuple[str, int], dict]:
    tickers = {r["ticker"]: r for r in csv.DictReader(TICKERS.open(encoding="utf-8"))}
    out = {}
    for r in csv.DictReader(MANIFEST.open(encoding="utf-8")):
        t = tickers[r["ticker"]]
        out[(r["ticker"], int(r["year"]))] = {
            "ticker": r["ticker"], "year": int(r["year"]), "exchange": t["exchange"],
            "sector": r["sector"], "detail": t["reason"].split(" - ")[0].strip(),
            "is_financial": r["is_financial"].strip().lower() == "true",
            "path": RAW_ROOT / r["repo_path"],
        }
    return out


def allowed_vars(theme: str, is_financial: bool, catalog: dict[str, dict]) -> list[str]:
    if is_financial:
        return [n for n, v in catalog.items() if "financial" in v["applies_to"]]
    names = THEMES[theme]["vars"] + [v for v in CORE_VARS if v not in THEMES[theme]["vars"]]
    return [n for n in catalog if n in names]              # giữ thứ tự của danh mục


def describe_var(v: dict) -> str:
    if v["statement"] == "notes":
        kind = "cờ từ thuyết minh, số lần nội dung này được nhắc tới"
    elif v["statement"] == "market":
        kind = "dữ liệu thị trường"
    else:
        kind = f'{v["unit"]}, {"phát sinh trong kỳ" if v["is_flow"] else "số dư cuối kỳ"}'
        if v.get("sign") == "negative":
            kind += ", ghi số âm"
    return f'- {v["name"]}: {v["vi_label"]} [{kind}]'


def header(doc: dict, theme: str) -> str:
    return (f'Doanh nghiệp: {doc["ticker"]} - {SECTOR_VI[doc["sector"]]} ({doc["detail"]}), '
            f'sàn {doc["exchange"]}.\nChủ đề: {THEMES[theme]["topic"]}.')


def var_block(names: list[str], catalog: dict[str, dict]) -> str:
    return "Danh sách biến được phép dùng:\n" + "\n".join(describe_var(catalog[n]) for n in names)


def must_line(must: list[str]) -> str:
    return f' Ít nhất một công thức phải dùng biến {", ".join(must)}.' if must else ""


def fewshot_for(theme: str, allowed: list[str], must: list[str]) -> list[dict]:
    """Tối đa 2 ví dụ cùng chủ đề + ví dụ chung cho đủ 3. Bỏ ví dụ dùng biến must_reference
    để không đưa sẵn đáp án cho yêu cầu 'phải dùng biến X'."""
    fits = [e for e in FEWSHOT if set(vars_in(e["formula"])) <= set(allowed)
            and not set(vars_in(e["formula"])) & set(must)]
    themed = [e for e in fits if theme in e["themes"]]
    generic = [e for e in fits if "*" in e["themes"]]
    picked = themed[:2] + [e for e in generic if e not in themed][: 3 - len(themed[:2])]
    return [{k: e[k] for k in ("name", "formula", "rationale", "source")} for e in picked]


STRICT_BLOCK = """\
ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng {n} đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {{"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}}
3. Ngữ pháp của formula:
   expr   := term (("+" | "-") term)*
   term   := factor ("*" factor)*
   factor := NUMBER | VAR | CALL | "(" expr ")" | "-" factor
   CALL   := F1 "(" expr ")"
           | "safe_div(" expr "," expr ")"
           | TS "(" expr "," LAG ")"
   F1     := rank | zscore | log | abs
   TS     := lag | delta | growth | mean | std
   LAG    := 1 | 2 | 4 | 8
   VAR    := đúng một tên trong danh sách biến ở trên
   Cấm: dấu "/", tên biến ngoài danh sách, hàm ngoài danh sách, công thức chỉ có hằng số.
Ví dụ một phần tử hợp lệ (không được lặp lại):
{{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {{"type": "line_item", "ref": "total_assets"}}}}"""


def response_schema(allowed: list[str]) -> dict:
    """JSON Schema cho F4 - dùng được thẳng với giải mã ràng buộc (outlines/xgrammar) nếu CHỐT 2 trượt."""
    item = {
        "type": "object", "additionalProperties": False,
        "required": ["name", "formula", "rationale", "source"],
        "properties": {
            "name": {"type": "string", "pattern": "^[a-z][a-z0-9_]{2,60}$"},
            "formula": {"type": "string", "minLength": 3, "maxLength": 300},
            "rationale": {"type": "string", "minLength": 10, "maxLength": 400},
            "source": {"type": "object", "additionalProperties": False, "required": ["type", "ref"],
                       "properties": {"type": {"enum": ["line_item"]}, "ref": {"type": "string"}}},
        },
    }
    return {"type": "array", "minItems": N_FORMULAS, "maxItems": N_FORMULAS, "items": item,
            "x_allowed_vars": allowed}


def build(catalog: dict[str, dict], docs: dict) -> list[dict]:
    base, records = [], []
    for ticker, year, theme, fams in PLAN:
        doc = docs[(ticker, year)]
        ctx = extract_context(doc["path"], theme)
        if ctx is None:
            sys.exit(f"Không tìm thấy mục thuyết minh chủ đề '{theme}' trong {ticker} {year}")
        allowed = allowed_vars(theme, doc["is_financial"], catalog)
        must = [m for m in THEMES[theme]["must"] if m in allowed]
        base.append((doc, theme, fams.split(), ctx, allowed, must))

    counters = {f: 0 for f in ("F1", "F2", "F3", "F4")}
    for pair_no, (doc, theme, fams, ctx, allowed, must) in enumerate(base, start=1):
        pair_id = f'P{pair_no:02d}-{doc["ticker"]}{doc["year"] % 100:02d}-{theme}'
        head, vars_txt = header(doc, theme), var_block(allowed, catalog)
        note_txt = (f'Trích thuyết minh báo cáo tài chính năm {doc["year"]} của {doc["ticker"]} '
                    f'(mục {ctx["note_no"]}. {ctx["note_title"]}):\n<<<\n{ctx["text"]}\n>>>')
        ask_plain = (f"Yêu cầu: đề xuất {N_FORMULAS} công thức đặc trưng khác nhau xoay quanh chủ đề trên, "
                     f"có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới.{must_line(must)}")
        ask_note = (f"Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất {N_FORMULAS} công thức đặc trưng "
                    f"khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới.{must_line(must)} "
                    'Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi '
                    'source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.')
        tail = f"Trả về mảng JSON gồm đúng {N_FORMULAS} phần tử theo định dạng đã quy định."

        variants = {
            "F1": ("none", [head, vars_txt, ask_plain, tail]),
            "F2": ("note", [head, note_txt, vars_txt, ask_note, tail]),
            "F3": ("note", [head, note_txt, vars_txt, ask_note]),
            "F4": ("none", [head, vars_txt, ask_plain, STRICT_BLOCK.format(n=N_FORMULAS)]),
        }
        shots = fewshot_for(theme, allowed, must)
        for fam in ("F1", "F2", "F3", "F4"):
            if fam not in fams:
                continue
            ctype, blocks = variants[fam]
            if fam == "F3":
                blocks = blocks + [
                    "Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):\n["
                    + ",\n".join(json.dumps(s, ensure_ascii=False) for s in shots) + "]", tail]
            counters[fam] += 1
            rec = {
                "id": f"{fam}-{counters[fam]:03d}",
                "family": fam,
                "pair_id": pair_id,
                "ticker": doc["ticker"],
                "year": doc["year"],
                "sector": doc["sector"],
                "is_financial": doc["is_financial"],
                "theme": theme,
                "context_type": ctype,
                "context": ctx["text"] if ctype == "note" else "",
                "context_source": ctx["source"] if ctype == "note" else "",
                "context_words": ctx["words"] if ctype == "note" else 0,
                "instruction": "\n\n".join(blocks),
                "system_prompt": SYSTEM_PROMPT.as_posix(),
                "allowed_vars": allowed,
                "n_formulas": N_FORMULAS,
                "must_reference": must,
                "fewshot": shots if fam == "F3" else [],
                "response_schema": response_schema(allowed) if fam == "F4" else None,
                "notes": (f'mục {ctx["note_no"]}. {ctx["note_title"]}'
                          + ("; ghép thêm mục chính sách kế toán" if ctx["with_policy"] else "")
                          + ("; cắt bớt ở 800 từ" if ctx["truncated"] else "")),
            }
            records.append(rec)
    return records


# ============================================================================ kiểm tra

def vars_in(formula: str) -> list[str]:
    tree = ast.parse(formula, mode="eval")
    return sorted({n.id for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id not in FUNCS})


def check_formula(formula: str, catalog: dict[str, dict]) -> list[str]:
    """Kiểm tra tối thiểu cho công thức mẫu - KHÔNG phải validator v0 (việc 2.3)."""
    errs = []
    tree = ast.parse(formula, mode="eval")
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div):
            errs.append("raw_division")
        if isinstance(n, ast.Call):
            name = getattr(n.func, "id", "?")
            if FUNCS.get(name) != len(n.args):
                errs.append(f"bad_call:{name}")
            elif FUNCS[name] == 2 and name != "safe_div":
                k = n.args[1]
                if not (isinstance(k, ast.Constant) and k.value in LAGS):
                    errs.append(f"bad_lag:{name}")
    errs += [f"unknown_var:{v}" for v in vars_in(formula) if v not in catalog]
    return errs


def check(records: list[dict], catalog: dict[str, dict]) -> list[str]:
    errs = []
    for e in FEWSHOT:
        errs += [f'fewshot {e["name"]}: {x}' for x in check_formula(e["formula"], catalog)]
    ids = set()
    for r in records:
        if r["id"] in ids:
            errs.append(f'{r["id"]}: trùng id')
        ids.add(r["id"])
        errs += [f'{r["id"]}: biến lạ {v}' for v in r["allowed_vars"] if v not in catalog]
        errs += [f'{r["id"]}: must_reference {m} ngoài allowed_vars'
                 for m in r["must_reference"] if m not in r["allowed_vars"]]
        if r["context_type"] == "note":
            for src in r["context_source"].split(";"):
                if not Path(src.split("#")[0]).exists():
                    errs.append(f'{r["id"]}: context_source không tồn tại {src}')
            if r["context_words"] < 150:
                errs.append(f'{r["id"]}: thuyết minh quá ngắn ({r["context_words"]} từ)')
        if r["family"] == "F3" and len(r["fewshot"]) < 2:
            errs.append(f'{r["id"]}: chỉ có {len(r["fewshot"])} ví dụ')
    fam = {f: sum(r["family"] == f for r in records) for f in ("F1", "F2", "F3", "F4")}
    for f, (lo, hi) in {"F1": (15, 20), "F2": (20, 25), "F3": (15, 20), "F4": (10, 15)}.items():
        if not lo <= fam[f] <= hi:
            errs.append(f"{f}: {fam[f]} prompt, spec yêu cầu {lo}-{hi}")
    if not 60 <= len(records) <= 80:
        errs.append(f"tổng {len(records)} prompt, spec yêu cầu 60-80")
    per_ticker: dict[str, int] = {}
    for r in records:
        per_ticker[r["ticker"]] = per_ticker.get(r["ticker"], 0) + 1
    for r in records:
        need = 3 if r["is_financial"] else 2
        if per_ticker[r["ticker"]] < need:
            errs.append(f'{r["ticker"]}: chỉ {per_ticker[r["ticker"]]} prompt, cần >= {need}')
    return sorted(set(errs))


# ============================================================================ xuất file

def write_preview(records: list[dict]) -> None:
    fam = {f: [r for r in records if r["family"] == f] for f in ("F1", "F2", "F3", "F4")}
    words = sorted(r["context_words"] for r in fam["F2"])
    lines = [
        "# Bộ thử P0 - xem nhanh",
        "",
        f"Sinh tự động bởi `src/eval/build_prompts.py`. **Không sửa tay** - sửa script rồi chạy lại.",
        "",
        f"Tổng **{len(records)}** prompt: " + ", ".join(f"{f} = {len(v)}" for f, v in fam.items())
        + f". Mỗi prompt yêu cầu {N_FORMULAS} công thức. System prompt chung: `{SYSTEM_PROMPT.as_posix()}`.",
        "",
        f"Đoạn thuyết minh (F2/F3): {words[0]}-{words[-1]} từ, trung vị {words[len(words) // 2]}.",
        "",
        "## Bảng cặp",
        "",
        "| pair_id | mã | năm | chủ đề | mục thuyết minh | từ | F1 | F2 | F3 | F4 |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    pairs: dict[str, dict] = {}
    for r in records:
        pairs.setdefault(r["pair_id"], {})[r["family"]] = r
    for pid, fs in pairs.items():
        r = fs["F2"]
        lines.append(f'| {pid} | {r["ticker"]} | {r["year"]} | {r["theme"]} | {r["notes"]} | '
                     f'{r["context_words"]} | ' + " | ".join(fs[f]["id"] if f in fs else "" for f in
                                                             ("F1", "F2", "F3", "F4")) + " |")
    lines += ["", "## Toàn văn", ""]
    for r in records:
        lines += [f'### {r["id"]} · {r["pair_id"]}', "",
                  f'allowed_vars ({len(r["allowed_vars"])}): `{", ".join(r["allowed_vars"])}`  ',
                  f'must_reference: `{", ".join(r["must_reference"]) or "-"}`  ',
                  f'context_source: `{r["context_source"] or "-"}`', "",
                  "````text", r["instruction"], "````", ""]
    PREVIEW.write_text("\n".join(lines), encoding="utf-8")


def scan(docs: dict) -> None:
    themes = list(THEMES)
    print(f'{"báo cáo":10s}' + "".join(f"{t[:9]:>10s}" for t in themes))
    for key in sorted(docs):
        doc = docs[key]
        cells = []
        for t in themes:
            ctx = extract_context(doc["path"], t)
            cells.append("-" if ctx is None else f'{ctx["words"]}{"+" if ctx["with_policy"] else ""}')
        print(f"{key[0]}_{key[1]:<5d}" + "".join(f"{c:>10s}" for c in cells))
    print("\nsố = số từ đoạn thuyết minh cắt được (tối đa 800), '+' = đã ghép mục chính sách vì mục riêng ngắn")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true", help="in ma trận mục thuyết minh x báo cáo")
    ap.add_argument("--check", action="store_true", help="chỉ kiểm tra eval/prompts.jsonl đã có")
    args = ap.parse_args()

    catalog, docs = load_catalog(), load_docs()
    if args.scan:
        scan(docs)
        return
    if args.check:
        records = [json.loads(ln) for ln in PROMPTS.read_text(encoding="utf-8").splitlines() if ln.strip()]
    else:
        records = build(catalog, docs)
        PROMPTS.parent.mkdir(parents=True, exist_ok=True)
        SYSTEM_PROMPT.parent.mkdir(parents=True, exist_ok=True)
        PROMPTS.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")
        SYSTEM_PROMPT.write_text(SYSTEM_TEXT, encoding="utf-8")
        write_preview(records)
        print(f"Đã ghi {len(records)} prompt -> {PROMPTS}, xem nhanh ở {PREVIEW}")

    errs = check(records, catalog)
    print("\n".join(errs) if errs else "Kiểm tra: không có lỗi.")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
