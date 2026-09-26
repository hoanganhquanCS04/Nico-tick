# Rubric chấm công thức

Dùng cho: chấm tay C4 ở P0 (việc 2.6, 80 công thức trong `eval/c4_blind.csv`) và khâu người duyệt (HITL) ở P4.

## 1. Bốn tiêu chí

Không có "đáp án đúng" cho một công thức nhân tố, nên chấm theo 4 tiêu chí: 3 do máy chấm, 1 do người chấm.

| # | Tiêu chí | Ai chấm | Kiểu |
|---|---|---|---|
| C1 | Viết đúng luật DSL: đúng hàm, đúng số tham số, `k ∈ {1,2,4,8}`, không có `/` trần, lồng ≤ 6 tầng, ≤ 6 biến, không phải hằng số | `bench/scripts/validator.py` | có / không |
| C2 | Mọi biến có trong `config/variables.yaml` | validator | có / không |
| C3 | Không trùng công thức đã sinh (so dạng chuẩn hoá); chép lại ví dụ mẫu của đề F3 cũng tính là trùng | validator | có / không |
| C4 | **Có nghĩa kinh tế** | người | điểm 1–5 |

**Công thức "hợp lệ" = C1 và C2 và C3.** Ngưỡng 60% ở CHỐT 2 tính theo định nghĩa này, chia cho số
công thức **đã yêu cầu** (lượt hỏng tính 0, không bỏ khỏi mẫu số). C4 chỉ chấm trên công thức đã hợp lệ.

## 2. C4 hỏi điều gì

> Đưa công thức này cho một người làm phân tích cổ phiếu. Họ có thấy đây là một cách **hợp lý để xếp hạng
> các công ty** không, và họ có **kể được vì sao** nó liên quan tới lợi suất cổ phiếu không?

C4 **không** hỏi công thức có sinh lời không. Chuyện đó để backtest (P5) trả lời. C4 lọc những công thức
đúng luật nhưng vô nghĩa, loại mà máy không phát hiện được.

## 3. Thang điểm

| Điểm | Nghĩa | Nhận ra bằng cách nào |
|---|---|---|
| **5** | Là, hoặc gần như là, một nhân tố **đã có tên** trong tài liệu | Có trong danh sách mục 5, đúng cách chia |
| **4** | Chưa có tên, nhưng **cơ chế rõ và cụ thể** | Kể được 1 câu "điểm cao thì … vì …" mà người khác gật đầu ngay |
| **3** | Không sai, so được giữa công ty, nhưng **chỉ mô tả cấu trúc**, cơ chế tới lợi suất mờ | Kể được công thức đo cái gì, nhưng không rõ vì sao ảnh hưởng giá |
| **2** | **Ghép cơ học** hoặc thực chất đo **độ to** của công ty | Phải cố lắm mới nghĩ ra câu chuyện, hoặc kết quả vẫn là "số tiền" |
| **1** | **Vô nghĩa hoặc sai bản chất** | Cộng thứ khác loại, đếm trùng, phép tính không giải thích được |

## 4. Quy trình cho từng công thức (khoảng 1 phút)

**Bước 1. Đọc công thức, chưa đọc cột `rationale`.** Biến nào chưa rõ thì tra bảng ở mục 8. Cần biết công ty
nào thì tra `prompt_id` trong `eval/prompts_preview.md`.

**Bước 2. Dọn phần thừa** (không đổi thứ hạng nên coi như không có):
- Nhân / chia với hằng số dương, `log()`: không đổi thứ hạng. `zscore(x) * 1.5` chấm như `zscore(x)`, `market_cap` chấm như `log(market_cap)`.
- `safe_div(x, x)` bằng 1, hay các phép chia lồng triệt tiêu nhau: dọn đi rồi chấm phần còn lại.
  **Phải dọn mới ra nghĩa thì tối đa 4**: AI không tự viết ra ý đó, và dạng lằng nhằng thường hỏng khi mẫu số bằng 0.
