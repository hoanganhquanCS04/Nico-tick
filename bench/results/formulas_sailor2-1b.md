# Công thức do `sailor2-1b` sinh ra

Sinh bởi `bench/scripts/inspect_formulas.py` từ `bench/results/formulas.csv`. Nguồn gốc: `bench/results/raw/sailor2-1b__seed*.jsonl`.

- **396** công thức sinh ra (76 prompt × 3 seed × ~3), **94** hợp lệ, **81** công thức khác nhau
- Sạch (≥ 2 biến, không lỗi ngữ nghĩa): **50**, trong đó 42 khác nhau
- Cột *lặp* = số lần cùng công thức (dạng chuẩn hoá) xuất hiện qua các prompt và seed

## Công thức hợp lệ, theo chủ đề prompt

### associates

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `net_income_parent + net_income` | tổ hợp | Khác | — | Lợi nhuận sau thuế của cổ đông công ty mẹ, lợi nhuận sau thuế thu nhập, net_income_parent, net_income_parent |
| 2 | `share_of_associates * total_assets` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Lợi ích cổ đông không kiểm soát tăng trưởng tài sản, ảnh hưởng đến lợi suất cổ phiếu. |
| 1 | `share_of_associates * (total_assets + equity)` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Lợi ích cổ đông không kiểm soát tăng trưởng tài sản, ảnh hưởng đến lợi suất cổ phiếu. |
| 1 | `cfi * market_cap` | tổ hợp | Định giá | nhân với quy mô công ty | Lưu chuyển tiền thuần từ hoạt động đầu tư, ảnh hưởng đến lợi suất cổ phiếu |
| 1 | `financial_income + equity` | tổ hợp | Liên kết / đầu tư tài chính | cộng/trừ chỉ tiêu kỳ với thời điểm | Doanh thu thuần tăng trưởng, lợi nhuận kế toán trước thuế, lợi nhuận sau thuế, lợi nhuận sau thuế thu nhập, lợi nhuận sau thuế của cổ đông công ty mẹ, net_incom |
| 1 | `long_term_investments + investments_associates` | tổ hợp | Liên kết / đầu tư tài chính | — | Đầu tư tài chính dài hạn, bao gồm cả liên doanh, liên kết, lợi nhuận thuần phát sinh trong quý |
| 1 | `pretax_profit + net_income` | tổ hợp | Khác | — | Lợi nhuận kế toán trước thuế, ảnh hưởng đến lợi suất cổ phiếu. |
| 1 | `market_cap` | 1 biến | Định giá | — | Vốn hoá thị trường, ảnh hưởng đến lợi suất cổ phiếu |
| 1 | `net_income_parent` | 1 biến | Khác | — | Lợi nhuận sau thuế của cổ đông công ty mẹ, ảnh hưởng đến lợi suất cổ phiếu |

### bank_loans

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `audit_opinion_qualified` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Ý kiến kiểm toán không phải chấp nhận toàn phần, tác động đến xếp hạng cổ phiếu. |
| 1 | `contingent_liabilities_disclosed` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Thuyết minh nợ tiềm tàng, xếp hạng cao hơn. |
| 1 | `going_concern_flag` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Thuyết minh nghi ngờ khả năng hoạt động liên tục, xếp hạng theo lát cắt ngang. |
| 1 | `growth(cfo, 4)` | 1 biến | Khác | — | CFO tăng trưởng quá nhanh có thể ảnh hưởng đến lợi suất, xếp hạng theo lát cắt ngang. |
| 1 | `related_party_disclosed` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Thuyết minh giao dịch với bên liên quan, giúp đánh giá tác động đến lợi suất. |

