# Công thức do `qwen35-0.8b` sinh ra

Sinh bởi `bench/scripts/inspect_formulas.py` từ `bench/results/formulas.csv`. Nguồn gốc: `bench/results/raw/qwen35-0.8b__seed*.jsonl`.

- **628** công thức sinh ra (76 prompt × 3 seed × ~3), **111** hợp lệ, **79** công thức khác nhau
- Sạch (≥ 2 biến, không lỗi ngữ nghĩa): **58**, trong đó 45 khác nhau
- Cột *lặp* = số lần cùng công thức (dạng chuẩn hoá) xuất hiện qua các prompt và seed

## Công thức hợp lệ, theo chủ đề prompt

### associates

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `safe_div(market_cap, growth(total_assets, 4))` | tỷ số | Định giá, Đầu tư / tăng trưởng tài sản | — | Lợi suất trên vốn hóa cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời, nhưng khi công ty mở rộng tài sản quá nhanh, lợi suất có thể bị đẩy cao. |
| 2 | `safe_div(net_income, share_of_associates)` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Lợi nhuận từ công ty liên kết chiếm tỷ trọng lớn trong lợi nhuận, cho thấy lợi suất cổ phiếu phụ thuộc nhiều vào phần lợi nhuận từ công ty này thay vì lợi nhuận |
| 2 | `safe_div(net_income_parent, equity)` | tỷ số | Sinh lời | — | Lợi nhuận của cổ đông mẹ là chỉ số phản ánh hiệu quả đầu tư của công ty mẹ và khả năng tái cấu trúc vốn cho công ty liên kết. |
| 2 | `safe_div(share_of_associates, equity)` | tỷ số | Liên kết / đầu tư tài chính | — | So sánh phần lợi ích của liên kết với vốn chủ sở hữu để đánh giá rủi ro. |
| 2 | `safe_div(share_of_associates, growth(total_assets, 4))` | tỷ số | Đầu tư / tăng trưởng tài sản, Liên kết / đầu tư tài chính | — | Lợi nhuận từ công ty liên kết tăng trưởng quá nhanh so với tổng tài sản, cho thấy công ty này có khả năng tăng trưởng mạnh nhưng lợi suất cổ phiếu có thể bị đẩy |
| 1 | `safe_div(market_cap, equity)` | tỷ số | Định giá | — | Vốn hoá thị trường là chỉ số cơ bản để so sánh mức độ rủi ro và khả năng sinh lời của công ty liên kết với các công ty khác. |
| 1 | `safe_div(net_income_parent, share_of_associates)` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Lợi nhuận của cổ đông công ty mẹ so với phần lợi ích của công ty liên kết cho thấy tỷ lệ chia cổ phần của công ty mẹ lớn hơn tỷ lệ của công ty liên kết. |
| 1 | `share_of_associates` | 1 biến | Liên kết / đầu tư tài chính | — | Phần lợi nhuận của công ty liên doanh liên kết là yếu tố then chốt trong đầu tư liên kết. |