- `abs()` bọc quanh biến ghi số âm (dự phòng, capex…): bình thường, không trừ điểm.

**Bước 3. Có lỗi chết không? Có thì cho 1 điểm.** Xét bước này **trước** luật "số tiền" ở bước 4: công thức
vừa sai đơn vị vừa ra số tiền thì là **1**, không phải 2. Đừng dồn mọi thứ vô nghĩa vào mức 2.
- Cộng / trừ **tiền với cờ thuyết minh**: `equity + audit_opinion_qualified`.
- Cộng / trừ **tiền với tỷ lệ hoặc %**: `equity + growth(revenue, 4)`, `inventory - safe_div(cogs, revenue)`.
- Cộng / trừ **số dư cuối kỳ với phát sinh trong kỳ**: `total_assets + net_income` (tài sản là số tại một thời điểm, lợi nhuận là số cộng dồn cả kỳ).
- **Đếm trùng** hoặc cộng những thứ lồng nhau: `revenue + gross_profit` (lợi nhuận gộp nằm sẵn trong doanh thu).
- Cộng những khoản **không cùng nghĩa**, không ai cộng chúng lại trong phân tích: `payables_suppliers + long_term_investments`.

**Bước 4. Kết quả có so được giữa công ty to và công ty nhỏ không?**
Nếu kết quả vẫn là **một số tiền (VND)** thì công thức chủ yếu xếp hạng theo độ to của công ty → **tối đa 2 điểm**.
Các dạng vẫn là số tiền: tổng / hiệu các khoản tiền; `zscore`, `rank`, `abs`, `lag`, `mean`, `delta` của một
khoản tiền; tỷ số nhân với một khoản tiền (`revenue * safe_div(net_income, total_assets)`).
Các dạng so được: tỷ số tiền/tiền (`safe_div`), `growth()`, `rank`/`zscore` của một tỷ số, cờ thuyết minh.
*Ngoại lệ:* **vốn hoá** (`market_cap`, `log(market_cap)`, hay bất kỳ cách viết nào ra đúng vốn hoá) chính là nhân tố quy mô
đã biết. Các số tiền khác (tổng tài sản, doanh thu…) chỉ là quy mô "đội lốt", vẫn tối đa 2.

**Cờ thuyết minh không phải tiền.** Các biến `*_disclosed`, `going_concern_flag`, `audit_opinion_qualified` chỉ là
có / không (hoặc đếm từ khoá), **không phải số tiền nợ tiềm tàng hay số tiền giao dịch bên liên quan**. Vì vậy:
- cờ × tỷ lệ → **không** phải số tiền, chấm theo nghĩa;
- tiền ÷ cờ, cờ ÷ tiền → vẫn là quy mô (hoặc nghịch đảo quy mô) → tối đa 2.

**Bước 5. Kể được cơ chế không?** Thử nói 1 câu: *"Công ty điểm cao thì [rủi ro hơn / lợi nhuận kém chất lượng
hơn / đang rẻ hơn / tăng trưởng mạnh hơn…] vì …"*.
- **Không chấm hướng.** Đảo dấu công thức thì điểm như nhau, mô hình xếp hạng sẽ tự học dấu.
- Không kể được, hoặc phải bịa → **2**.
- Kể được → chọn **3 / 4 / 5** theo bảng mục 3.

**Bước 6. Giờ mới đọc `rationale`.** Nó chỉ để hiểu ý khi công thức mơ hồ. **Không cộng điểm vì lời giải
thích hay**: AI hay bịa. Nếu rationale nói sai về chính công thức thì ghi `rationale lệch` vào comment, giữ nguyên điểm.

**Quy tắc chung**
- **Mảnh yếu nhất quyết định.** Công thức ghép nhiều mảnh, có một mảnh vô nghĩa thì cả công thức theo mảnh đó.
- **Phân vân giữa 2 mức thì chọn mức thấp hơn** và ghi comment. Quy tắc này giúp 2 người chấm gần nhau hơn.
- **Bắt buộc ghi comment** khi cho 1 hoặc 5, hoặc khi phân vân. Chỉ cần vài chữ: "cộng stock + flow", "= accruals Sloan".