### cip

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `market_cap + net_income` | tổ hợp | Định giá | — | Vốn hoá thị trường tăng, giá trị công ty tăng, ảnh hưởng đến lợi nhuận và lợi suất. |
| 2 | `growth(long_term_assets, 4)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Tài sản tăng trưởng quá nhanh, lợi suất giảm, xếp hạng cao hơn. |
| 1 | `cfo - market_cap` | tổ hợp | Định giá | — | Lưu chuyển tiền thuần từ hoạt động kinh doanh, ảnh hưởng đến lợi nhuận và lợi suất, tăng trưởng tài sản và nợ vay. |
| 1 | `cfo - net_income` | tổ hợp | Chất lượng lợi nhuận (dồn tích) | — | Lưu chuyển tiền thuần từ hoạt động kinh doanh, ảnh hưởng đến lợi nhuận và lợi suất. |
| 1 | `long_term_assets + construction_in_progress` | tổ hợp | Đầu tư / tăng trưởng tài sản | — | Đánh giá tổng tài sản dài hạn, tài sản cố định, và tài sản dở dang dài hạn của VGC, bao gồm xây dựng cơ bản dở dang và chu kỳ đầu tư. |
| 1 | `growth(long_term_debt, 4)` | 1 biến | Đòn bẩy / thanh khoản | — | Tài sản dở dang dài hạn tăng trưởng, xếp hạng cao hơn. |

### commitments

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `cash_and_equivalents + contingent_liabilities_disclosed` | tổ hợp | Đòn bẩy / thanh khoản, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tài sản dở dang dài hạn + nợ tiềm tàng, cân bằng lợi nhuận và rủi ro |
| 2 | `total_assets` | 1 biến | Khác | — | Tổng tài sản, phát sinh trong quý |
| 1 | `long_term_debt + contingent_liabilities_disclosed` | tổ hợp | Đòn bẩy / thanh khoản, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Nợ thuê tài chính dài hạn tăng 4 lần, lợi suất giảm 4% |
| 1 | `market_cap + contingent_liabilities_disclosed` | tổ hợp | Định giá, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Vốn hoá thị trường + cam kết, cân bằng lợi nhuận và rủi ro |
| 1 | `total_assets + contingent_liabilities_disclosed` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tăng tài sản 4 lần, nợ tiềm tàng 4 lần, lợi suất giảm 4% |
| 1 | `total_liabilities + contingent_liabilities_disclosed` | tổ hợp | Đòn bẩy / thanh khoản, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tăng nợ tiềm tàng 4 lần, lợi suất giảm 4% |
| 1 | `total_assets + total_liabilities` | tổ hợp | Đòn bẩy / thanh khoản | — | Tổng tài sản + nợ ngoài bảng, cân bằng lợi nhuận và rủi ro |
| 1 | `cfo` | 1 biến | Khác | — | Lưu chuyển tiền thuần, phát sinh trong quý |
| 1 | `equity` | 1 biến | Khác | — | Vốn chủ sở hữu, phát sinh trong quý |
| 1 | `net_income` | 1 biến | Khác | — | Lợi nhuận sau thuế, phát sinh trong quý |
| 1 | `revenue` | 1 biến | Khác | — | Doanh thu thuần, phát sinh trong quý |

### customer_advances

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `cash_and_equivalents + inventory` | tổ hợp | Đòn bẩy / thanh khoản, Vốn lưu động | — | Các khoản phải thu ngắn hạn tăng nhanh, ảnh hưởng đến tổng tài sản và lợi nhuận. |
| 1 | `cash_and_equivalents + customer_advances` | tổ hợp | Đòn bẩy / thanh khoản, Vốn lưu động | — | Dùng biến cash_and_equivalents (tiền và tương đương tiền) và customer_advances (người mua trả tiền trước ngắn hạn) để phân tích doanh thu chưa thực hiện và lợi  |
| 1 | `market_cap + cash_and_equivalents + customer_advances + inventory + total_assets` | tổ hợp | Định giá, Đòn bẩy / thanh khoản, Vốn lưu động | — | Vốn hoá thị trường tăng, ảnh hưởng đến lợi nhuận và doanh thu. |
| 1 | `customer_advances + cash_and_equivalents + inventory + total_assets` | tổ hợp | Đòn bẩy / thanh khoản, Vốn lưu động | — | Người mua trả tiền trước ngắn hạn, ảnh hưởng đến doanh thu và lợi nhuận. |
| 1 | `cash_and_equivalents + inventory + total_assets` | tổ hợp | Đòn bẩy / thanh khoản, Vốn lưu động | — | Tổng tiền và hàng tồn kho tăng nhanh, ảnh hưởng đến lợi nhuận và doanh thu. |
| 1 | `cfo + net_income` | tổ hợp | Chất lượng lợi nhuận (dồn tích) | — | Lưu chuyển tiền thuần từ hoạt động kinh doanh, ảnh hưởng đến lợi nhuận và lợi suất. |
| 1 | `current_liabilities + inventory` | tổ hợp | Đòn bẩy / thanh khoản, Vốn lưu động | — | Nợ ngắn hạn tăng, ảnh hưởng đến doanh thu và lợi nhuận. |
| 1 | `market_cap + current_liabilities` | tổ hợp | Định giá, Đòn bẩy / thanh khoản | — | Vốn hoá thị trường tăng, ảnh hưởng đến lợi nhuận và lợi suất. |
| 1 | `current_liabilities + net_income` | tổ hợp | Đòn bẩy / thanh khoản | cộng/trừ chỉ tiêu kỳ với thời điểm | Dùng current_liabilities (nợ ngắn hạn) và net_income (lợi nhuận gộp) để đánh giá tác động của người mua trả tiền trước ngắn hạn đối với lợi nhuận và doanh thu t |
| 1 | `customer_advances + customer_advances` | 1 biến | Vốn lưu động | — | Người mua trả tiền trước ngắn hạn tăng, ảnh hưởng đến doanh thu và lợi nhuận. |
| 1 | `customer_advances + equity` | tổ hợp | Vốn lưu động | — | Người mua trả tiền trước, xếp hạng dựa trên doanh thu trả trước, doanh thu tương lai, lợi nhuận gộp, lưu chuyển tiền thuần |
| 1 | `customer_advances + inventory` | tổ hợp | Vốn lưu động | — | Người mua trả tiền trước ngắn hạn, ảnh hưởng đến doanh thu và lợi nhuận. |
| 1 | `inventory + net_income` | tổ hợp | Vốn lưu động | cộng/trừ chỉ tiêu kỳ với thời điểm | Dùng inventory (hàng tồn kho) và net_income (doanh thu thuần) để đánh giá tác động của người mua trả tiền trước ngắn hạn đến lợi nhuận và doanh thu tương lai. |
| 1 | `total_assets + inventory` | tổ hợp | Vốn lưu động | — | Tổng tài sản tăng, ảnh hưởng đến doanh thu và lợi nhuận. |
| 1 | `net_income + revenue` | tổ hợp | Khác | — | Lợi nhuận gộp tăng, ảnh hưởng đến lợi nhuận và lợi suất. |
| 1 | `total_assets + total_assets` | 1 biến | Khác | — | Tổng tài sản tăng, ảnh hưởng đến doanh thu và lợi nhuận. |

### debt

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `cash_and_equivalents + current_liabilities` | tổ hợp | Đòn bẩy / thanh khoản | — | Cân bằng giữa tài sản và nợ ngắn hạn, đảm bảo lợi nhuận ổn định. |
| 2 | `current_liabilities + short_term_debt` | tổ hợp | Đòn bẩy / thanh khoản | — | Tăng nợ ngắn hạn, tăng chi phí tài chính, cần kiểm soát chặt chẽ. |
| 2 | `short_term_debt + long_term_debt` | tổ hợp | Đòn bẩy / thanh khoản | — | Vay và nợ thuê tài chính ngắn hạn, dài hạn, cần cân bằng tài chính. |
| 1 | `cash_and_equivalents + interest_expense` | tổ hợp | Đòn bẩy / thanh khoản | cộng/trừ chỉ tiêu kỳ với thời điểm | Tài sản tăng, lợi nhuận thuần tăng, tăng trưởng lợi suất. |
| 1 | `long_term_debt + equity` | tổ hợp | Đòn bẩy / thanh khoản | — | Vay và nợ thuê tài chính dài hạn, tăng lợi nhuận, cần kiểm soát chi phí tài chính. |
| 1 | `total_assets + equity` | tổ hợp | Khác | — | Vốn chủ sở hữu tăng, tăng lợi nhuận, cần duy trì ổn định. |
| 1 | `revenue + financial_expense` | tổ hợp | Khác | — | Doanh thu thuần tăng, chi phí tài chính tăng, cần tối ưu hóa. |
| 1 | `market_cap + interest_expense` | tổ hợp | Định giá, Đòn bẩy / thanh khoản | — | Vốn hoá thị trường tăng, lợi nhuận kế toán tăng, xếp hạng cao hơn. |
| 1 | `growth(total_assets, 4)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Tài sản tăng nhanh, lợi suất giảm, xếp hạng cao hơn. |

