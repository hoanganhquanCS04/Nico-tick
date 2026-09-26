# Công thức do `qwen35-2b` sinh ra

Sinh bởi `bench/scripts/inspect_formulas.py` từ `bench/results/formulas.csv`. Nguồn gốc: `bench/results/raw/qwen35-2b__seed*.jsonl`.

- **403** công thức sinh ra (76 prompt × 3 seed × ~3), **207** hợp lệ, **151** công thức khác nhau
- Sạch (≥ 2 biến, không lỗi ngữ nghĩa): **173**, trong đó 127 khác nhau
- Cột *lặp* = số lần cùng công thức (dạng chuẩn hoá) xuất hiện qua các prompt và seed

## Công thức hợp lệ, theo chủ đề prompt

### associates

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(safe_div(investments_associates, share_of_associates), 4)` | biến đổi của tỷ số | Liên kết / đầu tư tài chính | — | Công thức này đo lường tốc độ tăng trưởng của khoản đầu tư vào công ty liên kết so với phần lãi lỗ thực tế, phản ánh hiệu quả đầu tư của cổ phiếu trong việc nắm |
| 2 | `safe_div(lag(share_of_associates, 1), equity)` | tỷ số | Liên kết / đầu tư tài chính | — | Đánh giá mức độ nợ phải trả và rủi ro tài chính liên quan đến các khoản đầu tư vào công ty liên kết so với vốn chủ sở hữu. |
| 2 | `safe_div(long_term_investments, equity)` | tỷ số | Liên kết / đầu tư tài chính | — | Tỷ lệ đầu tư dài hạn so với vốn chủ sở hữu đo lường mức độ tăng trưởng tài sản và khả năng sinh lời của công ty liên doanh. |
| 2 | `safe_div(safe_div(investments_associates, revenue), 4)` | tỷ số | Liên kết / đầu tư tài chính | — | Tỷ lệ này đo lường mức độ đầu tư vào liên kết so với doanh thu thuần, cho thấy mức độ tập trung vào các khoản đầu tư dài hạn và ổn định. |
| 2 | `safe_div(share_of_associates, pretax_profit)` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Tỷ lệ phần lãi lỗ trong liên doanh so với lợi nhuận kế toán phản ánh hiệu quả đầu tư liên kết và khả năng sinh lời từ các khoản đầu tư dài hạn. |
| 2 | `safe_div(share_of_associates, revenue)` | tỷ số | Liên kết / đầu tư tài chính | — | Tỷ lệ phần lãi lỗ trong liên doanh so với doanh thu thuần cho thấy mức độ phụ thuộc vào hoạt động kinh doanh liên kết và hiệu quả sử dụng vốn. |
| 1 | `growth(safe_div(investments_associates, share_of_associates), 1)` | biến đổi của tỷ số | Liên kết / đầu tư tài chính | — | Tỷ lệ tăng trưởng phần lãi lỗ trong công ty liên kết so với tổng vốn đầu tư cho thấy mức độ tăng trưởng lợi nhuận thực tế từ các khoản đầu tư liên kết. |
| 1 | `safe_div(growth(share_of_associates, 1), safe_div(revenue, 1))` | tỷ số | Liên kết / đầu tư tài chính | — | Công thức này đo lường tốc độ tăng trưởng phần lãi lỗ trong công ty liên doanh so với tốc độ tăng trưởng doanh thu thuần, phản ánh hiệu quả đầu tư và khả năng s |
| 1 | `safe_div(lag(long_term_investments, 1), equity)` | tỷ số | Liên kết / đầu tư tài chính | — | Đánh giá mức độ tài sản dài hạn (bao gồm cả đầu tư) so với vốn chủ sở hữu, cho thấy khả năng tài chính hóa và rủi ro tài chính. |
| 1 | `safe_div(market_cap, growth(revenue, 4))` | tỷ số | Định giá | — | Tỷ lệ vốn thị trường so với tốc độ tăng trưởng doanh thu cho thấy sức khỏe tài chính và khả năng mở rộng thị trường, hỗ trợ xếp hạng cổ phiếu. |
| 1 | `safe_div(net_income, safe_div(investments_associates, share_of_associates))` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Lợi nhuận sau thuế trên mỗi đồng vốn đầu tư vào liên kết cho phép so sánh hiệu quả sinh lời giữa các công ty liên kết có tỷ lệ sở hữu khác nhau. |
| 1 | `safe_div(net_income, share_of_associates)` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Lợi nhuận sau thuế trên mỗi đồng lãi lỗ trong công ty liên kết cho thấy hiệu quả sinh lời từ khoản đầu tư dài hạn. |
| 1 | `safe_div(safe_div(net_income, investments_associates), share_of_associates)` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Chỉ số này biểu thị mức lợi nhuận sau thuế trên mỗi đồng vốn đầu tư vào công ty liên doanh, cho thấy hiệu quả sử dụng vốn cho các khoản đầu tư dài hạn. |
| 1 | `safe_div(safe_div(total_assets, investments_associates), share_of_associates)` | tỷ số | Liên kết / đầu tư tài chính | — | Chỉ số này đo lường mức tăng trưởng tài sản trên mỗi đồng vốn đầu tư, phản ánh quy mô mở rộng và khả năng sinh lời của các khoản đầu tư dài hạn. |
| 1 | `safe_div(share_of_associates, net_income)` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Tỷ lệ phần lãi lỗ trong liên doanh so với lợi nhuận sau thuế phản ánh hiệu quả đầu tư liên kết, giúp xếp hạng cổ phiếu dựa trên dòng tiền thực tế. |
| 1 | `safe_div(total_assets, investments_associates)` | tỷ số | Liên kết / đầu tư tài chính | — | Tỷ lệ giữa tổng tài sản và khoản đầu tư vào liên kết cho thấy mức độ mở rộng tài sản do đầu tư liên kết tạo ra so với tổng tài sản doanh nghiệp. |

### bank_loans

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 1 | `(safe_div(equity, total_assets) * 0.4) + (safe_div(cfo, cff) * 0.3) + (safe_div(pretax_profit, 0) * 0.3)` | tổ hợp | Sinh lời | — | Đánh giá tỷ trọng vốn chủ sở hữu so với tổng tài sản để đo lường chất lượng vốn đầu tư, kết hợp với tỷ lệ dòng tiền thuần từ hoạt động kinh doanh và đầu tư so v |

### cip

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(construction_in_progress, 1)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Công thức này đo lường tốc độ tăng trưởng của vốn đang đầu tư, phản ánh trực tiếp tốc độ triển khai dự án mới và khả năng tạo ra dòng tiền từ các khoản đầu tư d |
| 2 | `safe_div(construction_in_progress, depreciation)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ đầu tư xây dựng so với khấu hao cho thấy tốc độ mở rộng cơ sở hạ tầng, tác động tích cực đến dòng tiền và lợi nhuận trong ngắn hạn. |
| 2 | `safe_div(construction_in_progress, equity)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ đầu tư xây dựng so với vốn chủ sở hữu phản ánh tốc độ đầu tư dài hạn, biến số quan trọng cho xếp hạng cổ phiếu trong giai đoạn xây dựng. |
| 2 | `safe_div(construction_in_progress, total_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ đầu tư xây dựng so với tổng tài sản cho thấy mức độ đầu tư vào cơ sở hạ tầng so với tổng tài sản, có thể dự báo tăng trưởng doanh thu và lợi nhuận. |
| 1 | `rank(construction_in_progress)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Công thức xếp hạng dựa trên mức độ tăng trưởng của khoản đầu tư xây dựng cơ bản dở dang, giúp xác định vị trí của doanh nghiệp trong nhóm đầu tư hạ tầng và dự á |
| 1 | `safe_div(construction_in_progress, long_term_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Xác định mức độ đầu tư xây dựng cơ bản tương đối so với tổng tài sản dài hạn, đánh giá tỷ trọng vốn đầu tư dài hạn trong cấu trúc tài sản của doanh nghiệp. |
| 1 | `safe_div(construction_in_progress, revenue)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ đầu tư xây dựng so với doanh thu cho thấy mức độ đầu tư dự án chưa hoàn thiện so với doanh thu thực tế, ảnh hưởng đến dòng tiền và lợi nhuận. |
| 1 | `safe_div(construction_in_progress, safe_div(cfo, safe_div(revenue, 1)))` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Đánh giá tốc độ đầu tư xây dựng cơ bản bằng tỷ lệ giữa chi phí đầu tư xây dựng TSCĐ (bao gồm cả các khoản phát sinh trong kỳ) và dòng tiền thuần từ hoạt động ki |
| 1 | `safe_div(growth(construction_in_progress, 1), growth(construction_in_progress, 4))` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ tăng trưởng của khoản đầu tư xây dựng cơ bản so với kỳ trước cho thấy tốc độ mở rộng quy mô và khả năng tạo ra giá trị mới, là yếu tố then chốt quyết định |

### commitments

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(contingent_liabilities_disclosed, total_assets)` | tỷ số | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Đánh giá rủi ro biến động tài sản để xác định mức độ rủi ro liên quan đến các khoản cam kết dài hạn và nợ tiềm tàng. |
| 1 | `safe_div(contingent_liabilities_disclosed, total_assets) * 100` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Công thức này đo lường mức độ rủi ro từ các khoản cam kết vốn và cam kết mua bán so với tổng tài sản, phản ánh khả năng thanh toán và sự ổn định tài chính trong |
| 1 | `safe_div(cash_and_equivalents, cfo)` | tỷ số | Đòn bẩy / thanh khoản | — | Phân tích sự biến động giữa dòng tiền thuần và tiền gửi để đo lường tính ổn định của dòng tiền thực tế. |
| 1 | `safe_div(cash_and_equivalents, safe_div(cash_and_equivalents, lag(cash_and_equivalents, 1)))` | 1 biến | Đòn bẩy / thanh khoản | — | Đánh giá tốc độ tăng trưởng của dòng tiền và tài sản tương đương tiền, phản ánh khả năng sinh lời và duy trì dòng tiền cho cổ phần, là yếu tố then chốt cho các  |
| 1 | `safe_div(cfo, cash_and_equivalents)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ cam kết trên dòng tiền cho thấy mức độ ràng buộc về cam kết mua bán và cam kết vốn; tỷ lệ cao có thể làm giảm dòng tiền thực tế và lợi suất. |
| 1 | `safe_div(cfo, long_term_debt)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ dòng tiền thuần từ hoạt động kinh doanh so với nợ vay dài hạn đo lường khả năng trả nợ và duy trì hoạt động; tỷ lệ thấp hơn cho thấy rủi ro vỡ nợ cao hơn. |
| 1 | `safe_div(cfo, safe_div(cash_and_equivalents, safe_div(total_assets, 1)))` | tỷ số | Đòn bẩy / thanh khoản | — | Công thức này đo lường tỷ lệ dòng tiền thuần so với tài sản, phản ánh khả năng sinh lời và thanh khoản của doanh nghiệp trong bối cảnh rủi ro cam kết. |
| 1 | `safe_div(equity, construction_in_progress)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Đo lường áp lực vốn chủ sở hữu khi so sánh với tài sản đang đầu tư xây dựng để đánh giá khả năng thanh toán các khoản cam kết dài hạn. |
| 1 | `safe_div(equity, long_term_debt)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ vốn chủ sở hữu so với nợ dài hạn phản ánh mức độ độc lập tài chính của doanh nghiệp; tỷ lệ thấp hơn cho thấy sự phụ thuộc lớn vào vay nợ dài hạn. |
| 1 | `safe_div(total_liabilities, safe_div(cfo, safe_div(cash_and_equivalents, 1)))` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ phải trả so với dòng tiền thuần cho thấy mức độ an toàn của doanh nghiệp đối với các khoản nợ tiềm tàng và cam kết. |

### customer_advances

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(customer_advances, revenue)` | tỷ số | Vốn lưu động | — | Tỷ lệ người mua trả tiền trước so với doanh thu thuần phản ánh mức độ tín dụng của khách hàng, cao hơn có nghĩa là doanh thu chưa thực hiện sẽ chuyển thành doan |
| 2 | `growth(cfo, 4)` | 1 biến | Khác | — | Lợi suất dựa trên tăng trưởng lưu chuyển tiền thuần từ hoạt động kinh doanh cho thấy khả năng sinh lời bền vững của doanh nghiệp. |
| 2 | `growth(customer_advances, 4)` | 1 biến | Vốn lưu động | — | Tốc độ tăng trưởng của khoản người mua trả tiền trước cho thấy sự mở rộng thị trường và tăng trưởng doanh thu trong tương lai. |
| 2 | `safe_div(customer_advances, growth(revenue, 1))` | tỷ số | Vốn lưu động | — | Tỷ lệ giữa số tiền người mua trả tiền trước và tốc độ tăng trưởng doanh thu cho thấy mức độ ổn định của dòng tiền trước khi doanh số tăng, đặc biệt quan trọng k |
| 2 | `safe_div(growth(revenue, 1), revenue)` | 1 biến | Khác | — | Tỷ lệ tăng trưởng doanh thu so với doanh thu kỳ trước đo lường tốc độ tăng trưởng doanh thu chưa thực hiện, cao hơn dự báo tăng trưởng doanh thu thực tế sẽ xảy  |
| 2 | `safe_div(short_term_receivables, revenue)` | tỷ số | Vốn lưu động | — | Chỉ số tốc độ thu hồi nợ ngắn hạn giúp đánh giá hiệu quả quản lý dòng tiền và khả năng thanh toán của doanh nghiệp. |
| 1 | `safe_div(revenue - customer_advances, revenue)` | tỷ số | Vốn lưu động | cộng/trừ chỉ tiêu kỳ với thời điểm | Phần doanh thu thuần không phải là tiền mặt (doanh thu chưa thực hiện) cao hơn so với tiền mặt phản ánh chất lượng dòng tiền và khả năng thanh toán, làm giảm lợ |
| 1 | `safe_div(customer_advances, cash_and_equivalents)` | tỷ số | Đòn bẩy / thanh khoản, Vốn lưu động | — | Đánh giá mức độ tín dụng của khách hàng đối với doanh nghiệp, phản ánh khả năng thanh toán và chất lượng dòng tiền từ các khoản vay ngắn hạn. |
| 1 | `safe_div(customer_advances, current_liabilities)` | tỷ số | Đòn bẩy / thanh khoản, Vốn lưu động | — | Tỷ lệ người mua trả tiền trước so với nợ ngắn hạn đo lường khả năng thanh toán của khách hàng; tỷ lệ cao cho thấy dòng tiền bán hàng từ khoản phải thu ngắn hạn  |
| 1 | `safe_div(customer_advances, inventory)` | tỷ số | Vốn lưu động | — | Tỷ lệ người mua trả tiền trước so với hàng tồn kho cho biết mức độ tồn kho của khách hàng và áp lực thanh toán. |
| 1 | `safe_div(growth(customer_advances, 1), growth(revenue, 1))` | tỷ số | Vốn lưu động | — | So sánh tốc độ tăng trưởng của khoản phải thu ngắn hạn so với tốc độ tăng trưởng doanh thu thuần, giúp đánh giá mức độ tăng trưởng tín dụng của khách hàng so vớ |
| 1 | `safe_div(growth(customer_advances, 1), safe_div(growth(revenue, 1), 1))` | tỷ số | Vốn lưu động | — | Công thức này đo lường tốc độ tăng trưởng của khoản tiền người mua trả trước so với tốc độ tăng trưởng doanh thu thuần. Do doanh thu chưa thực hiện và doanh thu |
| 1 | `safe_div(growth(revenue, 1), safe_div(customer_advances, revenue))` | tỷ số | Vốn lưu động | — | So sánh tốc độ tăng trưởng doanh thu với mức người mua trả tiền trước giúp đánh giá sự ổn định của dòng tiền từ khách hàng so với tốc độ tăng trưởng doanh thu,  |
| 1 | `safe_div(revenue, total_assets)` | tỷ số | Khác | — | Tỷ lệ doanh thu so với tổng tài sản đo lường mức độ tài sản cố định và tài sản lưu chuyển hàng hóa, ảnh hưởng trực tiếp đến khả năng thanh toán và dòng tiền doa |

### debt

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(interest_expense, safe_div(cash_and_equivalents, safe_div(total_assets, 4)))` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay so với vốn chủ sở hữu giúp đo lường mức độ rủi ro tài chính và khả năng thanh toán, ảnh hưởng trực tiếp đến lợi suất cổ phiếu. |
| 3 | `safe_div(total_assets, equity)` | tỷ số | Khác | — | Hệ số đòn bẩy tài sản tăng trưởng phản ánh tốc độ tăng trưởng tài sản so với vốn chủ sở hữu; tăng trưởng nhanh làm tăng rủi ro và biến động lợi nhuận. |
| 2 | `safe_div(interest_expense, current_liabilities)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay so với nợ ngắn hạn đo khả năng thanh toán nợ vay; thấp làm tăng rủi ro khi dòng tiền bán hàng chậm lại. |
| 2 | `safe_div(interest_expense, safe_div(cash_and_equivalents, safe_div(total_assets, safe_div(current_liabilities, 1))))` | tỷ số | Đòn bẩy / thanh khoản | — | Đo lường mức độ tác động của chi phí lãi vay lên khả năng thanh toán và khả năng vay nợ của doanh nghiệp, phản ánh rủi ro thanh khoản và chi phí tài chính. |
| 2 | `safe_div(interest_expense, safe_div(equity, safe_div(total_assets, 4)))` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay trên vốn chủ sở hữu phản ánh mức độ rủi ro tài chính và áp lực thanh khoản, là yếu tố then chốt ảnh hưởng đến lợi suất cổ phiếu trong bối  |
| 1 | `safe_div(short_term_debt + long_term_debt, interest_expense)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ vay so với chi phí lãi vay đo lường mức độ phụ thuộc vào chi phí tài chính; tỷ lệ cao làm tăng rủi ro khi lãi suất tăng. |
| 1 | `safe_div(current_liabilities, short_term_debt)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ thanh toán nợ ngắn hạn so với nợ phải trả ngắn hạn đo khả năng trả nợ trong vòng 12 tháng; tỷ lệ thấp làm tăng rủi ro vỡ nợ và giảm lợi suất. |
| 1 | `safe_div(interest_expense, long_term_debt)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay so với nợ dài hạn phản ánh mức độ phụ thuộc vào chi phí tài chính, nơi chi phí lãi vay cao làm giảm lợi nhuận và tăng rủi ro nợ. |
| 1 | `safe_div(interest_expense, revenue)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay so với doanh thu cho thấy mức độ phụ thuộc vào hoạt động kinh doanh, giúp xếp hạng doanh nghiệp có chi phí vay cao hay thấp. |
| 1 | `safe_div(interest_expense, safe_div(cfo, safe_div(current_liabilities, 4)))` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ che phủ chi phí lãi vay bằng dòng tiền kinh doanh giúp đánh giá khả năng sinh lời từ hoạt động kinh doanh. |
| 1 | `safe_div(interest_expense, safe_div(current_liabilities, 4))` | tỷ số | Đòn bẩy / thanh khoản | — | Chỉ tiêu này phản ánh khả năng trả nợ ngắn hạn của doanh nghiệp, giảm thiểu rủi ro vỡ nợ và tác động tích cực đến lợi nhuận. |
| 1 | `safe_div(interest_expense, safe_div(long_term_debt, short_term_debt))` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay so với tổng nợ vay (bao gồm ngắn hạn và dài hạn) phản ánh mức độ phụ thuộc vào chi phí lãi vay, từ đó dự báo rủi ro thanh khoản và biến độ |
| 1 | `safe_div(interest_expense, safe_div(total_assets, current_liabilities))` | tỷ số | Đòn bẩy / thanh khoản | — | Chi phí lãi vay trên tổng tài sản và nợ phải trả đo lường mức độ rủi ro thanh khoản và chi phí cố định, ảnh hưởng trực tiếp đến lợi nhuận sau thuế và giá cổ phi |
| 1 | `safe_div(interest_expense, safe_div(total_liabilities, safe_div(current_liabilities, safe_div(short_term_debt, long_term_debt))))` | tỷ số | Đòn bẩy / thanh khoản | — | Đo lường tỷ lệ chi phí lãi vay so với tổng nợ phải trả và nợ ngắn hạn để đánh giá mức độ rủi ro vay nợ và khả năng thanh toán, từ đó dự báo biến động lợi nhuận  |
| 1 | `safe_div(interest_expense, short_term_debt)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay so với nợ vay ngắn hạn phản ánh mức độ rủi ro tài chính và áp lực lãi suất; tỷ lệ cao làm giảm lợi suất cổ phiếu khi lãi vay tăng. |
| 1 | `safe_div(interest_expense, total_assets)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay trên tổng tài sản phản ánh mức độ rủi ro thanh khoản và khả năng chịu đựng biến động lãi suất; mức tăng cao làm giảm lợi suất cổ phiếu tro |
| 1 | `safe_div(long_term_debt, safe_div(equity, safe_div(current_liabilities, 4)))` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ dài hạn so với vốn chủ sở hữu phản ánh cấu trúc nợ và mức độ rủi ro thanh khoản của doanh nghiệp. |
| 1 | `safe_div(total_assets, interest_expense)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ tài sản so với chi phí lãi vay đo lường quy mô tài sản so với chi phí tài chính; thấp làm tăng rủi ro khi dòng tiền bán hàng chậm lại. |

### fin_assets

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `growth(net_income, 4)` | 1 biến | Khác | — | Tăng trưởng lợi nhuận sau thuế cho thấy sức khỏe tài chính và khả năng tạo ra giá trị cho cổ đông trong tương lai. |
| 2 | `safe_div(market_cap, total_assets)` | tỷ số | Định giá | — | Tỷ lệ vốn thị trường trên tổng tài sản phản ánh mức độ rủi ro và khả năng thanh khoản của cổ phiếu, ảnh hưởng trực tiếp đến lợi suất trong ngắn hạn. |
| 1 | `growth(delta(total_assets, 1), 1)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Đánh giá tốc độ tăng trưởng của tổng tài sản trong kỳ so với kỳ trước, phản ánh sức khỏe tài chính và khả năng sinh lời của công ty. |
| 1 | `safe_div(cfi, equity)` | tỷ số | Khác | — | Tỷ lệ lưu chuyển tiền đầu tư trên vốn chủ sở hữu đo lường hiệu quả sử dụng vốn và dòng tiền thực tế. |
| 1 | `safe_div(cfo, safe_div(equity, 4))` | tỷ số | Khác | — | Tỷ lệ dòng tiền thuần từ hoạt động kinh doanh so với vốn chủ sở hữu cho thấy hiệu quả dòng tiền thực tế so với tài sản. |
| 1 | `safe_div(cfo, total_assets)` | tỷ số | Khác | — | Tỷ lệ lưu chuyển tiền thuần trên tài sản cho thấy dòng tiền thực tế sinh ra từ hoạt động kinh doanh, giảm thiểu rủi ro thanh khoản. |
| 1 | `safe_div(pretax_profit, total_assets)` | tỷ số | Sinh lời | — | Tỷ lệ lợi nhuận trên tổng tài sản đo lường hiệu quả sử dụng tài sản để tạo ra lợi nhuận, là yếu tố then chốt định giá cổ phiếu. |

### fixed_assets

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(cfo - capex, fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tăng trưởng dòng tiền thuần so với chi phí mua sắm cho thấy hiệu quả sử dụng vốn đầu tư, giảm rủi ro tài sản cố định không có dòng tiền. |
| 2 | `safe_div(tangible_fixed_assets, equity)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ tài sản cố định hữu hình so với vốn chủ sở hữu cho thấy mức độ đầu tư dài hạn và chất lượng tài sản cố định so với tài sản ngắn hạn. |
| 2 | `safe_div(tangible_fixed_assets, total_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ trọng tài sản cố định hữu hình so với tổng tài sản phản ánh tỷ trọng tài sản vật chất, cổ phiếu có tỷ trọng cao thường có lợi suất ổn định hơn. |
| 1 | `safe_div((capex - safe_div(construction_in_progress, fixed_assets)), fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tăng trưởng chi phí mua sắm xây dựng so với vốn cố định hữu hình cho thấy tốc độ đầu tư mới, đặc biệt là các khoản đầu tư lớn chưa hoàn thành. |
| 1 | `safe_div(cfo - capex, total_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ tăng trưởng chi phí đầu tư mới so với tổng tài sản cho thấy tốc độ mở rộng quy mô và khả năng tái đầu tư, là chỉ số dự báo lợi suất tăng trưởng trong ngắn |
| 1 | `safe_div(depreciation, revenue)` | tỷ số | Khác | — | Tỷ lệ khấu hao trên mỗi đơn vị doanh thu cho thấy mức độ đầu tư mới và khả năng tái đầu tư, đồng thời phản ánh hiệu quả sử dụng tài sản cố định. |
| 1 | `safe_div(depreciation, tangible_fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ khấu hao trên mỗi đồng tài sản cố định hữu hình cho thấy mức độ đầu tư mới đang được thực hiện; tỷ lệ cao có thể báo hiệu dòng tiền đầu tư mới mạnh hoặc d |
| 1 | `safe_div(tangible_fixed_assets, revenue)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ trọng tài sản cố định hữu hình so với doanh thu cho thấy mức độ đầu tư dài hạn và khả năng sinh lời bền vững của doanh nghiệp. |

### inventory

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(inventory_writedown, inventory)` | tỷ số | Dự phòng / chất lượng tài sản, Vốn lưu động | — | Chỉ tiêu này đo lường mức độ suy giảm giá trị tài sản ngắn hạn do dự phòng giảm giá, phản ánh hiệu quả quản lý tồn kho và khả năng thanh toán rủi ro. Giá trị cà |
| 3 | `safe_div(inventory_writedown, inventory_gross)` | tỷ số | Dự phòng / chất lượng tài sản, Vốn lưu động | — | Tỷ lệ trích lập dự phòng giảm giá so với giá vốn hàng bán cho thấy mức độ suy giảm giá trị thực tế của hàng tồn kho, tác động trực tiếp đến dòng tiền và khả năn |
| 2 | `safe_div(gross_profit, safe_div(current_assets, safe_div(current_liabilities, inventory_writedown)))` | tỷ số | Dự phòng / chất lượng tài sản, Sinh lời, Đòn bẩy / thanh khoản | — | Tỷ lệ giảm giá so với lợi nhuận gộp phản ánh mức độ suy giảm giá trị tài sản ngắn hạn, ảnh hưởng trực tiếp đến dòng tiền và khả năng thanh toán. |
| 1 | `growth(inventory_writedown, 1)` | 1 biến | Dự phòng / chất lượng tài sản | — | Công thức này đo lường tốc độ tăng trưởng của khoản dự phòng giảm giá hàng tồn kho, phản ánh trực tiếp áp lực về giá trị tài sản và nhu cầu thanh lý hàng hóa tr |
| 1 | `safe_div(current_assets - inventory, safe_div(current_assets, 1000000000))` | tỷ số | Vốn lưu động | — | Đo lường mức độ biến động của tài sản ngắn hạn so với hàng tồn kho thuần, phản ánh tốc độ thanh khoản và khả năng chuyển đổi hàng tồn kho thành dòng tiền ngắn h |
| 1 | `safe_div(current_assets - inventory_writedown, safe_div(current_assets, 1000000))` | tỷ số | Dự phòng / chất lượng tài sản | — | Đánh giá mức độ sụt giảm tài sản ngắn hạn do dự phòng giảm giá hàng tồn kho, phản ánh áp lực thanh khoản và rủi ro tồn kho trực tiếp. |
| 1 | `safe_div(cfo, inventory)` | tỷ số | Vốn lưu động | — | Dòng tiền thuần từ hoạt động kinh doanh so với mức tồn kho cho thấy khả năng chuyển đổi tài sản thành dòng tiền thực tế. |
| 1 | `safe_div(current_assets, inventory)` | tỷ số | Vốn lưu động | — | Chỉ số chất lượng dòng tiền từ hàng tồn kho so với tài sản ngắn hạn ngắn hạn, phản ánh hiệu quả quản lý kho và khả năng chuyển đổi hàng tồn kho thành doanh thu. |
| 1 | `safe_div(gross_profit, revenue)` | tỷ số | Sinh lời | — | Chỉ tiêu này đo lường tốc độ tăng trưởng lợi nhuận gộp trên mỗi đơn vị doanh thu, phản ánh hiệu quả kinh doanh và khả năng chuyển đổi hàng bán thành lợi nhuận t |
| 1 | `safe_div(gross_profit, safe_div(current_assets, safe_div(inventory, 1)))` | tỷ số | Sinh lời, Vốn lưu động | — | Tỷ lệ giảm giá trên lợi nhuận gộp phản ánh mức độ suy giảm giá trị tài sản ngắn hạn so với doanh thu, liên quan trực tiếp đến dòng tiền và khả năng thanh toán. |
| 1 | `safe_div(gross_profit, safe_div(current_assets, safe_div(inventory, inventory_writedown)))` | tỷ số | Dự phòng / chất lượng tài sản, Sinh lời, Vốn lưu động | — | Tỷ lệ giảm giá hàng tồn kho so với lợi nhuận gộp phản ánh mức độ suy giảm giá trị tài sản ngắn hạn, ảnh hưởng trực tiếp đến dòng tiền và lợi suất cổ phiếu. |
| 1 | `safe_div(growth(inventory, 1), safe_div(current_assets, 1000000))` | tỷ số | Vốn lưu động | — | Xác định tốc độ tăng trưởng hàng tồn kho so với tài sản ngắn hạn, đo lường tác động đến dòng tiền và khả năng thanh toán. |
| 1 | `safe_div(growth(inventory, 4), mean(current_assets, 4))` | tỷ số | Vốn lưu động | — | Tăng trưởng tốc độ tăng của hàng tồn kho so với quy mô tài sản ngắn hạn cho thấy khả năng thanh khoản và chuyển đổi dòng tiền, ảnh hưởng đến lợi suất. |
| 1 | `safe_div(growth(inventory, 4), safe_div(current_assets, safe_div(current_liabilities, inventory_writedown)))` | tỷ số | Dự phòng / chất lượng tài sản, Đòn bẩy / thanh khoản, Vốn lưu động | — | Tỷ lệ quay vòng hàng tồn kho so với tài sản và nợ ngắn hạn cho thấy khả năng quản lý kho hiệu quả, giảm giá thấp hơn. |
| 1 | `safe_div(growth(inventory_writedown, 1), safe_div(current_assets, 1000000))` | tỷ số | Dự phòng / chất lượng tài sản | — | Đo lường mức độ rủi ro và tốc độ tăng trưởng của các khoản dự phòng giảm giá, phản ánh hiệu quả quản lý tồn kho và chất lượng hàng hóa. |
| 1 | `safe_div(inventory, revenue)` | tỷ số | Vốn lưu động | — | Chỉ số tỷ lệ hiện hữu trên doanh thu cho thấy hiệu quả quản lý kho và tốc độ bán hàng, tác động đến dòng tiền từ hoạt động kinh doanh. |
| 1 | `safe_div(inventory_writedown, cogs)` | tỷ số | Dự phòng / chất lượng tài sản | — | Tỷ lệ trích lập dự phòng giảm giá so với giá vốn hàng bán cho thấy mức độ suy giảm giá trị thực tế của hàng tồn kho so với giá ghi nhận, ảnh hưởng trực tiếp đến |
| 1 | `safe_div(inventory_writedown, gross_profit)` | tỷ số | Dự phòng / chất lượng tài sản, Sinh lời | — | Tỷ lệ trích lập dự phòng giảm giá so với lợi nhuận gộp cho thấy mức độ suy giảm giá trị hàng tồn kho so với doanh thu thực tế, có thể dự báo lợi suất cổ phiếu b |
| 1 | `safe_div(inventory_writedown, safe_div(current_assets, inventory))` | tỷ số | Dự phòng / chất lượng tài sản, Vốn lưu động | — | So sánh số dư dự phòng giảm giá với giá trị tài sản ngắn hạn có thể thực hiện được để đánh giá mức độ suy giảm giá trị thực tế của dòng tiền. |
| 1 | `safe_div(inventory_writedown, safe_div(current_assets, safe_div(current_liabilities, 0)))` | tỷ số | Dự phòng / chất lượng tài sản, Đòn bẩy / thanh khoản | — | Công thức này đo lường mức độ suy giảm giá trị tài sản ngắn hạn do dự phòng giảm giá hàng tồn kho, tương tự như việc giảm giá vốn hàng bán. Sự gia tăng hoặc giả |
| 1 | `safe_div(revenue, inventory)` | tỷ số | Vốn lưu động | — | Chỉ số quay vòng hàng tồn kho cao cho thấy doanh nghiệp bán hàng hiệu quả, giảm áp lực lưu kho và tăng lợi suất. |

### receivables

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(receivables_customers, revenue)` | tỷ số | Vốn lưu động | — | Tỷ lệ phải thu ngắn hạn của khách hàng so với doanh thu cho thấy mức độ rủi ro tín dụng; tỷ lệ cao có thể báo hiệu cổ phiếu đang bị ép giá do khó thu hồi. |
| 2 | `safe_div(receivables_customers, current_assets - safe_div(receivables_customers, current_assets))` | tỷ số | Vốn lưu động | — | Đo lường tốc độ tăng trưởng của khoản phải thu ngắn hạn so với tài sản ngắn hạn, phản ánh khả năng chuyển đổi thành dòng tiền thực tế của doanh nghiệp. |
| 2 | `safe_div(receivables_customers, current_assets)` | tỷ số | Vốn lưu động | — | Tỷ lệ thu hồi nợ phải thu ngắn hạn so với tài sản ngắn hạn phản ánh khả năng chuyển đổi nợ thành tiền, ảnh hưởng trực tiếp đến dòng tiền thực tế và lợi suất cổ  |
| 1 | `(revenue - provision_doubtful_debt) * safe_div(receivables_customers, current_assets)` | tổ hợp | Dự phòng / chất lượng tài sản, Vốn lưu động | cộng/trừ chỉ tiêu kỳ với thời điểm | Công thức này đo lường tốc độ tăng trưởng của khoản phải thu ngắn hạn của khách hàng so với doanh thu thuần, điều chỉnh bằng việc trừ dự phòng khó đòi. Sự tăng  |
| 1 | `growth(receivables_customers, 4) - safe_div(current_assets, 4)` | tổ hợp | Vốn lưu động | — | Tăng trưởng của khoản phải thu ngắn hạn so với tài sản ngắn hạn phản ánh khả năng thu hồi nợ và tạo ra dòng tiền từ khách hàng, là yếu tố then chốt cho lợi suất |
| 1 | `safe_div(gross_profit, safe_div(receivables_customers, current_assets))` | tỷ số | Sinh lời, Vốn lưu động | — | Lợi nhuận gộp trên mỗi đơn vị vốn phải thu ngắn hạn đo lường hiệu quả kinh doanh thực sự, loại bỏ yếu tố tài chính để tập trung vào chất lượng sản phẩm. |
| 1 | `safe_div(growth(receivables_customers, 1), safe_div(receivables_customers, current_assets))` | tỷ số | Vốn lưu động | — | Đo lường tốc độ tăng trưởng của khoản phải thu ngắn hạn của khách hàng so với tổng tài sản ngắn hạn, phản ánh khả năng chuyển đổi doanh thu thành tiền mặt từ kh |
| 1 | `safe_div(growth(receivables_customers, 4), delta(receivables_customers, 4))` | 1 biến | Vốn lưu động | — | Sự tăng trưởng của khoản phải thu ngắn hạn của khách hàng phản ánh khả năng chuyển đổi nợ thành tiền và chất lượng dòng tiền từ khách hàng, là yếu tố then chốt  |
| 1 | `safe_div(growth(receivables_customers, 4), mean(receivables_customers, 4))` | 1 biến | Vốn lưu động | — | Tăng trưởng của khoản phải thu ngắn hạn cho thấy tốc độ tăng trưởng doanh thu và khả năng thanh toán khách hàng, là yếu tố then chốt cho lợi suất cổ phiếu trong |
| 1 | `safe_div(growth(revenue, 4), growth(provision_doubtful_debt, 4))` | tỷ số | Dự phòng / chất lượng tài sản | — | Tỷ lệ giữa doanh thu thuần và dự phòng nợ xấu đo lường chất lượng doanh thu, phản ánh mức độ rủi ro và khả năng sinh lời bền vững của doanh nghiệp. |
| 1 | `safe_div(net_income, receivables_customers)` | tỷ số | Sinh lời, Vốn lưu động | — | Tỷ lệ lợi nhuận sau thuế trên mỗi đồng nợ phải thu ngắn hạn cho thấy hiệu quả sử dụng vốn để tạo ra dòng tiền từ các khoản nợ khó đòi, là chỉ số chất lượng tài  |
| 1 | `safe_div(provision_doubtful_debt, current_assets)` | tỷ số | Dự phòng / chất lượng tài sản | — | Tỷ lệ dự phòng nợ xấu trên tổng tài sản ngắn hạn cho thấy mức độ rủi ro tín dụng và chất lượng tài sản ngắn hạn, ảnh hưởng trực tiếp đến dòng tiền thực tế. |
| 1 | `safe_div(provision_doubtful_debt, revenue)` | tỷ số | Dự phòng / chất lượng tài sản | — | Tăng trưởng dự phòng nợ xấu so với doanh thu cho thấy mức độ thận trọng trong quản lý rủi ro và khả năng bù đắp các khoản nợ khó đòi, tác động đến dòng tiền thu |
| 1 | `safe_div(receivables_customers, total_assets)` | tỷ số | Vốn lưu động | — | So sánh số dư phải thu ngắn hạn với tổng tài sản giúp đánh giá cấu trúc tài sản và khả năng thanh toán; tỷ lệ cao có thể chỉ thị cổ phiếu đang có dòng tiền đi v |

### related_party

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(receivables_customers, short_term_receivables)` | tỷ số | Vốn lưu động | — | Tỷ lệ quay vòng vốn phải thu ngắn hạn cho thấy tốc độ doanh nghiệp nhận tiền từ khách hàng và khả năng giữ tiền; doanh nghiệp có tỷ lệ cao thường có dòng tiền t |
| 2 | `safe_div(receivables_customers, related_party_disclosed)` | tỷ số | Vốn lưu động, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tỷ lệ tăng trưởng của khoản phải thu ngắn hạn đối với các giao dịch có thuyết minh giao dịch với bên liên quan cho thấy mức độ rủi ro và khả năng thanh toán từ  |
| 1 | `growth(receivables_customers, 4) - safe_div(receivables_customers, related_party_disclosed)` | tổ hợp | Vốn lưu động, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Sự tăng trưởng của khoản phải thu ngắn hạn so với kỳ trước trừ đi phần lớn các khoản phải thu liên quan đến bên liên quan cho thấy mức độ rủi ro thanh toán từ c |
| 1 | `safe_div(revenue - cogs, related_party_disclosed)` | tỷ số | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tỷ lệ lợi nhuận sau khi trừ giá vốn hàng bán so với tổng doanh thu cho thấy mức độ lợi nhuận thực sự mà doanh nghiệp có thể duy trì sau khi giao dịch với các bê |
| 1 | `safe_div(cfo, equity)` | tỷ số | Khác | — | Tỷ lệ dòng tiền thuần từ hoạt động kinh doanh so với vốn chủ sở hữu phản ánh khả năng chuyển đổi dòng tiền thành tài sản hoặc trả nợ, là yếu tố then chốt cho lợ |
| 1 | `safe_div(cfo, revenue)` | tỷ số | Khác | — | Tỷ lệ lưu chuyển tiền thuần trên doanh thu phản ánh chất lượng dòng tiền thực tế so với báo cáo lợi nhuận, giúp đánh giá hiệu quả sử dụng vốn và khả năng sinh l |
| 1 | `safe_div(equity, total_assets)` | tỷ số | Khác | — | Tỷ lệ nợ trên vốn chủ sở hữu đo lường rủi ro tài chính, ảnh hưởng đến lợi suất trong các kỳ có biến động lớn. |
| 1 | `safe_div(market_cap, safe_div(total_assets, 4))` | tỷ số | Định giá | — | Tỷ lệ vốn thị trường trên tài sản cho thấy mức độ rủi ro và tiềm năng tăng trưởng của doanh nghiệp. |
| 1 | `safe_div(receivables_customers, safe_div(short_term_receivables, 4))` | tỷ số | Vốn lưu động | — | Chỉ số quay vòng tiền hàng cho thấy khả năng thu hồi vốn ngắn hạn, ảnh hưởng đến dòng tiền và lợi nhuận. |
| 1 | `safe_div(revenue, cogs)` | tỷ số | Khác | — | Tỷ lệ doanh thu trên giá vốn hàng bán phản ánh khả năng tạo ra lợi nhuận thuần, là chỉ số quan trọng để xếp hạng cổ phiếu trong ngành bán lẻ. |
| 1 | `safe_div(revenue, related_party_disclosed)` | tỷ số | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tỷ lệ doanh thu có liên quan đến bên liên quan cao cho thấy dòng tiền từ giao dịch bên ngoài có thể tăng trưởng mạnh, dẫn đến lợi suất cổ phiếu cao hơn. |

### segment

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(gross_profit, gross_revenue)` | tỷ số | Sinh lời | — | Tỷ lệ lợi nhuận gộp trên doanh thu phản ánh hiệu quả kinh doanh cốt lõi, nơi các doanh nghiệp có biên lợi nhuận cao thường có lợi suất tăng trưởng mạnh hơn khi  |
| 2 | `safe_div(gross_profit, safe_div(gross_profit, lag(gross_profit, 1)))` | 1 biến | Sinh lời | — | Đánh giá tỷ lệ lợi nhuận gộp tăng trưởng so với kỳ trước để phản ánh sức khỏe và khả năng mở rộng quy mô của bộ phận theo quý. |
| 2 | `safe_div(gross_profit, safe_div(gross_revenue, lag(gross_revenue, 4)))` | tỷ số | Sinh lời | — | Tỷ lệ lợi nhuận gộp trên doanh thu bán hàng, phản ánh chất lượng sản phẩm và giá trị bán hàng của bộ phận. |
| 2 | `safe_div(gross_profit, safe_div(revenue, safe_div(gross_profit, lag(revenue, 4))))` | tỷ số | Sinh lời | — | Đánh giá tỷ lệ lợi nhuận gộp trên doanh thu thuần theo bộ phận, phản ánh hiệu quả chuyển đổi doanh thu thành lợi nhuận trong từng lĩnh vực. |
| 2 | `safe_div(long_term_assets, safe_div(total_assets, lag(total_assets, 4)))` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Chỉ số tỷ lệ tài sản dài hạn trên tổng tài sản, đo lường mức độ tài chính hóa và độ rủi ro của bộ phận. |
| 1 | `growth(gross_profit, 1)` | 1 biến | Khác | — | Đánh giá tốc độ tăng trưởng lợi nhuận gộp theo quý so với quý trước, phản ánh sức khỏe tăng trưởng doanh thu bán hàng và dịch vụ. |
| 1 | `rank(gross_profit)` | 1 biến | Khác | — | Xếp hạng lợi nhuận gộp theo quý để xác định vị trí tuyệt đối của bộ phận trong danh sách doanh thu và lợi nhuận của tập đoàn. |
| 1 | `safe_div(gross_profit, safe_div(gross_revenue, lag(gross_revenue, 1)))` | tỷ số | Sinh lời | — | Tính tỷ lệ lợi nhuận gộp trên doanh thu thuần, cho thấy hiệu quả kinh doanh thuần túy của bộ phận khi loại bỏ chi phí bán hàng. |
| 1 | `safe_div(gross_profit, safe_div(gross_revenue, safe_div(revenue, 1)))` | tỷ số | Sinh lời | — | Phân tích tỷ lệ lợi nhuận gộp trên doanh thu thuần cho thấy hiệu quả kinh doanh cốt lõi, ít phụ thuộc vào chi phí bán hàng và quản lý. |
| 1 | `safe_div(gross_revenue, revenue)` | tỷ số | Khác | — | Tỷ lệ doanh thu bán hàng và cung cấp dịch vụ trên doanh thu thuần cho thấy mức độ hoạt động thực tế, loại bỏ ảnh hưởng của các khoản mục không hoạt động. |
| 1 | `safe_div(gross_revenue, safe_div(total_assets, lag(total_assets, 1)))` | tỷ số | Khác | — | Xác định tỷ lệ doanh thu trên tổng tài sản, dùng để phân tích mức độ hoạt động kinh doanh của từng bộ phận so với tài sản cố định. |
| 1 | `safe_div(gross_revenue, segment_disclosed)` | tỷ số | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Xác định tỷ trọng doanh thu bán hàng và cung cấp dịch vụ của từng bộ phận so với tổng doanh thu, giúp phân tích cấu trúc doanh thu theo khu vực địa lý. |

### tax

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(current_tax_expense, pretax_profit)` | tỷ số | Sinh lời | — | Tỷ lệ chi phí thuế thu nhập doanh nghiệp trên lợi nhuận kế toán cao cho thấy áp lực thuế lớn, dẫn đến lợi nhuận sau thuế thấp hơn và lợi suất tương lai có thể b |
| 3 | `safe_div(current_tax_expense, retained_earnings)` | tỷ số | Khác | — | Tỷ lệ chi phí thuế thu nhập doanh nghiệp trên lợi nhuận sau thuế cao cho thấy phần lợi nhuận bị trừ đi để nộp thuế lớn, làm giảm lợi nhuận sau thuế và lợi suất  |
| 1 | `safe_div(current_tax_expense, pretax_profit) * safe_div(current_tax_expense, cfo)` | tổ hợp | Sinh lời | — | Công thức này tính tỷ lệ thuế thực tế so với lợi nhuận kế toán và dòng tiền thuần từ hoạt động kinh doanh, đo lường mức độ hiệu quả của việc sử dụng lợi nhuận đ |
| 1 | `safe_div(current_tax_expense, retained_earnings) * safe_div(current_tax_expense, revenue)` | tổ hợp | Khác | — | Công thức này xác định tốc độ tăng trưởng của chi phí thuế so với lợi nhuận sau thuế và doanh thu, đánh giá mức độ áp lực thuế đối với dòng tiền và khả năng tái |
| 1 | `safe_div(current_tax_expense, total_assets) * safe_div(revenue, current_tax_expense)` | tổ hợp | Khác | — | Công thức này đo lường mức độ giảm nhẹ thuế thu nhập doanh nghiệp (TNDN) trên cơ sở tài sản và doanh thu, phản ánh khả năng chuyển đổi lợi nhuận thành tiền mặt  |
| 1 | `safe_div(current_tax_expense, cfo)` | tỷ số | Khác | — | Sự tăng trưởng của chi phí thuế thu nhập doanh nghiệp so với lưu chuyển tiền thuần từ hoạt động kinh doanh cho thấy mức độ thuế thu nhập doanh nghiệp tăng cao,  |
| 1 | `safe_div(current_tax_expense, equity)` | tỷ số | Khác | — | Công thức này đo lường mức độ tăng giảm của chi phí thuế so với vốn chủ sở hữu, phản ánh tác động của thuế thu nhập doanh nghiệp lên khả năng tái đầu tư và tăng |
| 1 | `safe_div(current_tax_expense, operating_profit)` | tỷ số | Sinh lời | — | Tỷ lệ chi phí thuế trên lợi nhuận thuần từ hoạt động kinh doanh cao cho thấy doanh nghiệp chịu áp lực thuế lớn, có thể ảnh hưởng đến dòng tiền và lợi suất. |
| 1 | `safe_div(current_tax_expense, revenue)` | tỷ số | Khác | — | Công thức này xác định mức độ tăng giảm của chi phí thuế so với doanh thu thuần, cho thấy tác động của thuế thu nhập doanh nghiệp lên dòng tiền và khả năng sinh |
| 1 | `safe_div(current_tax_expense, total_assets)` | tỷ số | Khác | — | Công thức này đo lường mức độ tăng giảm đột ngột của chi phí thuế so với tài sản, phản ánh tác động trực tiếp của việc thay đổi thuế thu nhập doanh nghiệp lên l |

## Công thức KHÔNG hợp lệ, theo lỗi

### raw_division — 106 công thức

- `(current_assets - inventory) / (current_assets - inventory_writedown)` — F1-001 · raw_division
- `(inventory - current_assets) / inventory` — F1-002 · raw_division
- `inventory_writedown / inventory` — F1-002 · raw_division
- `cfo / current_assets` — F1-002 · raw_division
- `(inventory_gross - inventory) / total_assets` — F1-002 · raw_division
- `net_income / inventory` — F1-002 · raw_division
- `(inventory_gross - inventory_writedown) / current_assets` — F2-002 · raw_division
- `(inventory - current_assets) / inventory` — F1-003 · raw_division|duplicate
- `(receivables_customers - current_assets) / current_assets` — F2-004 · raw_division
- `receivables_customers / revenue` — F2-004 · raw_division
- `receivables_customers / equity` — F2-004 · raw_division
- `(receivables_customers - provision_doubtful_debt) / current_assets` — F2-005 · raw_division
- … và 94 công thức khác (xem `bench/results/formulas.csv`)

### duplicate — 41 công thức

- `safe_div(inventory_writedown, inventory_gross)` — F3-002 · duplicate
- `safe_div(gross_profit, safe_div(current_assets, safe_div(current_liabilities, inventory_writedown)))` — F4-002 · duplicate
- `safe_div(customer_advances, revenue)` — F3-011 · duplicate
- `safe_div(customer_advances, revenue)` — F4-009 · duplicate
- `safe_div(total_assets, equity)` — F2-015 · duplicate
- `safe_div(total_assets, equity)` — F3-012 · duplicate
- `safe_div(total_assets, equity)` — F4-010 · duplicate
- `growth(safe_div(investments_associates, share_of_associates), 4)` — F3-013 · duplicate
- `safe_div(contingent_liabilities_disclosed, total_assets)` — F3-015 · duplicate
- `safe_div(gross_profit, safe_div(gross_profit, lag(gross_profit, 1)))` — F2-020 · duplicate
- `safe_div(inventory_writedown, inventory_gross)` — F3-002 · duplicate
- `safe_div(inventory_writedown, inventory)` — F2-003 · duplicate
- … và 29 công thức khác (xem `bench/results/formulas.csv`)

### bad_arity — 24 công thức

- `safe_div(inventory_writedown, safe_div(gross_profit, safe_div(current_assets, safe_div(current_liabilities))))` — F4-002 · bad_arity:safe_div
- `safe_div(growth(construction_in_progress), growth(depreciation))` — F3-009 · bad_arity:growth
- `safe_div((share_of_associates - lag(share_of_associates, 1)) / lag(revenue, 1))` — F2-015 · bad_arity:safe_div|raw_division
- `safe_div((net_income - cogs) / safe_div(revenue, 4))` — F4-011 · bad_arity:safe_div|raw_division
- `safe_div((net_income + growth(revenue, 4) - growth(cfo, 4)) * (1 + safe_div(contingent_liabilities_disclosed, 1)) / safe_div(total_assets, 4))` — F4-012 · bad_arity:safe_div|raw_division|too_complex
- `safe_div((growth(equity, 4) - growth(equity, 1)) / growth(equity, 1))` — F1-017 · bad_arity:safe_div|raw_division
- `safe_div((close_price - market_cap) / market_cap)` — F1-017 · bad_arity:safe_div|raw_division
- `safe_div((cfi + cff) / (abs(cfo) + 1e-9))` — F1-017 · bad_arity:safe_div|raw_division
- `safe_div((receivables_customers - lag(receivables_customers, 1)) / lag(receivables_customers, 1))` — F1-004 · bad_arity:safe_div|raw_division
- `safe_div(receivables_customers / equity)` — F1-004 · bad_arity:safe_div|raw_division
- `safe_div(receivables_customers / revenue)` — F1-004 · bad_arity:safe_div|raw_division
- `safe_div(interest_expense, safe_div(current_liabilities, safe_div(total_assets, safe_div(current_liabilities))))` — F2-006 · bad_arity:safe_div
- … và 12 công thức khác (xem `bench/results/formulas.csv`)

### syntax_error — 15 công thức

- `growth((safe_div(capex, long_term_assets), 4) / safe_div(capex, total_assets), 4)` — F4-006 · syntax_error:Tuple
- `safe_div(revenue, safe_div(cfo, safe_div(receivables_customers, safe_div(prepaid_to_suppliers, safe_div(short_term_receivables, 0))))))` — F2-018 · syntax_error
- `(gross_profit / revenue) - (gross_profit / revenue)_{k-1}` — F1-014 · syntax_error
- `(gross_profit / revenue) - (gross_profit / revenue)_{lag_2}` — F2-021 · syntax_error
- `safe_div((net_income - (cfo + cfi + cff), 1) / total_assets)` — F4-014 · syntax_error:Tuple
- `safe_div(growth(inventory, 1) - safe_div(growth(inventory, 4), 2)` — F1-001 · syntax_error
- `growth((safe_div(capex, long_term_assets), 4) / safe_div(capex, long_term_assets), 4)` — F4-006 · syntax_error:Tuple
- `safe_div(revenue, safe_div(cfo, safe_div(receivables_customers, safe_div(prepaid_to_suppliers, safe_div(short_term_receivables, 0))))))` — F2-018 · syntax_error
- `safe_div(log(total_assets), safe_div(log(revenue), safe_div(log(cfo), 1))))` — F4-012 · syntax_error
- `(gross_profit / revenue) - (gross_profit / revenue)_{k-1}` — F1-014 · syntax_error
- `safe_div((net_income - (cfo + cfi + cff), safe_div(total_assets, 1)) / safe_div(equity, 1))` — F4-014 · syntax_error:Tuple
- `growth((safe_div(capex, long_term_assets), 4) / safe_div(capex, total_assets), 4)` — F4-006 · syntax_error:Tuple
- … và 3 công thức khác (xem `bench/results/formulas.csv`)

### too_complex — 3 công thức

- `(safe_div(equity, total_assets) * 0.4) + (safe_div(cfo, cfi) * 0.3) + (safe_div(cff, cfi) * 0.3) + (safe_div(pretax_profit, cfi) * 0.2) + (safe_div(net_income, cfi) * 0.1)` — F1-015 · too_complex
- `safe_div(revenue, safe_div(cfo, safe_div(receivables_customers, safe_div(prepaid_to_suppliers, safe_div(total_assets, safe_div(equity, related_party_disclosed))))))` — F2-017 · too_complex
- `safe_div(revenue, safe_div(cfo, safe_div(receivables_customers, safe_div(prepaid_to_suppliers, safe_div(total_assets, safe_div(equity, related_party_disclosed))))))` — F2-017 · too_complex

### bad_lag — 2 công thức

- `safe_div(delta(receivables_customers, 4), delta(receivables_customers, 3))` — F3-003 · bad_lag:delta
- `safe_div(delta(receivables_customers, 4), delta(receivables_customers, 3))` — F3-003 · bad_lag:delta

### copied_fewshot — 2 công thức

- `safe_div(construction_in_progress, fixed_assets)` — F3-008 · copied_fewshot
- `growth(total_assets, 4)` — F3-013 · copied_fewshot

### unknown_func — 2 công thức

- `revenue - revenue_lag(1, 1)` — F2-014 · unknown_func:revenue_lag
- `revenue - revenue_lag(1, 1)` — F2-014 · unknown_func:revenue_lag|duplicate

### unknown_var — 1 công thức

- `safe_div(shares_of_associates, total_assets)` — F3-013 · unknown_var:shares_of_associates