## 5. Danh sách nhân tố đã có tên (để nhận ra điểm 5)

| Nhân tố | Dạng trong biến của mình | Nguồn |
|---|---|---|
| Dồn tích (accruals) | `safe_div(net_income - cfo, total_assets)` | Sloan (1996) |
| ROA / ROE | `safe_div(net_income, total_assets)` · `safe_div(net_income, equity)` | Haugen & Baker (1996); Fama & French (2015) |
| Lợi nhuận gộp trên tài sản | `safe_div(gross_profit, total_assets)` | Novy-Marx (2013) |
| Biên lợi nhuận gộp | `safe_div(gross_profit, revenue)` | Piotroski (2000), thành phần F-score |
| Vòng quay tài sản | `safe_div(revenue, total_assets)` | Piotroski (2000) |
| Lợi suất lợi nhuận E/P | `safe_div(net_income, market_cap)` | Basu (1977) |
| Giá trị sổ sách / giá B/M | `safe_div(equity, market_cap)` | Fama & French (1992) |
| Dòng tiền / giá | `safe_div(cfo, market_cap)` | Lakonishok, Shleifer & Vishny (1994) |
| Tăng trưởng tài sản | `growth(total_assets, 4)` | Cooper, Gulen & Schill (2008) |
| Đầu tư (capex) | `safe_div(capex, total_assets)` | Titman, Wei & Xie (2004) |
| Tăng tồn kho | `growth(inventory, 4)` · `safe_div(delta(inventory, 4), total_assets)` | Thomas & Zhang (2002) |
| Đòn bẩy | `safe_div(total_liabilities, total_assets)` · `safe_div(total_assets, equity)` | Bhandari (1988) |
| Tiền mặt nắm giữ | `safe_div(cash_and_equivalents, total_assets)` | Palazzo (2012) |
| Tăng trưởng lợi nhuận / doanh thu | `growth(net_income, 4)` · `growth(revenue, 4)` | Lakonishok et al. (1994) |
| Quy mô | `market_cap` · `log(market_cap)` | Banz (1981) |
| Quán tính giá (momentum) | `growth(close_price, 4)` | Jegadeesh & Titman (1993) |
| Nghi ngờ hoạt động liên tục | `going_concern_flag` | Kausar, Taffler & Tan (2009) |

**Chỉ công thức có trong bảng này (hoặc cho cùng thứ hạng, ví dụ `safe_div(total_liabilities, equity)` xếp hạng y như `safe_div(total_liabilities, total_assets)`) mới được 5.**
Thấy một nhân tố có tên mà bảng chưa có thì ghi comment kèm trích dẫn, cả nhóm quyết định có thêm vào bảng không.
Đúng ý tưởng của một nhân tố trên nhưng **đổi mẫu số không có lý do** (ví dụ dồn tích chia cho TSCĐ hữu hình
thay vì tổng tài sản) thì cho **4**. Chu kỳ `k` khác (1 thay vì 4) không trừ điểm.

## 6. Ví dụ neo cho từng mức

Tự đặt ra để minh hoạ, **không lấy từ 80 công thức cần chấm**.

