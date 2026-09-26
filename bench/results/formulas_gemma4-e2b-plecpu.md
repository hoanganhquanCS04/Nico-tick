# Công thức do `gemma4-e2b-plecpu` sinh ra

Sinh bởi `bench/scripts/inspect_formulas.py` từ `bench/results/formulas.csv`. Nguồn gốc: `bench/results/raw/gemma4-e2b-plecpu__seed*.jsonl`.

- **669** công thức sinh ra (76 prompt × 3 seed × ~3), **341** hợp lệ, **221** công thức khác nhau
- Sạch (≥ 2 biến, không lỗi ngữ nghĩa): **123**, trong đó 74 khác nhau
- Cột *lặp* = số lần cùng công thức (dạng chuẩn hoá) xuất hiện qua các prompt và seed

## Công thức hợp lệ, theo chủ đề prompt

### associates

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(share_of_associates, 1) * safe_div(net_income, total_assets)` | tổ hợp | Sinh lời, Đầu tư / tăng trưởng tài sản, Liên kết / đầu tư tài chính | — | Công thức này đo lường mức độ tăng trưởng lợi nhuận từ các công ty liên kết so với tổng tài sản, phản ánh hiệu quả hoạt động của mảng kinh doanh cốt lõi. |
| 3 | `share_of_associates * safe_div(net_income, total_assets)` | tổ hợp | Sinh lời, Liên kết / đầu tư tài chính | nhân với quy mô công ty | Đo lường tỷ lệ đóng góp của lợi nhuận từ công ty liên kết vào lợi nhuận sau thuế của công ty mẹ, cho thấy mức độ phụ thuộc và đóng góp của mảng liên kết. |
| 3 | `growth(share_of_associates, 1)` | 1 biến | Liên kết / đầu tư tài chính | — | Tỷ lệ tăng trưởng lợi nhuận từ các công ty liên kết là chỉ báo trực tiếp về hiệu quả của mô hình liên doanh, ảnh hưởng mạnh đến lợi suất cổ phiếu. |
| 3 | `std(long_term_investments, 4)` | 1 biến | Liên kết / đầu tư tài chính | — | Biến động của các khoản đầu tư dài hạn có thể phản ánh rủi ro và sự biến động của lợi suất cổ phiếu. |
| 3 | `zscore(growth(share_of_associates, 1))` | 1 biến | Liên kết / đầu tư tài chính | — | Công thức này đo lường mức độ tăng trưởng lợi nhuận từ các công ty liên kết trong kỳ so với mức trung bình của các công ty liên kết trong cùng kỳ, giúp xác định |
| 2 | `std(share_of_associates, 4) * zscore(share_of_associates)` | 1 biến | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Công thức này đo lường mức độ biến động (rủi ro) của phần lãi lỗ từ các công ty liên kết, giúp đánh giá tính ổn định của nguồn thu nhập liên kết. |
| 2 | `growth(share_of_associates, 2)` | 1 biến | Liên kết / đầu tư tài chính | — | Tốc độ tăng trưởng lợi nhuận từ liên doanh là chỉ báo quan trọng về hiệu quả kinh doanh của các liên kết. |
| 2 | `safe_div(cfi, net_income)` | tỷ số | Sinh lời | — | Lưu chuyển tiền thuần từ hoạt động đầu tư (CFI) so với lợi nhuận sau thuế cho thấy chất lượng của dòng tiền tạo ra, là yếu tố quan trọng cho lợi suất. |
| 2 | `safe_div(net_income, total_assets)` | tỷ số | Sinh lời | — | Tỷ lệ lợi nhuận sau thuế trên tổng tài sản thể hiện hiệu quả sử dụng tài sản tổng thể của doanh nghiệp, là thước đo cơ bản về khả năng sinh lời. |
| 2 | `safe_div(share_of_associates, net_income_parent)` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Tỷ lệ lợi nhuận từ các công ty liên kết so với lợi nhuận sau thuế của công ty mẹ cho thấy mức độ phụ thuộc và hiệu quả của mô hình liên kết. |
| 1 | `zscore(growth(share_of_associates, 1)) * abs(revenue) * 0.5` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Công thức này đo lường mức độ tăng trưởng lợi nhuận từ các công ty liên doanh/liên kết so với mức trung bình của toàn thị trường, được điều chỉnh theo quy mô do |
| 1 | `zscore(growth(share_of_associates, 4)) * abs(revenue) * 0.5` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Công thức này đo lường mức độ tăng trưởng lợi nhuận từ các công ty liên doanh/liên kết so với mức trung bình của toàn thị trường, được điều chỉnh theo quy mô do |
| 1 | `zscore(growth(share_of_associates, 4)) * abs(growth(revenue, 4))` | tổ hợp | Liên kết / đầu tư tài chính | — | Công thức này đo lường mức độ tăng trưởng của phần lãi lỗ từ công ty liên doanh/liên kết so với mức tăng trưởng doanh thu trong kỳ. Tỷ lệ cao cho thấy sự tăng t |
| 1 | `zscore(lag(cfi, 1)) * abs(long_term_investments)` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Đo lường sự biến động của dòng tiền thuần từ hoạt động đầu tư trong quá khứ, được chuẩn hóa theo quy mô tài sản dài hạn để dự đoán khả năng tạo ra dòng tiền tíc |
| 1 | `zscore(growth(share_of_associates, 1)) * abs(revenue) * log(equity)` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Công thức này đo lường mức độ tăng trưởng lợi nhuận từ các công ty liên doanh/liên kết so với mức trung bình của thị trường, được điều chỉnh theo quy mô doanh t |
| 1 | `zscore(growth(share_of_associates, 4)) * abs(revenue)` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Công thức này đo lường mức độ tăng trưởng lợi nhuận từ các công ty liên doanh/liên kết so với mức trung bình của thị trường, được nhân với doanh thu để đánh giá |
| 1 | `zscore(lag(net_income, 2)) * abs(share_of_associates)` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | So sánh lợi nhuận sau thuế gần đây với phần lãi lỗ từ liên doanh, giúp xác định xem hiệu quả hoạt động kinh doanh có tương quan với kết quả từ các liên kết hay  |
| 1 | `delta(equity, 1) * safe_div(investments_associates, total_assets)` | tổ hợp | Liên kết / đầu tư tài chính | — | Đo lường sự thay đổi tương đối của vốn chủ sở hữu so với tổng tài sản, đồng thời xem xét mức độ đầu tư vào liên doanh. Sự thay đổi tích cực của tỷ lệ này cho th |
| 1 | `delta(minority_interest, 4) * log(market_cap)` | tổ hợp | Định giá | nhân với quy mô công ty | Đo lường sự biến động (delta) của lợi ích cổ đông không kiểm soát. Sự biến động mạnh trong lợi ích này, khi nhân với log của vốn hóa thị trường, có thể là tín h |
| 1 | `delta(net_income_parent, 2) * rank(net_income_parent)` | 1 biến | Khác | nhân với quy mô công ty | Sự thay đổi lợi nhuận sau thuế của công ty mẹ trong quá khứ có thể là tín hiệu cho lợi suất sắp tới. |
| 1 | `delta(net_income_parent, 4) - delta(share_of_associates, 4)` | tổ hợp | Liên kết / đầu tư tài chính | — | Công thức này so sánh sự thay đổi của lợi nhuận sau thuế của công ty mẹ với sự thay đổi của phần lãi lỗ từ công ty liên doanh/liên kết. Sự chênh lệch dương cho  |
| 1 | `delta(share_of_associates, 4) * financial_income` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Công thức này tập trung vào sự thay đổi (delta) trong lợi nhuận từ các công ty liên kết, nhân với thu nhập tài chính. Nó đánh giá hiệu quả của các khoản đầu tư  |
| 1 | `growth(share_of_associates, 1) * zscore(share_of_associates)` | 1 biến | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Tốc độ tăng trưởng lợi nhuận từ liên doanh là yếu tố quan trọng dự báo lợi suất trong quý tới. |
| 1 | `rank(minority_interest) * lag(minority_interest, 2)` | 1 biến | Khác | lặp một biến hai lần; nhân với quy mô công ty | Công thức này sử dụng sự xếp hạng của lợi ích cổ đông không kiểm soát (minority_interest) và so sánh nó với giá trị của nó trong quá khứ. Điều này giúp xác định |
| 1 | `lag(minority_interest, 2) * safe_div(equity, total_assets)` | tổ hợp | Khác | nhân với quy mô công ty | Đo lường sự thay đổi trong mức độ lợi ích cổ đông không kiểm soát so với tỷ lệ vốn chủ sở hữu trên tổng tài sản. Sự biến động của tỷ lệ này có thể phản ánh sự t |
| 1 | `zscore(long_term_investments) * safe_div(equity, total_assets)` | tổ hợp | Liên kết / đầu tư tài chính | nhân với quy mô công ty | Đo lường mức độ tập trung vào đầu tư dài hạn so với cấu trúc vốn của công ty, giúp đánh giá tính ổn định và định hướng chiến lược của doanh nghiệp. |
| 1 | `growth(investments_associates, 2)` | 1 biến | Liên kết / đầu tư tài chính | — | Tốc độ tăng trưởng của khoản đầu tư vào công ty liên kết phản ánh sự mở rộng hoặc thu hẹp chiến lược liên kết của doanh nghiệp. |
| 1 | `growth(investments_associates, 4)` | 1 biến | Liên kết / đầu tư tài chính | — | Tốc độ tăng trưởng của khoản đầu tư vào công ty liên kết phản ánh sự mở rộng chiến lược và tiềm năng tăng trưởng của danh mục đầu tư. |
| 1 | `growth(long_term_investments, 2)` | 1 biến | Liên kết / đầu tư tài chính | — | Tốc độ tăng trưởng của khoản đầu tư dài hạn phản ánh sự gia tăng giá trị của các tài sản liên quan, có thể là tín hiệu tích cực cho lợi suất. |
| 1 | `rank(net_income_parent * safe_div(total_assets, investments_associates))` | tổ hợp | Sinh lời, Liên kết / đầu tư tài chính | nhân với quy mô công ty | Công thức này tạo ra một chỉ số dựa trên tỷ lệ lợi nhuận sau thuế của công ty mẹ so với tổng tài sản, được điều chỉnh bằng mức độ đầu tư vào công ty liên kết, n |
| 1 | `safe_div(investments_associates, equity)` | tỷ số | Liên kết / đầu tư tài chính | — | Tỷ lệ giữa khoản đầu tư vào công ty liên kết và vốn chủ sở hữu cho thấy mức độ đòn bẩy tài chính trong hoạt động liên kết. |
| 1 | `safe_div(minority_interest, equity)` | tỷ số | Khác | — | Tỷ lệ lợi ích cổ đông không kiểm soát so với vốn chủ sở hữu có thể là chỉ báo về mức độ phụ thuộc hoặc rủi ro trong cấu trúc liên kết. |
| 1 | `safe_div(minority_interest, total_assets)` | tỷ số | Khác | — | Tỷ lệ lợi ích cổ đông không kiểm soát so với tổng tài sản cho thấy mức độ rủi ro và mức độ tham gia vào các cấu trúc liên kết. |
| 1 | `safe_div(share_of_associates, net_income)` | tỷ số | Sinh lời, Liên kết / đầu tư tài chính | — | Tỷ lệ phần lợi nhuận từ liên kết so với lợi nhuận sau thuế của công ty mẹ cho thấy mức độ đóng góp của hoạt động liên kết vào kết quả cuối cùng. |
| 1 | `safe_div(share_of_associates, revenue)` | tỷ số | Liên kết / đầu tư tài chính | — | Tỷ lệ lợi nhuận từ các công ty liên kết so với doanh thu cho thấy hiệu quả của mô hình liên doanh trong việc tạo ra thu nhập. |
| 1 | `zscore(revenue * minority_interest)` | tổ hợp | Khác | nhân với quy mô công ty | Công thức này kết hợp doanh thu và lợi ích cổ đông không kiểm soát để đánh giá hiệu suất sinh lời của các cổ phiếu, phản ánh khả năng tạo ra doanh thu từ các li |
| 1 | `zscore(growth(net_income_parent, 1))` | 1 biến | Khác | — | Công thức này tập trung vào tốc độ tăng trưởng lợi nhuận sau thuế của công ty mẹ, xem xét khả năng sinh lời tổng thể của doanh nghiệp thông qua các hoạt động li |
| 1 | `zscore(lag(share_of_associates, 1))` | 1 biến | Liên kết / đầu tư tài chính | — | Đo lường sự biến động của phần lãi lỗ từ công ty liên kết trong kỳ, sử dụng độ trễ (lag) để xem xét tác động của kết quả kỳ trước lên hiệu suất hiện tại. |

### bank_loans

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 2 | `abs(related_party_disclosed) * (1 - audit_opinion_qualified)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Công thức này tập trung vào rủi ro quản trị và minh bạch. Tỷ lệ này định lượng mức độ rủi ro liên quan đến giao dịch với bên liên quan và rủi ro kiểm toán, nhữn |
| 2 | `abs(net_income - cfo)` | tổ hợp | Chất lượng lợi nhuận (dồn tích) | — | Sự khác biệt giữa lợi nhuận kế toán và dòng tiền thuần cho thấy mức độ chất lượng của lợi nhuận, trong khi việc điều chỉnh dự phòng tín dụng (thường ảnh hưởng đ |
| 2 | `abs(going_concern_flag)` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Sự hiện diện của tín hiệu nghi ngờ khả năng hoạt động liên tục là một yếu tố tiêu cực mạnh, làm giảm kỳ vọng lợi suất trong tương lai. |
| 2 | `delta(safe_div(net_income, total_assets), 4)` | biến đổi của tỷ số | Sinh lời | — | Tỷ suất lợi nhuận sau thuế trên tổng tài sản là thước đo hiệu quả hoạt động tổng thể, có thể phản ánh chất lượng kinh doanh trong kỳ. |
| 2 | `zscore(related_party_disclosed)` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Đo lường mức độ bất thường của việc có giao dịch với bên liên quan trong kỳ so với mức trung bình của toàn thị trường. Sự gia tăng bất thường có thể là tín hiệu |
| 1 | `mean(cff, 2) * (1 + contingent_liabilities_disclosed)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Công thức này kết hợp lưu chuyển tiền từ hoạt động tài chính (cff) với mức độ rủi ro tiềm tàng (contingent_liabilities_disclosed). Lưu chuyển tiền tốt hơn kết h |
| 1 | `abs(related_party_disclosed) * (1 - going_concern_flag)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Các yếu tố như giao dịch với bên liên quan và nghi ngờ khả năng hoạt động liên tục là các tín hiệu cảnh báo rủi ro tiềm ẩn, làm giảm chất lượng cổ phiếu. |
| 1 | `mean(cff, 2) * safe_div(equity, total_assets) * (1 - going_concern_flag)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Công thức này đánh giá khả năng thanh khoản và khả năng thanh toán. Lưu chuyển tiền từ hoạt động tài chính (cff) kết hợp với tỷ lệ vốn chủ sở hữu trên tổng tài  |
| 1 | `related_party_disclosed * 2` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Mức độ giao dịch với bên liên quan là chỉ báo về rủi ro quản trị và minh bạch, ảnh hưởng tiêu cực đến định giá cổ phiếu. |
| 1 | `abs(cfo) * safe_div(total_assets, equity)` | tổ hợp | Khác | nhân với quy mô công ty | Lưu chuyển tiền thuần từ hoạt động kinh doanh so với tỷ lệ tài sản trên vốn chủ sở hữu phản ánh khả năng tạo tiền mặt từ hoạt động cốt lõi. |
| 1 | `zscore(lag(net_income, 1)) * abs(cfo)` | tổ hợp | Chất lượng lợi nhuận (dồn tích) | nhân với quy mô công ty | Đo lường sự biến động của lợi nhuận sau thuế trong quý trước đó, được chuẩn hóa theo giá trị tuyệt đối của dòng tiền thuần từ hoạt động kinh doanh. Điều này giú |
| 1 | `log(pretax_profit) * abs(related_party_disclosed)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới); nhân với quy mô công ty | Đo lường mối liên hệ giữa lợi nhuận (pretax_profit) và mức độ rủi ro liên quan đến giao dịch với bên liên quan (related_party_disclosed). Lợi nhuận cao đi kèm v |
| 1 | `related_party_disclosed * audit_opinion_qualified` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Mức độ minh bạch và rủi ro kiểm toán là yếu tố quan trọng ảnh hưởng đến sự ổn định và định giá cổ phiếu. |
| 1 | `delta(cfo, 1) * safe_div(equity, 1)` | tổ hợp | Khác | — | Phân tích sự thay đổi của dòng tiền thuần từ hoạt động kinh doanh so với vốn chủ sở hữu, một chỉ báo quan trọng về khả năng tạo ra dòng tiền bền vững từ hoạt độ |
| 1 | `growth(net_income, 2) * zscore(cff)` | tổ hợp | Khác | nhân với quy mô công ty | Phân tích tốc độ tăng trưởng lợi nhuận trong hai quý gần nhất, được chuẩn hóa theo sự biến động của dòng tiền tài chính. Công thức này tìm kiếm các chu kỳ tăng  |
| 1 | `growth(net_income, 2) * zscore(market_cap)` | tổ hợp | Định giá | nhân với quy mô công ty | Đánh giá mối quan hệ giữa sự tăng trưởng lợi nhuận sau thuế trong hai quý trước và vốn hóa thị trường, xem xét liệu lợi nhuận có được thị trường định giá đúng m |
| 1 | `log(pretax_profit) * std(net_income, 4)` | tổ hợp | Khác | nhân với quy mô công ty | Công thức này kết hợp lợi nhuận trước thuế với độ biến động của lợi nhuận sau thuế. Lợi nhuận cao đi kèm với sự ổn định (biến động thấp) có thể là dấu hiệu của  |
| 1 | `related_party_disclosed * zscore(close_price)` | tổ hợp | Định giá, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới); nhân với quy mô công ty | Cổ phiếu có mức độ minh bạch về giao dịch với bên liên quan cao hơn (related_party_disclosed) có thể mang lại rủi ro khác biệt, được điều chỉnh theo biến động g |
| 1 | `abs(lag(cfo, 2))` | 1 biến | Khác | chỉ là quy mô (không chuẩn hoá) | Phân tích sự thay đổi của dòng tiền thuần từ hoạt động kinh doanh trong hai quý trước, giúp đánh giá tính ổn định của dòng tiền, yếu tố quan trọng đối với ngân  |
| 1 | `abs(related_party_disclosed)` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Sự hiện diện của thuyết minh về khả năng hoạt động liên tục (going concern) là tín hiệu cảnh báo rủi ro tiềm ẩn, ảnh hưởng tiêu cực đến lợi suất. |
| 1 | `rank(net_income)` | 1 biến | Khác | — | Xếp hạng lợi nhuận sau thuế giúp xác định vị thế của doanh nghiệp trong kỳ, ảnh hưởng đến định giá. |
| 1 | `safe_div(cfo, pretax_profit)` | tỷ số | Sinh lời | — | Công thức này đánh giá khả năng chuyển đổi hoạt động kinh doanh thành dòng tiền. Tỷ lệ này cho thấy mức độ hiệu quả của việc tạo ra tiền mặt từ hoạt động cốt lõ |
| 1 | `zscore(cff)` | 1 biến | Khác | — | Lưu chuyển tiền thuần từ hoạt động tài chính (cff) là chỉ báo về khả năng quản lý rủi ro và huy động vốn, ảnh hưởng đến sự ổn định của cổ phiếu. |
| 1 | `zscore(lag(net_income, 1))` | 1 biến | Khác | — | Đo lường sự biến động của lợi nhuận sau thuế trong quý trước, có thể phản ánh chất lượng hoạt động kinh doanh và khả năng tạo ra dòng tiền trong kỳ tiếp theo. |
| 1 | `zscore(lag(total_assets, 1))` | 1 biến | Khác | — | Đo lường sự thay đổi tương đối của tổng tài sản qua các quý, giúp xác định các quý có sự biến động bất thường trong cơ cấu tài sản, có thể liên quan đến chất lư |

