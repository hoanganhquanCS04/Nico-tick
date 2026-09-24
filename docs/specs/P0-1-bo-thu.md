# SPEC — P0 Task 1: Bộ thử (15–20 BCTC mẫu + 60–80 prompt)

| | |
|---|---|
| **Người làm** | ML |
| **Hạn** | 24/09/2026 |
| **Phụ thuộc** | Không (không cần chờ P1) |
| **Chặn** | Task 2 (benchmark) — không có bộ thử thì không benchmark được |

## 1. Mục tiêu

Tạo ra một **bộ thử cố định** để đo các mô hình ứng viên trên cùng một thước đo.
Bộ thử này sẽ được tái sử dụng ở P4 (sinh ~150 công thức) và P6 (baseline API), nên
đừng làm tạm bợ — nhưng cũng đừng mở rộng quá phạm vi P0.

**Trong phạm vi:** chọn mẫu, tải dữ liệu, chuẩn hoá danh mục biến, viết prompt, viết rubric.
**Ngoài phạm vi:** parse BCTC tự động ở quy mô lớn (task #6), RAG/PhoBERT (P3), chạy mô hình (task 2).

---

## 2. Đầu ra bắt buộc

| File | Nội dung |
|---|---|
| `data/sample/tickers.csv` | Danh sách 15–20 mã đã chọn + lý do |
| `data/sample/raw/<ticker>/<year>/*.txt` | File OCR text từ HuggingFace |
| `config/variables.yaml` | Danh mục 40–60 biến chuẩn hoá |
| `eval/prompts.jsonl` | 60–80 prompt |
| `eval/rubric.md` | Tiêu chí chấm |
| `eval/manual_scores.csv` | Bảng chấm tay (khung rỗng, điền ở task 2.6) |

---

## 3. Việc 1.1 — Chọn mẫu 15–20 mã

**Tiêu chí phân tầng** (không chọn theo cảm tính, phải ghi lý do):

| Chiều | Yêu cầu |
|---|---|
| Ngành | ≥6 ngành. Gợi ý: sản xuất/công nghiệp 4, bán lẻ–tiêu dùng 3, bất động sản 3, xây dựng–vật liệu 2, tiện ích–năng lượng 2, logistics 2, ngân hàng 2, chứng khoán 1, thuỷ sản–nông nghiệp 1 |
| Vốn hoá | ≥6 mã lớn (VN30), ≥7 mã vừa, ≥5 mã nhỏ |
| Sàn | Cả HOSE và HNX, không chỉ HOSE |
| Năm | Mỗi mã lấy **2 năm**: 1 năm gần (2023–2024) + 1 năm xa (2016–2018) |
| Chất lượng OCR | Cố ý giữ ≥3 mã có OCR xấu — để biết mô hình gãy ở đâu |

**Vì sao giữ ngân hàng và chứng khoán:** mẫu biểu BCTC của hai nhóm này khác hẳn doanh nghiệp
thường (không có hàng tồn kho, không có doanh thu thuần theo nghĩa thông thường). Giữ 2–3 mã để
biết công thức sinh ra có gãy không, nhưng **đánh dấu cờ riêng** trong `tickers.csv` để khi
tính tỷ lệ hợp lệ có thể tách ra xem.

**Schema `tickers.csv`:**

```csv
ticker,exchange,sector,cap_tier,years,is_financial,ocr_quality,reason
HPG,HOSE,steel,large,"2017,2024",false,good,"đại diện sản xuất vốn hoá lớn, chu kỳ rõ"
```

- `cap_tier`: `large` | `mid` | `small`
- `is_financial`: `true` cho ngân hàng/chứng khoán/bảo hiểm
- `ocr_quality`: `good` | `fair` | `poor` — đánh giá bằng mắt sau khi tải

**Xong khi:** đủ 15–20 dòng, thoả cả 5 tiêu chí trên, mỗi dòng có `reason` viết được thành câu.

---

## 4. Việc 1.2 — Tải dữ liệu mẫu

Nguồn: `tinixai/ocr_annual_financials` (HuggingFace, CC BY-NC 4.0, 194GB, cấu trúc phân cấp theo mã/năm/loại báo cáo).

**Tuyệt đối không `snapshot_download` toàn bộ.** Dùng `allow_patterns` lọc theo mã đã chọn:

```python
from huggingface_hub import snapshot_download

tickers = ["HPG", "MWG", "VHM", ...]          # đọc từ tickers.csv
years    = ["2017", "2024"]
patterns = [f"*/{t}/*{y}*" for t in tickers for y in years]   # điều chỉnh sau khi xem cây thư mục thật

snapshot_download(
    repo_id="tinixai/ocr_annual_financials",
    repo_type="dataset",
    allow_patterns=patterns,
    local_dir="data/sample/raw",
)
```

**Bước 0 bắt buộc:** gọi `HfApi().list_repo_files(repo_id, repo_type="dataset")` trước, in ra
50 đường dẫn đầu để biết cấu trúc thư mục thật, rồi mới viết `allow_patterns`. Đoán pattern
rồi tải nhầm 194GB là hỏng cả ngày.

**Lấy cả PDF cho 3–5 mã** để đối chiếu OCR với bản gốc (dataset công bố độ chính xác ~95% với
số liệu và bảng — cần tự kiểm chứng trên mẫu, con số này sẽ đưa vào phần hạn chế của báo cáo).

**Xong khi:** đúng số mã × số năm đã chọn nằm trong `data/sample/raw/`, dung lượng < 5GB,
mở ngẫu nhiên 3 file thấy có cả bảng số lẫn phần thuyết minh.

---

## 5. Việc 1.3 — `config/variables.yaml` (quan trọng nhất)

File này là **giao ước giữa 4 mô-đun**: prompt (1.4) đưa cho mô hình danh sách biến hợp lệ,
validator (2.3) kiểm tra biến có tồn tại không, P4 sinh 150 công thức trên cùng danh mục này,
P5 tính giá trị biến từ BCTC quý. Sai ở đây thì hỏng dây chuyền.

> **Cập nhật 22/09 sau khi tải dữ liệu — cách làm đã đổi.** OCR trả về **bảng HTML** kèm
> **mã số chỉ tiêu VAS**, không phải text thuần:
> `<tr><td>Hàng tồn kho</td><td>140</td><td>10.1</td><td>46.091.222.189.472</td><td>34.504.487.406.261</td></tr>`
> Vì vậy **trích biến theo mã số, không dò khớp tên tiếng Việt**. Trường `aliases` hạ xuống
> vai trò dự phòng cho dòng không có mã số. Cột thứ ba là số hiệu thuyết minh — chính là
> **cầu nối bảng số sang đoạn văn**, dùng thẳng cho RAG ở P3 và cho truy vết nguồn.
> Ngân hàng chỉ có 28–49 mã VAS (trung vị chung là 74) nên phải có bộ map riêng.

**Schema mỗi biến:**

```yaml
- name: total_assets              # snake_case, tiếng Anh, duy nhất
  vi_label: Tổng cộng tài sản
  statement: balance_sheet        # balance_sheet | income_statement | cash_flow | notes | market
  vas_code: "270"                 # mã số chỉ tiêu theo mẫu BCTC Việt Nam, để trống nếu là biến dẫn xuất
  unit: VND                       # VND | ratio | shares | days | pct
  sign: positive                  # positive | negative | any  — dùng để kiểm tra vô lý
  is_flow: false                  # true = chỉ tiêu kỳ (doanh thu), false = chỉ tiêu thời điểm (tài sản)
  applies_to: [non_financial, financial]
  coverage: 20/20                 # điền sau khi đối chiếu mẫu
  aliases: ["TỔNG CỘNG TÀI SẢN", "Tổng tài sản"]   # biến thể chữ trong BCTC/OCR
```

**Phân bổ 40–60 biến:**

| Nhóm | Số lượng | Ví dụ |
|---|---|---|
| Bảng cân đối | 15–18 | `total_assets`, `equity`, `inventory`, `receivables`, `cash`, `short_term_debt`, `long_term_debt`, `payables` |
| Kết quả kinh doanh | 10–12 | `revenue`, `cogs`, `gross_profit`, `sga_expense`, `interest_expense`, `ebit`, `net_income`, `financial_income` |
| Lưu chuyển tiền tệ | 6–8 | `cfo`, `cfi`, `cff`, `capex`, `depreciation`, `dividends_paid` |
| Thị trường | 4–5 | `market_cap`, `close_price`, `shares_outstanding`, `adv20` |
| Từ thuyết minh | 5–8 | `related_party_receivables`, `provision_doubtful_debt`, `inventory_writedown`, `audit_opinion_qualified`, `segment_revenue_top1` |

**Nhóm "từ thuyết minh" là nhóm quan trọng nhất về mặt nghiên cứu** — đây chính là thứ
tạo ra giả thuyết H2. Nếu danh mục biến chỉ có chỉ tiêu bảng số thì ablation "bỏ RAG" ở P6
không có gì để đo, và đóng góp G2 mất một nửa.

**Xong khi:** mỗi biến map được về ít nhất 12/20 DN mẫu (`coverage` ≥ 12/20);
riêng nhóm thuyết minh chấp nhận `coverage` thấp hơn nhưng phải ghi rõ.

---

## 6. Việc 1.4 — 60–80 prompt

### 6.1. Ngôn ngữ công thức (DSL v0)

Phải định nghĩa trước khi viết prompt, nếu không mô hình sinh ra mỗi lần một kiểu và
không chấm được.

**Toán tử:** `+` `-` `*` `/` `( )`
**Hàm chuỗi thời gian** (đơn vị `k` = số quý):

| Hàm | Nghĩa |
|---|---|
| `lag(x, k)` | giá trị x của k quý trước |
| `delta(x, k)` | `x - lag(x, k)` |
| `growth(x, k)` | `(x - lag(x,k)) / abs(lag(x,k))` |
| `mean(x, k)` | trung bình x trong k quý gần nhất |
| `std(x, k)` | độ lệch chuẩn x trong k quý gần nhất |

**Hàm lát cắt ngang:** `rank(x)`, `zscore(x)` — chuẩn hoá trong cùng kỳ, trên toàn bộ mã.
**Hàm khác:** `log(x)`, `abs(x)`, `safe_div(a, b)`

**Ràng buộc:** `k ∈ {1, 2, 4, 8}` · độ sâu biểu thức ≤ 6 · số biến khác nhau ≤ 6 ·
mọi phép chia phải dùng `safe_div` · không được là hằng số thuần.

**Format output mô hình phải sinh ra (JSON):**

```json
{
  "name": "accruals_to_assets",
  "formula": "safe_div(net_income - cfo, total_assets)",
  "rationale": "Chênh lệch giữa lợi nhuận kế toán và dòng tiền thực đo chất lượng lợi nhuận",
  "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}
}
```

`source.type` là `line_item` hoặc `note`. Trường này chính là **truy vết nguồn** mà đề cương
yêu cầu (task #16) — bắt mô hình sinh ra từ bây giờ, đừng để P4 mới thêm vào.

### 6.2. Bốn họ prompt

| Họ | Số lượng | Nội dung đưa vào | Mục đích nghiên cứu |
|---|---|---|---|
| **F1** structured-only | 15–20 | Chỉ danh mục biến (không có văn bản) | Nhánh đối chứng của H2 |
| **F2** notes-augmented | 20–25 | Danh mục biến + 1–2 đoạn thuyết minh thật (300–800 từ) | **Nhánh chính**, nuôi H2 và G2 |
| **F3** few-shot | 15–20 | Như F2 + 2–3 ví dụ công thức mẫu | Đo mức cải thiện khi có ví dụ |
| **F4** constrained-format | 10–15 | Như F1 nhưng ép JSON schema nghiêm ngặt, nhắc lại grammar | **Phương án cứu nếu CHỐT 2 trượt** |

F4 không phải để cho đủ số. Task #18 đặt ngưỡng GO/NO-GO là tỷ lệ hợp lệ ≥60%, và phương án
dự phòng ghi sẵn trong timeline là *"chuyển few-shot có ràng buộc grammar, đừng đổi mô hình lần nữa"*.
Muốn dùng phương án đó ở ngày 03/11 thì phải có số đo của nó từ 24/09.

### 6.3. Schema `eval/prompts.jsonl`

```json
{
  "id": "F2-007",
  "family": "F2",
  "ticker": "HPG",
  "year": 2024,
  "context_type": "note",
  "context": "<nguyên văn đoạn thuyết minh đã cắt>",
  "context_source": "data/sample/raw/HPG/2024/thuyet_minh.txt#L120-L180",
  "instruction": "<nguyên văn prompt gửi mô hình>",
  "allowed_vars": ["total_assets", "inventory", "..."],
  "n_formulas": 3,
  "must_reference": ["inventory"],
  "notes": "đoạn nói về trích lập dự phòng giảm giá hàng tồn kho"
}
```

- `n_formulas`: số công thức yêu cầu mỗi lần gọi — đặt **3** cho mọi prompt để tổng
  công thức sinh ra ổn định (~80 prompt × 3 = 240 công thức/mô hình/seed).
- `must_reference`: để trống nếu không ràng buộc. Có giá trị thì validator kiểm thêm.
- `context_source`: **bắt buộc điền** — đây là truy vết nguồn, dùng lại ở demo Streamlit (task #24).

**Phân bổ mẫu:** trải đều trên các mã, không dồn 30 prompt vào một mã.
Mỗi mã có ít nhất 2 prompt, mã tài chính có ít nhất 3.

**Xong khi:** 60–80 dòng JSONL hợp lệ, đủ 4 họ theo tỷ lệ trên, mọi `allowed_vars` đều
tồn tại trong `variables.yaml`, mọi `context_source` trỏ tới file có thật.

---

## 7. Việc 1.5 — Rubric

Không có ground truth cho "công thức đúng", nên chấm theo 4 tiêu chí — 3 tự động, 1 tay:

| # | Tiêu chí | Cách chấm | Kiểu |
|---|---|---|---|
| C1 | Parse được theo DSL | validator | tự động, nhị phân |
| C2 | Mọi biến tồn tại trong `variables.yaml` | validator | tự động, nhị phân |
| C3 | Không trùng công thức đã sinh (dạng chuẩn hoá) | validator | tự động, nhị phân |
| C4 | Có nghĩa kinh tế | người chấm | tay, thang 1–5 |

**Công thức "hợp lệ" = C1 ∧ C2 ∧ C3.** Đây là định nghĩa dùng cho ngưỡng 60% ở CHỐT 2 —
ghi rõ trong rubric để sau này không cãi nhau về cách tính.

**Thang C4:**

| Điểm | Nghĩa |
|---|---|
| 5 | Có cơ sở lý thuyết tài chính rõ, tương đương nhân tố đã công bố |
| 4 | Hợp lý, giải thích được, chưa thấy trong tài liệu |
| 3 | Không sai nhưng tầm thường (ví dụ tỷ số hiển nhiên) |
| 2 | Ghép biến cơ học, khó giải thích |
| 1 | Vô nghĩa hoặc sai đơn vị (cộng chỉ tiêu kỳ với chỉ tiêu thời điểm) |

**Hiệu chỉnh người chấm:** 2 người chấm thử cùng 10 công thức trước. Lệch >1 điểm ở quá 3/10 mẫu
thì phải làm rõ rubric rồi chấm lại. Ghi lại số này — nó là bằng chứng cho khâu HITL (task #17)
và trả lời được câu hỏi trong mục 6 của đề cương ("khâu chuyên gia duyệt nên do nhóm tự làm hay mời người ngoài").

**Schema `eval/manual_scores.csv`:** `formula_id,model,seed,prompt_id,formula,rater,c4_score,comment`

---

## 8. Định nghĩa hoàn thành (DoD)

- [ ] `tickers.csv` đủ 15–20 mã, thoả cả 5 tiêu chí phân tầng
- [ ] Dữ liệu mẫu tải về < 5GB, mở kiểm tra 3 file ngẫu nhiên thấy có bảng số + thuyết minh
- [ ] `variables.yaml` có 40–60 biến, trong đó ≥5 biến lấy từ thuyết minh, mỗi biến `coverage` ≥12/20
- [ ] `prompts.jsonl` 60–80 dòng, đủ 4 họ, validate được bằng script
- [ ] `rubric.md` có định nghĩa "hợp lệ" và thang C4, đã hiệu chỉnh 2 người chấm trên 10 mẫu
- [ ] Chạy thử 1 prompt qua 1 mô hình bất kỳ, ra được JSON đúng format → chứng minh bộ thử dùng được

## 9. Rủi ro

| Rủi ro | Xử lý |
|---|---|
| `allow_patterns` sai → tải nhầm cả kho 194GB | Liệt kê file trước, tải thử 1 mã, kiểm dung lượng rồi mới chạy đủ |
| OCR xấu ở mã nhỏ → không trích được biến | Đã cố ý giữ 3 mã OCR xấu; nếu quá tệ thì hạ `coverage` yêu cầu và ghi vào phần hạn chế |
| Hết giờ ngày 23/09 | Cắt prompt xuống **mức sàn 60**, giữ đủ 4 họ. **Không** cắt `variables.yaml` |
| BCTC ngân hàng không map được danh mục biến | Đã có cờ `is_financial`; báo cáo tỷ lệ hợp lệ tách riêng 2 nhóm |