| Công thức | Điểm | Vì sao |
|---|---|---|
| `safe_div(net_income - cfo, total_assets)` | 5 | Dồn tích Sloan, đúng dạng |
| `safe_div(provision_doubtful_debt, receivables_customers)` | 4 | Tỷ lệ dự phòng nợ khó đòi cao → khách trả chậm, chất lượng doanh thu kém |
| `safe_div(delta(receivables_customers, 4), revenue)` | 4 | Phải thu tăng nhanh so với doanh thu → bán chịu để đẩy doanh số |
| `related_party_disclosed * safe_div(receivables_customers, revenue)` | 4 | Phải thu cao ở công ty có giao dịch bên liên quan → nghi rút tiền qua bên liên quan |
| `safe_div(prepaid_to_suppliers, current_assets)` | 3 | Đo cấu trúc tài sản ngắn hạn, khó nói vì sao ảnh hưởng giá |
| `safe_div(short_term_investments, total_assets)` | 3 | Như trên |
| `zscore(revenue)` | 2 | Vẫn là số tiền → xếp theo độ to công ty |
| `revenue * safe_div(net_income, total_assets)` | 2 | ROA nhân với doanh thu → quay lại số tiền |
| `safe_div(cogs, share_capital)` | 2 | Tỷ số được nhưng tử và mẫu không liên quan |
| `total_assets + net_income` | 1 | Cộng số dư cuối kỳ với phát sinh trong kỳ |
| `revenue + gross_profit` | 1 | Đếm trùng |
| `equity + audit_opinion_qualified` | 1 | Cộng tiền với cờ thuyết minh |

## 7. Cách chấm cả nhóm (P0)

**Ai chấm:** 2 người chấm **độc lập** cả 80 công thức (đề xuất: Thắng và Trung). Quân làm trọng tài cho các
công thức lệch nhau, không chấm trực tiếp: Quân đã xem output mô hình quá nhiều nên dễ đoán ra mô hình qua
"văn phong", mất tính mù.

**Luật mù:** không mở `eval/c4_key.csv`, và **không mở `bench/results/formulas*.csv` / `formulas_*.md`** (các file đó
có tên mô hình cạnh từng công thức). Không bàn nhau, không xem file của người kia hay `eval/c4_ai_claude.csv`
trước khi gộp điểm. **Không điền thẳng vào `eval/c4_blind.csv`**: đó là file trắng dùng chung.

**Công cụ:** mỗi người tạo 1 Google Sheet → Tệp → Nhập → Tải lên `eval/c4_blind.csv` → điền cột `rater`,
`c4_score`, `comment` → Tệp → Tải xuống → CSV → lưu thành `eval/c4_scores_<tên không dấu>.csv`
(ví dụ `c4_scores_thang.csv`). Đừng mở file CSV bằng Excel: file không có BOM nên Excel hiển thị lỗi phông
tiếng Việt, và máy cài tiếng Việt còn tách cột bằng dấu `;`.

**Các bước:**
1. **Hiệu chỉnh (V06):** cả 2 chấm C001–C010, rồi chạy `python bench/scripts/c4_merge.py --only C001-C010`.
   Nếu **quá 3/10 công thức lệch từ 2 điểm trở lên**: ngồi lại xem lệch ở đâu, thêm quy tắc hoặc ví dụ vào
   rubric này, rồi chấm lại 10 mẫu đó. Không lệch nhiều thì đi tiếp.
2. **Chấm hết (V07):** C011–C080, độc lập, chia 2 buổi (chấm liền 80 cái thì cuối buổi dễ chấm ẩu).
3. **Gộp:** `python bench/scripts/c4_merge.py`. Script in mức đồng thuận và danh sách công thức lệch ≥2 điểm.
4. **Trọng tài:** 3 người xem các công thức lệch, thống nhất điểm, ghi vào `eval/c4_consensus.csv`
   (`formula_id,c4_score,comment`). **Không sửa file điểm của từng người**: số đồng thuận báo cáo phải là số
   trước khi bàn.
5. Chạy lại `c4_merge.py`. Chỉ khi mọi công thức đã có điểm cuối, script mới mở khoá tên mô hình và ghi
   `bench/results/c4.md` để điền tờ trình.

Điểm cuối mỗi công thức = điểm trọng tài nếu có, không thì trung bình 2 người.

## 8. Tra hàm và biến

**Tra biến nhanh nhất:** mở `eval/prompts_preview.md`, tìm `### <prompt_id>` (ví dụ `### F4-001`). Ở đó có tên
công ty, chủ đề, và đúng danh sách biến mà AI nhận được, kèm nghĩa và loại (số dư / phát sinh / ghi số âm).