### cip

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(cfo, 1) * lag(construction_in_progress, 1)` | tổ hợp | Đầu tư / tăng trưởng tài sản | nhân với quy mô công ty | Sự tăng trưởng của dòng tiền thuần kết hợp với mức độ dở dang của các dự án sẽ cho thấy khả năng tài trợ và tiến độ hoàn thành các nghĩa vụ đầu tư trong kỳ. |
| 3 | `lag(depreciation, 2)` | 1 biến | Khác | chỉ là quy mô (không chuẩn hoá) | Khấu hao là chi phí cố định, sự biến động của nó theo thời gian có thể là tín hiệu về mức độ sử dụng tài sản hiện tại. |
| 3 | `safe_div(abs(capex), construction_in_progress)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi tiền chi mua sắm, xây dựng so với chi phí dở dang cho thấy áp lực đầu tư mới, có thể dẫn đến lợi suất ngắn hạn thấp hơn. |
| 3 | `safe_div(capex, revenue)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi tiêu cho xây dựng mới so với doanh thu phản ánh mức độ đầu tư vào tăng trưởng trong kỳ, ảnh hưởng đến định giá. |
| 3 | `safe_div(construction_in_progress, total_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi phí xây dựng cơ bản dở dang so với tổng tài sản phản ánh mức độ cam kết và khối lượng dự án đang triển khai, có thể là tín hiệu cho các chu kỳ tăng tr |
| 2 | `growth(construction_in_progress, 1) * safe_div(revenue, total_assets) + zscore(construction_in_progress) * 0.5` | tổ hợp | Đầu tư / tăng trưởng tài sản | — | Công thức này đo lường mức độ tăng trưởng của tài sản dở dang so với tổng tài sản và chuẩn hóa theo phân phối của nó. Nó dự đoán rằng sự gia tăng của tài sản dở |
| 2 | `delta(net_income, 4)` | 1 biến | Khác | — | Thay đổi lợi nhuận sau thuế trong 4 quý gần nhất là chỉ báo quan trọng về hiệu quả kinh doanh và khả năng sinh lời. |
| 2 | `growth(capex, 2)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Tốc độ tăng của chi tiêu vốn (capex) so với quá khứ có thể dự báo áp lực lên lợi nhuận trong tương lai. |
| 2 | `safe_div(construction_in_progress, equity)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi phí dở dang so với vốn chủ sở hữu đo lường mức độ rủi ro vốn trong các dự án, ảnh hưởng trực tiếp đến lợi suất cổ phiếu trong chu kỳ đầu tư. |
| 1 | `lag(capex, 2) * safe_div(revenue, net_income) + abs(capex) * zscore(capex)` | tổ hợp | Sinh lời, Đầu tư / tăng trưởng tài sản | lặp một biến hai lần; nhân với quy mô công ty | Công thức này tập trung vào mối quan hệ giữa chi tiêu đầu tư (capex) và doanh thu, được nhìn lại qua hai quý. Tăng trưởng chi tiêu đầu tư so với lợi nhuận cho t |
| 1 | `abs(net_income) * safe_div(construction_in_progress, construction_in_progress) + lag(net_income, 1)` | tổ hợp | Sinh lời, Đầu tư / tăng trưởng tài sản | nhân với quy mô công ty | Công thức này xem xét lợi nhuận sau thuế so với tài sản dở dang. Lợi nhuận cao hơn so với tài sản dở dang cho thấy hiệu quả kinh doanh trong giai đoạn xây dựng, |
| 1 | `lag(capex, 2) * safe_div(equity, long_term_assets) + delta(capex, 2)` | tổ hợp | Đầu tư / tăng trưởng tài sản | nhân với quy mô công ty | Đo lường mối quan hệ giữa chi tiêu đầu tư (CAPEX) và nguồn vốn chủ sở hữu. Tỷ lệ cao có thể chỉ ra sự mở rộng mạnh mẽ của hoạt động đầu tư so với khả năng tài t |
| 1 | `lag(capex, 2) * safe_div(equity, long_term_debt) + delta(capex, 2)` | tổ hợp | Đầu tư / tăng trưởng tài sản, Đòn bẩy / thanh khoản | nhân với quy mô công ty | Công thức này tập trung vào dòng tiền chi ra cho đầu tư (capex) so với cơ cấu vốn chủ sở hữu. Tỷ lệ này phản ánh áp lực tài chính từ việc đầu tư, có thể là tín  |
| 1 | `safe_div(construction_in_progress, revenue)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi phí dở dang so với doanh thu cho thấy gánh nặng chi phí đầu tư so với khả năng tạo ra doanh thu, ảnh hưởng đến chất lượng lợi nhuận. |

### commitments

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `abs(contingent_liabilities_disclosed) * growth(revenue, 1)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Mức độ cam kết tiềm tàng (contingent_liabilities_disclosed) càng lớn so với doanh thu trong kỳ càng cho thấy rủi ro tài chính chưa được định giá đầy đủ, làm giả |
| 3 | `abs(contingent_liabilities_disclosed) * safe_div(1 + cash_and_equivalents, total_assets)` | tổ hợp | Đòn bẩy / thanh khoản, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tỷ lệ nợ tiềm tàng so với tài sản cho thấy rủi ro tài chính tiềm ẩn, ảnh hưởng tiêu cực đến lợi suất. |
| 3 | `abs(contingent_liabilities_disclosed) * safe_div(total_assets, cash_and_equivalents)` | tổ hợp | Đòn bẩy / thanh khoản, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Công thức này đo lường mức độ rủi ro tiềm tàng (cam kết/nợ tiềm tàng) so với tổng tài sản, cho thấy mức độ phụ thuộc của công ty vào các nghĩa vụ chưa được ghi  |
| 3 | `growth(revenue, 1)` | 1 biến | Khác | — | Tăng trưởng doanh thu trong kỳ là một chỉ báo cơ bản về khả năng tạo ra dòng tiền trong tương lai, doanh nghiệp có tăng trưởng cao hơn sẽ có lợi suất tốt hơn. |
| 2 | `growth(cfo, 2) * log(revenue)` | tổ hợp | Khác | nhân với quy mô công ty | Lưu chuyển tiền thuần tăng trưởng nhanh kết hợp với doanh thu cho thấy động lực tích cực cho giá cổ phiếu. |
| 2 | `safe_div(capex, construction_in_progress)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi tiêu cho tài sản mới (capex) so với tài sản dở dang cho thấy mức độ tái đầu tư, nếu tỷ lệ này cao có thể là dấu hiệu của việc tài sản đang bị sử dụng  |
| 1 | `abs(capex) * safe_div(equity, construction_in_progress)` | tổ hợp | Đầu tư / tăng trưởng tài sản | nhân với quy mô công ty | Đo lường mức độ sử dụng vốn đầu tư (CAPEX) so với vốn chủ sở hữu, giúp đánh giá áp lực tài chính từ các dự án đang triển khai. Tỷ lệ cao có thể gây áp lực lên c |
| 1 | `cfo * safe_div(total_liabilities, cash_and_equivalents)` | tổ hợp | Đòn bẩy / thanh khoản | nhân với quy mô công ty | Đánh giá khả năng thanh toán ngắn hạn thông qua lưu chuyển tiền thuần so với tổng nợ phải trả, phản ánh sức khỏe dòng tiền trong việc đáp ứng nghĩa vụ nợ. |
| 1 | `delta(cash_and_equivalents, 1) - delta(equity, 1)` | tổ hợp | Đòn bẩy / thanh khoản | — | Công thức này so sánh sự thay đổi (delta) của dòng tiền mặt và vốn chủ sở hữu trong kỳ. Sự gia tăng của dòng tiền mặt so với vốn chủ sở hữu cho thấy khả năng th |
| 1 | `growth(cfo, 2) * log(net_income)` | tổ hợp | Chất lượng lợi nhuận (dồn tích) | nhân với quy mô công ty | So sánh tốc độ tăng trưởng của dòng tiền thuần với lợi nhuận sau thuế, một chỉ báo về chất lượng lợi nhuận và khả năng tạo ra dòng tiền thực tế. |
| 1 | `safe_div(cfo, total_liabilities) * log(cash_and_equivalents)` | tổ hợp | Đòn bẩy / thanh khoản | nhân với quy mô công ty | Đánh giá khả năng thanh toán bằng dòng tiền thuần so với tổng nợ phải trả, được điều chỉnh bằng mức độ tiền mặt hiện có. Tỷ lệ cao cho thấy khả năng xoay vòng v |
| 1 | `zscore(contingent_liabilities_disclosed) * log(cash_and_equivalents)` | tổ hợp | Đòn bẩy / thanh khoản, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới); nhân với quy mô công ty | Công thức này đo lường mức độ rủi ro tiềm tàng (contingent liabilities) được thể hiện trong thuyết minh, chuẩn hóa theo toàn thị trường, và nhân với tỷ lệ tiền  |
| 1 | `zscore(equity) - zscore(total_liabilities)` | tổ hợp | Đòn bẩy / thanh khoản | — | Chỉ số này đo lường sức khỏe cơ cấu vốn, sự chênh lệch giữa vốn chủ sở hữu và nợ phải trả. |
| 1 | `growth(cfo, 2)` | 1 biến | Khác | — | Đo lường tốc độ tăng trưởng của dòng tiền thuần từ hoạt động kinh doanh so với quý trước, là chỉ báo sức khỏe hoạt động thực tế, giúp dự đoán khả năng tạo ra dò |
| 1 | `growth(revenue, 2)` | 1 biến | Khác | — | Tăng trưởng doanh thu trong kỳ phản ánh khả năng thực hiện các cam kết kinh doanh trong tương lai, một yếu tố quan trọng cho lợi suất cổ phiếu. |
| 1 | `safe_div(cfo, total_liabilities)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ này đánh giá khả năng thanh toán ngắn hạn thông qua dòng tiền hoạt động so với tổng nợ phải trả, là chỉ số quan trọng về sức khỏe tài chính tức thời. |

### customer_advances

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(customer_advances, revenue)` | tỷ số | Vốn lưu động | — | Tỷ lệ tiền người mua trả trước so với doanh thu cho thấy mức độ tiền mặt đã được thu về từ các giao dịch bán hàng, là chỉ báo trực tiếp về chất lượng dòng tiền  |
| 3 | `safe_div(revenue, total_assets)` | tỷ số | Khác | — | Tỷ lệ doanh thu (bao gồm cả chưa thực hiện) so với tổng tài sản phản ánh mức độ tài sản đang được sử dụng để tạo ra doanh thu, cho thấy tính chất của tài sản. |
| 3 | `zscore(customer_advances)` | 1 biến | Vốn lưu động | — | Tỷ lệ người mua trả tiền trước (customer_advances) được chuẩn hóa để đo lường mức độ phụ thuộc vào tiền mặt từ khách hàng, một chỉ báo mạnh mẽ về chất lượng doa |
| 3 | `zscore(growth(revenue, 1))` | 1 biến | Khác | — | Tốc độ tăng trưởng doanh thu (growth(revenue, 1)) trong quý trước là một yếu tố quan trọng dự báo sự mở rộng của hoạt động kinh doanh, ảnh hưởng tích cực đến lợ |
| 2 | `zscore(customer_advances) * 1.5` | 1 biến | Vốn lưu động | — | Tỷ lệ người mua trả tiền trước (customer_advances) được chuẩn hóa để đo lường mức độ phụ thuộc vào tiền trả trước của doanh nghiệp, một chỉ báo quan trọng cho d |
| 2 | `abs(safe_div(revenue, lag(customer_advances, 1))) * log(cash_and_equivalents)` | tổ hợp | Đòn bẩy / thanh khoản, Vốn lưu động | nhân với quy mô công ty | Đo lường mức độ doanh thu thực tế có thể bù đắp cho các khoản tiền khách hàng đã trả trước trong kỳ trước, sau đó điều chỉnh theo mức độ thanh khoản (cash_and_e |
| 2 | `growth(inventory, 1) * safe_div(total_assets, inventory)` | tổ hợp | Đầu tư / tăng trưởng tài sản, Vốn lưu động | — | Đánh giá tốc độ tăng của hàng tồn kho so với tổng tài sản, cho thấy mức độ rủi ro về giá trị hàng tồn kho. Tốc độ tăng cao có thể là tín hiệu tiêu cực. |
| 2 | `safe_div(customer_advances, equity)` | tỷ số | Vốn lưu động | — | Tỷ lệ tiền người mua trả trước so với vốn chủ sở hữu đo lường mức độ tài trợ hoạt động kinh doanh bằng nguồn vốn của cổ đông, cho thấy sự phụ thuộc vào vốn huy  |
| 1 | `growth(cfo, 2) * safe_div(equity, cash_and_equivalents)` | tổ hợp | Đòn bẩy / thanh khoản | — | Tăng trưởng dòng tiền thuần so với vốn chủ sở hữu cho thấy hiệu quả sử dụng vốn và khả năng sinh lời từ hoạt động kinh doanh. |
| 1 | `safe_div(revenue, total_assets) * lag(revenue, 1)` | tổ hợp | Khác | nhân với quy mô công ty | Tỷ lệ doanh thu so với tổng tài sản trong kỳ trước cho thấy khả năng tạo ra doanh thu tương lai dựa trên quy mô tài sản. |
| 1 | `growth(cfo, 4)` | 1 biến | Khác | — | Tốc độ tăng trưởng của dòng tiền thuần so với vốn chủ sở hữu phản ánh hiệu quả sử dụng vốn và khả năng sinh lời. |
| 1 | `safe_div(revenue, lag(total_assets, 2))` | tỷ số | Khác | — | Tỷ lệ doanh thu so với tổng tài sản trong quá khứ cho thấy khả năng tạo ra doanh thu tương lai từ tài sản hiện có. |
| 1 | `safe_div(short_term_receivables, customer_advances)` | tỷ số | Vốn lưu động | — | So sánh các khoản phải thu ngắn hạn với tiền người mua trả trước giúp đánh giá tính thanh khoản của các khoản tiền thu được, một yếu tố quan trọng cho dòng tiền |
| 1 | `zscore(lag(cfo, 1))` | 1 biến | Khác | — | Lưu chuyển tiền thuần từ hoạt động kinh doanh (cfo) của quý trước là chỉ báo trực tiếp về sức khỏe dòng tiền, có tác động mạnh mẽ đến giá cổ phiếu. |

### debt

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(long_term_debt, total_assets)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ dài hạn trên tổng tài sản là thước đo mức độ đòn bẩy tài chính tổng thể của công ty, rủi ro cao hơn cho cổ phiếu. |
| 3 | `zscore(lag(interest_expense, 1))` | 1 biến | Đòn bẩy / thanh khoản | — | Đo lường sự thay đổi bất thường của chi phí lãi vay trong quý hiện tại so với quý trước, chuẩn hóa trên toàn bộ thị trường để xác định các quý có rủi ro hoặc bi |
| 2 | `rank(growth(long_term_debt, 2))` | 1 biến | Đòn bẩy / thanh khoản | — | Xếp hạng dựa trên tốc độ tăng trưởng của nợ vay dài hạn trong các quý trước, cho thấy xu hướng gia tăng gánh nặng tài chính trong tương lai. |
| 2 | `rank(safe_div(long_term_debt, total_liabilities))` | biến đổi của tỷ số | Đòn bẩy / thanh khoản | — | Xếp hạng dựa trên tỷ lệ nợ dài hạn so với tổng nợ (bao gồm cả ngắn hạn), phản ánh mức độ phụ thuộc vào nợ vay dài hạn của doanh nghiệp. |
| 2 | `safe_div(short_term_debt, total_liabilities)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ ngắn hạn so với tổng nợ phải trả phản ánh mức độ phụ thuộc vào nguồn vốn ngắn hạn, tăng rủi ro thanh khoản. |
| 1 | `abs(interest_expense) * safe_div(total_liabilities, total_liabilities)` | tổ hợp | Đòn bẩy / thanh khoản | nhân với quy mô công ty | Tỷ lệ chi phí lãi vay so với tổng nợ cho thấy mức độ áp lực chi phí tài chính. Tỷ lệ cao hơn có thể báo hiệu rủi ro thanh khoản cao hơn trong quý tới. |
| 1 | `growth(financial_expense, 2) * mean(financial_expense, 2)` | 1 biến | Khác | — | Phân tích xu hướng tăng trưởng của chi phí tài chính trong hai quý gần nhất, sau đó chuẩn hóa bằng giá trị trung bình, giúp xác định các doanh nghiệp có xu hướn |
| 1 | `growth(interest_expense, 1) * log(interest_expense)` | 1 biến | Đòn bẩy / thanh khoản | nhân với quy mô công ty | Đánh giá tốc độ tăng trưởng chi phí lãi vay trong kỳ, một chỉ báo trực tiếp về áp lực tài chính và khả năng trả nợ trong tương lai. |
| 1 | `lag(interest_expense, 1) * safe_div(current_liabilities, total_liabilities)` | tổ hợp | Đòn bẩy / thanh khoản | nhân với quy mô công ty | Đo lường mối quan hệ giữa chi phí lãi vay kỳ trước và tỷ lệ nợ ngắn hạn so với tổng nợ, dự đoán áp lực thanh khoản trong kỳ tới. |
| 1 | `rank(lag(interest_expense, 1)) * safe_div(interest_expense, revenue)` | tổ hợp | Đòn bẩy / thanh khoản | nhân với quy mô công ty | Đo lường tỷ lệ chi phí lãi vay so với doanh thu trong kỳ trước, một chỉ báo trực tiếp về áp lực chi phí tài chính lên kết quả kinh doanh. |
| 1 | `rank(growth(cfo, 1))` | 1 biến | Khác | — | Đánh giá khả năng tạo ra dòng tiền hoạt động (CFO) tăng trưởng trong quý tới, một chỉ báo quan trọng về sức khỏe hoạt động, có thể liên quan đến khả năng trả nợ |
| 1 | `rank(growth(cfo, 2))` | 1 biến | Khác | — | Tốc độ tăng trưởng lưu chuyển tiền thuần từ hoạt động kinh doanh là yếu tố quan trọng, có thể là tín hiệu tích cực cho lợi suất cổ phiếu. |
| 1 | `rank(growth(interest_expense, 4))` | 1 biến | Đòn bẩy / thanh khoản | — | Xếp hạng các doanh nghiệp có xu hướng tăng trưởng chi phí lãi vay trong 4 quý gần nhất, giúp dự đoán xu hướng chi phí tài chính trong tương lai. |
| 1 | `rank(mean(financial_expense, 4))` | 1 biến | Khác | — | Xếp hạng dựa trên giá trị trung bình của chi phí tài chính trong 4 quý gần nhất, giúp xác định các doanh nghiệp có xu hướng chi phí tài chính cao hơn mức trung  |
| 1 | `safe_div(short_term_debt + long_term_debt, total_assets)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ tổng thể so với tổng tài sản đo mức độ đòn bẩy tài chính, mức độ đòn bẩy cao hơn làm tăng rủi ro thua lỗ. |
| 1 | `safe_div(short_term_debt + long_term_debt, total_liabilities)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ phải trả so với tổng nợ phải trả đo mức độ rủi ro thanh khoản, tỷ lệ cao hơn cho thấy áp lực trả nợ lớn hơn. |
| 1 | `safe_div(interest_expense, net_income)` | tỷ số | Sinh lời, Đòn bẩy / thanh khoản | — | Tỷ lệ chi phí lãi vay so với lợi nhuận sau thuế cho thấy mức độ chi phí lãi vay ăn mòn lợi nhuận ròng; tỷ lệ cao hơn làm giảm chất lượng lợi nhuận. |
| 1 | `safe_div(long_term_debt, total_liabilities)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ dài hạn so với tổng nợ phải trả đánh giá cấu trúc tài trợ dài hạn, ảnh hưởng đến khả năng chống chịu rủi ro lãi suất. |
| 1 | `safe_div(short_term_debt, current_liabilities)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ ngắn hạn trên nợ ngắn hạn đo lường mức độ phụ thuộc vào nguồn vốn ngắn hạn để chi trả các nghĩa vụ nợ. Tỷ lệ cao cho thấy rủi ro thanh khoản cao hơn, l |
| 1 | `safe_div(total_liabilities, total_assets)` | tỷ số | Đòn bẩy / thanh khoản | — | Tỷ lệ nợ trên tổng tài sản là thước đo đòn bẩy tài chính tổng thể. Đòn bẩy cao hơn thường đi kèm với rủi ro lợi suất cao hơn trong môi trường lãi suất biến động |
| 1 | `zscore(mean(financial_expense, 1))` | 1 biến | Khác | — | Đánh giá mức độ biến động trung bình của chi phí tài chính trong một khoảng thời gian ngắn, chuẩn hóa để xác định các quý có chi phí tài chính cao bất thường, l |
| 1 | `zscore(mean(financial_expense, 2))` | 1 biến | Khác | — | Xếp hạng dựa trên mức độ biến động trung bình của chi phí tài chính trong 2 quý gần nhất, giúp lọc ra các doanh nghiệp có xu hướng chi phí tài chính không ổn đị |

### fin_assets

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `safe_div(cfo, equity)` | tỷ số | Khác | — | Tỷ lệ dòng tiền từ hoạt động kinh doanh so với vốn chủ sở hữu cho thấy khả năng tạo ra dòng tiền bền vững, là yếu tố quan trọng cho lợi suất. |
| 2 | `mean(related_party_disclosed, 1)` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Đánh giá mức độ minh bạch và rủi ro giao dịch với bên liên quan. Mức độ minh bạch (thường là số lần nhắc đến thấp) có thể là tín hiệu tích cực, giảm thiểu rủi r |
| 2 | `zscore(growth(net_income, 2))` | 1 biến | Khác | — | Sử dụng sự tăng trưởng lợi nhuận sau thuế trong hai quý trước để đánh giá đà tăng trưởng lợi nhuận. Các công ty có đà tăng trưởng lợi nhuận ổn định hơn có thể d |
| 1 | `growth(pretax_profit, 1) * safe_div(total_assets, equity)` | tổ hợp | Sinh lời, Đầu tư / tăng trưởng tài sản | — | Đo lường mức độ tăng trưởng lợi nhuận so với tổng tài sản, cho thấy hiệu quả sử dụng tài sản trong việc tạo ra lợi nhuận. Tỷ lệ cao có thể gợi ý về khả năng sin |
| 1 | `mean(cfo, 1) * safe_div(cfi, 1)` | tổ hợp | Khác | — | Đánh giá sự cân bằng giữa dòng tiền từ hoạt động kinh doanh (CFO) và hoạt động đầu tư (CFI). Tỷ lệ này phản ánh chất lượng dòng tiền, nơi dòng tiền từ kinh doan |
| 1 | `rank(cff)` | 1 biến | Khác | — | Thứ hạng của dòng tiền tài chính cho thấy mức độ thanh khoản và khả năng huy động vốn của doanh nghiệp, ảnh hưởng đến giá cổ phiếu. |
| 1 | `std(pretax_profit, 2)` | 1 biến | Khác | — | Độ biến động của lợi nhuận trước thuế trong 2 quý gần nhất cho thấy sự không ổn định của kết quả kinh doanh, ảnh hưởng đến lợi suất. |

### fixed_assets

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(capex, 1) * safe_div(fixed_assets, total_assets)` | tổ hợp | Đầu tư / tăng trưởng tài sản | — | Công thức này đo lường mức độ tăng trưởng chi tiêu đầu tư mới (capex) so với tổng tài sản, cho thấy khả năng mở rộng hoạt động trong quý tới. Tỷ lệ cao có thể d |
| 3 | `lag(depreciation, 1) * safe_div(revenue, revenue)` | tổ hợp | Khác | nhân với quy mô công ty | Đo lường mức độ khấu hao so với doanh thu trong kỳ trước, giúp đánh giá mức độ hao mòn tài sản cố định so với khả năng tạo ra doanh thu. Tỷ lệ này có thể phản á |
| 3 | `zscore(depreciation) * zscore(equity)` | tổ hợp | Khác | nhân với quy mô công ty | So sánh mức độ khấu hao (chi phí) với vốn chủ sở hữu. Một tỷ lệ cao có thể ám chỉ việc sử dụng tài sản hiệu quả để tạo ra lợi nhuận, ảnh hưởng đến giá trị vốn c |
| 3 | `safe_div(depreciation, fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ khấu hao so với tổng tài sản cố định phản ánh mức độ hao mòn của cơ sở vật chất, cho thấy mức độ sử dụng và tuổi thọ của tài sản trong kỳ. |
| 2 | `abs(capex) * safe_div(revenue, capex)` | tổ hợp | Đầu tư / tăng trưởng tài sản | nhân với quy mô công ty; tự triệt tiêu (x · y/x = y) | Tỷ lệ chi tiêu cho đầu tư mới (capex) so với doanh thu cho thấy mức độ mở rộng kinh doanh, một chỉ báo quan trọng về tiềm năng tăng trưởng trong quý tới. |
| 2 | `safe_div(abs(capex), equity)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi tiêu vốn so với vốn chủ sở hữu đo lường mức độ phụ thuộc vào đầu tư mới, có thể là rủi ro hoặc cơ hội. |
| 2 | `safe_div(revenue, tangible_fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Doanh thu so với tài sản cố định hữu hình đo lường hiệu quả sử dụng tài sản trong việc tạo ra doanh thu, giúp đánh giá chất lượng tài sản tạo ra dòng tiền. |
| 2 | `zscore(long_term_assets)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Điểm chuẩn hóa của tài sản dài hạn giúp đánh giá vị thế tài sản của công ty so với thị trường, ảnh hưởng đến định giá. |
| 1 | `rank(fixed_assets) * mean(fixed_assets, 4)` | 1 biến | Đầu tư / tăng trưởng tài sản | nhân với quy mô công ty | Công thức này sử dụng giá trị tài sản cố định để xếp hạng, sau đó lấy giá trị trung bình của nó. Nó đánh giá mức độ hiện hữu và quy mô tài sản, có thể là yếu tố |
| 1 | `zscore(fixed_assets) * rank(fixed_assets)` | 1 biến | Đầu tư / tăng trưởng tài sản | lặp một biến hai lần; nhân với quy mô công ty | Công thức này sử dụng giá trị tài sản cố định để xếp hạng, đo lường mức độ trọng số của tài sản cố định trong tổng thể tài sản, dự đoán cổ phiếu có tài sản cố đ |
| 1 | `lag(safe_div(depreciation, fixed_assets), 2)` | biến đổi của tỷ số | Đầu tư / tăng trưởng tài sản | — | Phân tích tỷ lệ khấu hao so với tài sản cố định trong hai quý trước, giúp đánh giá tính ổn định của chi phí khấu hao. Tỷ lệ thay đổi có thể là tín hiệu cho sự t |
| 1 | `safe_div(abs(capex), fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi tiêu cho đầu tư mới (capex) so với tổng tài sản cố định cho thấy mức độ tái đầu tư vào cơ sở vật chất, là yếu tố quan trọng cho tăng trưởng dài hạn. |
| 1 | `safe_div(abs(capex), revenue)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ chi tiêu cho đầu tư mới (capex) so với doanh thu cho thấy mức độ mở rộng hoạt động trong kỳ, có thể là tín hiệu của sự tăng trưởng trong tương lai. |
| 1 | `safe_div(fixed_assets, equity)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ tài sản cố định trên vốn chủ sở hữu đo lường mức độ tài sản được tài trợ bằng vốn chủ sở hữu, ảnh hưởng đến rủi ro và khả năng sinh lời. |
| 1 | `safe_div(tangible_fixed_assets, fixed_assets)` | tỷ số | Đầu tư / tăng trưởng tài sản | — | Tỷ lệ tài sản cố định hữu hình còn lại so với tổng tài sản cho thấy mức độ tài sản cố định đóng góp vào tổng tài sản, là thước đo cơ cấu tài sản. |
| 1 | `zscore(fixed_assets)` | 1 biến | Đầu tư / tăng trưởng tài sản | — | Sử dụng Z-score của giá trị tài sản cố định để xếp hạng các công ty có mức độ đầu tư tài sản cố định cao hơn hoặc thấp hơn mức trung bình trong cùng kỳ, dự đoán |
| 1 | `zscore(safe_div(capex, revenue))` | biến đổi của tỷ số | Đầu tư / tăng trưởng tài sản | — | Đo lường mức độ chi tiêu cho đầu tư mới (capex) so với doanh thu trong kỳ, là chỉ báo về mức độ mở rộng hoặc tái đầu tư. Giá trị cao có thể gợi ý về tiềm năng t |

### inventory

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `rank(lag(inventory_writedown, 1))` | 1 biến | Dự phòng / chất lượng tài sản | — | Xếp hạng dựa trên sự thay đổi của dự phòng giảm giá hàng tồn kho trong quý trước, giúp nắm bắt xu hướng biến động ngắn hạn của rủi ro tồn kho. |
| 3 | `safe_div(inventory, total_assets)` | tỷ số | Vốn lưu động | — | Tỷ lệ hàng tồn kho so với tổng tài sản thể hiện mức độ phụ thuộc của doanh nghiệp vào hàng tồn kho, tỷ lệ cao có thể làm giảm lợi suất cổ phiếu. |
| 3 | `zscore(inventory_writedown)` | 1 biến | Dự phòng / chất lượng tài sản | — | Đo lường mức độ biến động của dự phòng giảm giá hàng tồn kho so với mức trung bình của toàn thị trường, cho thấy rủi ro tiềm ẩn từ việc ghi nhận lỗ trong kỳ. |
| 3 | `zscore(lag(inventory_writedown, 1))` | 1 biến | Dự phòng / chất lượng tài sản | — | Đo lường mức độ bất thường của sự thay đổi dự phòng giảm giá hàng tồn kho trong quý trước so với phân phối toàn thị trường, giúp xác định các cổ phiếu có rủi ro |
| 2 | `delta(inventory_writedown, 2) * safe_div(market_cap, total_assets)` | tổ hợp | Định giá, Dự phòng / chất lượng tài sản | — | Sự thay đổi của dự phòng giảm giá hàng tồn kho so với quy mô vốn hóa thị trường cho thấy sự biến động của rủi ro tồn kho so với giá trị thị trường của cổ phiếu. |
| 2 | `rank(inventory_writedown) - rank(inventory_writedown)` | 1 biến | Dự phòng / chất lượng tài sản | — | Công thức này sử dụng hàm rank để xếp hạng mức độ dự phòng giảm giá hàng tồn kho, giúp xác định cổ phiếu có mức độ rủi ro cao nhất trong lát cắt ngang. |
| 2 | `rank(abs(lag(inventory_writedown, 1)))` | 1 biến | Dự phòng / chất lượng tài sản | — | Xếp hạng dựa trên sự thay đổi gần nhất của dự phòng giảm giá hàng tồn kho, giúp nắm bắt xu hướng ngắn hạn của rủi ro tồn kho. |
| 1 | `delta(inventory_writedown, 4) * safe_div(1, total_assets)` | tổ hợp | Dự phòng / chất lượng tài sản | hàm áp lên hằng số | Sự thay đổi của dự phòng giảm giá hàng tồn kho so với quy mô tài sản tổng thể là một chỉ báo về sự biến động trong việc đánh giá giá trị hàng tồn kho. |
| 1 | `safe_div(revenue, inventory_gross) * lag(1, 2)` | tổ hợp | Vốn lưu động | hàm áp lên hằng số | Tỷ lệ doanh thu so với hàng tồn kho gốc trong quá khứ cho thấy khả năng thanh lý hàng tồn kho và tác động đến lợi nhuận. |
| 1 | `zscore(inventory_writedown) * log(current_assets)` | tổ hợp | Dự phòng / chất lượng tài sản | nhân với quy mô công ty | Công thức này đo lường mức độ biến động của dự phòng giảm giá hàng tồn kho so với mức độ tài sản ngắn hạn, chuẩn hóa theo lát cắt ngang. Tỷ lệ cao có thể chỉ ra |
| 1 | `delta(safe_div(inventory, total_assets), 4)` | biến đổi của tỷ số | Vốn lưu động | — | Sự thay đổi của tỷ lệ hàng tồn kho trên tổng tài sản phản ánh hiệu quả quản lý hàng tồn kho trong kỳ. |
| 1 | `growth(inventory_gross, 4)` | 1 biến | Vốn lưu động | — | Đo lường tốc độ tăng trưởng của giá trị hàng tồn kho gốc trong 4 quý gần nhất, phản ánh sự biến động của giá hàng hóa trong kỳ. |
| 1 | `growth(inventory_writedown, 4)` | 1 biến | Dự phòng / chất lượng tài sản | — | Đo lường tốc độ thay đổi của dự phòng giảm giá hàng tồn kho trong 4 quý gần nhất, giúp nhận diện xu hướng biến động của rủi ro dự phòng. |
| 1 | `rank(growth(inventory_writedown, 1))` | 1 biến | Dự phòng / chất lượng tài sản | — | Đánh giá tốc độ tăng trưởng của dự phòng giảm giá hàng tồn kho qua các quý, xác định các cổ phiếu có xu hướng gia tăng rủi ro dự phòng trong tương lai. |
| 1 | `rank(inventory_writedown)` | 1 biến | Dự phòng / chất lượng tài sản | — | Xếp hạng dựa trên mức độ dự phòng giảm giá hàng tồn kho, giá trị dự phòng cao hơn (rank cao) có thể liên quan đến rủi ro định giá tài sản trong tương lai. |
| 1 | `zscore(growth(inventory_gross, 2))` | 1 biến | Vốn lưu động | — | Tốc độ tăng trưởng của hàng tồn kho gốc trong 2 quý trước là chỉ báo về sự gia tăng rủi ro về hàng tồn kho. |
| 1 | `zscore(growth(inventory_writedown, 2))` | 1 biến | Dự phòng / chất lượng tài sản | — | Đánh giá tốc độ tăng trưởng của dự phòng giảm giá hàng tồn kho qua hai quý, giúp xác định các cổ phiếu có xu hướng rủi ro tồn kho tăng nhanh. |

### receivables

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(receivables_customers, 1) * safe_div(current_assets, total_assets)` | tổ hợp | Đầu tư / tăng trưởng tài sản, Vốn lưu động | — | Công thức này đo lường mức độ tăng trưởng của khoản phải thu khách hàng so với tổng tài sản trong kỳ, cho thấy hiệu quả quản lý rủi ro tín dụng và khả năng thu  |
| 3 | `safe_div(receivables_customers, revenue)` | tỷ số | Vốn lưu động | — | Tỷ lệ khoản phải thu của khách hàng so với doanh thu phản ánh hiệu quả quản lý tín dụng và khả năng thu tiền từ khách hàng. Tỷ lệ cao có thể chỉ ra vấn đề về th |
| 3 | `safe_div(receivables_customers, total_assets)` | tỷ số | Vốn lưu động | — | Tỷ lệ phải thu ngắn hạn của khách hàng so với tổng tài sản thể hiện mức độ rủi ro thanh khoản và khả năng thu hồi của doanh nghiệp; tỷ lệ cao cho thấy rủi ro ca |
| 3 | `zscore(receivables_customers)` | 1 biến | Vốn lưu động | — | Độ biến động của khoản phải thu khách hàng là chỉ báo trực tiếp về rủi ro tín dụng và khả năng thu hồi của doanh nghiệp. |
| 2 | `delta(provision_doubtful_debt, 1)` | 1 biến | Dự phòng / chất lượng tài sản | — | Sự thay đổi (tăng/giảm) của dự phòng nợ phải thu khó đòi trong kỳ cho thấy sự thay đổi trong nhận thức về rủi ro tín dụng của doanh nghiệp. Dự phòng tăng có thể |
| 2 | `safe_div(provision_doubtful_debt, current_assets)` | tỷ số | Dự phòng / chất lượng tài sản | — | Tỷ lệ dự phòng phải thu khó đòi trên tài sản ngắn hạn là thước đo trực tiếp về chất lượng tài sản, dự phòng lớn cho thấy khả năng thu hồi kém. |
| 2 | `safe_div(provision_doubtful_debt, short_term_receivables)` | tỷ số | Dự phòng / chất lượng tài sản, Vốn lưu động | — | Tỷ lệ dự phòng phải thu khó đòi trên tổng các khoản phải thu ngắn hạn cho thấy mức độ suy giảm chất lượng của các khoản phải thu còn lại. |
| 2 | `safe_div(short_term_receivables, total_assets)` | tỷ số | Vốn lưu động | — | Tỷ lệ khoản phải thu ngắn hạn so với tổng tài sản phản ánh mức độ rủi ro thanh khoản và khả năng thu hồi của doanh nghiệp. Tỷ lệ cao cho thấy áp lực về dòng tiề |
| 1 | `abs(cfo - revenue) * lag(1, 2)` | tổ hợp | Khác | hàm áp lên hằng số | Sự chênh lệch giữa dòng tiền thuần và doanh thu trong kỳ trước có thể chỉ ra vấn đề về chất lượng dòng tiền và khả năng thu hồi nợ. |
| 1 | `abs(provision_doubtful_debt) * safe_div(1, receivables_customers)` | tổ hợp | Dự phòng / chất lượng tài sản, Vốn lưu động | hàm áp lên hằng số; nhân với quy mô công ty | Mức độ dự phòng nợ khó đòi so với tổng số phải thu cho thấy mức độ thận trọng của công ty; dự phòng cao có thể là dấu hiệu của chất lượng tài sản kém. |
| 1 | `rank(receivables_customers)` | 1 biến | Vốn lưu động | — | Xếp hạng trực tiếp dựa trên quy mô tuyệt đối của khoản phải thu ngắn hạn của khách hàng, cho thấy mức độ tập trung rủi ro trong danh mục khách hàng. |
| 1 | `safe_div(cfo, receivables_customers)` | tỷ số | Vốn lưu động | — | Tỷ lệ lưu chuyển tiền thuần so với khoản phải thu cho thấy khả năng thanh khoản để bù đắp các khoản nợ phải thu. |
| 1 | `safe_div(net_income, abs(provision_doubtful_debt))` | tỷ số | Dự phòng / chất lượng tài sản, Sinh lời | — | Tỷ lệ lợi nhuận sau thuế so với dự phòng nợ khó đòi đánh giá mức độ bảo đảm của dự phòng hiện tại. |
| 1 | `safe_div(net_income, receivables_customers)` | tỷ số | Sinh lời, Vốn lưu động | — | Tỷ lệ lợi nhuận sau thuế trên mỗi đồng phải thu ngắn hạn phản ánh hiệu quả chuyển đổi doanh thu thành lợi nhuận từ các khoản phải thu, là chỉ báo chất lượng lợi |
| 1 | `safe_div(provision_doubtful_debt, receivables_customers)` | tỷ số | Dự phòng / chất lượng tài sản, Vốn lưu động | — | Tỷ lệ giữa dự phòng nợ khó đòi và tổng phải thu ngắn hạn cho thấy mức độ bảo đảm rủi ro của công ty; tỷ lệ thấp có thể ám chỉ rủi ro tiềm ẩn cao. |
| 1 | `safe_div(receivables_customers, short_term_receivables)` | tỷ số | Vốn lưu động | — | Dựa trên thuyết minh, số dư phải thu ngắn hạn của khách hàng khó có khả năng thu hồi là chỉ báo trực tiếp về chất lượng nợ; tỷ lệ này đo lường mức độ rủi ro của |
| 1 | `zscore(delta(provision_doubtful_debt, 1))` | 1 biến | Dự phòng / chất lượng tài sản | — | Đo lường sự thay đổi bất thường của dự phòng nợ khó đòi trong kỳ, cho thấy sự biến động trong đánh giá rủi ro tín dụng của công ty. |
| 1 | `zscore(provision_doubtful_debt)` | 1 biến | Dự phòng / chất lượng tài sản | — | Sử dụng Z-score của dự phòng nợ khó đòi để chuẩn hóa mức độ rủi ro tín dụng, giúp đánh giá mức độ bảo đảm rủi ro của công ty. |

### related_party

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `abs(related_party_disclosed) * safe_div(revenue, total_assets)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Công thức này đo lường mức độ phụ thuộc của doanh nghiệp vào các giao dịch với bên liên quan so với quy mô tài sản, cho thấy rủi ro từ các mối quan hệ nội bộ. |
| 2 | `net_income * safe_div(related_party_disclosed, revenue)` | tổ hợp | Sinh lời, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới); nhân với quy mô công ty | Đo lường mức độ lợi nhuận được tạo ra có liên quan đến các bên liên quan, là chỉ báo về chất lượng lợi nhuận. |
| 1 | `abs(related_party_disclosed) * (short_term_receivables + payables_suppliers)` | tổ hợp | Vốn lưu động, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tỷ lệ giao dịch với bên liên quan (related_party_disclosed) nhân với tổng các khoản phải thu và phải trả ngắn hạn cho thấy mức độ phụ thuộc vào các giao dịch bê |
| 1 | `zscore(short_term_receivables) * abs(cfo)` | tổ hợp | Vốn lưu động | nhân với quy mô công ty | Kết hợp rủi ro thanh khoản ngắn hạn (phải thu) với lưu chuyển tiền, cho thấy khả năng thanh toán và rủi ro ngắn hạn. |
| 1 | `abs(related_party_disclosed) * short_term_receivables` | tổ hợp | Vốn lưu động, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới); nhân với quy mô công ty | Mức độ giao dịch với các bên liên quan (related_party_disclosed) kết hợp với các khoản phải thu ngắn hạn cho thấy rủi ro giao dịch và sự phụ thuộc vào các bên l |
| 1 | `zscore(related_party_disclosed) * growth(revenue, 1)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Đánh giá mức độ quan tâm của thị trường đến các giao dịch với bên liên quan so với mức trung bình chung, kết hợp với tốc độ tăng trưởng doanh thu để xem liệu cá |
| 1 | `std(net_income, 2) * log(revenue)` | tổ hợp | Khác | nhân với quy mô công ty | Biến động lợi nhuận so với doanh thu cho thấy sự không ổn định của kết quả kinh doanh trong quý. |
| 1 | `short_term_receivables * safe_div(equity, total_assets)` | tổ hợp | Vốn lưu động | nhân với quy mô công ty | Đo lường mức độ rủi ro thanh khoản ngắn hạn (phải thu) so với cơ cấu vốn chủ sở hữu, là một chỉ báo về áp lực thanh khoản. |
| 1 | `rank(related_party_disclosed)` | 1 biến | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Mức độ giao dịch với bên liên quan là tín hiệu quan trọng về tính minh bạch và rủi ro tiềm ẩn. |
| 1 | `safe_div(short_term_receivables + prepaid_to_suppliers, related_party_disclosed)` | tỷ số | Vốn lưu động, Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tỷ lệ tài sản ngắn hạn (dòng tiền) so với mức độ giao dịch liên quan đo lường khả năng thanh khoản để đối phó với các nghĩa vụ/quyền lợi liên quan. |
| 1 | `safe_div(net_income, equity)` | tỷ số | Sinh lời | — | Tỷ lệ lợi nhuận sau thuế trên vốn chủ sở hữu là thước đo cơ bản về hiệu quả sinh lời, tỷ lệ cao cho thấy cổ phiếu đang định giá thấp so với khả năng sinh lời th |
| 1 | `safe_div(revenue, related_party_disclosed)` | tỷ số | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Tỷ lệ doanh thu so với giao dịch liên quan cho thấy mức độ doanh thu được tạo ra thông qua các đối tác liên quan, ảnh hưởng đến tính bền vững của doanh thu. |
| 1 | `safe_div(revenue, short_term_receivables)` | tỷ số | Vốn lưu động | — | Tỷ lệ doanh thu so với các khoản phải thu ngắn hạn cho thấy khả năng thu hồi tiền từ hoạt động kinh doanh, tỷ lệ cao có thể là dấu hiệu của chất lượng doanh thu |
| 1 | `safe_div(short_term_receivables, revenue)` | tỷ số | Vốn lưu động | — | Tỷ lệ này đo lường khả năng thanh khoản ngắn hạn của doanh nghiệp, một yếu tố quan trọng trong đánh giá rủi ro giao dịch. |

### segment

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(gross_profit, 1) * zscore(gross_profit)` | 1 biến | Khác | nhân với quy mô công ty | Công thức này đo lường sự tăng trưởng lợi nhuận gộp trong quý trước so với mức trung bình của toàn thị trường, cho thấy hiệu suất sinh lời ngắn hạn. Lợi suất ca |
| 3 | `zscore(gross_profit) * lag(gross_profit, 1)` | 1 biến | Khác | lặp một biến hai lần; nhân với quy mô công ty | Công thức này tập trung vào động lượng của lợi nhuận gộp, sử dụng giá trị chuẩn hóa của lợi nhuận hiện tại nhân với giá trị của lợi nhuận trong quý trước. Nó tì |
| 3 | `zscore(gross_profit) * zscore(revenue)` | tổ hợp | Khác | nhân với quy mô công ty | Công thức này đo lường mức độ hiệu quả chuyển đổi doanh thu thành lợi nhuận trong kỳ, được chuẩn hóa theo lát cắt ngang toàn thị trường. Cổ phiếu có điểm cao ch |
| 2 | `growth(revenue, 1) * zscore(revenue)` | 1 biến | Khác | nhân với quy mô công ty | Đo lường tốc độ tăng trưởng doanh thu của bộ phận Xây lắp và xây dựng so với mức trung bình của toàn thị trường. Tốc độ tăng trưởng cao thường là tín hiệu tích  |
| 2 | `zscore(gross_profit) * log(gross_revenue)` | tổ hợp | Khác | nhân với quy mô công ty | Công thức này đo lường mức độ hiệu quả chuyển đổi doanh thu thành lợi nhuận gộp, được chuẩn hóa theo lát cắt ngang thị trường. Lợi suất cao cho thấy khả năng qu |
| 2 | `rank(operating_profit) * mean(operating_profit, 2)` | 1 biến | Khác | nhân với quy mô công ty | Xếp hạng lợi nhuận thuần từ hoạt động kinh doanh so với mức trung bình giúp tìm các quý có hiệu suất vượt trội. |
| 2 | `zscore(growth(revenue, 4))` | 1 biến | Khác | — | Đo lường mức độ tăng trưởng doanh thu theo quý, chuẩn hóa để so sánh hiệu suất tăng trưởng giữa các doanh nghiệp. |
| 1 | `abs(gross_revenue - cogs) * lag(gross_revenue, 1)` | tổ hợp | Khác | nhân với quy mô công ty | Sự chênh lệch giữa doanh thu và giá vốn trong kỳ trước có thể phản ánh biên lợi nhuận cơ bản. |
| 1 | `abs(gross_revenue - cogs) * lag(gross_revenue, 2)` | tổ hợp | Khác | nhân với quy mô công ty | Sự chênh lệch giữa doanh thu và giá vốn trong quá khứ cho thấy biên lợi nhuận cơ bản của doanh nghiệp. |
| 1 | `growth(gross_profit, 1) * lag(gross_profit, 2)` | 1 biến | Khác | nhân với quy mô công ty | Đo lường sự tăng trưởng của lợi nhuận gộp theo thời gian, so sánh mức tăng trưởng gần đây với mức tăng trưởng xa hơn. Điều này giúp xác định các chu kỳ tăng trư |
| 1 | `segment_disclosed * growth(net_income, 1)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Đánh giá mức độ tác động của việc công bố phân khúc (segment_disclosed) lên lợi nhuận sau thuế trong quý tiếp theo, ngụ ý về chất lượng của các hoạt động kinh d |
| 1 | `growth(operating_profit, 1) * lag(operating_profit, 2)` | 1 biến | Khác | nhân với quy mô công ty | Đo lường tốc độ tăng trưởng của lợi nhuận hoạt động (operating_profit) trong các quý gần nhất. Tốc độ tăng trưởng ổn định của lợi nhuận hoạt động thường là tín  |
| 1 | `growth(revenue, 1) * rank(segment_disclosed)` | tổ hợp | Cờ thuyết minh | dùng cờ thuyết minh (chỉ là số lần nhắc tới) | Công thức này tập trung vào tốc độ tăng trưởng doanh thu của các bộ phận khác nhau trong quý trước và so sánh nó với mức độ phân tách hoạt động của doanh nghiệp |
| 1 | `safe_div(gross_revenue, cogs) * lag(gross_revenue, 1)` | tổ hợp | Khác | nhân với quy mô công ty | Tỷ lệ biên lợi nhuận gộp trong kỳ hiện tại so với kỳ trước giúp đánh giá hiệu quả hoạt động cốt lõi. |

### tax

| lặp | công thức | dạng | họ | lỗi ngữ nghĩa | lý do (một lần sinh) |
|---|---|---|---|---|---|
| 3 | `growth(net_income, 1)` | 1 biến | Khác | — | Đánh giá tốc độ tăng trưởng lợi nhuận sau thuế trong quý gần nhất, là chỉ báo trực tiếp về chất lượng lợi nhuận và khả năng sinh lời của doanh nghiệp. |
| 3 | `safe_div(current_tax_expense, pretax_profit)` | tỷ số | Sinh lời | — | Tỷ lệ chi phí thuế so với lợi nhuận trước thuế là thước đo trực tiếp về mức độ chịu thuế của lợi nhuận, ảnh hưởng đến lợi nhuận ròng. |
| 2 | `safe_div(operating_profit, total_assets)` | tỷ số | Sinh lời | — | Tỷ lệ lợi nhuận hoạt động trên tổng tài sản cho thấy hiệu quả sử dụng tài sản tạo ra lợi nhuận, một chỉ báo về chất lượng lợi nhuận. |
| 1 | `log(current_tax_expense)` | 1 biến | Khác | — | Logarit của chi phí thuế TNDN thể hiện mức độ biến động hoặc mức độ 'đáng kể' của chi phí thuế trong kỳ, có thể là một đặc trưng của chất lượng lợi nhuận. |
| 1 | `zscore(current_tax_expense)` | 1 biến | Khác | — | Sử dụng Z-score của chi phí thuế TNDN hiện hành để xếp hạng, giúp xác định các quý có mức chi phí thuế bất thường so với phân phối của các quý khác. |

## Công thức KHÔNG hợp lệ, theo lỗi

### bad_arity — 116 công thức

- `zscore(inventory_writedown, inventory_gross, current_assets)` — F1-001 · bad_arity:zscore
- `growth(inventory, revenue, 1)` — F1-001 · bad_arity:growth
- `zscore(abs(inventory_writedown), cogs, market_cap)` — F1-001 · bad_arity:zscore
- `zscore(inventory_writedown, 4)` — F4-001 · bad_arity:zscore
- `zscore(inventory_writedown) * zscore(inventory_writedown, 1)` — F1-002 · bad_arity:zscore
- `growth(inventory - inventory_gross, revenue, 1)` — F1-002 · bad_arity:growth
- `zscore(inventory_writedown, 4)` — F4-002 · bad_arity:zscore|duplicate
- `growth(net_income, 4) * safe_div(1 + std(receivables_customers, 4))` — F4-003 · bad_arity:safe_div
- `zscore(interest_expense, 4) * safe_div(long_term_debt, total_liabilities)` — F2-006 · bad_arity:zscore
- `zscore(interest_expense, 4)` — F4-004 · bad_arity:zscore
- `growth(safe_div(short_term_debt, total_assets)) * growth(safe_div(short_term_debt, total_assets), 2)` — F1-006 · bad_arity:growth
- `growth(interest_expense, revenue, 1)` — F3-005 · bad_arity:growth
- … và 104 công thức khác (xem `bench/results/formulas.csv`)

### syntax_error — 102 công thức

- `delta(current_assets, 4) safe_div(inventory, current_assets)` — F4-001 · syntax_error
- `abs(current_assets * 0.01) safe_div(inventory_gross, current_assets) lag(abs(current_assets * 0.01), 1)` — F2-002 · syntax_error
- `growth(inventory) safe_div(revenue, inventory)` — F1-003 · syntax_error
- `lag(gross_profit) safe_div(inventory_gross, gross_profit)` — F1-003 · syntax_error
- `delta(current_assets, 4) safe_div(inventory, current_assets)` — F4-002 · syntax_error
- `abs(provision_doubtful_debt) safe_div(receivables_customers, provision_doubtful_debt)` — F2-004 · syntax_error
- `zscore(receivables_customers, 1) lag(receivables_customers, 1)` — F2-004 · syntax_error
- `zscore(total_liabilities, k=1)` — F2-007 · syntax_error:keyword
- `growth(interest_expense, k=1)` — F2-007 · syntax_error:keyword
- `zscore(short_term_debt safe_div(long_term_debt, total_liabilities))` — F2-008 · syntax_error
- `rank(growth(short_term_debt safe_div(total_assets, short_term_debt)))` — F2-008 · syntax_error
- `abs(revenue lag(1)) safe_div(capex, long_term_assets lag(1))` — F1-007 · syntax_error
- … và 90 công thức khác (xem `bench/results/formulas.csv`)

### raw_division — 51 công thức

- `abs(inventory_writedown / total_assets)` — F3-001 · raw_division
- `abs(inventory_writedown / (inventory_gross + 1e-6)) * lag(inventory_writedown / inventory_gross, 1)` — F1-002 · raw_division
- `abs(inventory_writedown / inventory_gross)` — F3-002 · raw_division
- `zscore(receivables_customers) * (1.0 / revenue)` — F1-004 · raw_division
- `lag(cfo, 1) * (1.0 / receivables_customers)` — F1-004 · raw_division
- `abs(cfo / (receivables_customers + 1))` — F4-003 · raw_division
- `growth(short_term_debt / total_assets, 1)` — F1-005 · raw_division
- `zscore(capex / fixed_assets)` — F2-010 · raw_division
- `zscore(short_term_receivables / revenue)` — F2-013 · raw_division
- `abs(revenue / (short_term_receivables + payables_suppliers)) * related_party_disclosed` — F2-017 · raw_division
- `net_income / total_assets` — F2-017 · raw_division
- `abs(short_term_receivables / payables_suppliers)` — F2-017 · raw_division
- … và 39 công thức khác (xem `bench/results/formulas.csv`)

### duplicate — 45 công thức

- `zscore(inventory_writedown)` — F2-002 · duplicate
- `zscore(inventory_writedown)` — F2-003 · duplicate
- `zscore(lag(inventory_writedown, 1))` — F2-003 · duplicate
- `safe_div(revenue, inventory_gross) * lag(1, 2)` — F4-002 · duplicate
- `safe_div(receivables_customers, total_assets)` — F3-004 · duplicate
- `safe_div(provision_doubtful_debt, short_term_receivables)` — F3-004 · duplicate
- `delta(provision_doubtful_debt, 1)` — F3-004 · duplicate
- `zscore(lag(interest_expense, 1))` — F1-006 · duplicate
- `zscore(lag(interest_expense, 1))` — F2-008 · duplicate
- `safe_div(depreciation, fixed_assets)` — F3-008 · duplicate
- `zscore(customer_advances)` — F2-014 · duplicate
- `safe_div(customer_advances, revenue)` — F3-011 · duplicate
- … và 33 công thức khác (xem `bench/results/formulas.csv`)

### unknown_func — 8 công thức

- `zscore(depreciation(revenue, 1))` — F4-006 · unknown_func:depreciation
- `ratio(pretax_profit, total_assets, lag(1))` — F2-025 · unknown_func:ratio|bad_arity:lag
- `zscore(ratio(cfo, total_assets))` — F2-025 · unknown_func:ratio
- `growth(ratio(market_cap, pretax_profit), 1)` — F2-025 · unknown_func:ratio
- `rank(safe_div(long_term_debt(k), total_assets(k)))` — F2-008 · unknown_func:long_term_debt|unknown_func:total_assets|unknown_var:k
- `zscore(interest_expense(lag(1)))` — F2-008 · unknown_func:interest_expense|bad_arity:lag|constant_only
- `ratio(pretax_profit, total_assets, lag(1))` — F2-025 · unknown_func:ratio|bad_arity:lag
- `zscore(ratio(cfo, total_assets))` — F2-025 · unknown_func:ratio

### bad_lag — 4 công thức

- `delta(provision_doubtful_debt, current_assets) * (1.0 / (current_assets + provision_doubtful_debt))` — F1-004 · bad_lag:delta|raw_division
- `growth(inventory - inventory_gross, revenue) * log(revenue)` — F1-002 · bad_lag:growth
- `growth(short_term_debt, total_assets)` — F1-005 · bad_lag:growth
- `rank(mean(financial_expense, 3))` — F1-006 · bad_lag:mean

### constant_only — 1 công thức

- `1` — F3-001 · constant_only

### copied_fewshot — 1 công thức

- `safe_div(net_income, market_cap)` — F3-014 · copied_fewshot