### bank_loans

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 1 | `delta(safe_div(net_income - cfo, total_assets), 4)` | biến đổi của tỷ số | Chất lượng lợi nhuận (dồn tích), Sinh lời | — | Lợi suất tăng trên vốn chủ so với cùng kỳ năm trước báo hiệu chất lượng hoạt động đi lên. |
| 1 | `growth(equity, 4)` | 1 biến | Khác | — | Tăng trưởng vốn chủ sở hữu nhanh thường đi kèm lợi suất cổ phiếu cao, giúp xác định mức độ rủi ro vốn. |
| 1 | `growth(pretax_profit, 4)` | 1 biến | Khác | — | Tăng trưởng lợi nhuận trước thuế thường đi kèm lợi suất cổ phiếu cao, giúp xác định mức độ rủi ro lợi nhuận. |
| 1 | `safe_div(net_income - cfo, cfo)` | tỷ số | Chất lượng lợi nhuận (dồn tích), Sinh lời | — | Cải thiện tỷ suất sinh lời trên vốn chủ so với cùng kỳ năm trước báo hiệu chất lượng hoạt động đi lên. |
| 1 | `safe_div(net_income - cfo, equity)` | tỷ số | Chất lượng lợi nhuận (dồn tích), Sinh lời | — | Giá trị sổ sách cao so với vốn hoá là nhân tố giá trị kinh điển (Fama & French 1992). |
| 1 | `safe_div(cfo, equity)` | tỷ số | Khác | — | Lợi nhuận từ dòng tiền thuần (cfo) cao hơn so với vốn chủ sở hữu (equity) cho thấy doanh nghiệp có khả năng phục hồi tốt hơn và chất lượng lợi nhuận cao hơn. |
| 1 | `safe_div(cfo, net_income)` | tỷ số | Chất lượng lợi nhuận (dồn tích), Sinh lời | — | Lợi nhuận từ dòng tiền thuần (cfo) là chỉ tiêu cơ bản cho chất lượng lợi nhuận, giúp xác định mức độ hiệu quả của hoạt động kinh doanh và khả năng phục hồi của  |
| 1 | `safe_div(equity, total_assets)` | tỷ số | Khác | — | Lợi nhuận cao nhưng tài sản lớn làm giảm tỷ suất sinh lời trên vốn, phù hợp với mô hình Fama & French 1992. |