**Đọc hàm** (k là số quý: 1 = quý trước, 4 = cùng kỳ năm trước):

| Hàm | Đọc là | Kết quả còn là số tiền? |
|---|---|---|
| `safe_div(a, b)` | a chia b | Không, nếu a và b đều là tiền |
| `lag(x, k)` | x của k quý trước | Còn |
| `delta(x, k)` | x bây giờ trừ x của k quý trước (tăng bao nhiêu đồng) | Còn, nếu x là tiền |
| `growth(x, k)` | x tăng bao nhiêu % so với k quý trước | Không |
| `mean(x, k)` · `std(x, k)` | trung bình · độ dao động của k quý gần nhất | Còn, nếu x là tiền |
| `rank(x)` | thứ hạng của x giữa mọi công ty trong cùng quý | Không đổi bản chất: rank của tiền vẫn là xếp theo độ to |
| `zscore(x)` | x cao hơn mức trung bình các công ty bao nhiêu | Như `rank` |
| `log(x)` · `abs(x)` | logarit · bỏ dấu âm | `log` của tiền vẫn đo độ to |

Đọc công thức **từ trong ra ngoài** và dịch thành một câu tiếng Việt trước khi chấm. Không dịch nổi thành
câu có nghĩa thì thường là ≤ 2 điểm.

**Tra biến theo tên:** nguồn `config/variables.yaml`. **Số dư** = số tại thời điểm cuối kỳ (bảng cân đối). **Phát sinh** = số cộng dồn
trong kỳ (kết quả kinh doanh, lưu chuyển tiền). **Cờ thuyết minh** = điểm có / không hoặc đếm từ khoá,
không phải tiền. Cột "Âm" đánh dấu biến ghi số âm trong BCTC.

<details><summary>65 biến (bấm để mở)</summary>