### fixed_assets

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 1 | `cfo + growth(total_assets, 4)` | tổ hợp | Đầu tư / tăng trưởng tài sản | — | CFO tăng, lợi nhuận tăng, lợi suất cải thiện. |
| 1 | `total_assets * growth(total_assets, 4)` | 1 biến | Đầu tư / tăng trưởng tài sản | nhân với quy mô công ty | Tài sản tăng trưởng quá nhanh, dẫn đến lợi suất giảm. |
| 1 | `market_cap + growth(total_assets, 4)` | tổ hợp | Định giá, Đầu tư / tăng trưởng tài sản | — | Vốn hoá tăng, lợi nhuận tăng, lợi suất cải thiện. |
| 1 | `total_assets + growth(total_assets, 4)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Tăng trưởng tổng tài sản, lợi nhuận tăng, lợi suất cải thiện. |

### inventory

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 1 | `cogs + inventory_writedown` | tổ hợp | Dự phòng / chất lượng tài sản | cộng/trừ chỉ tiêu kỳ với thời điểm | Giảm giá hàng tồn kho, tác động đến giá vốn hàng bán và lợi nhuận gộp |
| 1 | `current_assets + inventory_gross` | tổ hợp | Vốn lưu động | — | Tăng hàng tồn kho và giảm giá hàng tồn kho, tăng tổng tài sản, cải thiện lợi nhuận gộp và lợi nhuận sau thuế. |
| 1 | `current_assets + inventory_writedown` | tổ hợp | Dự phòng / chất lượng tài sản | — | Tăng trưởng hàng tồn kho dẫn đến tăng tổng tài sản, cải thiện lợi nhuận gộp và lợi nhuận sau thuế. |
| 1 | `current_assets - inventory_writedown` | tổ hợp | Dự phòng / chất lượng tài sản | — | Giảm dự phòng giảm giá, tác động đến nợ ngắn hạn và vốn chủ sở hữu |
| 1 | `customer_advances + inventory_writedown` | tổ hợp | Dự phòng / chất lượng tài sản, Vốn lưu động | — | Tăng trưởng người mua trả tiền trước, tác động đến doanh thu và lợi nhuận |
| 1 | `inventory_writedown * inventory_gross` | tổ hợp | Dự phòng / chất lượng tài sản, Vốn lưu động | nhân với quy mô công ty | Giảm giá hàng tồn kho, tác động đến lợi nhuận gộp và lợi nhuận sau thuế thu nhập. |
| 1 | `inventory_writedown + inventory_gross` | tổ hợp | Dự phòng / chất lượng tài sản, Vốn lưu động | — | Giảm giá hàng tồn kho tăng lên khi tồn kho tăng, ảnh hưởng đến lợi nhuận gộp và lợi nhuận sau thuế. |
| 1 | `net_income + net_income` | 1 biến | Khác | — | Tăng trưởng doanh thu và lợi nhuận, tác động đến lợi nhuận gộp và lợi nhuận sau thuế |

### receivables

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `total_assets - customer_advances` | tổ hợp | Vốn lưu động | — | Phải thu ngắn hạn của khách hàng giảm dần, dự phòng khó đòi tăng, ảnh hưởng đến lợi nhuận gộp và lợi nhuận sau thuế. |
| 1 | `receivables_customers - equity` | tổ hợp | Vốn lưu động | — | Tăng tài sản ngắn hạn, dự phòng khó đòi tăng, ảnh hưởng đến lợi nhuận gộp và doanh thu, tăng vốn chủ sở hữu. |
| 1 | `receivables_customers - revenue` | tổ hợp | Vốn lưu động | cộng/trừ chỉ tiêu kỳ với thời điểm | Tăng tài sản ngắn hạn, dự phòng khó đòi tăng, ảnh hưởng đến lợi nhuận gộp và doanh thu, tăng lợi nhuận sau thuế. |
| 1 | `receivables_customers - total_assets` | tổ hợp | Vốn lưu động | — | Tăng tài sản ngắn hạn, dự phòng khó đòi tăng, ảnh hưởng đến lợi nhuận gộp và doanh thu. |
| 1 | `total_assets - equity` | tổ hợp | Khác | — | Tăng trưởng phải thu ngắn hạn góp phần vào tổng tài sản, tăng trưởng doanh thu và lợi nhuận, giúp xếp hạng cổ phiếu theo chiều tích cực. |
| 1 | `total_assets - gross_profit` | tổ hợp | Khác | cộng/trừ chỉ tiêu kỳ với thời điểm | Tăng trưởng phải thu góp phần vào lợi nhuận gộp, giúp cải thiện lợi nhuận sau thuế, tăng xếp hạng cổ phiếu. |
| 1 | `total_assets - net_income` | tổ hợp | Khác | cộng/trừ chỉ tiêu kỳ với thời điểm | Tăng trưởng phải thu góp phần vào lợi nhuận sau thuế, cải thiện lợi nhuận gộp, tăng xếp hạng cổ phiếu. |
| 1 | `safe_div(provision_doubtful_debt, 10)` | 1 biến | Dự phòng / chất lượng tài sản | — | Dự phòng phải thu khó đòi, tăng khả năng thu hồi khó hơn, giảm lợi suất. |

### related_party

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 1 | `log(total_assets - prepaid_to_suppliers + net_income - cogs)` | tổ hợp | Vốn lưu động | — | Công thức này đo lường lợi nhuận sau thuế thu nhập (cfo) của NTP, giao dịch với các bên liên quan (related_party_disclosed) và các chỉ số tài chính (revenues, e |
| 1 | `safe_div(receivables_customers, total_assets)` | tỷ số | Vốn lưu động | — | Các khoản phải thu ngắn hạn cao cho thấy rủi ro tài chính và lợi suất thấp hơn. |

### segment

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 1 | `total_assets + equity + gross_profit` | tổ hợp | Khác | — | Tăng trưởng tài sản và lợi nhuận gộp đóng góp vào tăng trưởng tổng thể, cải thiện lợi suất. |
| 1 | `gross_revenue + gross_profit` | tổ hợp | Khác | — | Tăng trưởng doanh thu và lợi nhuận gộp dẫn đến tăng trưởng tài sản, cải thiện lợi suất cổ phiếu. |
| 1 | `total_assets + gross_profit + segment_disclosed` | tổ hợp | Cờ thuyết minh | cộng/trừ chỉ tiêu kỳ với thời điểm; dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tăng trưởng tài sản và lợi nhuận gộp trong bộ phận giúp cải thiện lợi nhuận sau thuế, xếp hạng cao hơn. |

## Công thức KHÔNG hợp lệ, theo lỗi

### syntax_error — 129 công thức

- `rank(GAS - tiện ích - năng lượng (khí), zscore(GAS - tiện ích - năng lượng (khí), 16.744.655.874.477), mean(GAS - tiện ích - năng lượng (khí), 11.637.281.488.165)` — F2-004 · syntax_error
- `safe_div(delta(short_term_receivables, 4), mean(total_assets, 4)` — F3-003 · syntax_error
- `rank(x), zscore(x), mean(x) + (1 - 2) * growth(x) + log(x) + abs(x) + safe_div(x, 1.5)` — F2-005 · syntax_error:Tuple
- `safe_div(delta(short_term_receivables, 4), mean(total_assets, 4)` — F3-004 · syntax_error
- `rank(x), zscore(x), mean(x, k)` — F1-005 · syntax_error:Tuple
- `rank(x), zscore(x), mean(x, k) + log(x) + abs(x) + safe_div(x, b)` — F2-006 · syntax_error:Tuple
- `interest_expense(current_liabilities, 100), growth(short_term_debt, 100), growth(long_term_debt, 100)` — F4-004 · syntax_error:Tuple
- `depreciation(revenue, 100), growth(current_liabilities, 100), growth(short_term_debt, 100), growth(long_term_debt, 100)` — F4-004 · syntax_error:Tuple
- `cfo = (market_cap - net_income) / net_income` — F4-004 · syntax_error
- `rank(LA - interest_expense, k=1)` — F1-006 · syntax_error:keyword
- `rank(LA - interest_expense, k=2)` — F1-006 · syntax_error:keyword
- `rank(LA - interest_expense, k=3)` — F1-006 · syntax_error:keyword
- … và 117 công thức khác (xem `bench/results/formulas.csv`)

### missing_field — 46 công thức

- `` — F3-002 · missing_field:name|missing_field:formula|missing_field:rationale|missing_field:source
- `interest_expense` — F2-008 · missing_field:name
- `cash_to_current_liabilities` — F3-006 · missing_field:name|unknown_var:cash_to_current_liabilities
- `net_debt_to_equity` — F3-006 · missing_field:name|unknown_var:net_debt_to_equity
- `accruals_to_assets` — F3-006 · missing_field:name|unknown_var:accruals_to_assets
- `rank(x, 3) - 1` — F2-009 · missing_field:name|missing_field:source|bad_arity:rank|unknown_var:x
- `rank(x, 3) - 1` — F2-009 · missing_field:name|missing_field:source|bad_arity:rank|unknown_var:x|duplicate
- `rank(x, 3) - 1` — F2-009 · missing_field:name|missing_field:source|bad_arity:rank|unknown_var:x|duplicate
- `` — F2-021 · missing_field:name|missing_field:formula|missing_field:rationale
- `inventory_change_to_assets` — F3-002 · missing_field:name|unknown_var:inventory_change_to_assets
- `accruals_to_assets` — F3-002 · missing_field:name|unknown_var:accruals_to_assets
- `rank(x), zscore(x), mean(x, k)` — F2-007 · missing_field:name|syntax_error:Tuple
- … và 34 công thức khác (xem `bench/results/formulas.csv`)

### copied_fewshot — 28 công thức

- `safe_div(cash_and_equivalents, current_liabilities)` — F3-005 · copied_fewshot
- `safe_div(short_term_debt + long_term_debt - cash_and_equivalents, equity)` — F3-005 · copied_fewshot
- `safe_div(construction_in_progress, fixed_assets)` — F3-007 · copied_fewshot
- `safe_div(construction_in_progress, fixed_assets)` — F3-008 · copied_fewshot
- `safe_div(abs(capex), depreciation)` — F3-009 · copied_fewshot
- `safe_div(net_income, market_cap)` — F3-009 · copied_fewshot
- `safe_div(cash_and_equivalents, current_liabilities)` — F3-010 · copied_fewshot
- `delta(safe_div(net_income, mean(equity, 4)), 4)` — F3-019 · copied_fewshot
- `safe_div(equity, market_cap)` — F3-019 · copied_fewshot
- `safe_div(net_income - cfo, total_assets)` — F3-019 · copied_fewshot
- `safe_div(delta(inventory, 4), mean(total_assets, 4))` — F3-001 · copied_fewshot
- `safe_div(cash_and_equivalents, current_liabilities)` — F3-005 · copied_fewshot
- … và 16 công thức khác (xem `bench/results/formulas.csv`)

### unknown_func — 22 công thức

- `rank(x, 2) - (1 - 2) * growth(x, 2) + (1 - 2) * inventory_writedown(x) + (1 - 2) * net_income(x)` — F2-003 · unknown_func:net_income|bad_arity:rank|unknown_func:inventory_writedown|unknown_var:x
- `inventory_writedown(total_assets, 4)` — F4-002 · unknown_func:inventory_writedown
- `rank(LTV, k) + growth(LTV, k) + interest_expense(LTV, k)` — F2-007 · unknown_func:interest_expense|bad_arity:rank|bad_lag:growth|unknown_var:LTV|unknown_var:k
- `asset_growth(total_assets, 4)` — F4-005 · unknown_func:asset_growth
- `asset_growth(total_assets, 4)` — F4-004 · unknown_func:asset_growth
- `interest_expense(current_liabilities, 100)` — F4-004 · unknown_func:interest_expense
- `cash_and_equivalents(total_assets, 100)` — F4-004 · unknown_func:cash_and_equivalents
- `depreciation(100, 100)` — F4-004 · unknown_func:depreciation|constant_only
- `market_cap(net_income, 100)` — F4-004 · unknown_func:market_cap
- `asset_growth(total_assets, 4)` — F4-005 · unknown_func:asset_growth|duplicate
- `interest_expense(current_liabilities, 100)` — F4-005 · unknown_func:interest_expense|duplicate
- `cash_and_equivalents(total_assets, 100)` — F4-005 · unknown_func:cash_and_equivalents|duplicate
- … và 10 công thức khác (xem `bench/results/formulas.csv`)

### not_object — 21 công thức

- `` — F2-002 · not_object
- `` — F2-002 · not_object
- `` — F2-002 · not_object
- `` — F1-003 · not_object
- `` — F1-003 · not_object
- `` — F1-003 · not_object
- `` — F3-012 · not_object
- `` — F3-012 · not_object
- `` — F3-012 · not_object
- `` — F2-012 · not_object
- `` — F2-012 · not_object
- `` — F2-012 · not_object
- … và 9 công thức khác (xem `bench/results/formulas.csv`)

### raw_division — 14 công thức

- `log((short_term_receivables - prepaid_to_suppliers) / prepaid_to_suppliers)` — F4-011 · raw_division
- `log((receivables_customers - net_income) / net_income)` — F4-011 · raw_division
- `log((total_assets - cogs) / cogs)` — F4-011 · raw_division
- `log((payables_suppliers - net_income) / net_income)` — F4-011 · raw_division
- `log((equity - net_income) / net_income)` — F4-011 · raw_division
- `log((cogs - net_income) / net_income)` — F4-011 · raw_division
- `log((net_income - cogs) / cogs)` — F4-011 · raw_division
- `(revenue - receivables_customers) * (receivables_customers - total_assets) / (total_assets - net_income) * 100` — F2-017 · raw_division
- `(revenue - net_income) / (revenue - total_assets) * 100` — F2-017 · raw_division
- `(revenue - net_income) / (revenue - total_assets) * 100` — F2-017 · raw_division|duplicate
- `log((short_term_receivables - prepaid_to_suppliers) / prepaid_to_suppliers)` — F4-011 · raw_division
- `log((receivables_customers - net_income) / net_income)` — F4-011 · raw_division
- … và 2 công thức khác (xem `bench/results/formulas.csv`)

### unknown_var — 12 công thức

- `total_debt + equity` — F4-007 · unknown_var:total_debt
- `(cfo + 1) * growth` — F4-014 · unknown_var:growth
- `audit_opinion_qualified + growth` — F4-014 · unknown_var:growth
- `current_liabilities + current_debt` — F4-004 · unknown_var:current_debt
- `total_depreciation - accumulated_depreciation` — F4-006 · unknown_var:total_depreciation
- `market_cap + total_capex` — F4-006 · unknown_var:total_capex
- `Gross_revenue - Gross_profit` — F4-013 · unknown_var:Gross_profit|unknown_var:Gross_revenue
- `Gross_revenue - Gross_profit` — F4-013 · unknown_var:Gross_profit|unknown_var:Gross_revenue|duplicate
- `Gross_revenue - Gross_profit` — F4-013 · unknown_var:Gross_profit|unknown_var:Gross_revenue|duplicate
- `Gross_revenue - Gross_profit` — F4-013 · unknown_var:Gross_profit|unknown_var:Gross_revenue|duplicate
- `Gross_revenue - Gross_profit` — F4-013 · unknown_var:Gross_profit|unknown_var:Gross_revenue|duplicate
- `pre-tax_profit * 4` — F4-010 · unknown_var:pre|unknown_var:tax_profit

### duplicate — 11 công thức

- `market_cap + net_income` — F4-007 · duplicate
- `growth(total_assets, 4)` — F4-014 · duplicate
- `current_assets + inventory_gross` — F4-002 · duplicate
- `market_cap + net_income` — F4-002 · duplicate
- `market_cap + growth(total_assets, 4)` — F4-006 · duplicate
- `growth(long_term_assets, 4)` — F4-007 · duplicate
- `growth(long_term_assets, 4)` — F4-007 · duplicate
- `growth(long_term_assets, 4)` — F4-007 · duplicate
- `growth(long_term_assets, 4)` — F4-007 · duplicate
- `growth(long_term_assets, 4)` — F4-007 · duplicate
- `long_term_investments + investments_associates` — F1-011 · duplicate

### too_complex — 8 công thức

- `long_term_investments + investments_associates + total_assets + equity + minority_interest + revenue + financial_income + share_of_associates + net_income_parent` — F1-010 · too_complex
- `log(receivables_customers + net_income - cogs + net_income - net_income - net_income)` — F1-012 · too_complex
- `log(total_assets + net_income - cogs + net_income - net_income - net_income)` — F1-012 · too_complex
- `rank(total_assets - equity + net_income - cfo + cfi + related_party_disclosed + audit_opinion_qualified + going_concern_flag + contingent_liabilities_disclosed + market_cap + close_price + shares_outstanding + adv20)` — F1-017 · too_complex
- `(total_assets + equity + net_income + cfo + cfi + related_party_disclosed + audit_opinion_qualified + going_concern_flag + contingent_liabilities_disclosed + market_cap + close_price + shares_outstanding + adv20)` — F2-025 · too_complex
- `(long_term_assets + fixed_assets + equity + revenue + net_income + depreciation + cfo + capex)` — F1-007 · too_complex
- `long_term_investments + investments_associates + total_assets + equity + minority_interest + revenue + financial_income + share_of_associates + net_income + net_income_parent + cfi` — F1-010 · too_complex
- `long_term_investments + investments_associates + total_assets + equity + minority_interest + revenue + financial_income + share_of_associates + net_income + net_income_parent + cfi` — F1-010 · too_complex|duplicate

### bad_arity — 8 công thức

- `rank(x, 1) + (1 - growth(x, 1)) * (1 - growth(x, 2)) + (1 - growth(x, 3)) * (1 - growth(x, 4)) + (1 - growth(x, 5)) * (1 - growth(x, 6))` — F2-001 · bad_arity:rank|bad_lag:growth|unknown_var:x|too_complex
- `rank(x, 3) + (1 - 1) * (total_assets - total_liabilities) * (current_liabilities + short_term_debt + long_term_debt) * interest_expense` — F1-006 · bad_arity:rank|unknown_var:x|too_complex
- `rank(x, 3) + (1 - 1) * (total_assets - total_liabilities) * (current_liabilities + short_term_debt + long_term_debt) * interest_expense` — F1-006 · bad_arity:rank|unknown_var:x|too_complex|duplicate
- `rank(x, 1) * (1 - growth(x, 1)) + log(x) + abs(x) + safe_div(x, 2) + mean(x, 2) + std(x, 2)` — F2-014 · bad_arity:rank|unknown_var:x|too_complex
- `rank(x, 3)` — F1-001 · bad_arity:rank|unknown_var:x
- `rank(current_assets, 1) + (current_assets - inventory_writedown) * (current_assets - inventory_writedown) / (current_assets + inventory_writedown)` — F1-002 · bad_arity:rank|raw_division
- `rank(x, 2) - inventory_writedown + inventory_writedown` — F2-003 · bad_arity:rank|unknown_var:x
- `rank(x, 2) - inventory_writedown + inventory_writedown` — F2-003 · bad_arity:rank|unknown_var:x|duplicate

### bad_lag — 3 công thức

- `rank(x, 3) * (1 - growth(x, 3)) + log(x) + abs(x) + safe_div(x, 3) + mean(x, 3) + std(x, 3)` — F2-014 · bad_lag:std|bad_lag:mean|bad_arity:rank|bad_lag:growth|unknown_var:x|too_complex
- `growth(revenue, 100)` — F4-004 · bad_lag:growth
- `rank(x, 2) - growth(x, 2) + growth(x, 1) + growth(x, 3)` — F2-003 · bad_lag:growth|bad_arity:rank|unknown_var:x