### cip

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `safe_div(depreciation, total_assets)` | tỷ số | Khác | — | Chi khấu hao tài sản cố định cho thấy doanh nghiệp đang mở rộng năng lực, lợi suất ngắn hạn thường thấp hơn (Titman, Wei, Xie 2004). |
| 1 | `depreciation` | 1 biến | Khác | — | Khấu hao tài sản cố định ảnh hưởng trực tiếp đến lợi suất. |
| 1 | `growth(market_cap, 4)` | 1 biến | Định giá | — | Tăng trưởng vốn hóa thị trường cho thấy khả năng tăng trưởng của giá trị cổ phiếu. |
| 1 | `growth(net_income, 4)` | 1 biến | Khác | — | Tăng trưởng lợi nhuận cho thấy khả năng tăng trưởng lợi nhuận của doanh nghiệp. |
| 1 | `growth(tangible_fixed_assets, 4)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Tăng trưởng tài sản hữu hình trực tiếp ảnh hưởng lớn đến tỷ suất vốn hóa và khả năng tái cấu trúc vốn. |

### commitments

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `contingent_liabilities_disclosed` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Doanh nghiệp có cam kết nợ tiềm tàng hoặc khoản mục ngoài bảng thường có lợi suất sau đó thấp hơn, dẫn đến việc cổ phiếu bị đẩy cao hơn (Cooper, Gulen, Schill 2 |
| 2 | `growth(cfo, 4)` | 1 biến | Khác | — | Lợi nhuận từ hoạt động kinh doanh tăng trưởng thường phản ánh hiệu quả tài chính và khả năng phục hồi của doanh nghiệp. |
| 1 | `contingent_liabilities_disclosed + (long_term_debt * 0.5) + (market_cap * 0.5)` | tổ hợp | Định giá, Đòn bẩy / thanh khoản, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Kết hợp các yếu tố rủi ro từ cam kết, nợ dài hạn và vốn hóa thị trường để xây dựng một chỉ số tổng thể rủi ro toàn diện cho cổ phiếu. |
| 1 | `contingent_liabilities_disclosed + (long_term_debt * 0.5)` | tổ hợp | Đòn bẩy / thanh khoản, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Đưa ra tổng nợ tiềm tàng và nợ thuê dài hạn để đánh giá mức độ rủi ro từ các cam kết mua bán khí cụ thể, ảnh hưởng trực tiếp đến lợi suất. |
| 1 | `cfo + net_income + equity` | tổ hợp | Chất lượng lợi nhuận (dồn tích) | — | Dòng tiền và lợi nhuận (bao gồm cả dòng tiền thuần từ hoạt động kinh doanh và lợi nhuận sau thuế) là các chỉ số quan trọng phản ánh khả năng sinh lời và khả năn |
| 1 | `total_assets + total_liabilities + equity` | tổ hợp | Đòn bẩy / thanh khoản | — | Tổng tài sản và nợ (bao gồm cả tài sản dở dang và nợ phải trả) là yếu tố then chốt trong việc xác định khả năng thanh toán. Khi tổng tài sản và nợ cao hơn, doan |
| 1 | `growth(total_liabilities, 4)` | 1 biến | Đòn bẩy / thanh khoản | — | Tăng trưởng tổng nợ phải trả cho thấy áp lực thanh toán và khả năng thanh toán của doanh nghiệp. |
| 1 | `safe_div(cash_and_equivalents, total_assets)` | tỷ số | Đòn bẩy / thanh khoản | — | Phần tài sản và tiền tương đương là nguồn tài chính chính, giúp xác định mức độ rủi ro và khả năng thanh toán. Khi tỷ số này tăng lên, cổ phiếu thường có chất l |
| 1 | `safe_div(contingent_liabilities_disclosed, equity)` | tỷ số | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Nợ tiềm tàng và cam kết là khoản chi phí lớn nhất đối với doanh nghiệp, ảnh hưởng trực tiếp đến lợi nhuận và khả năng thanh toán. Việc phân tích nó giúp xác địn |
| 1 | `safe_div(net_income, total_liabilities)` | tỷ số | Sinh lời, Đòn bẩy / thanh khoản | — | Lợi nhuận sau thuế thu nhập doanh nghiệp là chỉ tiêu cơ bản cho việc phân tích lợi suất. Khi lợi nhuận cao hơn so với nợ, cổ phiếu thường có chất lượng tốt hơn  |

### customer_advances

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `safe_div(cfo, total_assets)` | tỷ số | Khác | — | Lợi suất tương lai từ dòng tiền phản ánh khả năng thanh toán của doanh nghiệp, chất lượng lợi nhuận và khả năng sinh lời tương lai. |
| 1 | `growth(customer_advances, 4)` | 1 biến | Vốn lưu động | — | Tăng tỷ trọng của khoản phải thu trước giúp xác định khả năng trả nợ ngắn hạn của doanh nghiệp. |
| 1 | `safe_div(cfo, market_cap)` | tỷ số | Định giá | — | Lợi suất từ dòng tiền so với vốn hóa cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời. |
| 1 | `safe_div(gross_profit, market_cap)` | tỷ số | Định giá, Sinh lời | — | Lợi nhuận gộp trên mỗi đồng vốn hóa cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời, giúp xác định mức độ rủi ro khi doanh thu thực hiện chậm lại. |
| 1 | `safe_div(gross_profit, revenue)` | tỷ số | Sinh lời | — | Lợi nhuận gộp trên tổng doanh thu cho thấy hiệu quả kinh doanh và khả năng sinh lời của doanh nghiệp. |
| 1 | `safe_div(market_cap, net_income)` | tỷ số | Định giá, Sinh lời | — | Lợi suất vốn (Vốn hóa thị trường) so với lợi nhuận cho thấy mức độ rủi ro và khả năng sinh lời của cổ phiếu. Giá trị vốn cao hơn lợi nhuận sẽ làm giảm lợi suất. |
| 1 | `safe_div(net_income, cfo)` | tỷ số | Chất lượng lợi nhuận (dồn tích), Sinh lời | — | Lợi nhuận sau thuế trên lưu chuyển tiền thuần cho thấy khả năng thanh toán thực tế và chất lượng lợi nhuận. |

### debt

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(cash_and_equivalents, 4)` | 1 biến | Đòn bẩy / thanh khoản | — | Tăng trưởng dòng tiền thuần thường phản ánh khả năng thanh toán nợ ngắn hạn và phát sinh lợi nhuận. |
| 3 | `growth(depreciation, 4)` | 1 biến | Khác | — | Tăng trưởng khấu hao tài sản cố định thường đi kèm lợi suất thấp hơn, phản ánh hiệu quả tài sản. |
| 3 | `growth(total_assets, 4)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Tăng tổng tài sản có thể làm tăng lợi suất cổ phiếu, đặc biệt khi so sánh với lợi nhuận thuần. |
| 1 | `total_assets - total_liabilities + equity` | tổ hợp | Đòn bẩy / thanh khoản | — | Công thức này tính hiệu quả tài chính bằng cách trừ nợ ngắn hạn và tổng tài sản để lấy chỉ số vốn hóa. Hiệu quả này giúp đánh giá mức độ thanh toán nợ ngắn hạn  |
| 1 | `net_income + depreciation + cfo + market_cap` | tổ hợp | Chất lượng lợi nhuận (dồn tích), Định giá | — | Lợi nhuận thuần (net_income) là chỉ số trực tiếp phản ánh hiệu quả kinh doanh. Khi kết hợp với các biến hỗ trợ như chi phí tài chính và vốn hóa thị trường, nó g |
| 1 | `safe_div(interest_expense, total_assets)` | tỷ số | Đòn bẩy / thanh khoản | — | Chi phí lãi vay tỷ lệ cao làm giảm lợi nhuận ròng, tăng rủi ro tài chính và hạn chế khả năng tái tạo vốn. |

### fin_assets

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 1 | `close_price * shares_outstanding` | tổ hợp | Định giá | nhân với quy mô công ty | Giá trị thị trường cho thấy tiềm năng tăng trưởng của cổ phiếu. |

### fixed_assets

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `market_cap` | 1 biến | Định giá | — | Giá trị vốn hóa thị trường ảnh hưởng trực tiếp đến lợi suất. |
| 2 | `safe_div(cfo, capex)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Phân tích dòng tiền thuần từ hoạt động kinh doanh so với chi phí mua sắm, xây dựng TSCĐ và tài sản dài hạn khác. Tỷ trọng cao cho thấy dòng tiền mang lại hiệu q |
| 2 | `safe_div(tangible_fixed_assets, fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ trọng tài sản cố định hữu hình so với tài sản cố định tổng. Tỷ trọng cao cho thấy tài sản cố định hữu hình chiếm tỷ trọng lớn hơn trong tổng tài sản, có thể  |
| 1 | `safe_div(net_income - cfo, fixed_assets)` | tỷ số | Chất lượng lợi nhuận (dồn tích), Sinh lời, Đầu tư / tăng trưởng tài sản | — | Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996). |
| 1 | `safe_div(net_income - cfo, tangible_fixed_assets)` | tỷ số | Chất lượng lợi nhuận (dồn tích), Sinh lời, Đầu tư / tăng trưởng tài sản | — | Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996). |
| 1 | `safe_div(depreciation, accumulated_depreciation)` | tỷ số | Khác | — | Lợi suất khấu hao cao cho thấy tài sản cố định bị khấu hao nhanh, có thể dẫn đến giảm giá trị tài sản và tăng rủi ro thanh toán. |
| 1 | `safe_div(fixed_assets, capex)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ trọng tài sản cố định so với chi phí mua sắm, xây dựng TSCĐ và tài sản dài hạn khác. Tỷ trọng cao cho thấy tài sản cố định đóng góp lớn vào tổng chi phí đầu  |
| 1 | `safe_div(fixed_assets, total_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ trọng cao cho thấy tài sản cố định chiếm tỷ trọng lớn trong tổng vốn, phản ánh mức độ rủi ro và khả năng thanh toán vốn. |
| 1 | `safe_div(long_term_assets, fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ trọng cao cho thấy phần lớn tài sản cố định là tài sản dài hạn, phản ánh khả năng phát triển bền vững và khả năng sinh lời của công ty. |
| 1 | `safe_div(total_assets, fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ trọng cao cho thấy tổng tài sản bao gồm cả tài sản cố định và tài sản dài hạn, phản ánh cấu trúc tài sản tổng thể của công ty. |

### inventory

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `growth(inventory, 4)` | 1 biến | Vốn lưu động | — | Lăng động tăng trưởng hàng tồn kho thường phản ánh hiệu quả quản lý và khả năng phục hồi của doanh nghiệp. |
| 2 | `growth(inventory_writedown, 4)` | 1 biến | Dự phòng / chất lượng tài sản | — | Lợi suất giảm giá hàng tồn kho tăng quá nhanh thường đi kèm lợi suất thấp hơn. |
| 2 | `safe_div(inventory_writedown, mean(total_assets, 4))` | tỷ số | Dự phòng / chất lượng tài sản | — | Tồn kho giảm giá nhanh hơn quy mô tài sản báo hiệu hàng bán chậm, dự báo lợi suất thấp hơn (Thomas & Zhang 2002). |
| 2 | `safe_div(inventory_writedown, total_assets)` | tỷ số | Dự phòng / chất lượng tài sản | — | Tồn kho giảm giá nhanh hơn quy mô tài sản báo hiệu hàng bán chậm, dự báo lợi suất thấp hơn (Thomas & Zhang 2002). |
| 1 | `abs(inventory_writedown)` | 1 biến | Dự phòng / chất lượng tài sản | chỉ là quy mô (không chuẩn hoá) | Giảm giá hàng tồn kho thường đi kèm với nợ ngắn hạn, giúp xác định khả năng thanh toán nợ trước. |
| 1 | `growth(inventory_gross, 4)` | 1 biến | Vốn lưu động | — | Tăng trưởng giá vốn hàng tồn kho thường là dấu hiệu của sự gia tăng nhu cầu hoặc cải thiện chất lượng, giúp doanh nghiệp có thể dự báo xu hướng tăng trưởng dài  |
| 1 | `mean(inventory, 4)` | 1 biến | Vốn lưu động | — | Độ trung bình của giá vốn hàng tồn kho cho thấy mức độ biến động của giá trị hàng tồn kho trong kỳ, giúp doanh nghiệp xác định được mức độ rủi ro và khả năng qu |
| 1 | `zscore(inventory)` | 1 biến | Vốn lưu động | — | Z-score giúp xác định mức độ rủi ro của dòng vốn từ hàng tồn kho, đánh giá khả năng thanh toán trước. |

### receivables

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(receivables_customers, 4)` | 1 biến | Vốn lưu động | — | Tăng trưởng số dư phải thu ngắn hạn của khách hàng phản ánh khả năng thu hồi tài sản và khả năng thu hút khách hàng mới, giúp xác định xu hướng tăng trưởng doan |
| 3 | `zscore(receivables_customers)` | 1 biến | Vốn lưu động | — | Z-score đo lường mức độ lệch chuẩn so với trung bình, giúp xác định mức độ rủi ro và khả năng thu hồi của khoản phải thu ngắn hạn của khách hàng. |
| 1 | `total_assets - provision_doubtful_debt` | tổ hợp | Dự phòng / chất lượng tài sản | — | Tổng tài sản ngắn hạn (total_assets) là nguồn tài sản chủ động, trong khi dự phòng nợ khó đòi (provision_doubtful_debt) là khoản chi phí để giảm thiểu rủi ro. V |
| 1 | `abs(receivables_customers)` | 1 biến | Vốn lưu động | chỉ là quy mô (không chuẩn hoá) | Giá trị tuyệt đối của số dư phải thu ngắn hạn của khách hàng phản ánh mức độ rủi ro về khả năng thu hồi tài sản. |

### related_party

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `related_party_disclosed` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Công ty có các giao dịch chủ yếu với các bên liên quan như nhau, nhưng công ty TNHH Thương mại Xuất nhập khẩu Minh Hải có giao dịch với công ty Cổ phần Nhựa Thi |
| 1 | `growth(revenue, 4)` | 1 biến | Khác | — | Tăng trưởng doanh thu thuần thường phản ánh sức mạnh thương mại và khả năng phục hồi. |
| 1 | `safe_div(cfo, receivables_customers)` | tỷ số | Vốn lưu động | — | Lực lượng thanh toán từ hoạt động kinh doanh so với số dư phải thu ngắn hạn cho thấy khả năng thanh toán. |

### segment

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `growth(gross_profit, 4)` | 1 biến | Khác | — | Lợi nhuận gộp tăng trưởng thường là dấu hiệu của hiệu quả kinh doanh và khả năng tái sử dụng vốn. |

### tax

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(current_tax_expense, revenue)` | tỷ số | Khác | — | Tỷ trọng chi phí thuế TNDN hiện hành so với doanh thu phát sinh trong kỳ cho thấy mức độ chi phí này có thể ảnh hưởng trực tiếp đến lợi nhuận thực tế và khả năn |
| 1 | `retained_earnings + net_income - current_tax_expense` | tổ hợp | Khác | cộng/trừ chỉ tiêu kỳ với thời điểm | Lợi nhuận sau thuế là kết quả cuối cùng của hoạt động kinh doanh. Việc tích hợp các dòng này giúp doanh nghiệp xác định khả năng tái tạo vốn và khả năng phục hồ |
| 1 | `current_tax_expense + (net_income - retained_earnings)` | tổ hợp | Khác | cộng/trừ chỉ tiêu kỳ với thời điểm | Chi phí thuế TNDN hiện hành là khoản chi phí cố định. Khi doanh nghiệp có chi phí cao hơn so với mức chuẩn, nó sẽ giảm lợi suất và tăng áp lực thuế. Việc so sán |
| 1 | `operating_profit + pretax_profit - current_tax_expense` | tổ hợp | Khác | — | Lợi nhuận từ hoạt động kinh doanh là kết quả thực tế của doanh nghiệp. Việc tích hợp các dòng lợi nhuận khác (như lợi nhuận trước thuế) và chi phí thuế TNDN để  |
| 1 | `retained_earnings + other_income - current_tax_expense` | tổ hợp | Khác | cộng/trừ chỉ tiêu kỳ với thời điểm | Lợi nhuận sau thuế là thước đo hiệu quả kinh doanh chính. Việc tích hợp các dòng lợi nhuận khác (như thu nhập khác) và chi phí thuế TNDN để tính lợi nhuận sau t |
| 1 | `safe_div(pretax_profit, total_assets)` | tỷ số | Sinh lời | — | Lợi nhuận kế toán trước thuế trên tổng tài sản cho thấy mức độ hiệu quả sử dụng vốn và khả năng tái tạo tài sản của doanh nghiệp. |
| 1 | `safe_div(retained_earnings, equity)` | tỷ số | Khác | — | Lợi nhuận sau thuế chưa phân phối trên vốn chủ sở hữu cho thấy tỷ suất lợi nhuận thực tế, ảnh hưởng đến khả năng tái sử dụng vốn và giá trị cổ phiếu (Sloan 1996 |
| 1 | `safe_div(revenue, total_assets)` | tỷ số | Khác | — | Lợi suất tăng trưởng của doanh nghiệp so với tổng tài sản cho thấy khả năng tăng trưởng của doanh nghiệp. |

## Công thức KHÔNG hợp lệ, theo lỗi

### syntax_error — 274 công thức

- `rank(inventory_writedown, k=4) + zscore(inventory_writedown, k=4)` — F1-001 · syntax_error:keyword
- `rank(current_assets, k=4) + zscore(current_assets, k=4)` — F1-001 · syntax_error:keyword
- `rank(inventory_writedown, k=4) + zscore(inventory_writedown, k=4)` — F1-002 · syntax_error:keyword
- `rank(current_assets, k=4) + zscore(current_assets, k=4)` — F1-002 · syntax_error:keyword
- `rank(revenue, k=4) + zscore(revenue, k=4)` — F1-002 · syntax_error:keyword
- `rank_inventory = (inventory_writedown / inventory_gross) * 100` — F2-002 · syntax_error
- `rank_current_assets = current_assets / total_assets` — F2-002 · syntax_error
- `rank_revenue = revenue / net_income` — F2-002 · syntax_error
- `rank(inventory_writedown, k=4) + zscore(inventory_writedown, k=4)` — F1-003 · syntax_error:keyword
- `rank(inventory_writedown, k=4) + zscore(inventory_writedown, k=4) + growth(inventory_writedown, k=4)` — F1-003 · syntax_error:keyword
- `rank(inventory_writedown, k=4) + zscore(inventory_writedown, k=4) + growth(inventory_writedown, k=4) + mean(inventory_writedown, k=4)` — F1-003 · syntax_error:keyword
- `rank_inventory_writedown = (inventory_writedown / inventory_gross) * 100` — F2-003 · syntax_error
- … và 262 công thức khác (xem `bench/results/formulas.csv`)

### copied_fewshot — 104 công thức

- `safe_div(delta(inventory, 4), mean(total_assets, 4))` — F3-001 · copied_fewshot
- `safe_div(net_income - cfo, total_assets)` — F3-001 · copied_fewshot
- `safe_div(net_income, market_cap)` — F3-001 · copied_fewshot
- `safe_div(delta(inventory, 4), mean(total_assets, 4))` — F3-002 · copied_fewshot
- `safe_div(net_income - cfo, total_assets)` — F3-002 · copied_fewshot
- `safe_div(net_income, market_cap)` — F3-002 · copied_fewshot
- `safe_div(delta(short_term_receivables, 4), mean(total_assets, 4))` — F3-003 · copied_fewshot
- `safe_div(net_income - cfo, total_assets)` — F3-003 · copied_fewshot
- `safe_div(net_income, market_cap)` — F3-003 · copied_fewshot
- `safe_div(delta(short_term_receivables, 4), mean(total_assets, 4))` — F3-004 · copied_fewshot
- `safe_div(net_income - cfo, total_assets)` — F3-004 · copied_fewshot
- `safe_div(net_income, market_cap)` — F3-004 · copied_fewshot
- … và 92 công thức khác (xem `bench/results/formulas.csv`)

### bad_arity — 54 công thức

- `rank(inventory_writedown, k)` — F2-001 · bad_arity:rank|unknown_var:k
- `rank(current_assets, k)` — F2-001 · bad_arity:rank|unknown_var:k
- `rank(net_income, k)` — F2-001 · bad_arity:rank|unknown_var:k
- `zscore(inventory_writedown, 4)` — F4-002 · bad_arity:zscore
- `zscore(inventory_writedown, 4)` — F4-002 · bad_arity:zscore|duplicate
- `rank(interest_expense, k) + zscore(interest_expense, k)` — F1-005 · bad_arity:rank|bad_arity:zscore|unknown_var:k
- `rank(net_income, k) + zscore(net_income, k)` — F1-005 · bad_arity:rank|bad_arity:zscore|unknown_var:k
- `rank(operating_profit, k) + zscore(operating_profit, k)` — F1-005 · bad_arity:rank|bad_arity:zscore|unknown_var:k
- `rank(interest_expense, 4)` — F4-004 · bad_arity:rank
- `zscore(interest_expense, 4)` — F4-004 · bad_arity:zscore
- `rank(interest_expense, k) + zscore(interest_expense, k)` — F1-006 · bad_arity:rank|bad_arity:zscore|unknown_var:k|duplicate
- `rank(interest_expense, 4)` — F4-005 · bad_arity:rank|duplicate
- … và 42 công thức khác (xem `bench/results/formulas.csv`)

### duplicate — 39 công thức

- `growth(total_assets, 4)` — F4-006 · duplicate
- `growth(total_assets, 4)` — F4-007 · duplicate
- `growth(total_assets, 4)` — F4-008 · duplicate
- `growth(cash_and_equivalents, 4)` — F4-009 · duplicate
- `safe_div(share_of_associates, growth(total_assets, 4))` — F3-013 · duplicate
- `growth(market_cap, 4)` — F3-013 · duplicate
- `growth(total_assets, 4)` — F4-011 · duplicate
- `contingent_liabilities_disclosed` — F3-015 · duplicate
- `growth(cash_and_equivalents, 4)` — F4-012 · duplicate
- `growth(total_assets, 4)` — F4-015 · duplicate
- `growth(cash_and_equivalents, 4)` — F4-005 · duplicate
- `growth(total_assets, 4)` — F4-006 · duplicate
- … và 27 công thức khác (xem `bench/results/formulas.csv`)

### raw_division — 20 công thức

- `net_income / (total_assets - equity)` — F4-014 · raw_division
- `net_income / pretax_profit` — F4-014 · raw_division
- `net_income / pretax_profit` — F4-015 · raw_division|duplicate
- `rank_long_term_debt / (long_term_debt + equity)` — F2-012 · raw_division|unknown_var:rank_long_term_debt
- `long_term_debt / (long_term_debt + fixed_assets)` — F2-012 · raw_division
- `rank_related_party_disclosed / equity` — F2-017 · raw_division|unknown_var:rank_related_party_disclosed
- `net_income / equity` — F2-017 · raw_division
- `related_party_disclosed / equity` — F2-017 · raw_division
- `net_income / equity` — F4-011 · raw_division|duplicate
- `short_term_receivables / receivables_customers` — F4-011 · raw_division
- `net_income - equity / (total_assets + equity)` — F4-014 · raw_division
- `cfi / cff` — F4-014 · raw_division
- … và 8 công thức khác (xem `bench/results/formulas.csv`)

### unknown_func — 15 công thức

- `risk(receivables_customers)` — F4-003 · unknown_func:risk
- `depreciation(total_assets, 4)` — F4-006 · unknown_func:depreciation
- `depreciation(total_assets, 4)` — F4-007 · unknown_func:depreciation|duplicate
- `depreciation(tangible_fixed_assets, 4)` — F4-007 · unknown_func:depreciation
- `depreciation(total_assets, 4)` — F4-008 · unknown_func:depreciation|duplicate
- `risk(receivables_customers)` — F4-003 · unknown_func:risk
- `depreciation(capex, 4)` — F4-006 · unknown_func:depreciation
- `depreciation(total_assets, 4)` — F4-007 · unknown_func:depreciation
- `depreciation(total_assets, 4)` — F4-008 · unknown_func:depreciation|duplicate
- `risk(inventory_writedown, 4)` — F4-001 · unknown_func:risk
- `risk(inventory_writedown, 4)` — F4-002 · unknown_func:risk|duplicate
- `depreciation(total_assets, 4)` — F4-006 · unknown_func:depreciation
- … và 3 công thức khác (xem `bench/results/formulas.csv`)

### unknown_var — 6 công thức

- `safe_div(growth(x, 4), mean(x, 4))` — F3-011 · unknown_var:x
- `conting_liabilities_disclosed` — F4-012 · unknown_var:conting_liabilities_disclosed
- `log(principal + interest_rate) - (risk_factor * 0.05)` — F4-014 · unknown_var:interest_rate|unknown_var:principal|unknown_var:risk_factor
- `conting_liabilities_disclosed` — F4-012 · unknown_var:conting_liabilities_disclosed
- `safe_div(growth(x, 4), market_cap)` — F3-011 · unknown_var:x
- `growth(conting_liabilities_disclosed, 4)` — F4-012 · unknown_var:conting_liabilities_disclosed

### missing_field — 4 công thức

- `rank_zscore = zscore(net_income) + 0.5 * (abs(cfo) - abs(cfi) + abs(cff)), rationale: Tăng cường độ lệch chuẩn của dòng tiền thuần từ hoạt động kinh doanh và đầu tư giúp xác định khả năng phục hồi của doanh nghiệp trước các biến động thị trường, phản ánh hiệu quả chuyển hóa vốn đầu tư.` — F1-016 · missing_field:rationale|syntax_error
- `risk_score = abs(cfo) + abs(cfi) + abs(cff) - 0.5 * (abs(cfo) + abs(cfi) + abs(cff)), rationale: Tổng lưu chuyển tiền thuần từ hoạt động kinh doanh, đầu tư và tài chính được tích lũy để đánh giá mức độ rủi ro tín dụng, cao hơn khi có dòng tiền thuần từ hoạt động đầu tư và tài chính lớn hơn.` — F1-016 · missing_field:rationale|syntax_error
- `risk_score = abs(cfo) + abs(cfi) + abs(cff) - 0.5 * (abs(cfo) + abs(cfi) + abs(cff)), rationale: Tổng lưu chuyển tiền thuần từ hoạt động kinh doanh, đầu tư và tài chính được tích lũy để đánh giá mức độ rủi ro tín dụng, cao hơn khi có dòng tiền thuần từ hoạt động đầu tư và tài chính lớn hơn.` — F1-016 · missing_field:rationale|syntax_error
- `rank(gross_profit, k=4, net_income, k=4)` — F1-014 · missing_field:source|syntax_error

### bad_lag — 1 công thức

- `safe_div(growth(x, k), mean(x, k))` — F3-011 · bad_lag:growth|bad_lag:mean|unknown_var:k|unknown_var:x