| Biến | Nghĩa | Loại | Âm |
|---|---|---|---|
| `current_assets` | TÀI SẢN NGẮN HẠN | số dư |  |
| `cash_and_equivalents` | Tiền và các khoản tương đương tiền | số dư |  |
| `short_term_investments` | Đầu tư tài chính ngắn hạn | số dư |  |
| `short_term_receivables` | Các khoản phải thu ngắn hạn | số dư |  |
| `receivables_customers` | Phải thu ngắn hạn của khách hàng | số dư |  |
| `prepaid_to_suppliers` | Trả trước cho người bán ngắn hạn | số dư |  |
| `provision_doubtful_debt` | Dự phòng phải thu ngắn hạn khó đòi | số dư | âm |
| `inventory` | Hàng tồn kho (thuần) | số dư |  |
| `inventory_gross` | Hàng tồn kho (gốc, trước dự phòng) | số dư |  |
| `inventory_writedown` | Dự phòng giảm giá hàng tồn kho | số dư | âm |
| `long_term_assets` | TÀI SẢN DÀI HẠN | số dư |  |
| `fixed_assets` | Tài sản cố định | số dư |  |
| `tangible_fixed_assets` | Tài sản cố định hữu hình | số dư |  |
| `accumulated_depreciation` | Giá trị hao mòn luỹ kế | số dư | âm |
| `construction_in_progress` | Tài sản dở dang dài hạn | số dư |  |
| `long_term_investments` | Đầu tư tài chính dài hạn | số dư |  |
| `investments_associates` | Đầu tư vào công ty liên doanh, liên kết | số dư |  |
| `total_assets` | TỔNG CỘNG TÀI SẢN | số dư |  |
| `total_liabilities` | NỢ PHẢI TRẢ | số dư |  |
| `current_liabilities` | Nợ ngắn hạn | số dư |  |
| `payables_suppliers` | Phải trả người bán ngắn hạn | số dư |  |
| `customer_advances` | Người mua trả tiền trước ngắn hạn | số dư |  |
| `short_term_debt` | Vay và nợ thuê tài chính ngắn hạn | số dư |  |
| `long_term_liabilities` | Nợ dài hạn | số dư |  |
| `long_term_debt` | Vay và nợ thuê tài chính dài hạn | số dư |  |
| `equity` | VỐN CHỦ SỞ HỮU | số dư |  |
| `share_capital` | Vốn góp của chủ sở hữu | số dư |  |
| `retained_earnings` | Lợi nhuận sau thuế chưa phân phối | số dư |  |
| `minority_interest` | Lợi ích cổ đông không kiểm soát | số dư |  |
| `total_resources` | TỔNG CỘNG NGUỒN VỐN | số dư |  |
| `gross_revenue` | Doanh thu bán hàng và cung cấp dịch vụ | phát sinh |  |
| `revenue_deductions` | Các khoản giảm trừ doanh thu | phát sinh |  |
| `revenue` | Doanh thu thuần | phát sinh |  |
| `cogs` | Giá vốn hàng bán | phát sinh |  |
| `gross_profit` | Lợi nhuận gộp | phát sinh |  |
| `financial_income` | Doanh thu hoạt động tài chính | phát sinh |  |
| `financial_expense` | Chi phí tài chính | phát sinh |  |
| `interest_expense` | Chi phí lãi vay | phát sinh |  |
| `share_of_associates` | Phần lãi lỗ trong công ty liên doanh, liên kết | phát sinh |  |
| `selling_expense` | Chi phí bán hàng | phát sinh |  |
| `admin_expense` | Chi phí quản lý doanh nghiệp | phát sinh |  |
| `operating_profit` | Lợi nhuận thuần từ hoạt động kinh doanh | phát sinh |  |
| `other_income` | Thu nhập khác | phát sinh |  |
| `pretax_profit` | Tổng lợi nhuận kế toán trước thuế | phát sinh |  |
| `current_tax_expense` | Chi phí thuế TNDN hiện hành | phát sinh |  |
| `net_income` | Lợi nhuận sau thuế thu nhập doanh nghiệp | phát sinh |  |
| `net_income_parent` | Lợi nhuận sau thuế của cổ đông công ty mẹ | phát sinh |  |
| `eps_basic` | Lãi cơ bản trên cổ phiếu | phát sinh |  |
| `depreciation` | Khấu hao tài sản cố định | phát sinh |  |
| `cfo` | Lưu chuyển tiền thuần từ hoạt động kinh doanh | phát sinh |  |
| `capex` | Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác | phát sinh | âm |
| `cfi` | Lưu chuyển tiền thuần từ hoạt động đầu tư | phát sinh |  |
| `dividends_paid` | Cổ tức, lợi nhuận đã trả cho chủ sở hữu | phát sinh | âm |
| `cff` | Lưu chuyển tiền thuần từ hoạt động tài chính | phát sinh |  |
| `net_cash_change` | Lưu chuyển tiền thuần trong kỳ | phát sinh |  |
| `cash_end` | Tiền và tương đương tiền cuối kỳ | số dư |  |
| `related_party_disclosed` | Có thuyết minh giao dịch với bên liên quan | cờ thuyết minh |  |
| `audit_opinion_qualified` | Ý kiến kiểm toán không phải chấp nhận toàn phần | cờ thuyết minh |  |
| `going_concern_flag` | Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục | cờ thuyết minh |  |
| `segment_disclosed` | Có thuyết minh bộ phận theo lĩnh vực hoặc khu vực | cờ thuyết minh |  |
| `contingent_liabilities_disclosed` | Có thuyết minh nợ tiềm tàng hoặc cam kết | cờ thuyết minh |  |
| `market_cap` | Vốn hoá thị trường | thị trường |  |
| `close_price` | Giá đóng cửa | thị trường |  |
| `shares_outstanding` | Số cổ phiếu đang lưu hành | thị trường |  |
| `adv20` | Giá trị giao dịch bình quân 20 phiên | thị trường |  |

</details>
