# Bộ thử P0 - xem nhanh

Sinh tự động bởi `src/eval/build_prompts.py`. **Không sửa tay** - sửa script rồi chạy lại.

Tổng **76** prompt: F1 = 17, F2 = 25, F3 = 19, F4 = 15. Mỗi prompt yêu cầu 3 công thức. System prompt chung: `bench/system_prompt.txt`.

Đoạn thuyết minh (F2/F3): 185-719 từ, trung vị 440.

## Bảng cặp

| pair_id | mã | năm | chủ đề | mục thuyết minh | từ | F1 | F2 | F3 | F4 |
|---|---|---|---|---|---|---|---|---|---|
| P01-ANV17-inventory | ANV | 2017 | inventory | mục 7. Hàng tồn kho; ghép thêm mục chính sách kế toán | 430 | F1-001 | F2-001 | F3-001 | F4-001 |
| P02-HPG24-inventory | HPG | 2024 | inventory | mục 10. Hàng tồn kho | 653 | F1-002 | F2-002 | F3-002 |  |
| P03-PNJ24-inventory | PNJ | 2024 | inventory | mục 9. HÀNG TÔN KHO; ghép thêm mục chính sách kế toán | 438 | F1-003 | F2-003 |  | F4-002 |
| P04-GAS24-receivables | GAS | 2024 | receivables | mục 5. PHÀI THU NGẢN HẠN CỦA KHÁCH HÀNG | 407 | F1-004 | F2-004 | F3-003 | F4-003 |
| P05-HUT24-receivables | HUT | 2024 | receivables | mục 7. Nợ xấu | 272 |  | F2-005 | F3-004 |  |
| P06-TNG24-debt | TNG | 2024 | debt | mục 22. VAY DÀI HẠN; cắt bớt theo trần 800 từ / 3.500 ký tự | 695 | F1-005 | F2-006 |  | F4-004 |
| P07-NLG17-debt | NLG | 2017 | debt | mục 22. VAY VÀ NỘ | 525 | F1-006 | F2-007 | F3-005 | F4-005 |
| P08-POW17-debt | POW | 2017 | debt | mục 21. VAY VÀ NỘ THUÊ TÀI CHÍNH DÀI HẠN; cắt bớt theo trần 800 từ / 3.500 ký tự | 626 |  | F2-008 | F3-006 |  |
| P09-HAH24-fixed_assets | HAH | 2024 | fixed_assets | mục 12. Tài sản cố định hữu hình; ghép thêm mục chính sách kế toán | 636 | F1-007 | F2-009 | F3-007 | F4-006 |
| P10-TNG17-fixed_assets | TNG | 2017 | fixed_assets | mục 10. TĂNG, GIÀM TÀI SẢN CỔ ĐỊNH HỮU HÌNH | 415 |  | F2-010 | F3-008 |  |
| P11-HPG17-cip | HPG | 2017 | cip | mục 15. Chi phí xây dựng cơ bản dở dang; ghép thêm mục chính sách kế toán | 348 |  | F2-011 |  | F4-007 |
| P12-VGC24-cip | VGC | 2024 | cip | mục 16. CHI PHÍ XÂY DỰNG CƠ BẢN DỞ DANG; cắt bớt theo trần 800 từ / 3.500 ký tự | 710 | F1-008 | F2-012 | F3-009 | F4-008 |
| P13-NLG24-customer_advances | NLG | 2024 | customer_advances | mục 26. DOANH THU CHU'A THỰC HIỆN | 185 |  | F2-013 | F3-010 |  |
| P14-IDC24-customer_advances | IDC | 2024 | customer_advances | mục 26. DOANH THU CHU'A THỰC HIỆN | 231 | F1-009 | F2-014 | F3-011 | F4-009 |
| P15-CTD17-associates | CTD | 2017 | associates | mục 15. ĐẦU TƯ VÀO CÁC CÔNG TY LIÊN KẾT | 454 | F1-010 | F2-015 | F3-012 | F4-010 |
| P16-PVT17-associates | PVT | 2017 | associates | mục 12. ĐẦU TƯ VÀO CÔNG TY LIÊN DOANH, LIÊN KẾT | 535 | F1-011 | F2-016 | F3-013 |  |
| P17-NTP17-related_party | NTP | 2017 | related_party | mục 30. NGHIỆP VỤ VÀ SỐ DỰ VỚI CÁC BÊN LIÊN QUAN | 440 | F1-012 | F2-017 | F3-014 |  |
| P18-MWG24-related_party | MWG | 2024 | related_party | mục 33. NGHIỆP VỤ VỚI CÁC BÊN LIÊN QUAN; ghép thêm mục chính sách kế toán | 377 |  | F2-018 |  | F4-011 |
| P19-GAS17-commitments | GAS | 2017 | commitments | mục 39. CÁC KHOÀN CAM KẾT | 478 | F1-013 | F2-019 | F3-015 | F4-012 |
| P20-VNM24-segment | VNM | 2024 | segment | mục 2. Báo cáo bộ phận; ghép thêm mục chính sách kế toán | 351 | F1-014 | F2-020 | F3-016 |  |
| P21-PC124-segment | PC1 | 2024 | segment | mục 5. Báo cáo bộ phận; cắt bớt theo trần 800 từ / 3.500 ký tự | 560 |  | F2-021 |  | F4-013 |
| P22-PNJ17-tax | PNJ | 2017 | tax | mục 33. CHI PHÍ THUÊ THU NHẬP DOANH NGHIỆP HIỆN HÀNH | 223 |  | F2-022 | F3-017 |  |
| P23-VCB24-bank_loans | VCB | 2024 | bank_loans | mục 9. Cho vay khách hàng | 345 | F1-015 | F2-023 | F3-018 | F4-014 |
| P24-SHB17-bank_loans | SHB | 2017 | bank_loans | mục 11. CHO VAY KHÁCH HÀNG; cắt bớt theo trần 800 từ / 3.500 ký tự | 719 | F1-016 | F2-024 | F3-019 |  |
| P25-BVS24-fin_assets | BVS | 2024 | fin_assets | mục 7. CÁC LOẠI TÀI SẢN TÀI CHÍNH; cắt bớt theo trần 800 từ / 3.500 ký tự | 616 | F1-017 | F2-025 |  | F4-015 |

## Toàn văn

### F1-001 · P01-ANV17-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `-`

````text
Doanh nghiệp: ANV - nông nghiệp - thuỷ sản (cá tra), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-001 · P01-ANV17-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `data/sample/raw/ocr_results/ANV/2017/ANV_Baocaotaichinh_2017_Kiemtoan_Hopnhat/ANV_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1126-L1134;data/sample/raw/ocr_results/ANV/2017/ANV_Baocaotaichinh_2017_Kiemtoan_Hopnhat/ANV_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L689-L727`

````text
Doanh nghiệp: ANV - nông nghiệp - thuỷ sản (cá tra), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Trích thuyết minh báo cáo tài chính năm 2017 của ANV (mục 7. Hàng tồn kho):
<<<
7. Hàng tồn kho
Giá gốc | Dự phòng | Giá gốc | Dự phòng
Hàng mua đang di trên đường | 638.847.142 | - | 85.426.211.696 | -
Nguyên liệu, vật liệu | 104.809.626.291 | - | 107.078.052.436 | -
Công cụ, dụng cụ | 8.195.859.517 | - | 8.962.734.636 | -
Chi phí sản xuất, kinh doanh dở dang | 448.918.854.648 | - | 333.825.709.763 | -
Thành phẩm | 287.763.413.487 | (13.310.329.735) | 621.068.098.648 | (268.405.509)
Hàng gửi đi bán | 36.802.630.810 | - | 38.997.321.974 | -
Cộng | 887.129.231.895 | (13.310.329.735) | 1.195.358.129.153 | (268.405.509)
Hàng tồn kho có trị giá 110.526.335.129 VND (số đầu năm là 315.230.545.435 VND) đã được thế chấp để đảm bảo cho các khoản vay của Ngân hàng TMCP Đầu tư và Phát triển Việt Nam.
Tình hình biến động dự phòng giảm giá hàng tồn kho như sau:
 | Năm nay | Năm trước
Số đầu năm | 268.405.509 | 1.660.540.609
Trích lập/(Hoàn nhập) dự phòng | 13.041.924.226 | (1.392.135.100)
Số cuối năm | 13.310.329.735 | 268.405.509

7. Hàng tôn kho
Hàng tồn kho được ghi nhận theo giá thấp hơn giữa giá gốc và giá trị thuần có thể thực hiện được.
Giá gốc hàng tồn kho được xác định như sau:
- Nguyên vật liệu, hàng hóa: bao gồm chi phí mua và các chi phí liên quan trực tiếp khác phát sinh để có được hàng tồn kho ở địa điểm và trạng thái hiện tại.
- Chi phí sản xuất kinh doanh dở dang: chi bao gồm chi phí nguyên vật liệu chính.
- Thành phẩm: bao gồm chi phí nguyên vật liệu, nhân công trực tiếp và chi phí sản xuất chung có liên quan trực tiếp được phân bổ dựa trên mức độ hoạt động bình thường.
Giá xuất kho được tính theo phương pháp bình quân gia quyền và được hạch toán theo phương pháp kê khai thường xuyên.
Giá trị thuần có thể thực hiện được là giá bán ước tính của hàng tồn kho trong kỳ sản xuất, kinh doanh bình thường trừ chi phí ước tính để hoàn thành và chi phí ước tính cần thiết cho việc tiêu thụ chúng.
Dự phòng giảm giá hàng tồn kho được lập cho từng mặt hàng tồn kho có giá gốc lớn hơn giá trị thuần có thể thực hiện được. Tăng, giảm số dư dự phòng giảm giá hàng tồn kho cần phải trích lập tại ngày kết thúc năm tài chính được ghi nhận vào giá vốn hàng bán.
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-001 · P01-ANV17-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `data/sample/raw/ocr_results/ANV/2017/ANV_Baocaotaichinh_2017_Kiemtoan_Hopnhat/ANV_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1126-L1134;data/sample/raw/ocr_results/ANV/2017/ANV_Baocaotaichinh_2017_Kiemtoan_Hopnhat/ANV_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L689-L727`

````text
Doanh nghiệp: ANV - nông nghiệp - thuỷ sản (cá tra), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Trích thuyết minh báo cáo tài chính năm 2017 của ANV (mục 7. Hàng tồn kho):
<<<
7. Hàng tồn kho
Giá gốc | Dự phòng | Giá gốc | Dự phòng
Hàng mua đang di trên đường | 638.847.142 | - | 85.426.211.696 | -
Nguyên liệu, vật liệu | 104.809.626.291 | - | 107.078.052.436 | -
Công cụ, dụng cụ | 8.195.859.517 | - | 8.962.734.636 | -
Chi phí sản xuất, kinh doanh dở dang | 448.918.854.648 | - | 333.825.709.763 | -
Thành phẩm | 287.763.413.487 | (13.310.329.735) | 621.068.098.648 | (268.405.509)
Hàng gửi đi bán | 36.802.630.810 | - | 38.997.321.974 | -
Cộng | 887.129.231.895 | (13.310.329.735) | 1.195.358.129.153 | (268.405.509)
Hàng tồn kho có trị giá 110.526.335.129 VND (số đầu năm là 315.230.545.435 VND) đã được thế chấp để đảm bảo cho các khoản vay của Ngân hàng TMCP Đầu tư và Phát triển Việt Nam.
Tình hình biến động dự phòng giảm giá hàng tồn kho như sau:
 | Năm nay | Năm trước
Số đầu năm | 268.405.509 | 1.660.540.609
Trích lập/(Hoàn nhập) dự phòng | 13.041.924.226 | (1.392.135.100)
Số cuối năm | 13.310.329.735 | 268.405.509

7. Hàng tôn kho
Hàng tồn kho được ghi nhận theo giá thấp hơn giữa giá gốc và giá trị thuần có thể thực hiện được.
Giá gốc hàng tồn kho được xác định như sau:
- Nguyên vật liệu, hàng hóa: bao gồm chi phí mua và các chi phí liên quan trực tiếp khác phát sinh để có được hàng tồn kho ở địa điểm và trạng thái hiện tại.
- Chi phí sản xuất kinh doanh dở dang: chi bao gồm chi phí nguyên vật liệu chính.
- Thành phẩm: bao gồm chi phí nguyên vật liệu, nhân công trực tiếp và chi phí sản xuất chung có liên quan trực tiếp được phân bổ dựa trên mức độ hoạt động bình thường.
Giá xuất kho được tính theo phương pháp bình quân gia quyền và được hạch toán theo phương pháp kê khai thường xuyên.
Giá trị thuần có thể thực hiện được là giá bán ước tính của hàng tồn kho trong kỳ sản xuất, kinh doanh bình thường trừ chi phí ước tính để hoàn thành và chi phí ước tính cần thiết cho việc tiêu thụ chúng.
Dự phòng giảm giá hàng tồn kho được lập cho từng mặt hàng tồn kho có giá gốc lớn hơn giá trị thuần có thể thực hiện được. Tăng, giảm số dư dự phòng giảm giá hàng tồn kho cần phải trích lập tại ngày kết thúc năm tài chính được ghi nhận vào giá vốn hàng bán.
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "inventory_change_to_assets", "formula": "safe_div(delta(inventory, 4), mean(total_assets, 4))", "rationale": "Tồn kho tăng nhanh hơn quy mô tài sản báo hiệu hàng bán chậm, dự báo lợi suất thấp hơn (Thomas & Zhang 2002).", "source": {"type": "line_item", "ref": "inventory, total_assets"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-001 · P01-ANV17-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `-`

````text
Doanh nghiệp: ANV - nông nghiệp - thuỷ sản (cá tra), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-002 · P02-HPG24-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `-`

````text
Doanh nghiệp: HPG - sản xuất công nghiệp (thép), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-002 · P02-HPG24-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `data/sample/raw/ocr_results/HPG/2024/bao-cao-tai-chinh-hop-nhat-nam-2024-da-kiem-toan-1/bao-cao-tai-chinh-hop-nhat-nam-2024-da-kiem-toan-1_extracted.txt#L1063-L1094`

````text
Doanh nghiệp: HPG - sản xuất công nghiệp (thép), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Trích thuyết minh báo cáo tài chính năm 2024 của HPG (mục 10. Hàng tồn kho):
<<<
10. Hàng tồn kho
10.1 Ngắn hạn
Giá gốc VND | Dự phòng VND | Giá gốc VND | Dự phòng VND
Hàng mua đang đi trên đường | 5.559.003.181.956 | - | 4.990.397.929.773 | -
Nguyên vật liệu | 20.324.528.389.776 | (17.265.822.207) | 15.440.615.820.401 | (8.114.279.314)
Công cụ và dụng cụ | 3.326.224.899.798 | (3.462.076.448) | 2.207.960.043.082 | (3.897.886.241)
Chi phí sản xuất kinh doanh dở dang (i) | 4.048.570.091.614 | (9.717.188.881) | 3.356.842.753.839 | (12.264.604.904)
Thành phẩm | 12.155.686.194.056 | (62.049.506.084) | 7.845.693.017.557 | (97.266.005.297)
Hàng hóa | 673.704.904.662 | (8.575.298.721) | 570.688.881.053 | (2.337.662.933)
Hàng gửi đi bán | 104.574.419.951 | - | 216.169.399.245 | -
 | 46.192.292.081.813 | (101.069.892.341) | 34.628.367.844.950 | (123.880.438.689)
(i) Trong số dư chi phí sản xuất kinh doanh dở dang tại ngày 31 tháng 12 năm 2024 có 1.695 tỷ VND (1/1/2024: 1.326 tỷ VND) chi phí liên quan Dự án đầu tư xây dựng hạ tầng kỹ thuật Phân khu A – Khu đô thị Bắc Quốc lộ 5 thuộc Khu đô thị Phó Nói tinh Hưng Yên (“Dự án Bắc QL5”) do Công ty Cổ phần Xây dựng và Phát triển Đô thị Hòa Phát – công ty con của Tập đoàn thực hiện. Trong đó có 1.007 tỷ VND là chi phí bồi thường giải phóng mặt bằng đã được cơ quan Nhà nước có thẩm quyền xác nhận và 688 tỷ VND là chi phí đầu tư cơ sở hạ tầng kỹ thuật của Dự án (1/1/2024: lần lượt là 707 tỷ VND và 619 tỷ VND). Ngoài ra, Tập đoàn cũng đang ghi nhận 4,5 tỷ VND trên tài khoản phải thu ngắn hạn khác chi phí bồi thường giải phóng mặt bằng mà Tập đoàn đã thực hiện nhưng đang chờ xác nhận của cơ quan Nhà nước có thẩm quyền liên quan đến Dự án này (Thuyết minh 9.1).
Trước đây, Dự án Bắc QL5 đã được Ủy ban Nhân Dân (“UBND”) tỉnh Hưng Yên giao cho Công ty Cổ phần Xây dựng và Phát triển Đô thị Hòa Phát tiếp tục làm chủ đầu tư để thực hiện theo cơ chế giao đất có thu tiền sử dụng đất tại Văn bản số 1488/UBND-KT1 ngày 14 tháng 7 năm 2016 (“Văn bản số 1488”).
Ngày 28 tháng 12 năm 2023, Thanh tra Chính phủ đã ban hành Kết luận thanh tra số 3136/KL-TTCP về công tác quản lý, sử dụng đất theo tỉnh thần Nghị quyết số 73/NQ-CP và 116/NQ-CP của Chính phủ; công tác quy hoạch và thực hiện quy hoạch xây dựng của UBND tỉnh Hưng Yên (giai đoạn 2011 – 6/2022). Theo đó, Thanh tra Chính phủ kiến nghị UBND tỉnh Hưng Yên thu hồi Văn bản số 1488 về việc tiếp tục giao thực hiện Dự án Bắc QL5 và rà soát hồ sơ pháp lý để dấu thầu lựa chọn lại chủ đầu tư dự án theo quy định của pháp luật. Tại ngày phát hành báo cáo, Tập đoàn chưa nhận được công văn chính thức của UBND tỉnh Hưng Yên về vấn đề nêu trên.
Trong hàng tồn kho tại ngày 31 tháng 12 năm 2024 có 671 tỷ VND hàng tồn kho (1/1/2024: 20.212 tỷ VND) được ghi nhận theo giá trị thuần có thể thực hiện được.
Tại ngày 31 tháng 12 năm 2024, hàng tồn kho có giá trị ghi sổ là 29.769 tỷ VND (1/1/2024: 24.178 tỷ VND) được thế chấp tại các ngân hàng để đảm bảo cho các khoản vay của Tập đoàn.
10.2 Dài hạn
Giá gốc VND | Dự phòng VND | Giá gốc VND | Dự phòng VND
Chi phí sản xuất kinh doanh dở dang | 94.859.885.024 | - | 46.356.652.469 | -
Thiết bị, vật tư, phụ tùng thay thế dài hạn | 429.422.385.383 | - | - | -
 | 524.282.270.407 | - | 46.356.652.469 | -
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-002 · P02-HPG24-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `data/sample/raw/ocr_results/HPG/2024/bao-cao-tai-chinh-hop-nhat-nam-2024-da-kiem-toan-1/bao-cao-tai-chinh-hop-nhat-nam-2024-da-kiem-toan-1_extracted.txt#L1063-L1094`

````text
Doanh nghiệp: HPG - sản xuất công nghiệp (thép), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Trích thuyết minh báo cáo tài chính năm 2024 của HPG (mục 10. Hàng tồn kho):
<<<
10. Hàng tồn kho
10.1 Ngắn hạn
Giá gốc VND | Dự phòng VND | Giá gốc VND | Dự phòng VND
Hàng mua đang đi trên đường | 5.559.003.181.956 | - | 4.990.397.929.773 | -
Nguyên vật liệu | 20.324.528.389.776 | (17.265.822.207) | 15.440.615.820.401 | (8.114.279.314)
Công cụ và dụng cụ | 3.326.224.899.798 | (3.462.076.448) | 2.207.960.043.082 | (3.897.886.241)
Chi phí sản xuất kinh doanh dở dang (i) | 4.048.570.091.614 | (9.717.188.881) | 3.356.842.753.839 | (12.264.604.904)
Thành phẩm | 12.155.686.194.056 | (62.049.506.084) | 7.845.693.017.557 | (97.266.005.297)
Hàng hóa | 673.704.904.662 | (8.575.298.721) | 570.688.881.053 | (2.337.662.933)
Hàng gửi đi bán | 104.574.419.951 | - | 216.169.399.245 | -
 | 46.192.292.081.813 | (101.069.892.341) | 34.628.367.844.950 | (123.880.438.689)
(i) Trong số dư chi phí sản xuất kinh doanh dở dang tại ngày 31 tháng 12 năm 2024 có 1.695 tỷ VND (1/1/2024: 1.326 tỷ VND) chi phí liên quan Dự án đầu tư xây dựng hạ tầng kỹ thuật Phân khu A – Khu đô thị Bắc Quốc lộ 5 thuộc Khu đô thị Phó Nói tinh Hưng Yên (“Dự án Bắc QL5”) do Công ty Cổ phần Xây dựng và Phát triển Đô thị Hòa Phát – công ty con của Tập đoàn thực hiện. Trong đó có 1.007 tỷ VND là chi phí bồi thường giải phóng mặt bằng đã được cơ quan Nhà nước có thẩm quyền xác nhận và 688 tỷ VND là chi phí đầu tư cơ sở hạ tầng kỹ thuật của Dự án (1/1/2024: lần lượt là 707 tỷ VND và 619 tỷ VND). Ngoài ra, Tập đoàn cũng đang ghi nhận 4,5 tỷ VND trên tài khoản phải thu ngắn hạn khác chi phí bồi thường giải phóng mặt bằng mà Tập đoàn đã thực hiện nhưng đang chờ xác nhận của cơ quan Nhà nước có thẩm quyền liên quan đến Dự án này (Thuyết minh 9.1).
Trước đây, Dự án Bắc QL5 đã được Ủy ban Nhân Dân (“UBND”) tỉnh Hưng Yên giao cho Công ty Cổ phần Xây dựng và Phát triển Đô thị Hòa Phát tiếp tục làm chủ đầu tư để thực hiện theo cơ chế giao đất có thu tiền sử dụng đất tại Văn bản số 1488/UBND-KT1 ngày 14 tháng 7 năm 2016 (“Văn bản số 1488”).
Ngày 28 tháng 12 năm 2023, Thanh tra Chính phủ đã ban hành Kết luận thanh tra số 3136/KL-TTCP về công tác quản lý, sử dụng đất theo tỉnh thần Nghị quyết số 73/NQ-CP và 116/NQ-CP của Chính phủ; công tác quy hoạch và thực hiện quy hoạch xây dựng của UBND tỉnh Hưng Yên (giai đoạn 2011 – 6/2022). Theo đó, Thanh tra Chính phủ kiến nghị UBND tỉnh Hưng Yên thu hồi Văn bản số 1488 về việc tiếp tục giao thực hiện Dự án Bắc QL5 và rà soát hồ sơ pháp lý để dấu thầu lựa chọn lại chủ đầu tư dự án theo quy định của pháp luật. Tại ngày phát hành báo cáo, Tập đoàn chưa nhận được công văn chính thức của UBND tỉnh Hưng Yên về vấn đề nêu trên.
Trong hàng tồn kho tại ngày 31 tháng 12 năm 2024 có 671 tỷ VND hàng tồn kho (1/1/2024: 20.212 tỷ VND) được ghi nhận theo giá trị thuần có thể thực hiện được.
Tại ngày 31 tháng 12 năm 2024, hàng tồn kho có giá trị ghi sổ là 29.769 tỷ VND (1/1/2024: 24.178 tỷ VND) được thế chấp tại các ngân hàng để đảm bảo cho các khoản vay của Tập đoàn.
10.2 Dài hạn
Giá gốc VND | Dự phòng VND | Giá gốc VND | Dự phòng VND
Chi phí sản xuất kinh doanh dở dang | 94.859.885.024 | - | 46.356.652.469 | -
Thiết bị, vật tư, phụ tùng thay thế dài hạn | 429.422.385.383 | - | - | -
 | 524.282.270.407 | - | 46.356.652.469 | -
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "inventory_change_to_assets", "formula": "safe_div(delta(inventory, 4), mean(total_assets, 4))", "rationale": "Tồn kho tăng nhanh hơn quy mô tài sản báo hiệu hàng bán chậm, dự báo lợi suất thấp hơn (Thomas & Zhang 2002).", "source": {"type": "line_item", "ref": "inventory, total_assets"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F1-003 · P03-PNJ24-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `-`

````text
Doanh nghiệp: PNJ - bán lẻ - tiêu dùng (bán lẻ trang sức), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-003 · P03-PNJ24-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `data/sample/raw/ocr_results/PNJ/2024/PNJ_Baocaotaichinh_2024_Kiemtoan_Hopnhat/PNJ_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L875-L883;data/sample/raw/ocr_results/PNJ/2024/PNJ_Baocaotaichinh_2024_Kiemtoan_Hopnhat/PNJ_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L446-L452`

````text
Doanh nghiệp: PNJ - bán lẻ - tiêu dùng (bán lẻ trang sức), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Trích thuyết minh báo cáo tài chính năm 2024 của PNJ (mục 9. HÀNG TÔN KHO):
<<<
9 HÀNG TÔN KHO
Giá gốc VND | Dự phòng VND | Giá gốc VND | Dự phòng VND
Nguyên vật liệu | 634.610.808.014 | - | 1.336.881.052.967 | -
Công cụ, dụng cụ | 45.696.244.733 | - | 39.140.960.355 | -
Chỉ phí SXKDđở dang | 249.862.078.812 | - | 182.116.093.085 | -
Thành phẩm | 8.466.765.298.103 | - | 7.079.496.646.224 | -
Hàng hóa | 3.677.652.498.252 | (59.416.450.603) | 2.307.114.254.166 | (3.811.047.508)
 | 13.074.586.927.914 | (59.416.450.603) | 10.944.749.006.797 | (3.811.047.508)
Tại ngày 31 tháng 12 năm 2024, hàng tồn kho luận chuyển của Tập đoàn (không cần xác định số lượng và chứng loại, tuy nhiên phải đảm bảo về giá trị không thấp hơn giá trị quy định trong hợp đồng vay) với tổng giá trị là 2.930.000.000.000 Đồng (tại ngày 31 tháng 12 năm 2023: 3.990.000.000.000 Đồng) đã được dùng để làm tài sản thể chấp cho các khoản vay ngắn hạn ngân hàng thương mại (Thuyết minh 19).
Biến động về dự phòng giảm giá hàng tồn kho trong năm tài chính như sau:
 | 2024VND | 2023VND
Số dư đầu năm | 3.811.047.508 | 2.010.094.632
Tăng dự phòng (Thuyết minh 29) | 55.605.403.095 | 1.800.952.876
Số dư cuối năm | 59.416.450.603 | 3.811.047.508

2.8 Hàng tồn kho
Hàng tồn kho được thể hiện theo giá thấp hơn giữa giá gốc và giá trị thuần có thể thực hiện được. Giá gốc được xác định trên cơ sở bình quân gia quyền và bao gồm tất cả các chi phí mua, chi phí chế biến và các chi phí liên quan trực tiếp khác phát sinh để có được hàng tồn kho ở địa điểm và trạng thái hiện tại. Trong trường hợp các sản phẩm được sản xuất, giá gốc bao gồm tất cả các chi phí trực tiếp và chi phí sản xuất chung dựa trên mức độ hoạt động bình thường. Giá trị thuần có thể thực hiện được là giá bán ước tính của hàng tồn kho trong năm tài chính kinh doanh bình thường trừ chi phí ước tính để hoàn thành sản phẩm và chi phí ước tính cần thiết cho việc tiêu thụ.
Tập đoàn áp dụng phương pháp kê khai thường xuyên để hạch toán hàng tồn kho.
Dự phòng được lập cho hàng tồn kho bị lỗi thời, chậm lưu chuyển và bị hồng. Chênh lệch giữa khoản dự phòng phải lập ở cuối năm tài chính này và khoản dự phòng đã lập ở cuối năm tài chính trước được ghi nhận tăng hoặc giảm giá vốn hàng bán trong năm tài chính.
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-002 · P03-PNJ24-inventory

allowed_vars (15): `current_assets, inventory, inventory_gross, inventory_writedown, total_assets, current_liabilities, payables_suppliers, customer_advances, equity, revenue, cogs, gross_profit, net_income, cfo, market_cap`  
must_reference: `inventory_writedown`  
context_source: `-`

````text
Doanh nghiệp: PNJ - bán lẻ - tiêu dùng (bán lẻ trang sức), sàn HOSE.
Chủ đề: hàng tồn kho và dự phòng giảm giá hàng tồn kho.

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- inventory_gross: Hàng tồn kho (gốc, trước dự phòng) [VND, số dư cuối kỳ]
- inventory_writedown: Dự phòng giảm giá hàng tồn kho [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến inventory_writedown.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-004 · P04-GAS24-receivables

allowed_vars (13): `current_assets, short_term_receivables, receivables_customers, prepaid_to_suppliers, provision_doubtful_debt, total_assets, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `receivables_customers`  
context_source: `-`

````text
Doanh nghiệp: GAS - tiện ích - năng lượng (khí), sàn HOSE.
Chủ đề: phải thu khách hàng và nợ khó đòi.

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- provision_doubtful_debt: Dự phòng phải thu ngắn hạn khó đòi [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến receivables_customers.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-004 · P04-GAS24-receivables

allowed_vars (13): `current_assets, short_term_receivables, receivables_customers, prepaid_to_suppliers, provision_doubtful_debt, total_assets, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `receivables_customers`  
context_source: `data/sample/raw/ocr_results/GAS/2024/GAS_Baocaotaichinh_2024_Kiemtoan_Hopnhat/GAS_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1136-L1146`

````text
Doanh nghiệp: GAS - tiện ích - năng lượng (khí), sàn HOSE.
Chủ đề: phải thu khách hàng và nợ khó đòi.

Trích thuyết minh báo cáo tài chính năm 2024 của GAS (mục 5. PHÀI THU NGẢN HẠN CỦA KHÁCH HÀNG):
<<<
5 PHÀI THU NGẢN HẠN CỦA KHÁCH HÀNG
 | 2024VND | 2023VND
Bên thứ ba (*) | 11.637.281.488.165 | 8.262.139.798.385
Bên liên quan (Thuyết minh 35(b)) | 5.107.374.386.312 | 4.279.141.434.495
 | 16.744.655.874.477 | 12.541.281.232.880
(*) Chi tiết khách hàng bên thu ba có số dư chiếm từ 10% trở lên trong tổng số dư phải thu ngắn hạn của khách hàng như sau:
 | 2024VND | 2023VND
Công ty Nhiệt điện Phú Mỹ | 1.739.993.982.218 | 1.738.932.577.442
Tại ngày 31 tháng 12 năm 2024, số dư các khoản phải thu ngắn hạn của khách hàng bao gồm 2.056 tỷ Đồng đến từ Công ty TNHH Năng lượng Mề Kông ("PM2.2") và Công ty Điện lực TNHH BOT Phú Mỹ 3 ("PM3") (tại ngày 31 tháng 12 năm 2023: 1.078 tỷ Đồng). Các khoản phải thu này phát sinh từ phần chênh lệch giữa đơn giá bán khí mới và đơn giá bán khí cũ do có sự thay đổi về các nguồn cung cấp khí của Tổng Công ty cho PM2.2 và PM3. Tổng Công ty cho rằng đơn giá bán khí mới để ghi nhận doanh thu và phải thu ngắn hạn của khách hàng nếu trên được ước tính trên cơ sở hợp lý nhất dựa theo các nguyên tắc về giá bán khí đã được các bên mua và bán đồng thuận và tương đồng với giá thị trường mà Tổng Công ty đã bán cho các khách hàng khác. Trong năm 2024, Tổng Công ty đã nhận được Thông báo Kết luận của Văn phòng Chính phủ về việc ký kết các phụ lục sửa đổi của Hợp đồng mua bán khí cũng nhu ý kiến của Bộ Công thương về việc ký kết các phụ lục này. Tại ngày phê chuẩn báo cáo tài chính hợp nhất, các bên vẫn đang trong quá trình thảo luận để ký kết chính thức các phụ lục của các hợp đồng mua bán khí liên quan đến đơn giá bán khí mới này. Ban Tổng Giám đốc đánh giá khả năng ký kết chính thức các phụ lục nếu trên theo đơn giá được phê duyệt là cao.
Tại ngày 31 tháng 12 năm 2024 và ngày 31 tháng 12 năm 2023, số dư các khoản phải thu ngắn hạn của khách hàng khó có khả năng thu hồi lần lượt là 5.441.791.177.829 Đồng và 1.795.966.693.990 Đồng như đã trình bày tại Thuyết minh 8.
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- provision_doubtful_debt: Dự phòng phải thu ngắn hạn khó đòi [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến receivables_customers. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-003 · P04-GAS24-receivables

allowed_vars (13): `current_assets, short_term_receivables, receivables_customers, prepaid_to_suppliers, provision_doubtful_debt, total_assets, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `receivables_customers`  
context_source: `data/sample/raw/ocr_results/GAS/2024/GAS_Baocaotaichinh_2024_Kiemtoan_Hopnhat/GAS_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1136-L1146`

````text
Doanh nghiệp: GAS - tiện ích - năng lượng (khí), sàn HOSE.
Chủ đề: phải thu khách hàng và nợ khó đòi.

Trích thuyết minh báo cáo tài chính năm 2024 của GAS (mục 5. PHÀI THU NGẢN HẠN CỦA KHÁCH HÀNG):
<<<
5 PHÀI THU NGẢN HẠN CỦA KHÁCH HÀNG
 | 2024VND | 2023VND
Bên thứ ba (*) | 11.637.281.488.165 | 8.262.139.798.385
Bên liên quan (Thuyết minh 35(b)) | 5.107.374.386.312 | 4.279.141.434.495
 | 16.744.655.874.477 | 12.541.281.232.880
(*) Chi tiết khách hàng bên thu ba có số dư chiếm từ 10% trở lên trong tổng số dư phải thu ngắn hạn của khách hàng như sau:
 | 2024VND | 2023VND
Công ty Nhiệt điện Phú Mỹ | 1.739.993.982.218 | 1.738.932.577.442
Tại ngày 31 tháng 12 năm 2024, số dư các khoản phải thu ngắn hạn của khách hàng bao gồm 2.056 tỷ Đồng đến từ Công ty TNHH Năng lượng Mề Kông ("PM2.2") và Công ty Điện lực TNHH BOT Phú Mỹ 3 ("PM3") (tại ngày 31 tháng 12 năm 2023: 1.078 tỷ Đồng). Các khoản phải thu này phát sinh từ phần chênh lệch giữa đơn giá bán khí mới và đơn giá bán khí cũ do có sự thay đổi về các nguồn cung cấp khí của Tổng Công ty cho PM2.2 và PM3. Tổng Công ty cho rằng đơn giá bán khí mới để ghi nhận doanh thu và phải thu ngắn hạn của khách hàng nếu trên được ước tính trên cơ sở hợp lý nhất dựa theo các nguyên tắc về giá bán khí đã được các bên mua và bán đồng thuận và tương đồng với giá thị trường mà Tổng Công ty đã bán cho các khách hàng khác. Trong năm 2024, Tổng Công ty đã nhận được Thông báo Kết luận của Văn phòng Chính phủ về việc ký kết các phụ lục sửa đổi của Hợp đồng mua bán khí cũng nhu ý kiến của Bộ Công thương về việc ký kết các phụ lục này. Tại ngày phê chuẩn báo cáo tài chính hợp nhất, các bên vẫn đang trong quá trình thảo luận để ký kết chính thức các phụ lục của các hợp đồng mua bán khí liên quan đến đơn giá bán khí mới này. Ban Tổng Giám đốc đánh giá khả năng ký kết chính thức các phụ lục nếu trên theo đơn giá được phê duyệt là cao.
Tại ngày 31 tháng 12 năm 2024 và ngày 31 tháng 12 năm 2023, số dư các khoản phải thu ngắn hạn của khách hàng khó có khả năng thu hồi lần lượt là 5.441.791.177.829 Đồng và 1.795.966.693.990 Đồng như đã trình bày tại Thuyết minh 8.
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- provision_doubtful_debt: Dự phòng phải thu ngắn hạn khó đòi [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến receivables_customers. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "receivables_accrual", "formula": "safe_div(delta(short_term_receivables, 4), mean(total_assets, 4))", "rationale": "Phải thu ngắn hạn phình ra là phần dồn tích chưa thành tiền, thường đi trước lợi suất kém.", "source": {"type": "line_item", "ref": "short_term_receivables, total_assets"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-003 · P04-GAS24-receivables

allowed_vars (13): `current_assets, short_term_receivables, receivables_customers, prepaid_to_suppliers, provision_doubtful_debt, total_assets, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `receivables_customers`  
context_source: `-`

````text
Doanh nghiệp: GAS - tiện ích - năng lượng (khí), sàn HOSE.
Chủ đề: phải thu khách hàng và nợ khó đòi.

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- provision_doubtful_debt: Dự phòng phải thu ngắn hạn khó đòi [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến receivables_customers.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F2-005 · P05-HUT24-receivables

allowed_vars (13): `current_assets, short_term_receivables, receivables_customers, prepaid_to_suppliers, provision_doubtful_debt, total_assets, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `receivables_customers`  
context_source: `data/sample/raw/ocr_results/HUT/2024/4_hut_2025_4_2_f4a0b52_vi_baocaotaichinh_kiemtoan_2024_bchn_sign/4_hut_2025_4_2_f4a0b52_vi_baocaotaichinh_kiemtoan_2024_bchn_sign_extracted.txt#L1458-L1470`

````text
Doanh nghiệp: HUT - bất động sản (hạ tầng + BĐS), sàn HNX.
Chủ đề: phải thu khách hàng và nợ khó đòi.

Trích thuyết minh báo cáo tài chính năm 2024 của HUT (mục 7. Nợ xấu):
<<<
7. Nợ xấu
a. Các khoản phải thu quá hạn thanh toán, hoặc chưa quá hạn nhưng khó có khả năng thu hồi
Giá gốc | Dự phòng | Giá trị có thể thu hồi | Giá gốc | Dự phòng | Giá trị có thể thu hồi
Sở GTVT tỉnh Thái Bình | 89.903.800.000 | 89.903.800.000 | - | 89.903.800.000 | 89.903.800.000 | -
Ông Bùi Văn Khoa | 19.800.000.000 | 19.800.000.000 | - | 19.800.000.000 | 19.800.000.000 | -
Các đối tượng khác | 49.923.612.800 | 46.717.919.020 | 3.205.693.780 | 45.501.009.837 | 44.038.623.282 | 1.462.386.555
Công ty IT Fusion | 3.150.000.000 | 3.150.000.000 | - | 3.150.000.000 | 3.150.000.000 | -
Các đối tượng khác | 1.835.031.826 | 1.835.031.826 | - | 1.835.031.826 | 1.835.031.826 | -
Cộng | 164.612.444.626 | 161.406.750.846 | 3.205.693.780 | 160.189.841.663 | 158.727.455.108 | 1.462.386.555
b. Đánh giá của Công ty về khả năng thu hồi nợ quá hạn
Công ty đã đánh giá và trích lập dự phòng đối với các khoản nợ quá hạn, nợ khó có khả năng thu hồi với sự thận trọng phù hợp. Công ty sẽ tiếp tục thực hiện các biện pháp để đảm bảo thu hồi được số nợ quá hạn.
c. Chi tiết tình hình tăng, giảm dự phòng nợ phải thu khó đòi
 | Năm nay | Năm trước
Số dư đầu năm | 158.727.455.108 | 154.109.309.303
Trích lập dự phòng bổ sung trong năm | 2.690.238.352 | 2.887.513.676
Hoàn nhập dự phòng trong năm | (10.942.614) | (9.520.403.844)
Tăng do hợp nhất | - | 11.251.035.973
Số dư cuối năm | 161.406.750.846 | 158.727.455.108
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- provision_doubtful_debt: Dự phòng phải thu ngắn hạn khó đòi [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến receivables_customers. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-004 · P05-HUT24-receivables

allowed_vars (13): `current_assets, short_term_receivables, receivables_customers, prepaid_to_suppliers, provision_doubtful_debt, total_assets, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `receivables_customers`  
context_source: `data/sample/raw/ocr_results/HUT/2024/4_hut_2025_4_2_f4a0b52_vi_baocaotaichinh_kiemtoan_2024_bchn_sign/4_hut_2025_4_2_f4a0b52_vi_baocaotaichinh_kiemtoan_2024_bchn_sign_extracted.txt#L1458-L1470`

````text
Doanh nghiệp: HUT - bất động sản (hạ tầng + BĐS), sàn HNX.
Chủ đề: phải thu khách hàng và nợ khó đòi.

Trích thuyết minh báo cáo tài chính năm 2024 của HUT (mục 7. Nợ xấu):
<<<
7. Nợ xấu
a. Các khoản phải thu quá hạn thanh toán, hoặc chưa quá hạn nhưng khó có khả năng thu hồi
Giá gốc | Dự phòng | Giá trị có thể thu hồi | Giá gốc | Dự phòng | Giá trị có thể thu hồi
Sở GTVT tỉnh Thái Bình | 89.903.800.000 | 89.903.800.000 | - | 89.903.800.000 | 89.903.800.000 | -
Ông Bùi Văn Khoa | 19.800.000.000 | 19.800.000.000 | - | 19.800.000.000 | 19.800.000.000 | -
Các đối tượng khác | 49.923.612.800 | 46.717.919.020 | 3.205.693.780 | 45.501.009.837 | 44.038.623.282 | 1.462.386.555
Công ty IT Fusion | 3.150.000.000 | 3.150.000.000 | - | 3.150.000.000 | 3.150.000.000 | -
Các đối tượng khác | 1.835.031.826 | 1.835.031.826 | - | 1.835.031.826 | 1.835.031.826 | -
Cộng | 164.612.444.626 | 161.406.750.846 | 3.205.693.780 | 160.189.841.663 | 158.727.455.108 | 1.462.386.555
b. Đánh giá của Công ty về khả năng thu hồi nợ quá hạn
Công ty đã đánh giá và trích lập dự phòng đối với các khoản nợ quá hạn, nợ khó có khả năng thu hồi với sự thận trọng phù hợp. Công ty sẽ tiếp tục thực hiện các biện pháp để đảm bảo thu hồi được số nợ quá hạn.
c. Chi tiết tình hình tăng, giảm dự phòng nợ phải thu khó đòi
 | Năm nay | Năm trước
Số dư đầu năm | 158.727.455.108 | 154.109.309.303
Trích lập dự phòng bổ sung trong năm | 2.690.238.352 | 2.887.513.676
Hoàn nhập dự phòng trong năm | (10.942.614) | (9.520.403.844)
Tăng do hợp nhất | - | 11.251.035.973
Số dư cuối năm | 161.406.750.846 | 158.727.455.108
>>>

Danh sách biến được phép dùng:
- current_assets: TÀI SẢN NGẮN HẠN [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- provision_doubtful_debt: Dự phòng phải thu ngắn hạn khó đòi [VND, số dư cuối kỳ, ghi số âm]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến receivables_customers. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "receivables_accrual", "formula": "safe_div(delta(short_term_receivables, 4), mean(total_assets, 4))", "rationale": "Phải thu ngắn hạn phình ra là phần dồn tích chưa thành tiền, thường đi trước lợi suất kém.", "source": {"type": "line_item", "ref": "short_term_receivables, total_assets"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F1-005 · P06-TNG24-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `-`

````text
Doanh nghiệp: TNG - sản xuất công nghiệp (dệt may vốn hoá nhỏ), sàn HNX.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-006 · P06-TNG24-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `data/sample/raw/ocr_results/TNG/2024/TNG_Baocaotaichinh_2024_Kiemtoan/TNG_Baocaotaichinh_2024_Kiemtoan_extracted.txt#L1292-L1318`

````text
Doanh nghiệp: TNG - sản xuất công nghiệp (dệt may vốn hoá nhỏ), sàn HNX.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Trích thuyết minh báo cáo tài chính năm 2024 của TNG (mục 22. VAY DÀI HẠN):
<<<
22. VAY DÀI HẠN
Giá trị/Số có khả năng trả nợ | Tăng | Giảm | Số cuối nămGiá trị/Số có khả năng trả nợ
VND |  | VND | VND
Vay dài hạn | 716.279.584.223 | 114.479.625.701 | 224.253.960.000 | 606.505.249.924
Trái phiếu thường (Chỉ tiết tại Thuyết minh số 23) | 297.205.691.000 | 401.343.166.867 | 5.925.000.000 | 692.623.857.867
 | 1.013.485.275.223 | 515.822.792.568 | 230.178.960.000 | 1.299.129.107.791
Số phải trả trong vòng 12 tháng(Trình bày ở Thuyết minh số 21) | 201.381.680.000 |  |  | 206.007.352.895
- Vay | 201.381.680.000 |  |  | 206.007.352.895
Số phải trả sau 12 tháng | 812.103.595.223 |  |  | 1.093.121.754.896
- Vay | 514.897.904.223 |  |  | 400.497.897.029
- Trái phiếu thường | 297.205.691.000 |  |  | 692.623.857.867
 |  |  | Số cuối năm | Số đầu năm
 |  |  | VND | VND
Ngân hàng Thương mại Cổ phần Công thương Việt Nam - Chi nhánh Thái Nguyên (i) |  |  | 275.824.574.606 | 336.090.887.683
Ngân hàng Thương mại Cổ phần Đầu tư và Phát triển Việt Nam - Chi nhánh Thái Nguyên (ii) |  |  | 202.052.494.303 | 271.023.476.823
Ngân hàng Thương mại Cổ phần Ngoại thương Việt Nam - Chi nhánh Thái Nguyên (iii) |  |  | 115.188.181.015 | 99.165.219.717
Quỹ bảo vệ môi trường Việt Nam (iv) |  |  | 13.440.000.000 | 10.000.000.000
 |  |  | 606.505.249.924 | 716.279.584.223
STT | Bên cho vay | Hợp đồng | Hạn mức | Mục đích | Kỳ hạn gốc và lãi | Lãi suất trong năm | Tài sản đăm bảo
(i) | Ngân hàng Thương mại Cổ phần Công thương Việt Nam - Chi nhánh Thái Nguyên | 01/2022-HĐCVDADT/NHCT220-TNG | 123.100.000.000 VND | Thanh toán chi phí đầu tư hợp pháp của Dự án: Mở rộng nhà máy TNG Phú Bình | Thời hạn vay 7 năm kể từ ngày tiếp theo ngày Ngân hàng giải ngân khoản vay đầu tiên cho Công ty. Lãi suất áp dụng hiện tại là 12%/năm đối với các khoản vay bằng VND. | 12%/năm | Toàn bộ tài sản hình thành từ vốn vay của Dự án (Thuyết minh số 11).
(i) | Ngân hàng Thương mại Cổ phần Công thương Việt Nam - Chi nhánh Thái Nguyên | 07/2022-HĐCVDADT/NHCT220-TNG | 14.500.000.000 VND | Thanh toán các chi phí đầu tư hợp pháp cho dự án đầu tư máy móc, thiết bị toàn Công ty năm 2022 | Thời hạn vay 5 năm kể từ ngày tiếp theo ngày Ngân hàng giải ngân khoản vay đầu tiên cho Công ty. Đối với các khoản vay bằng VND, lãi suất cho vay bằng lãi suất cơ sở cộng (+) biên độ 3,5% một năm. | 12%/năm | Toàn bộ tài sản hình thành từ vốn vay của Dự án (Thuyết minh số 11).
(i) | Ngân hàng Thương mại Cổ phần Công thương Việt Nam - Chi nhánh Thái Nguyên | 08/2022-HĐCVDADT/NHCT220-TNG | 30.820.000.000 VND | Thanh toán các chi phí đầu tư hợp pháp cho dự án đầu tư máy móc, thiết bị toàn Công ty năm 2022 (lần 2) | Thời hạn vay 5 năm kể từ ngày tiếp theo ngày Ngân hàng giải ngân khoản vay đầu tiên cho Công ty. Đối với các khoản vay bằng VND, lãi suất cho vay bằng lãi suất cơ sở cộng (+) biên độ 3,5% một năm. | 12,5%/năm | Toàn bộ tài sản hình thành từ vốn vay của Dự án (Thuyết minh số 11).
(i) | Ngân hàng Thương mại Cổ phần Công thương Việt Nam - Chi nhánh Thái Nguyên | 11/2022-HĐCVDADT/NHCT220-TNG | 12.113.000.000 VND | Thanh toán các chi phí đầu tư hợp pháp cho dự án đầu tư máy móc, thiết bị toàn Công ty năm 2022 (lần 3) | Thời hạn vay 5 năm kể từ ngày tiếp theo ngày Ngân hàng giải ngân khoản vay đầu tiên cho Công ty. Đối với các khoản vay bằng VND, lãi suất cho vay bằng lãi suất cơ sở cộng (+) biên độ 3,5% một năm. | 12,5%/năm | Toàn bộ tài sản hình thành từ vốn vay của Dự án (Thuyết minh số 11).
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-004 · P06-TNG24-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `-`

````text
Doanh nghiệp: TNG - sản xuất công nghiệp (dệt may vốn hoá nhỏ), sàn HNX.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-006 · P07-NLG17-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `-`

````text
Doanh nghiệp: NLG - bất động sản (BĐS nhà ở tầm trung), sàn HOSE.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-007 · P07-NLG17-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `data/sample/raw/ocr_results/NLG/2017/NLG_Baocaotaichinh_2017_Kiemtoan_Hopnhat/NLG_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1115-L1170`

````text
Doanh nghiệp: NLG - bất động sản (BĐS nhà ở tầm trung), sàn HOSE.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Trích thuyết minh báo cáo tài chính năm 2017 của NLG (mục 22. VAY VÀ NỘ):
<<<
22. VAY VÀ NỘ
 | Số cuối năm | VND Số đầu năm
Vay ngắn hạn từ cá nhân (TM số 22.1) | 2.800.000.000 | 69.894.565.335
Vay ngắn hạn từ ngân hàng (TM số 22.1) | 113.644.486.982 | 82.126.096.080
Vay dài hạn đến hạn trả (TM số 22.2) | 99.522.177.000 | 101.943.358.000
Trái phiếu phát hành đến hạn trả (TM số 22.3) | - | 99.690.509.259
 | 215.966.663.982 | 353.654.528.674
Vay dài hạn từ ngân hàng (TM số 22.2) | 228.548.210.000 | 349.613.387.000
TỔNG CỘNG | 444.514.873.982 | 703.267.915.674
22.1 Vay ngắn hạn
Chi tiết các khoản vay ngắn hạn như sau:
 | Số cuối nămVND | Ngày đáo hạn | Mục đích vay | Lãi suất%/năm | Hình thức đảm bảo
Vay các cá nhân | 2.800.000.000 | Ngày 14 tháng 4năm 2018 | Hỗ trợ nhu cầuvốn lưu động | 10,5 | Tín chấp
Ngân hàng Thương mại Cổ phần Ngoại thương Việt Nam | 55.763.336.107 | Ngày 25 tháng 4 năm2018 |  | 7,8 | Quyền sử dụng đất và các tài sản trênđất tại xã An Thạnh, Huyện Bến Lức,Tính Long An
Ngân hàng Thương mại Cổ phần Phương Đông –Chi nhánh Tân Thuận | 44.836.439.795 | Từ ngày 24 tháng 5năm 2018 đến ngày 21tháng 9 năm 2018 | Hỗ trợ nhu cầuvốn lưu động | 7,5 | Quyền sử dụng đất tại bản đồ số 5, xãAn Thạnh, Huyện Bến Lức, Tính LongAn
Ngân hàng Nông Nghiệp và Phát Triển Nông Thôn Việt Nam– Chi nhánh 8 | 13.044.711.080 | Ngày 20 tháng 9năm 2018 |  | 7,5 | Quyền sử dụng đất và các tài sản trênđất tại xã An Thạnh, Huyện Bến Lức,Tính Long An
TỔNG CỘNG | 113.644.486.982 |  |  |  | 
THUYẾT MINH BÁO CÁO TÀI CHÍNH HỢP NHẮT (tiếp theo)
22.2 Vay dài hạn từ ngân hàng
Chi tiết các khoản vay dài hạn từ ngân hàng như sau:
Ngân hàng | Số cuối nămVND | Ngày đáo hạn | Mục đích vay | Lãi suất%/năm | Hình thức đảm bảo
- Khoản vay 1 | 42.360.745.000 | Ngày 6 tháng 5năm 2018 | Hỗ trợ nhu cầuvốn lưu động | 10,2 | Quyền sử dụng đất diện tích \( 1.064.307 \text{ m}^{2} \) và tài sản gắn liền với đất hình thành trong tương laithuộc Dự án Long An VCD
- Khoản vay 2 | 285.709.642.000 | Từ ngày 12 tháng 1năm 2018 đến ngày 12tháng 10 năm 2022 | Mua dự ánHoàng Nam | 9,9 | Thế chấp quyền tài sản dự án Hoàng nam
TỔNG CỘNG | 328.070.387.000 |  |  |  | 
Trong đó:- Vay dài hạnđến hạn trả- Vay dài hạn | 99.522.177.000228.548.210.000 |  |  |  | 
22.3 Tình hình tăng giảm các khoản vay và trái phiếu trong kỳ
 | Vay | Trái phiếu | VNDTổng cộng
Số đầu năm | 603.577.406.415 | 99.690.509.259 | 703.267.915.674
Tiền thu từ đi vay | 217.005.924.465 | - | 217.005.924.465
Tiền chi trả nợ gốc | (376.068.456.898) | (100.000.000.000) | (476.068.456.898)
Chi phí phát hành trái phiếu | - | 309.490.741 | 309.490.741
Số cuối năm | 444.514.873.982 | - | 444.514.873.982
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-005 · P07-NLG17-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `data/sample/raw/ocr_results/NLG/2017/NLG_Baocaotaichinh_2017_Kiemtoan_Hopnhat/NLG_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1115-L1170`

````text
Doanh nghiệp: NLG - bất động sản (BĐS nhà ở tầm trung), sàn HOSE.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Trích thuyết minh báo cáo tài chính năm 2017 của NLG (mục 22. VAY VÀ NỘ):
<<<
22. VAY VÀ NỘ
 | Số cuối năm | VND Số đầu năm
Vay ngắn hạn từ cá nhân (TM số 22.1) | 2.800.000.000 | 69.894.565.335
Vay ngắn hạn từ ngân hàng (TM số 22.1) | 113.644.486.982 | 82.126.096.080
Vay dài hạn đến hạn trả (TM số 22.2) | 99.522.177.000 | 101.943.358.000
Trái phiếu phát hành đến hạn trả (TM số 22.3) | - | 99.690.509.259
 | 215.966.663.982 | 353.654.528.674
Vay dài hạn từ ngân hàng (TM số 22.2) | 228.548.210.000 | 349.613.387.000
TỔNG CỘNG | 444.514.873.982 | 703.267.915.674
22.1 Vay ngắn hạn
Chi tiết các khoản vay ngắn hạn như sau:
 | Số cuối nămVND | Ngày đáo hạn | Mục đích vay | Lãi suất%/năm | Hình thức đảm bảo
Vay các cá nhân | 2.800.000.000 | Ngày 14 tháng 4năm 2018 | Hỗ trợ nhu cầuvốn lưu động | 10,5 | Tín chấp
Ngân hàng Thương mại Cổ phần Ngoại thương Việt Nam | 55.763.336.107 | Ngày 25 tháng 4 năm2018 |  | 7,8 | Quyền sử dụng đất và các tài sản trênđất tại xã An Thạnh, Huyện Bến Lức,Tính Long An
Ngân hàng Thương mại Cổ phần Phương Đông –Chi nhánh Tân Thuận | 44.836.439.795 | Từ ngày 24 tháng 5năm 2018 đến ngày 21tháng 9 năm 2018 | Hỗ trợ nhu cầuvốn lưu động | 7,5 | Quyền sử dụng đất tại bản đồ số 5, xãAn Thạnh, Huyện Bến Lức, Tính LongAn
Ngân hàng Nông Nghiệp và Phát Triển Nông Thôn Việt Nam– Chi nhánh 8 | 13.044.711.080 | Ngày 20 tháng 9năm 2018 |  | 7,5 | Quyền sử dụng đất và các tài sản trênđất tại xã An Thạnh, Huyện Bến Lức,Tính Long An
TỔNG CỘNG | 113.644.486.982 |  |  |  | 
THUYẾT MINH BÁO CÁO TÀI CHÍNH HỢP NHẮT (tiếp theo)
22.2 Vay dài hạn từ ngân hàng
Chi tiết các khoản vay dài hạn từ ngân hàng như sau:
Ngân hàng | Số cuối nămVND | Ngày đáo hạn | Mục đích vay | Lãi suất%/năm | Hình thức đảm bảo
- Khoản vay 1 | 42.360.745.000 | Ngày 6 tháng 5năm 2018 | Hỗ trợ nhu cầuvốn lưu động | 10,2 | Quyền sử dụng đất diện tích \( 1.064.307 \text{ m}^{2} \) và tài sản gắn liền với đất hình thành trong tương laithuộc Dự án Long An VCD
- Khoản vay 2 | 285.709.642.000 | Từ ngày 12 tháng 1năm 2018 đến ngày 12tháng 10 năm 2022 | Mua dự ánHoàng Nam | 9,9 | Thế chấp quyền tài sản dự án Hoàng nam
TỔNG CỘNG | 328.070.387.000 |  |  |  | 
Trong đó:- Vay dài hạnđến hạn trả- Vay dài hạn | 99.522.177.000228.548.210.000 |  |  |  | 
22.3 Tình hình tăng giảm các khoản vay và trái phiếu trong kỳ
 | Vay | Trái phiếu | VNDTổng cộng
Số đầu năm | 603.577.406.415 | 99.690.509.259 | 703.267.915.674
Tiền thu từ đi vay | 217.005.924.465 | - | 217.005.924.465
Tiền chi trả nợ gốc | (376.068.456.898) | (100.000.000.000) | (476.068.456.898)
Chi phí phát hành trái phiếu | - | 309.490.741 | 309.490.741
Số cuối năm | 444.514.873.982 | - | 444.514.873.982
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "cash_to_current_liabilities", "formula": "safe_div(cash_and_equivalents, current_liabilities)", "rationale": "Tiền mặt so với nợ ngắn hạn đo khả năng thanh toán; thấp làm tăng rủi ro khi dòng tiền bán hàng chậm lại.", "source": {"type": "line_item", "ref": "cash_and_equivalents, current_liabilities"}},
{"name": "net_debt_to_equity", "formula": "safe_div(short_term_debt + long_term_debt - cash_and_equivalents, equity)", "rationale": "Đòn bẩy ròng cao làm tăng rủi ro tài chính, cổ phiếu nhạy hơn với lãi suất.", "source": {"type": "line_item", "ref": "short_term_debt, long_term_debt, cash_and_equivalents, equity"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-005 · P07-NLG17-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `-`

````text
Doanh nghiệp: NLG - bất động sản (BĐS nhà ở tầm trung), sàn HOSE.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F2-008 · P08-POW17-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `data/sample/raw/ocr_results/POW/2017/POW_Baocaotaichinh_2017_Kiemtoan_Hopnhat/POW_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1041-L1064`

````text
Doanh nghiệp: POW - tiện ích - năng lượng (nhiệt điện), sàn HOSE.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Trích thuyết minh báo cáo tài chính năm 2017 của POW (mục 21. VAY VÀ NỘ THUÊ TÀI CHÍNH DÀI HẠN):
<<<
21. VAY VÀ NỘ THUÊ TÀI CHÍNH DÀI HẠN
Giá trịVND | Số có khả năngtrà nợVND | TăngVND | GiảmVND | Giá trịVND | Số có khả năngtrà nợVND
Vay dài hạn | 30.421.681.064.106 | 30.421.681.064.106 | 391.243.270.499 | 6.075.282.118.144 | 24.737.642.216.461 | 24.737.642.216.461
 | 30.421.681.064.106 | 30.421.681.064.106 | 391.243.270.499 | 6.075.282.118.144 | 24.737.642.216.461 | 24.737.642.216.461
Số phải trả trong vòng 12 tháng | 5.752.830.032.679 |  |  |  | 5.959.085.181.465 | 
Số phải trả sau 12 tháng | 24.668.851.031.427 |  |  |  | 18.778.557.034.996 | 
Chi tiết các khoản vay dài hạn như sau:
 | Số cuối nămVND | Số đầu nămVND
Các khoản vay tài trợ cho Nhà máy Nhiệt điện Vũng Ảng nhận bản giao từ Tập đoàn Dầu khí Việt Nam (i) | 11.450.214.577.237 | 14.411.475.537.982
Ngân hàng Citibank | 3.697.772.593.187 | 4.461.298.558.270
Ngân hàng Credit Agricole Corporate and Investment | 2.913.711.661.555 | 3.370.133.333.258
Ngân hàng TMCP Đại chúng Việt Nam | 1.868.440.226.086 | 2.038.298.426.086
Ngân hàng Phát triển Việt Nam | 1.472.339.106.579 | 1.588.192.734.484
Ngân hàng TMCP Ngoại thương Việt Nam | 1.237.514.993.619 | 1.859.282.752.702
Ngân hàng TMCP Sài Gòn - Hà Nội | 843.129.639.967 | 922.110.846.935
Ngân hàng TMCP An Bình | 432.484.560.000 | 352.889.944.699
Ngân hàng TMCP Quân đội | 306.729.952.784 | 315.906.976.392
Ngân hàng Credit Agricole CIB | 263.480.625.000 | 528.240.000.000
Ngân hàng TMCP Công thương Việt Nam | 233.703.118.976 | 269.655.118.976
Ngân hàng TMCP Việt Nam Thịnh Vượng | 17.240.771.471 | 194.046.933.097
Ngân hàng TMCP Phát triển Nhà Thành phố Hồ Chí Minh | - | 109.079.836.225
Vay cá nhân | 880.390.000 | 1.070.065.000
 | 24.737.642.216.461 | 30.421.681.064.106
Trừ: số phải trả trong vòng 12 tháng(được trình bày ở phân vay và nợ ngắn hạn) | 5.959.085.181.465 | 5.752.830.032.679
Số phải trả sau 12 tháng | 18.778.557.034.996 | 24.668.851.031.427
(i) Theo Nghị quyết số 753/NQ-DKVN ngày 05 tháng 02 năm 2016 của Hội đồng Thành viên Tập đoàn Dầu khí Việt Nam ("Tập đoàn"), Tập đoàn chấp thuận bản giao tài sản Nhà máy Nhiệt điện Vũng Áng 1 và Sân phân phối 500kV Trung tâm Điện lực Vũng Áng cho Tổng Công ty từ 24h ngày 31 tháng 12 năm 2015. Theo đó, Tập đoàn chuyển cho Tổng Công ty các hợp đồng vay có gốc USD tài trợ cho Nhà máy Nhiệt điện Vũng Áng có số dự tại ngày 31 tháng 12 năm 2015 là 764.516.576,33 USD (tương đường 16.034.180.412.163 VND). Tại ngày 31 tháng 12 năm 2017, số dư của các khoản vay này là 505.193.664,57 USD (tương đường 11.450.214.577.237 VND, trong đó, lãi chênh lệch tỷ giá phát sinh tại thời điểm cuối năm do đánh giá lại các khoản vay có gốc ngoại tệ này và được ghi nhận vào kết quả hoạt động kinh doanh năm 2017 là 27.785.486.563 VND). Định kỳ đến hạn trả nợ, Tổng Công ty chuyển tiền về Tập đoàn để thực hiện trả nợ gốc, lãi các khoản vay này cho Ngân hàng. Khoản vay được đảm bảo bằng bảo lãnh không hủy ngang của Bộ Tài chính cho 100% giá trị khoản vay (bao gồm nợ gốc, nợ lãi).
||2| ∑2.50,1 - |≤||
CÔNG TY TNHH MTV - TỔNG CÔNG TY ĐIỆN LỰC DẦU KHÍ VIỆT NAM THUYÊT MINH BÁO CÁO TÀI CHÍNH HỢP NHẮT (Tiếp theo)
Các khoản vay dài hạn của Tổng Công ty được giải ngân bằng Đô la Mỹ, Euro và Đồng Việt Nam để phục vụ cho việc đầu tư mua sắm tài sản cố định của Tổng Công ty.
Các khoản vay được phân loại theo đồng tiền giải ngân như sau:
Số cuối năm | Số đầu năm
VND | VND
Vay bằng Đô la Mỹ | 17.641.067.608.552 | 22.461.256.175.696
Vay bằng Euro | 1.920.633.080.526 | 2.169.174.006.516
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-006 · P08-POW17-debt

allowed_vars (16): `cash_and_equivalents, total_assets, total_liabilities, current_liabilities, short_term_debt, long_term_debt, equity, revenue, financial_expense, interest_expense, operating_profit, pretax_profit, net_income, depreciation, cfo, market_cap`  
must_reference: `interest_expense`  
context_source: `data/sample/raw/ocr_results/POW/2017/POW_Baocaotaichinh_2017_Kiemtoan_Hopnhat/POW_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1041-L1064`

````text
Doanh nghiệp: POW - tiện ích - năng lượng (nhiệt điện), sàn HOSE.
Chủ đề: vay nợ, trái phiếu và chi phí lãi vay.

Trích thuyết minh báo cáo tài chính năm 2017 của POW (mục 21. VAY VÀ NỘ THUÊ TÀI CHÍNH DÀI HẠN):
<<<
21. VAY VÀ NỘ THUÊ TÀI CHÍNH DÀI HẠN
Giá trịVND | Số có khả năngtrà nợVND | TăngVND | GiảmVND | Giá trịVND | Số có khả năngtrà nợVND
Vay dài hạn | 30.421.681.064.106 | 30.421.681.064.106 | 391.243.270.499 | 6.075.282.118.144 | 24.737.642.216.461 | 24.737.642.216.461
 | 30.421.681.064.106 | 30.421.681.064.106 | 391.243.270.499 | 6.075.282.118.144 | 24.737.642.216.461 | 24.737.642.216.461
Số phải trả trong vòng 12 tháng | 5.752.830.032.679 |  |  |  | 5.959.085.181.465 | 
Số phải trả sau 12 tháng | 24.668.851.031.427 |  |  |  | 18.778.557.034.996 | 
Chi tiết các khoản vay dài hạn như sau:
 | Số cuối nămVND | Số đầu nămVND
Các khoản vay tài trợ cho Nhà máy Nhiệt điện Vũng Ảng nhận bản giao từ Tập đoàn Dầu khí Việt Nam (i) | 11.450.214.577.237 | 14.411.475.537.982
Ngân hàng Citibank | 3.697.772.593.187 | 4.461.298.558.270
Ngân hàng Credit Agricole Corporate and Investment | 2.913.711.661.555 | 3.370.133.333.258
Ngân hàng TMCP Đại chúng Việt Nam | 1.868.440.226.086 | 2.038.298.426.086
Ngân hàng Phát triển Việt Nam | 1.472.339.106.579 | 1.588.192.734.484
Ngân hàng TMCP Ngoại thương Việt Nam | 1.237.514.993.619 | 1.859.282.752.702
Ngân hàng TMCP Sài Gòn - Hà Nội | 843.129.639.967 | 922.110.846.935
Ngân hàng TMCP An Bình | 432.484.560.000 | 352.889.944.699
Ngân hàng TMCP Quân đội | 306.729.952.784 | 315.906.976.392
Ngân hàng Credit Agricole CIB | 263.480.625.000 | 528.240.000.000
Ngân hàng TMCP Công thương Việt Nam | 233.703.118.976 | 269.655.118.976
Ngân hàng TMCP Việt Nam Thịnh Vượng | 17.240.771.471 | 194.046.933.097
Ngân hàng TMCP Phát triển Nhà Thành phố Hồ Chí Minh | - | 109.079.836.225
Vay cá nhân | 880.390.000 | 1.070.065.000
 | 24.737.642.216.461 | 30.421.681.064.106
Trừ: số phải trả trong vòng 12 tháng(được trình bày ở phân vay và nợ ngắn hạn) | 5.959.085.181.465 | 5.752.830.032.679
Số phải trả sau 12 tháng | 18.778.557.034.996 | 24.668.851.031.427
(i) Theo Nghị quyết số 753/NQ-DKVN ngày 05 tháng 02 năm 2016 của Hội đồng Thành viên Tập đoàn Dầu khí Việt Nam ("Tập đoàn"), Tập đoàn chấp thuận bản giao tài sản Nhà máy Nhiệt điện Vũng Áng 1 và Sân phân phối 500kV Trung tâm Điện lực Vũng Áng cho Tổng Công ty từ 24h ngày 31 tháng 12 năm 2015. Theo đó, Tập đoàn chuyển cho Tổng Công ty các hợp đồng vay có gốc USD tài trợ cho Nhà máy Nhiệt điện Vũng Áng có số dự tại ngày 31 tháng 12 năm 2015 là 764.516.576,33 USD (tương đường 16.034.180.412.163 VND). Tại ngày 31 tháng 12 năm 2017, số dư của các khoản vay này là 505.193.664,57 USD (tương đường 11.450.214.577.237 VND, trong đó, lãi chênh lệch tỷ giá phát sinh tại thời điểm cuối năm do đánh giá lại các khoản vay có gốc ngoại tệ này và được ghi nhận vào kết quả hoạt động kinh doanh năm 2017 là 27.785.486.563 VND). Định kỳ đến hạn trả nợ, Tổng Công ty chuyển tiền về Tập đoàn để thực hiện trả nợ gốc, lãi các khoản vay này cho Ngân hàng. Khoản vay được đảm bảo bằng bảo lãnh không hủy ngang của Bộ Tài chính cho 100% giá trị khoản vay (bao gồm nợ gốc, nợ lãi).
||2| ∑2.50,1 - |≤||
CÔNG TY TNHH MTV - TỔNG CÔNG TY ĐIỆN LỰC DẦU KHÍ VIỆT NAM THUYÊT MINH BÁO CÁO TÀI CHÍNH HỢP NHẮT (Tiếp theo)
Các khoản vay dài hạn của Tổng Công ty được giải ngân bằng Đô la Mỹ, Euro và Đồng Việt Nam để phục vụ cho việc đầu tư mua sắm tài sản cố định của Tổng Công ty.
Các khoản vay được phân loại theo đồng tiền giải ngân như sau:
Số cuối năm | Số đầu năm
VND | VND
Vay bằng Đô la Mỹ | 17.641.067.608.552 | 22.461.256.175.696
Vay bằng Euro | 1.920.633.080.526 | 2.169.174.006.516
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- short_term_debt: Vay và nợ thuê tài chính ngắn hạn [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_expense: Chi phí tài chính [VND, phát sinh trong kỳ]
- interest_expense: Chi phí lãi vay [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến interest_expense. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "cash_to_current_liabilities", "formula": "safe_div(cash_and_equivalents, current_liabilities)", "rationale": "Tiền mặt so với nợ ngắn hạn đo khả năng thanh toán; thấp làm tăng rủi ro khi dòng tiền bán hàng chậm lại.", "source": {"type": "line_item", "ref": "cash_and_equivalents, current_liabilities"}},
{"name": "net_debt_to_equity", "formula": "safe_div(short_term_debt + long_term_debt - cash_and_equivalents, equity)", "rationale": "Đòn bẩy ròng cao làm tăng rủi ro tài chính, cổ phiếu nhạy hơn với lãi suất.", "source": {"type": "line_item", "ref": "short_term_debt, long_term_debt, cash_and_equivalents, equity"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F1-007 · P09-HAH24-fixed_assets

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, accumulated_depreciation, construction_in_progress, total_assets, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `capex`  
context_source: `-`

````text
Doanh nghiệp: HAH - logistics - vận tải (vận tải container), sàn HOSE.
Chủ đề: tài sản cố định, khấu hao và đầu tư mới.

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- accumulated_depreciation: Giá trị hao mòn luỹ kế [VND, số dư cuối kỳ, ghi số âm]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến capex.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-009 · P09-HAH24-fixed_assets

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, accumulated_depreciation, construction_in_progress, total_assets, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `capex`  
context_source: `data/sample/raw/ocr_results/HAH/2024/HAH_Baocaotaichinh_2024_Kiemtoan_Hopnhat/HAH_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1329-L1368;data/sample/raw/ocr_results/HAH/2024/HAH_Baocaotaichinh_2024_Kiemtoan_Hopnhat/HAH_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L878-L899`

````text
Doanh nghiệp: HAH - logistics - vận tải (vận tải container), sàn HOSE.
Chủ đề: tài sản cố định, khấu hao và đầu tư mới.

Trích thuyết minh báo cáo tài chính năm 2024 của HAH (mục 12. Tài sản cố định hữu hình):
<<<
12. Tài sản cố định hữu hình
Nhà cửa, vật kiến trúc | Máy móc và thiết bị | Phương tiện vận tải, truyền dẫn | Thiết bị, dụng cụ quản lý | Tài sản có định khác | Cộng
536.053.228.057 | 364.988.076.318 | 3.247.044.653.608 | 8.778.254.144 | 40.364.554.536 | 4.197.228.766.663
5.881.506.027 | 85.432.334.900 | 1.994.462.255.389 | - | - | 2.085.776.096.316
- | - | (3.932.025.689) | - | - | (3.932.025.689)
- | - | (4.647.357.902) | - | (445.454.545) | (5.092.812.447)
541.934.734.084 | 450.420.411.218 | 5.232.927.525.406 | 8.778.254.144 | 39.919.099.991 | 6.273.980.024.843
49.764.389.448 | 282.565.189.420 | 127.466.213.527 | 3.278.226.707 | 426.492.137 | 463.500.511.239
219.604.191.161 | 305.078.749.290 | 774.348.567.365 | 5.098.572.358 | 24.535.262.774 | 1.328.665.342.948
31.292.773.044 | 21.262.186.507 | 326.571.100.839 | 1.599.048.334 | 1.964.440.603 | 382.689.549.327
- | - | (3.759.426.627) | - | - | (3.759.426.627)
- | - | - | - | (96.515.146) | (96.515.146)
250.896.964.205 | 326.340.935.797 | 1.097.160.241.577 | 6.697.620.692 | 26.403.188.231 | 1.707.498.950.502
316.449.036.896 | 59.909.327.028 | 2.472.696.086.243 | 3.679.681.786 | 15.829.291.762 | 2.868.563.423.715
291.037.769.879 | 124.079.475.421 | 4.135.767.283.829 | 2.080.633.452 | 13.515.911.760 | 4.566.481.074.341
Thanh lý, nhượng bán
Giảm do phân loại lại
Trong đó:
Đã khấu hao hết nhưng vẫn còn
Giá tri hao mòn
Khâu hao trong năm
Thanh lý, nhượng bán
Giảm do phân loại lại
Giá trị còn lại
Trong đó:
Tạm thời chưa sử dụng
Dang chò thanh lý
Một số tài sản cố định hữu hình có giá trị còn lại theo số sách là 4.379.760.015.155 VND đã được thể chấp để đảm bảo cho các khoản vay của các

10. Tài sản cố định hữu hình
Tài sản cố định hữu hình được thể hiện theo nguyên giá trừ hao mòn lũy kế. Nguyên giá tài sản cố định hữu hình bao gồm toàn bộ các chi phí mà Tập đoàn phải bỏ ra để có được tài sản cố định tính đến thời điểm đưa tài sản đó vào trạng thái sẵn sàng sử dụng. Các chi phí phát sinh sau ghi nhận ban đầu chi được ghi tăng nguyên giá tài sản cố định nếu các chi phí này chắc chắn làm tăng lợi ích kinh tế trong tương lai do sử dụng tài sản đó. Các chi phí phát sinh không thỏa mãn điều kiện trên được ghi nhận là chi phí sản xuất, kinh doanh trong kỳ.
Khi tài sản cố định hữu hình được bán hay thanh lý, nguyên giá và giá trị hao mòn lũy kế được xóa số và lãi, lỗ phát sinh do thanh lý được ghi nhận vào thu nhập hay chi phí trong kỳ.
Tài sản cố định hữu hình được khấu hao theo phương pháp đường thẳng dựa trên thời gian hữu dụng ước tính. Số năm khấu hao của các loại tài sản cố định hữu hình như sau:
Loai tài sản cố định | Số năm
Nhà cửa, vật kiến trúc | 05-20
Máy móc, thiết bị | 03-10
Phương tiện vận tải truyền dẫn | 06-15
Thiết bị, dụng cụ quản lý | 03-08
Tài sản cố định hữu hình khác | 04-10
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □
BẢO CÁO TÀI CHÍNH HỢP NHẤT
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- accumulated_depreciation: Giá trị hao mòn luỹ kế [VND, số dư cuối kỳ, ghi số âm]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến capex. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-007 · P09-HAH24-fixed_assets

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, accumulated_depreciation, construction_in_progress, total_assets, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `capex`  
context_source: `data/sample/raw/ocr_results/HAH/2024/HAH_Baocaotaichinh_2024_Kiemtoan_Hopnhat/HAH_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1329-L1368;data/sample/raw/ocr_results/HAH/2024/HAH_Baocaotaichinh_2024_Kiemtoan_Hopnhat/HAH_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L878-L899`

````text
Doanh nghiệp: HAH - logistics - vận tải (vận tải container), sàn HOSE.
Chủ đề: tài sản cố định, khấu hao và đầu tư mới.

Trích thuyết minh báo cáo tài chính năm 2024 của HAH (mục 12. Tài sản cố định hữu hình):
<<<
12. Tài sản cố định hữu hình
Nhà cửa, vật kiến trúc | Máy móc và thiết bị | Phương tiện vận tải, truyền dẫn | Thiết bị, dụng cụ quản lý | Tài sản có định khác | Cộng
536.053.228.057 | 364.988.076.318 | 3.247.044.653.608 | 8.778.254.144 | 40.364.554.536 | 4.197.228.766.663
5.881.506.027 | 85.432.334.900 | 1.994.462.255.389 | - | - | 2.085.776.096.316
- | - | (3.932.025.689) | - | - | (3.932.025.689)
- | - | (4.647.357.902) | - | (445.454.545) | (5.092.812.447)
541.934.734.084 | 450.420.411.218 | 5.232.927.525.406 | 8.778.254.144 | 39.919.099.991 | 6.273.980.024.843
49.764.389.448 | 282.565.189.420 | 127.466.213.527 | 3.278.226.707 | 426.492.137 | 463.500.511.239
219.604.191.161 | 305.078.749.290 | 774.348.567.365 | 5.098.572.358 | 24.535.262.774 | 1.328.665.342.948
31.292.773.044 | 21.262.186.507 | 326.571.100.839 | 1.599.048.334 | 1.964.440.603 | 382.689.549.327
- | - | (3.759.426.627) | - | - | (3.759.426.627)
- | - | - | - | (96.515.146) | (96.515.146)
250.896.964.205 | 326.340.935.797 | 1.097.160.241.577 | 6.697.620.692 | 26.403.188.231 | 1.707.498.950.502
316.449.036.896 | 59.909.327.028 | 2.472.696.086.243 | 3.679.681.786 | 15.829.291.762 | 2.868.563.423.715
291.037.769.879 | 124.079.475.421 | 4.135.767.283.829 | 2.080.633.452 | 13.515.911.760 | 4.566.481.074.341
Thanh lý, nhượng bán
Giảm do phân loại lại
Trong đó:
Đã khấu hao hết nhưng vẫn còn
Giá tri hao mòn
Khâu hao trong năm
Thanh lý, nhượng bán
Giảm do phân loại lại
Giá trị còn lại
Trong đó:
Tạm thời chưa sử dụng
Dang chò thanh lý
Một số tài sản cố định hữu hình có giá trị còn lại theo số sách là 4.379.760.015.155 VND đã được thể chấp để đảm bảo cho các khoản vay của các

10. Tài sản cố định hữu hình
Tài sản cố định hữu hình được thể hiện theo nguyên giá trừ hao mòn lũy kế. Nguyên giá tài sản cố định hữu hình bao gồm toàn bộ các chi phí mà Tập đoàn phải bỏ ra để có được tài sản cố định tính đến thời điểm đưa tài sản đó vào trạng thái sẵn sàng sử dụng. Các chi phí phát sinh sau ghi nhận ban đầu chi được ghi tăng nguyên giá tài sản cố định nếu các chi phí này chắc chắn làm tăng lợi ích kinh tế trong tương lai do sử dụng tài sản đó. Các chi phí phát sinh không thỏa mãn điều kiện trên được ghi nhận là chi phí sản xuất, kinh doanh trong kỳ.
Khi tài sản cố định hữu hình được bán hay thanh lý, nguyên giá và giá trị hao mòn lũy kế được xóa số và lãi, lỗ phát sinh do thanh lý được ghi nhận vào thu nhập hay chi phí trong kỳ.
Tài sản cố định hữu hình được khấu hao theo phương pháp đường thẳng dựa trên thời gian hữu dụng ước tính. Số năm khấu hao của các loại tài sản cố định hữu hình như sau:
Loai tài sản cố định | Số năm
Nhà cửa, vật kiến trúc | 05-20
Máy móc, thiết bị | 03-10
Phương tiện vận tải truyền dẫn | 06-15
Thiết bị, dụng cụ quản lý | 03-08
Tài sản cố định hữu hình khác | 04-10
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □
BẢO CÁO TÀI CHÍNH HỢP NHẤT
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- accumulated_depreciation: Giá trị hao mòn luỹ kế [VND, số dư cuối kỳ, ghi số âm]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến capex. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "cip_to_fixed_assets", "formula": "safe_div(construction_in_progress, fixed_assets)", "rationale": "Tỷ trọng công trình dở dang lớn báo hiệu năng lực mới sắp đưa vào khai thác, kèm rủi ro chậm tiến độ.", "source": {"type": "note", "ref": "chi phí xây dựng cơ bản dở dang"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-006 · P09-HAH24-fixed_assets

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, accumulated_depreciation, construction_in_progress, total_assets, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `capex`  
context_source: `-`

````text
Doanh nghiệp: HAH - logistics - vận tải (vận tải container), sàn HOSE.
Chủ đề: tài sản cố định, khấu hao và đầu tư mới.

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- accumulated_depreciation: Giá trị hao mòn luỹ kế [VND, số dư cuối kỳ, ghi số âm]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến capex.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F2-010 · P10-TNG17-fixed_assets

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, accumulated_depreciation, construction_in_progress, total_assets, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `capex`  
context_source: `data/sample/raw/ocr_results/TNG/2017/TNG_Baocaotaichinh_2017_Kiemtoan/TNG_Baocaotaichinh_2017_Kiemtoan_extracted.txt#L712-L727`

````text
Doanh nghiệp: TNG - sản xuất công nghiệp (dệt may vốn hoá nhỏ), sàn HNX.
Chủ đề: tài sản cố định, khấu hao và đầu tư mới.

Trích thuyết minh báo cáo tài chính năm 2017 của TNG (mục 10. TĂNG, GIÀM TÀI SẢN CỔ ĐỊNH HỮU HÌNH):
<<<
10. TĂNG, GIÀM TÀI SẢN CỔ ĐỊNH HỮU HÌNH
Nhà xuǒng vàvật kiến trúc | Máy mócvà thiết bị | Phương tiệnvận tải | Thiết bịvăn phòng | Tài sảnkhác | Tổng cộng
VND | VND | VND | VND | VND | VND
Số dư đầu năm | 663.579.937.073 | 602.081.775.048 | 9.942.253.146 | 3.551.721.851 | 1.586.314.137 | 1.280.742.001.255
Đầu tư xây dựng cơ bản hoàn thành | 983.566.435 | 64.569.825.844 | - | - | - | 65.553.392.279
Mua sắm mới trong năm | 2.589.385.999 | 40.417.632.300 | 524.545.455 | 954.244.200 | - | 44.485.807.954
Tăng do mua lại TSCĐ thuê tài chính | - | 10.108.822.322 | - | - | - | 10.108.822.322
Thanh lý, nhượng bán | (2.714.479.966) | (10.841.879.987) | (1.146.355.931) | - | - | (14.702.715.884)
Số dư cuối năm | 664.438.409.541 | 706.336.175.527 | 9.320.442.670 | 4.505.966.051 | 1.586.314.137 | 1.386.187.307.926
Số dư đầu năm | 114.264.143.978 | 275.727.400.492 | 2.828.416.933 | 2.884.928.403 | 517.968.960 | 396.222.858.766
Trích khấu hao trong năm | 30.556.503.914 | 67.033.280.317 | 1.057.062.785 | 340.610.914 | 209.804.485 | 99.197.262.415
Tăng do mua lại TSCĐ thuê tài chính | - | 4.963.082.409 | - | - | - | 4.963.082.409
Thanh lý | (988.917.905) | (10.603.078.057) | (570.454.419) | - | - | (12.162.450.381)
Giảm khác | - | (13.896.665) | - | - | - | (13.896.665)
Số dư cuối năm | 143.831.729.987 | 337.106.788.496 | 3.315.025.299 | 3.225.539.317 | 727.773.445 | 488.206.856.544
Tại ngày đầu năm | 549.315.793.095 | 326.354.374.556 | 7.113.836.213 | 666.793.448 | 1.068.345.177 | 884.519.142.489
Tại ngày cuối năm | 520.606.679.554 | 369.229.387.031 | 6.005.417.371 | 1.280.426.734 | 858.540.692 | 897.980.451.382
Như trình bày tại Thuyết minh số 17 và 18, Công ty đã thể chấp máy móc, thiết bị, phương tiện vận tải, nhà xuống và vật kiến trúc để đảm bào cho các khoản tiên vay tại các ngân hàng thương mại và tổ chức tín dụng.
Nguyên giá của tài sản cố định bao gồm các thiết bị đã khấu hao hết tại ngày 31 tháng 12 năm 2017 nhưng vẫn còn sử dụng với giá trị là 120.982.629.067 VND (tại ngày 31 tháng 12 năm 2016: 112.218.072.753 VND).
//E\( ^{n} \)/T H U H A J
\( \therefore {SA} = 5 \)
E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- accumulated_depreciation: Giá trị hao mòn luỹ kế [VND, số dư cuối kỳ, ghi số âm]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến capex. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-008 · P10-TNG17-fixed_assets

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, accumulated_depreciation, construction_in_progress, total_assets, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `capex`  
context_source: `data/sample/raw/ocr_results/TNG/2017/TNG_Baocaotaichinh_2017_Kiemtoan/TNG_Baocaotaichinh_2017_Kiemtoan_extracted.txt#L712-L727`

````text
Doanh nghiệp: TNG - sản xuất công nghiệp (dệt may vốn hoá nhỏ), sàn HNX.
Chủ đề: tài sản cố định, khấu hao và đầu tư mới.

Trích thuyết minh báo cáo tài chính năm 2017 của TNG (mục 10. TĂNG, GIÀM TÀI SẢN CỔ ĐỊNH HỮU HÌNH):
<<<
10. TĂNG, GIÀM TÀI SẢN CỔ ĐỊNH HỮU HÌNH
Nhà xuǒng vàvật kiến trúc | Máy mócvà thiết bị | Phương tiệnvận tải | Thiết bịvăn phòng | Tài sảnkhác | Tổng cộng
VND | VND | VND | VND | VND | VND
Số dư đầu năm | 663.579.937.073 | 602.081.775.048 | 9.942.253.146 | 3.551.721.851 | 1.586.314.137 | 1.280.742.001.255
Đầu tư xây dựng cơ bản hoàn thành | 983.566.435 | 64.569.825.844 | - | - | - | 65.553.392.279
Mua sắm mới trong năm | 2.589.385.999 | 40.417.632.300 | 524.545.455 | 954.244.200 | - | 44.485.807.954
Tăng do mua lại TSCĐ thuê tài chính | - | 10.108.822.322 | - | - | - | 10.108.822.322
Thanh lý, nhượng bán | (2.714.479.966) | (10.841.879.987) | (1.146.355.931) | - | - | (14.702.715.884)
Số dư cuối năm | 664.438.409.541 | 706.336.175.527 | 9.320.442.670 | 4.505.966.051 | 1.586.314.137 | 1.386.187.307.926
Số dư đầu năm | 114.264.143.978 | 275.727.400.492 | 2.828.416.933 | 2.884.928.403 | 517.968.960 | 396.222.858.766
Trích khấu hao trong năm | 30.556.503.914 | 67.033.280.317 | 1.057.062.785 | 340.610.914 | 209.804.485 | 99.197.262.415
Tăng do mua lại TSCĐ thuê tài chính | - | 4.963.082.409 | - | - | - | 4.963.082.409
Thanh lý | (988.917.905) | (10.603.078.057) | (570.454.419) | - | - | (12.162.450.381)
Giảm khác | - | (13.896.665) | - | - | - | (13.896.665)
Số dư cuối năm | 143.831.729.987 | 337.106.788.496 | 3.315.025.299 | 3.225.539.317 | 727.773.445 | 488.206.856.544
Tại ngày đầu năm | 549.315.793.095 | 326.354.374.556 | 7.113.836.213 | 666.793.448 | 1.068.345.177 | 884.519.142.489
Tại ngày cuối năm | 520.606.679.554 | 369.229.387.031 | 6.005.417.371 | 1.280.426.734 | 858.540.692 | 897.980.451.382
Như trình bày tại Thuyết minh số 17 và 18, Công ty đã thể chấp máy móc, thiết bị, phương tiện vận tải, nhà xuống và vật kiến trúc để đảm bào cho các khoản tiên vay tại các ngân hàng thương mại và tổ chức tín dụng.
Nguyên giá của tài sản cố định bao gồm các thiết bị đã khấu hao hết tại ngày 31 tháng 12 năm 2017 nhưng vẫn còn sử dụng với giá trị là 120.982.629.067 VND (tại ngày 31 tháng 12 năm 2016: 112.218.072.753 VND).
//E\( ^{n} \)/T H U H A J
\( \therefore {SA} = 5 \)
E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- accumulated_depreciation: Giá trị hao mòn luỹ kế [VND, số dư cuối kỳ, ghi số âm]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến capex. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "cip_to_fixed_assets", "formula": "safe_div(construction_in_progress, fixed_assets)", "rationale": "Tỷ trọng công trình dở dang lớn báo hiệu năng lực mới sắp đưa vào khai thác, kèm rủi ro chậm tiến độ.", "source": {"type": "note", "ref": "chi phí xây dựng cơ bản dở dang"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-011 · P11-HPG17-cip

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, construction_in_progress, total_assets, long_term_debt, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `construction_in_progress`  
context_source: `data/sample/raw/ocr_results/HPG/2017/HPG_Baocaotaichinh_2017_Kiemtoan_Hopnhat/HPG_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1269-L1277;data/sample/raw/ocr_results/HPG/2017/HPG_Baocaotaichinh_2017_Kiemtoan_Hopnhat/HPG_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L751-L753`

````text
Doanh nghiệp: HPG - sản xuất công nghiệp (thép), sàn HOSE.
Chủ đề: xây dựng cơ bản dở dang và chu kỳ đầu tư.

Trích thuyết minh báo cáo tài chính năm 2017 của HPG (mục 15. Chi phí xây dựng cơ bản dở dang):
<<<
15. Chi phí xây dựng cơ bản dở dang
 | 2017VND | 2016VND
Số dư đầu năm | 1.107.960.762.975 | 4.339.188.508.885
Tăng trong năm | 5.904.906.983.399 | 2.668.376.669.471
Tăng do mua công ty con | 40.336.054.000 | 1.408.754.512
Giảm do giải thể công ty con | (986.420.420) | (166.671.113)
Chuyển sang tài sản cố định hữu hình | (2.262.797.236.990) | (5.843.667.143.374)
Chuyển sang tài sản cố định vô hình | (1.401.135.096) | (16.766.590.000)
Chuyển sang bắt động sản đầu tư | - | (7.786.557.067)
Chuyển sang chi phí trả trước dài hạn | (59.426.854.519) | (28.388.477.090)
Chuyển sang chi phí trả trước ngắn hạn | (435.020.428) | (1.880.826.249)
Thanh lý | (903.319.497) | (2.045.295.000)
Biến động khác | (1.175.913.627) | (311.610.000)
Số dư cuối năm | 4.726.077.899.797 | 1.107.960.762.975
Các công trình xây dựng cơ bản đồ dang lớn như sau:
 | 31/12/2017VND | 1/1/2017VND
Dự án Khu liên hợp Gang thép tại Dung Quất | 1.536.739.121.107 | -
Dự án Khu liên hợp Gang thép tại Hải Dương | 38.474.562.924 | 66.188.073.600
Dự án mở rộng Nhà máy Ông thép | 58.771.465.017 | 156.166.783.570
Dự án Nhà máy Tôn mạ màu | 2.189.597.742.478 | 12.934.819.904
Dự án Nông nghiệp | 724.121.942.319 | 768.103.096.522
Các dự án khác | 178.373.065.952 | 104.567.989.379
 | 4.726.077.899.797 | 1.107.960.762.975
Tại ngày 31 tháng 12 năm 2017, giá trị ghi sổ của chi phí xây dựng cơ bản dở dang là 2.187.780 triệu VND (1/1/2017: Không) được thể chấp ngân hàng để bảo đảm cho các khoản vay của Tập đoàn.

3.10 Xây dựng cơ bản dở dang
Xây dựng cơ bản dở dang phần ánh (i) các khoản chi phí xây dựng và máy móc chưa được hoàn thành hoặc chưa lắp đặt xong và (ii) các khoản chi phí liên quan trực tiếp đến việc chăn nuôi lợn giống đang lớn và chưa sẵn sàng tạo ra sản phẩm. Không tính khấu hao cho xây dựng cơ bản dở dang trong quá trình xây dựng, lắp đặt và trong giai đoạn lợn giống chưa sẵn sàng tạo ra sản phẩm.
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến construction_in_progress. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-007 · P11-HPG17-cip

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, construction_in_progress, total_assets, long_term_debt, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `construction_in_progress`  
context_source: `-`

````text
Doanh nghiệp: HPG - sản xuất công nghiệp (thép), sàn HOSE.
Chủ đề: xây dựng cơ bản dở dang và chu kỳ đầu tư.

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến construction_in_progress.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-008 · P12-VGC24-cip

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, construction_in_progress, total_assets, long_term_debt, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `construction_in_progress`  
context_source: `-`

````text
Doanh nghiệp: VGC - sản xuất công nghiệp (vật liệu xây dựng + khu công nghiệp), sàn HOSE.
Chủ đề: xây dựng cơ bản dở dang và chu kỳ đầu tư.

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến construction_in_progress.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-012 · P12-VGC24-cip

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, construction_in_progress, total_assets, long_term_debt, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `construction_in_progress`  
context_source: `data/sample/raw/ocr_results/VGC/2024/VGC_Baocaotaichinh_2024_Kiemtoan_Hopnhat/VGC_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1241-L1249`

````text
Doanh nghiệp: VGC - sản xuất công nghiệp (vật liệu xây dựng + khu công nghiệp), sàn HOSE.
Chủ đề: xây dựng cơ bản dở dang và chu kỳ đầu tư.

Trích thuyết minh báo cáo tài chính năm 2024 của VGC (mục 16. CHI PHÍ XÂY DỰNG CƠ BẢN DỞ DANG):
<<<
16. CHI PHÍ XÂY DỰNG CƠ BẢN DỞ DANG
Số cuối năm | Số đầu năm
VND | VND
Dự án Khu công nghiệp Thuận Thành giai đoạn I (i) | 2.116.660.692.130 | 1.665.393.357.134
Dự án Khu công nghiệp Phú Hà giai đoạn I (ii) | 780.195.377.448 | 847.053.106.773
Dự án Khu công nghiệp Tiền Hải - Thái Bình (iii) | 567.455.107.466 | 567.758.824.716
Dự án khu công nghiệp Yên Mỹ (iv) | 564.410.924.283 | 967.377.801.285
Dự án Khu công nghiệp Phong Điền - Viglacera, Huế (v) | 482.601.472.479 | 361.179.656.400
Dự án Khu công nghiệp Vimariel (vi) | 460.702.696.662 | 324.616.900.668
Dự án Nhà máy kinh nổi Siêu trắng Phú Mỹ | 226.415.656.945 | 226.415.656.945
Dự án Khu công nghiệp Sông Công II giai đoạn 2 (vii) | 197.794.002.378 | 298.244.444
Dự án Khu du lịch sinh thái cao cấp Văn Hải (viii) | 149.385.843.263 | 759.915.074.391
Dự án Khu công nghiệp Hải Yên | 14.894.521.573 | 13.631.151.953
Dự án Khu công nghiệp Yên Phong II-C | - | 26.274.432.196
Các công trình khác | 533.416.580.979 | 469.462.797.835
 | 6.093.932.875.606 | 6.229.377.004.740
(i) Dự án đầu tư phát triển kết cấu hạ tầng Khu Công nghiệp Thuận Thành I được thực hiện theo Quyết định số 187/TCT-HĐQT ngày 31 tháng 5 năm 2021 và phê duyệt điều chỉnh theo Quyết định số 86/TCT-HĐQT ngày 08 tháng 5 năm 2023, Quyết định 151/TCT-HĐQT ngày 12 tháng 12 năm 2023 của Hội đồng Quản trị Tổng Công ty. Dự án có diện tích 262,71 ha nằm trên địa phận các Xã Ninh Xá, Trạm Lộ, Nghĩa Đạo, Huyện Thuận Thành, Tính Bắc Ních với tổng mức đầu tư là 3.395,8 tỷ VND bằng vốn tự có, vốn huy động và vốn vay thương mại. Dự án thực hiện đầu tư các hạng mục chủ yếu là: Sản nền; Đường nội bộ; Hệ thống cấp nước, thoát nước mưa; Hệ thống thoát nước thải; Hệ thống cấp điện trung thể; Hệ thống chiều sáng và trạm biến áp và nhà điều hành; Cây xanh, cảnh quan; Hệ thống kênh mương,... Tiến độ dự án được chia thành 3 giai đoạn: Giai đoạn chuẩn bị đầu tư (2020-2021); Giai đoạn thực hiện đầu tư (từ quý III/2021 đến năm 2025); và Giai đoạn kết thúc đầu tư (năm 2026). Tính đến thời điểm lập báo cáo, dự án đang trong giai đoạn thực hiện sản lắp mặt bằng, xây dựng hạ tầng xung quanh và bàn giao.
Tài sản gòm máy móc, trang thiết bị nội thất, phương tiện vận tải, quyền tài sản và lợi ích hợp pháp liên quan tới các hợp đồng mua bán/cho thuê/thi công liên quan đến công tác đến bù, giải phóng mặt bằng hình thành từ dự án Thuận Thành I đang được thế chấp cho khoản vay tại Ngân hàng TMCP Công Thương Việt Nam theo Hợp đồng cho vay số 01/2022-HDCVDADT/NHCT285-TTI ngày 30 tháng 12 năm 2022 và Văn bản sửa đổi, bổ sung hợp đồng cho vay đầu tư dự án ngày 28 tháng 12 năm 2023 (chi tiết tại Thuyết minh số 24).
(ii) Dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng Khu công nghiệp Phú Hà giai đoạn I được thực hiện theo Quyết định số 29/TCT-HĐQT ngày 23 tháng 01 năm 2015, Quyết định số 73/TCT-HĐQT ngày 08 tháng 11 năm 2019, Quyết định số 165/TCT-HĐQT ngày 30 tháng 8 năm 2022, Quyết định số 152/TCT-HĐQT ngày 22 tháng 12 năm 2023 và Quyết định số 176/TCT-HĐQT ngày 30 tháng 9 năm 2024 về việc phê duyệt điều chỉnh dự án và kế hoạch lựa chọn nhà thầu của Hội đồng Quản trị Tổng Công ty. Dự án có diện tích 356,29 ha nằm trên địa phận các xã Hà Thạch, Hà Lộc, Phú Hồ, thị xã Phú Thọ, tỉnh Phú Thọ với tổng mức đầu tư là 2.188,1 tỷ VND bằng vốn tư có, vốn huy động và vốn vay thương mại. Dự án thực hiện đầu tư các hạng mục chú yếu là: San nền; Đường nội bộ; Hệ thống cấp nước, thoát nước mưa, hệ thống thoát nước thải; Hệ thống cung cấp điện, chiếu sáng đường giao thông; Xây dựng [...]
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến construction_in_progress. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-009 · P12-VGC24-cip

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, construction_in_progress, total_assets, long_term_debt, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `construction_in_progress`  
context_source: `data/sample/raw/ocr_results/VGC/2024/VGC_Baocaotaichinh_2024_Kiemtoan_Hopnhat/VGC_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1241-L1249`

````text
Doanh nghiệp: VGC - sản xuất công nghiệp (vật liệu xây dựng + khu công nghiệp), sàn HOSE.
Chủ đề: xây dựng cơ bản dở dang và chu kỳ đầu tư.

Trích thuyết minh báo cáo tài chính năm 2024 của VGC (mục 16. CHI PHÍ XÂY DỰNG CƠ BẢN DỞ DANG):
<<<
16. CHI PHÍ XÂY DỰNG CƠ BẢN DỞ DANG
Số cuối năm | Số đầu năm
VND | VND
Dự án Khu công nghiệp Thuận Thành giai đoạn I (i) | 2.116.660.692.130 | 1.665.393.357.134
Dự án Khu công nghiệp Phú Hà giai đoạn I (ii) | 780.195.377.448 | 847.053.106.773
Dự án Khu công nghiệp Tiền Hải - Thái Bình (iii) | 567.455.107.466 | 567.758.824.716
Dự án khu công nghiệp Yên Mỹ (iv) | 564.410.924.283 | 967.377.801.285
Dự án Khu công nghiệp Phong Điền - Viglacera, Huế (v) | 482.601.472.479 | 361.179.656.400
Dự án Khu công nghiệp Vimariel (vi) | 460.702.696.662 | 324.616.900.668
Dự án Nhà máy kinh nổi Siêu trắng Phú Mỹ | 226.415.656.945 | 226.415.656.945
Dự án Khu công nghiệp Sông Công II giai đoạn 2 (vii) | 197.794.002.378 | 298.244.444
Dự án Khu du lịch sinh thái cao cấp Văn Hải (viii) | 149.385.843.263 | 759.915.074.391
Dự án Khu công nghiệp Hải Yên | 14.894.521.573 | 13.631.151.953
Dự án Khu công nghiệp Yên Phong II-C | - | 26.274.432.196
Các công trình khác | 533.416.580.979 | 469.462.797.835
 | 6.093.932.875.606 | 6.229.377.004.740
(i) Dự án đầu tư phát triển kết cấu hạ tầng Khu Công nghiệp Thuận Thành I được thực hiện theo Quyết định số 187/TCT-HĐQT ngày 31 tháng 5 năm 2021 và phê duyệt điều chỉnh theo Quyết định số 86/TCT-HĐQT ngày 08 tháng 5 năm 2023, Quyết định 151/TCT-HĐQT ngày 12 tháng 12 năm 2023 của Hội đồng Quản trị Tổng Công ty. Dự án có diện tích 262,71 ha nằm trên địa phận các Xã Ninh Xá, Trạm Lộ, Nghĩa Đạo, Huyện Thuận Thành, Tính Bắc Ních với tổng mức đầu tư là 3.395,8 tỷ VND bằng vốn tự có, vốn huy động và vốn vay thương mại. Dự án thực hiện đầu tư các hạng mục chủ yếu là: Sản nền; Đường nội bộ; Hệ thống cấp nước, thoát nước mưa; Hệ thống thoát nước thải; Hệ thống cấp điện trung thể; Hệ thống chiều sáng và trạm biến áp và nhà điều hành; Cây xanh, cảnh quan; Hệ thống kênh mương,... Tiến độ dự án được chia thành 3 giai đoạn: Giai đoạn chuẩn bị đầu tư (2020-2021); Giai đoạn thực hiện đầu tư (từ quý III/2021 đến năm 2025); và Giai đoạn kết thúc đầu tư (năm 2026). Tính đến thời điểm lập báo cáo, dự án đang trong giai đoạn thực hiện sản lắp mặt bằng, xây dựng hạ tầng xung quanh và bàn giao.
Tài sản gòm máy móc, trang thiết bị nội thất, phương tiện vận tải, quyền tài sản và lợi ích hợp pháp liên quan tới các hợp đồng mua bán/cho thuê/thi công liên quan đến công tác đến bù, giải phóng mặt bằng hình thành từ dự án Thuận Thành I đang được thế chấp cho khoản vay tại Ngân hàng TMCP Công Thương Việt Nam theo Hợp đồng cho vay số 01/2022-HDCVDADT/NHCT285-TTI ngày 30 tháng 12 năm 2022 và Văn bản sửa đổi, bổ sung hợp đồng cho vay đầu tư dự án ngày 28 tháng 12 năm 2023 (chi tiết tại Thuyết minh số 24).
(ii) Dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng Khu công nghiệp Phú Hà giai đoạn I được thực hiện theo Quyết định số 29/TCT-HĐQT ngày 23 tháng 01 năm 2015, Quyết định số 73/TCT-HĐQT ngày 08 tháng 11 năm 2019, Quyết định số 165/TCT-HĐQT ngày 30 tháng 8 năm 2022, Quyết định số 152/TCT-HĐQT ngày 22 tháng 12 năm 2023 và Quyết định số 176/TCT-HĐQT ngày 30 tháng 9 năm 2024 về việc phê duyệt điều chỉnh dự án và kế hoạch lựa chọn nhà thầu của Hội đồng Quản trị Tổng Công ty. Dự án có diện tích 356,29 ha nằm trên địa phận các xã Hà Thạch, Hà Lộc, Phú Hồ, thị xã Phú Thọ, tỉnh Phú Thọ với tổng mức đầu tư là 2.188,1 tỷ VND bằng vốn tư có, vốn huy động và vốn vay thương mại. Dự án thực hiện đầu tư các hạng mục chú yếu là: San nền; Đường nội bộ; Hệ thống cấp nước, thoát nước mưa, hệ thống thoát nước thải; Hệ thống cung cấp điện, chiếu sáng đường giao thông; Xây dựng [...]
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến construction_in_progress. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "capex_to_depreciation", "formula": "safe_div(abs(capex), depreciation)", "rationale": "Chi đầu tư vượt xa khấu hao cho thấy doanh nghiệp đang mở rộng năng lực, lợi suất ngắn hạn thường thấp hơn (Titman, Wei, Xie 2004).", "source": {"type": "line_item", "ref": "capex, depreciation"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-008 · P12-VGC24-cip

allowed_vars (13): `long_term_assets, fixed_assets, tangible_fixed_assets, construction_in_progress, total_assets, long_term_debt, equity, revenue, net_income, depreciation, cfo, capex, market_cap`  
must_reference: `construction_in_progress`  
context_source: `-`

````text
Doanh nghiệp: VGC - sản xuất công nghiệp (vật liệu xây dựng + khu công nghiệp), sàn HOSE.
Chủ đề: xây dựng cơ bản dở dang và chu kỳ đầu tư.

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- fixed_assets: Tài sản cố định [VND, số dư cuối kỳ]
- tangible_fixed_assets: Tài sản cố định hữu hình [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến construction_in_progress.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F2-013 · P13-NLG24-customer_advances

allowed_vars (12): `cash_and_equivalents, short_term_receivables, inventory, total_assets, current_liabilities, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `customer_advances`  
context_source: `data/sample/raw/ocr_results/NLG/2024/NLG_Baocaotaichinh_2024_Kiemtoan_Hopnhat/NLG_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1315-L1325`

````text
Doanh nghiệp: NLG - bất động sản (BĐS nhà ở tầm trung), sàn HOSE.
Chủ đề: người mua trả tiền trước, doanh thu chưa thực hiện và doanh thu tương lai.

Trích thuyết minh báo cáo tài chính năm 2024 của NLG (mục 26. DOANH THU CHU'A THỰC HIỆN):
<<<
26. DOANH THU CHU'A THỰC HIỆN
Doanh thu chưa thực hiện tại ngày 31 tháng 12 năm 2024 bao gồm:
Giá trị của khoản lợi nhuận mà Nhóm Công ty nhận được từ việc chuyển nhượng một phần dự án Mizuki cho NNH Mizuki, theo tỷ lệ sở hữu của Nhóm Công ty trong các liên doanh này và khoản lợi nhuận phát sinh từ việc cung cấp dịch vụ cho các công ty này. Những khoản doanh thu chưa thực hiện này sẽ được thực hiện khi các hàng hóa bất động sản được bản giao cho người mua nhà; và
- Tiền thuê nhà nhận trước từ khách hàng cho toàn bộ giai đoạn thuê và được phân bổ định kỳ.
Chi tiết như sau:
 | Số cuối năm | VND Số đầu năm
Ngắn hạn |  | 
Tiền cho thuê nhận trước | 25.495.948.477 | 7.589.982.574
Dải hạn |  | 
Lợi nhuận chưa thực hiện dự án Mizuki Park | 248.771.574.944 | 218.146.395.789
Tiền cho thuê nhận trước | 54.507.282.664 | 41.554.737.058
 | 303.278.857.608 | 259.701.132.847
TỔNG CỘNG | 328.774.806.085 | 267.291.115.421
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến customer_advances. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-010 · P13-NLG24-customer_advances

allowed_vars (12): `cash_and_equivalents, short_term_receivables, inventory, total_assets, current_liabilities, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `customer_advances`  
context_source: `data/sample/raw/ocr_results/NLG/2024/NLG_Baocaotaichinh_2024_Kiemtoan_Hopnhat/NLG_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1315-L1325`

````text
Doanh nghiệp: NLG - bất động sản (BĐS nhà ở tầm trung), sàn HOSE.
Chủ đề: người mua trả tiền trước, doanh thu chưa thực hiện và doanh thu tương lai.

Trích thuyết minh báo cáo tài chính năm 2024 của NLG (mục 26. DOANH THU CHU'A THỰC HIỆN):
<<<
26. DOANH THU CHU'A THỰC HIỆN
Doanh thu chưa thực hiện tại ngày 31 tháng 12 năm 2024 bao gồm:
Giá trị của khoản lợi nhuận mà Nhóm Công ty nhận được từ việc chuyển nhượng một phần dự án Mizuki cho NNH Mizuki, theo tỷ lệ sở hữu của Nhóm Công ty trong các liên doanh này và khoản lợi nhuận phát sinh từ việc cung cấp dịch vụ cho các công ty này. Những khoản doanh thu chưa thực hiện này sẽ được thực hiện khi các hàng hóa bất động sản được bản giao cho người mua nhà; và
- Tiền thuê nhà nhận trước từ khách hàng cho toàn bộ giai đoạn thuê và được phân bổ định kỳ.
Chi tiết như sau:
 | Số cuối năm | VND Số đầu năm
Ngắn hạn |  | 
Tiền cho thuê nhận trước | 25.495.948.477 | 7.589.982.574
Dải hạn |  | 
Lợi nhuận chưa thực hiện dự án Mizuki Park | 248.771.574.944 | 218.146.395.789
Tiền cho thuê nhận trước | 54.507.282.664 | 41.554.737.058
 | 303.278.857.608 | 259.701.132.847
TỔNG CỘNG | 328.774.806.085 | 267.291.115.421
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến customer_advances. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "cash_to_current_liabilities", "formula": "safe_div(cash_and_equivalents, current_liabilities)", "rationale": "Tiền mặt so với nợ ngắn hạn đo khả năng thanh toán; thấp làm tăng rủi ro khi dòng tiền bán hàng chậm lại.", "source": {"type": "line_item", "ref": "cash_and_equivalents, current_liabilities"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F1-009 · P14-IDC24-customer_advances

allowed_vars (12): `cash_and_equivalents, short_term_receivables, inventory, total_assets, current_liabilities, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `customer_advances`  
context_source: `-`

````text
Doanh nghiệp: IDC - bất động sản (khu công nghiệp), sàn HNX.
Chủ đề: người mua trả tiền trước, doanh thu chưa thực hiện và doanh thu tương lai.

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến customer_advances.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-014 · P14-IDC24-customer_advances

allowed_vars (12): `cash_and_equivalents, short_term_receivables, inventory, total_assets, current_liabilities, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `customer_advances`  
context_source: `data/sample/raw/ocr_results/IDC/2024/IDC_Baocaotaichinh_2024_Kiemtoan_Hopnhat/IDC_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1464-L1466`

````text
Doanh nghiệp: IDC - bất động sản (khu công nghiệp), sàn HNX.
Chủ đề: người mua trả tiền trước, doanh thu chưa thực hiện và doanh thu tương lai.

Trích thuyết minh báo cáo tài chính năm 2024 của IDC (mục 26. DOANH THU CHU'A THỰC HIỆN):
<<<
26. DOANH THU CHU'A THỰC HIỆN
 | Số cuối năm | VND Số đầu năm
Ngắn hạn | 1.144.345.071.562 | 660.565.738.967
- Khu công nghiệp Phú Mỹ 2 | 926.813.971.092 | 336.873.549.422
- Khu công nghiệp Hựu Thạnh | 112.075.570.212 | 228.710.671.100
- Khu công nghiệp Phú Mỹ 2 mở rộng | 54.089.990.940 | 44.072.708.334
- Khu công nghiệp Quế Võ 2 | 20.259.032.311 | 20.259.032.300
- Khu công nghiệp Mỹ Xuân B1 | 18.079.544.046 | 18.065.266.280
- Khu công nghiệp Nhơn Trạch 1 | 7.942.925.436 | 8.272.790.561
- Khu công nghiệp Kim Hoa | 3.897.003.720 | 4.041.091.206
- Khu công nghiệp Mỹ Xuân A | 1.120.122.065 | 267.245.336
Doanh thu nhận trước ngắn hạn khác | 66.911.740 | 3.384.428
Dài hạn | 4.599.772.152.061 | 4.584.182.020.007
- Khu công nghiệp Phú Mỹ 2 | 1.404.155.318.524 | 1.445.624.559.476
- Khu công nghiệp Phú Mỹ 2 mở rộng | 1.356.915.432.219 | 1.381.559.119.365
- Khu công nghiệp Quế Võ 2 | 639.281.850.675 | 640.942.560.063
- Khu công nghiệp Mỹ Xuân B1 | 612.322.225.531 | 623.859.452.725
- Khu công nghiệp Hựu Thạnh | 311.427.609.236 | 204.877.438.530
- Khu công nghiệp Nhơn Trạch 1 | 183.129.399.221 | 190.728.149.442
- Khu công nghiệp Kim Hoa | 92.229.088.119 | 95.975.916.153
- Khu công nghiệp Mỹ Xuân A | 106.648.213 | 402.697.588
Doanh thu nhận trước dài hạn khác | 204.580.323 | 212.126.665
TỔNG CỘNG | 5.744.117.223.623 | 5.244.747.758.974
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến customer_advances. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-011 · P14-IDC24-customer_advances

allowed_vars (12): `cash_and_equivalents, short_term_receivables, inventory, total_assets, current_liabilities, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `customer_advances`  
context_source: `data/sample/raw/ocr_results/IDC/2024/IDC_Baocaotaichinh_2024_Kiemtoan_Hopnhat/IDC_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1464-L1466`

````text
Doanh nghiệp: IDC - bất động sản (khu công nghiệp), sàn HNX.
Chủ đề: người mua trả tiền trước, doanh thu chưa thực hiện và doanh thu tương lai.

Trích thuyết minh báo cáo tài chính năm 2024 của IDC (mục 26. DOANH THU CHU'A THỰC HIỆN):
<<<
26. DOANH THU CHU'A THỰC HIỆN
 | Số cuối năm | VND Số đầu năm
Ngắn hạn | 1.144.345.071.562 | 660.565.738.967
- Khu công nghiệp Phú Mỹ 2 | 926.813.971.092 | 336.873.549.422
- Khu công nghiệp Hựu Thạnh | 112.075.570.212 | 228.710.671.100
- Khu công nghiệp Phú Mỹ 2 mở rộng | 54.089.990.940 | 44.072.708.334
- Khu công nghiệp Quế Võ 2 | 20.259.032.311 | 20.259.032.300
- Khu công nghiệp Mỹ Xuân B1 | 18.079.544.046 | 18.065.266.280
- Khu công nghiệp Nhơn Trạch 1 | 7.942.925.436 | 8.272.790.561
- Khu công nghiệp Kim Hoa | 3.897.003.720 | 4.041.091.206
- Khu công nghiệp Mỹ Xuân A | 1.120.122.065 | 267.245.336
Doanh thu nhận trước ngắn hạn khác | 66.911.740 | 3.384.428
Dài hạn | 4.599.772.152.061 | 4.584.182.020.007
- Khu công nghiệp Phú Mỹ 2 | 1.404.155.318.524 | 1.445.624.559.476
- Khu công nghiệp Phú Mỹ 2 mở rộng | 1.356.915.432.219 | 1.381.559.119.365
- Khu công nghiệp Quế Võ 2 | 639.281.850.675 | 640.942.560.063
- Khu công nghiệp Mỹ Xuân B1 | 612.322.225.531 | 623.859.452.725
- Khu công nghiệp Hựu Thạnh | 311.427.609.236 | 204.877.438.530
- Khu công nghiệp Nhơn Trạch 1 | 183.129.399.221 | 190.728.149.442
- Khu công nghiệp Kim Hoa | 92.229.088.119 | 95.975.916.153
- Khu công nghiệp Mỹ Xuân A | 106.648.213 | 402.697.588
Doanh thu nhận trước dài hạn khác | 204.580.323 | 212.126.665
TỔNG CỘNG | 5.744.117.223.623 | 5.244.747.758.974
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến customer_advances. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "cash_to_current_liabilities", "formula": "safe_div(cash_and_equivalents, current_liabilities)", "rationale": "Tiền mặt so với nợ ngắn hạn đo khả năng thanh toán; thấp làm tăng rủi ro khi dòng tiền bán hàng chậm lại.", "source": {"type": "line_item", "ref": "cash_and_equivalents, current_liabilities"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-009 · P14-IDC24-customer_advances

allowed_vars (12): `cash_and_equivalents, short_term_receivables, inventory, total_assets, current_liabilities, customer_advances, equity, revenue, gross_profit, net_income, cfo, market_cap`  
must_reference: `customer_advances`  
context_source: `-`

````text
Doanh nghiệp: IDC - bất động sản (khu công nghiệp), sàn HNX.
Chủ đề: người mua trả tiền trước, doanh thu chưa thực hiện và doanh thu tương lai.

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- inventory: Hàng tồn kho (thuần) [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- current_liabilities: Nợ ngắn hạn [VND, số dư cuối kỳ]
- customer_advances: Người mua trả tiền trước ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến customer_advances.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-010 · P15-CTD17-associates

allowed_vars (13): `long_term_investments, investments_associates, total_assets, equity, minority_interest, revenue, financial_income, share_of_associates, pretax_profit, net_income, net_income_parent, cfi, market_cap`  
must_reference: `share_of_associates`  
context_source: `-`

````text
Doanh nghiệp: CTD - xây dựng - vật liệu (xây dựng), sàn HOSE.
Chủ đề: đầu tư vào công ty liên doanh, liên kết.

Danh sách biến được phép dùng:
- long_term_investments: Đầu tư tài chính dài hạn [VND, số dư cuối kỳ]
- investments_associates: Đầu tư vào công ty liên doanh, liên kết [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- minority_interest: Lợi ích cổ đông không kiểm soát [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_income: Doanh thu hoạt động tài chính [VND, phát sinh trong kỳ]
- share_of_associates: Phần lãi lỗ trong công ty liên doanh, liên kết [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- net_income_parent: Lợi nhuận sau thuế của cổ đông công ty mẹ [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến share_of_associates.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-015 · P15-CTD17-associates

allowed_vars (13): `long_term_investments, investments_associates, total_assets, equity, minority_interest, revenue, financial_income, share_of_associates, pretax_profit, net_income, net_income_parent, cfi, market_cap`  
must_reference: `share_of_associates`  
context_source: `data/sample/raw/ocr_results/CTD/2017/CTD_Baocaotaichinh_2017_Kiemtoan_Hopnhat/CTD_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L940-L982`

````text
Doanh nghiệp: CTD - xây dựng - vật liệu (xây dựng), sàn HOSE.
Chủ đề: đầu tư vào công ty liên doanh, liên kết.

Trích thuyết minh báo cáo tài chính năm 2017 của CTD (mục 15. ĐẦU TƯ VÀO CÁC CÔNG TY LIÊN KẾT):
<<<
15. ĐẦU TƯ VÀO CÁC CÔNG TY LIÊN KẾT
 | Số cuối năm | VND Số đầu năm
Đầu tư vào các công ty liên kết | 227.204.788.931 | 194.783.616.306
Chi tiết khoản đầu tư của Nhóm Công ty vào các công ty liên kết như sau:
Tỷ lệ sở hữu(%) | Giá trị(VND) | Tỷ lệ sở hữu(%) | Giá trị(VND)
Công ty Cổ phần Đầu tưXây dựng Ricons (&quot;Ricons&quot;) | 18,58 | 142.451.914.317 | 19,20 | 96.563.534.057
Công ty Cổ phần Đầu tưHạ Tầng FCC (&quot;FCC&quot;) | 35 | 84.600.817.819 | 35 | 98.051.443.745
Công ty Cổ phần Thương mạiQuảng Trọng (&quot;Quảng Trọng&quot;) | 36 | 152.056.795 | 36 | 168.638.504
TỔNG CỘNG |  | 227.204.788.931 |  | 194.783.616.306
Ricons là một công ty cổ phần được thành lập theo Giấy CNĐKKD số 4103002810 do Sở KH&ĐT Thành phố Hồ Chí Minh cấp ngày 27 tháng 10 năm 2004, sau đó điều chỉnh thành Giấy chứng nhận đăng ký Doanh nghiệp ("Giấy CNĐKDN") số 0303527596 vào ngày 9 tháng 6 năm 2011 và các giấy CNĐKKD và Giấy CNĐKDN điều chỉnh. Hoạt động chính được đăng ký của Ricons là cung cấp dịch vụ xây dựng dân dụng và công nghiệp, kinh doanh vật liệu xây dựng và kinh doanh bất động sản. Nhóm Công ty có ảnh hưởng đắng kể về các chính sách tài chính và hoạt động của Ricons.
FCC là một công ty cổ phần được thành lập theo Giấy CNĐKDN số 0106605407 do Sở KH&ĐT Thành phố Hà Nội cấp ngày 21 tháng 7 năm 2014 và các Giấy CNĐKDN điều chỉnh. Hoạt động chính được đăng ký của FCC là xây dựng các công trình dân dụng và công nghiệp.
Quảng Trọng là một công ty cổ phần được thành lập theo Giấy CNĐKKD số 4903000474 do Sở KH&DT Tĩnh Bà Rịa Vũng Tàu cấp ngày 18 tháng 12 năm 2007, sau đó điều chỉnh thành Giấy chứng nhận đăng ký Doanh nghiệp ("Giấy CNĐKDN") số 3500740022 và các giấy CNĐKKD và Giấy CNĐKDN điều chỉnh. Hoạt động chính được đăng ký của Quảng Trọng là kinh doanh bất động sản và cung cấp dịch vụ quản lý dự án.
Chi tiết giá trị khoản đầu tư vào các công ty liên kết như sau:
Giá trị đầu tư:
Số đầu năm và cuối năm | 136.160.000.000
Phần lũy kế lợi nhuận sau khi mua các công ty liên kết:
Số đầu năm | 58.623.616.306
Phần lợi nhuận từ các công ty liên kết trong năm | 31.676.978.729
Lợi nhuận chưa thực hiện trong năm | 744.193.896
Số cuối năm | 91.044.788.931
Giá trị còn lại:
Số đầu năm | 194.783.616.306
Số cuối năm | 227.204.788.931
>>>

Danh sách biến được phép dùng:
- long_term_investments: Đầu tư tài chính dài hạn [VND, số dư cuối kỳ]
- investments_associates: Đầu tư vào công ty liên doanh, liên kết [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- minority_interest: Lợi ích cổ đông không kiểm soát [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_income: Doanh thu hoạt động tài chính [VND, phát sinh trong kỳ]
- share_of_associates: Phần lãi lỗ trong công ty liên doanh, liên kết [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- net_income_parent: Lợi nhuận sau thuế của cổ đông công ty mẹ [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến share_of_associates. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-012 · P15-CTD17-associates

allowed_vars (13): `long_term_investments, investments_associates, total_assets, equity, minority_interest, revenue, financial_income, share_of_associates, pretax_profit, net_income, net_income_parent, cfi, market_cap`  
must_reference: `share_of_associates`  
context_source: `data/sample/raw/ocr_results/CTD/2017/CTD_Baocaotaichinh_2017_Kiemtoan_Hopnhat/CTD_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L940-L982`

````text
Doanh nghiệp: CTD - xây dựng - vật liệu (xây dựng), sàn HOSE.
Chủ đề: đầu tư vào công ty liên doanh, liên kết.

Trích thuyết minh báo cáo tài chính năm 2017 của CTD (mục 15. ĐẦU TƯ VÀO CÁC CÔNG TY LIÊN KẾT):
<<<
15. ĐẦU TƯ VÀO CÁC CÔNG TY LIÊN KẾT
 | Số cuối năm | VND Số đầu năm
Đầu tư vào các công ty liên kết | 227.204.788.931 | 194.783.616.306
Chi tiết khoản đầu tư của Nhóm Công ty vào các công ty liên kết như sau:
Tỷ lệ sở hữu(%) | Giá trị(VND) | Tỷ lệ sở hữu(%) | Giá trị(VND)
Công ty Cổ phần Đầu tưXây dựng Ricons (&quot;Ricons&quot;) | 18,58 | 142.451.914.317 | 19,20 | 96.563.534.057
Công ty Cổ phần Đầu tưHạ Tầng FCC (&quot;FCC&quot;) | 35 | 84.600.817.819 | 35 | 98.051.443.745
Công ty Cổ phần Thương mạiQuảng Trọng (&quot;Quảng Trọng&quot;) | 36 | 152.056.795 | 36 | 168.638.504
TỔNG CỘNG |  | 227.204.788.931 |  | 194.783.616.306
Ricons là một công ty cổ phần được thành lập theo Giấy CNĐKKD số 4103002810 do Sở KH&ĐT Thành phố Hồ Chí Minh cấp ngày 27 tháng 10 năm 2004, sau đó điều chỉnh thành Giấy chứng nhận đăng ký Doanh nghiệp ("Giấy CNĐKDN") số 0303527596 vào ngày 9 tháng 6 năm 2011 và các giấy CNĐKKD và Giấy CNĐKDN điều chỉnh. Hoạt động chính được đăng ký của Ricons là cung cấp dịch vụ xây dựng dân dụng và công nghiệp, kinh doanh vật liệu xây dựng và kinh doanh bất động sản. Nhóm Công ty có ảnh hưởng đắng kể về các chính sách tài chính và hoạt động của Ricons.
FCC là một công ty cổ phần được thành lập theo Giấy CNĐKDN số 0106605407 do Sở KH&ĐT Thành phố Hà Nội cấp ngày 21 tháng 7 năm 2014 và các Giấy CNĐKDN điều chỉnh. Hoạt động chính được đăng ký của FCC là xây dựng các công trình dân dụng và công nghiệp.
Quảng Trọng là một công ty cổ phần được thành lập theo Giấy CNĐKKD số 4903000474 do Sở KH&DT Tĩnh Bà Rịa Vũng Tàu cấp ngày 18 tháng 12 năm 2007, sau đó điều chỉnh thành Giấy chứng nhận đăng ký Doanh nghiệp ("Giấy CNĐKDN") số 3500740022 và các giấy CNĐKKD và Giấy CNĐKDN điều chỉnh. Hoạt động chính được đăng ký của Quảng Trọng là kinh doanh bất động sản và cung cấp dịch vụ quản lý dự án.
Chi tiết giá trị khoản đầu tư vào các công ty liên kết như sau:
Giá trị đầu tư:
Số đầu năm và cuối năm | 136.160.000.000
Phần lũy kế lợi nhuận sau khi mua các công ty liên kết:
Số đầu năm | 58.623.616.306
Phần lợi nhuận từ các công ty liên kết trong năm | 31.676.978.729
Lợi nhuận chưa thực hiện trong năm | 744.193.896
Số cuối năm | 91.044.788.931
Giá trị còn lại:
Số đầu năm | 194.783.616.306
Số cuối năm | 227.204.788.931
>>>

Danh sách biến được phép dùng:
- long_term_investments: Đầu tư tài chính dài hạn [VND, số dư cuối kỳ]
- investments_associates: Đầu tư vào công ty liên doanh, liên kết [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- minority_interest: Lợi ích cổ đông không kiểm soát [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_income: Doanh thu hoạt động tài chính [VND, phát sinh trong kỳ]
- share_of_associates: Phần lãi lỗ trong công ty liên doanh, liên kết [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- net_income_parent: Lợi nhuận sau thuế của cổ đông công ty mẹ [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến share_of_associates. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "financial_income_share", "formula": "safe_div(financial_income, pretax_profit)", "rationale": "Lợi nhuận dựa nhiều vào thu nhập tài chính thay vì hoạt động cốt lõi thì kém bền vững.", "source": {"type": "line_item", "ref": "financial_income, pretax_profit"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}},
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Doanh nghiệp mở rộng tài sản quá nhanh thường có lợi suất sau đó thấp hơn (Cooper, Gulen, Schill 2008).", "source": {"type": "line_item", "ref": "total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-010 · P15-CTD17-associates

allowed_vars (13): `long_term_investments, investments_associates, total_assets, equity, minority_interest, revenue, financial_income, share_of_associates, pretax_profit, net_income, net_income_parent, cfi, market_cap`  
must_reference: `share_of_associates`  
context_source: `-`

````text
Doanh nghiệp: CTD - xây dựng - vật liệu (xây dựng), sàn HOSE.
Chủ đề: đầu tư vào công ty liên doanh, liên kết.

Danh sách biến được phép dùng:
- long_term_investments: Đầu tư tài chính dài hạn [VND, số dư cuối kỳ]
- investments_associates: Đầu tư vào công ty liên doanh, liên kết [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- minority_interest: Lợi ích cổ đông không kiểm soát [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_income: Doanh thu hoạt động tài chính [VND, phát sinh trong kỳ]
- share_of_associates: Phần lãi lỗ trong công ty liên doanh, liên kết [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- net_income_parent: Lợi nhuận sau thuế của cổ đông công ty mẹ [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến share_of_associates.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-011 · P16-PVT17-associates

allowed_vars (13): `long_term_investments, investments_associates, total_assets, equity, minority_interest, revenue, financial_income, share_of_associates, pretax_profit, net_income, net_income_parent, cfi, market_cap`  
must_reference: `share_of_associates`  
context_source: `-`

````text
Doanh nghiệp: PVT - logistics - vận tải (vận tải dầu khí), sàn HOSE.
Chủ đề: đầu tư vào công ty liên doanh, liên kết.

Danh sách biến được phép dùng:
- long_term_investments: Đầu tư tài chính dài hạn [VND, số dư cuối kỳ]
- investments_associates: Đầu tư vào công ty liên doanh, liên kết [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- minority_interest: Lợi ích cổ đông không kiểm soát [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_income: Doanh thu hoạt động tài chính [VND, phát sinh trong kỳ]
- share_of_associates: Phần lãi lỗ trong công ty liên doanh, liên kết [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- net_income_parent: Lợi nhuận sau thuế của cổ đông công ty mẹ [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến share_of_associates.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-016 · P16-PVT17-associates

allowed_vars (13): `long_term_investments, investments_associates, total_assets, equity, minority_interest, revenue, financial_income, share_of_associates, pretax_profit, net_income, net_income_parent, cfi, market_cap`  
must_reference: `share_of_associates`  
context_source: `data/sample/raw/ocr_results/PVT/2017/PVT_Baocaotaichinh_2017_Kiemtoan_Hopnhat/PVT_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L768-L796`

````text
Doanh nghiệp: PVT - logistics - vận tải (vận tải dầu khí), sàn HOSE.
Chủ đề: đầu tư vào công ty liên doanh, liên kết.

Trích thuyết minh báo cáo tài chính năm 2017 của PVT (mục 12. ĐẦU TƯ VÀO CÔNG TY LIÊN DOANH, LIÊN KẾT):
<<<
12. ĐẦU TƯ VÀO CÔNG TY LIÊN DOANH, LIÊN KẾT
Đầu tư vào Công ty liên kết:
 | Số cuối nămVND | Số đầu nămVND
Đầu tư vào các Công ty liên kết | 150.037.720.000 | 150.037.720.000
Phần lợi nhuận phát sinh sau ngày đầu tư trừcổ tức được chia | 43.648.804.453 | 38.910.405.750
 | 193.686.524.453 | 188.948.125.750
Giá gốc khoản đầu tư và thông tin chỉ tiết về các công ty liên kết tại ngày 31 tháng 12 năm 2017 như sau:
 | Số cuối nămVND | Số đầu nămVND
Công ty Cổ phần Dịch vụ Khai thác Dầu khí PTSC | 98.000.000.000 | 98.000.000.000
Công ty Cổ phần vận tải dầu khí Cửu Long | 52.037.720.000 | 52.037.720.000
 | 150.037.720.000 | 150.037.720.000
Công ty Cổ phần Dịch vụ Khai thác Dầu khí PTSC được thành lập theo Giấy chứng nhận đăng ký doanh nghiệp số 3501811660 do Sở Kế hoạch và Đầu tư tính Bà Rịa - Vũng Tàu cấp ngày 01 tháng 4 năm 2011. Tổng Công ty đã góp 98 tỷ đồng, tương ứng với 49% tổng vốn điều lệ theo Giấy chứng nhận đăng ký doanh nghiệp. Hoạt động chính của công ty này là dịch vụ vận hành và bảo dưỡng các công trình khai thác đầu khí; hoạt động dịch vụ hỗ trợ khai thác đầu thô và khí tự nhiên; cung cấp lao động chuyên ngành đầu khí.
Công ty Cổ phần Dịch vụ Vận tải Dầu khí Cửu Long được thành lập theo Giấy chứng nhận đăng ký doanh nghiệp số 4103006914 do Sở Kế hoạch và Đầu tư Thành phố Hồ Chí Minh cấp ngày 04 tháng 6 năm 2007. Tổng Công ty đã góp 52.037.720.000 đồng, tương ứng với 22.63% tổng vốn điều lệ theo Giấy chứng nhận đăng ký doanh nghiệp. Hoạt động chính của công ty này là kinh doanh vận tải hành khách bằng taxi theo hợp đồng, theo tuyến cổ định, kinh doanh vận tải hàng hóa bằng ô tô, bằng dưỡng thủy nội địa; mua bán phương tiện, máy móc thiết bị, phụ tùng ngành giao thông vận tải, sản phẩm gas LPG, CNG, LNG; đại lý kinh doanh xăng dầu; dịch vụ hoán cải phương tiện vận tải; kinh doanh bất động sản, cho thuê văn phòng; kinh doanh nhà hàng, khách sạn; kinh doanh lữ hành nội địa, quốc tế; kinh doanh bãi đồ xe, trạm dùng; đầu tư, sản xuất, kinh doanh nhà máy thủy điện; kinh doanh vận tải khách bằng xe buýt; kinh doanh vận tải biển và mua bán phân bón.
TỔNG CÔNG TY CỔ PHẦN VÂN TẢI DẦU KHÍ
Thông tin tài chính tóm tắt về Công ty liên doanh, liên kết được trình bày như sau:
 | Số cuối nămVND | Số đầu nămVND
Tổng tài sản | 865.081.792.417 | 810.453.003.285
Tổng công nợ | (333.005.912.823) | (287.292.588.494)
Tài sản thuần | 532.075.879.594 | 523.160.414.791
Phần tài sản thuần khoản đầu tư vào công ty liên kết | 193.686.524.453 | 188.948.125.750
 | Năm nayVND | Năm trướcVND
Lợi nhuận sau thuế | 55.938.261.902 | 55.944.341.581
Lợi nhuận thuần từ khoản đầu tư vào công ty liên kết | 27.116.030.203 | 26.785.452.437
>>>

Danh sách biến được phép dùng:
- long_term_investments: Đầu tư tài chính dài hạn [VND, số dư cuối kỳ]
- investments_associates: Đầu tư vào công ty liên doanh, liên kết [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- minority_interest: Lợi ích cổ đông không kiểm soát [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_income: Doanh thu hoạt động tài chính [VND, phát sinh trong kỳ]
- share_of_associates: Phần lãi lỗ trong công ty liên doanh, liên kết [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- net_income_parent: Lợi nhuận sau thuế của cổ đông công ty mẹ [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến share_of_associates. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-013 · P16-PVT17-associates

allowed_vars (13): `long_term_investments, investments_associates, total_assets, equity, minority_interest, revenue, financial_income, share_of_associates, pretax_profit, net_income, net_income_parent, cfi, market_cap`  
must_reference: `share_of_associates`  
context_source: `data/sample/raw/ocr_results/PVT/2017/PVT_Baocaotaichinh_2017_Kiemtoan_Hopnhat/PVT_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L768-L796`

````text
Doanh nghiệp: PVT - logistics - vận tải (vận tải dầu khí), sàn HOSE.
Chủ đề: đầu tư vào công ty liên doanh, liên kết.

Trích thuyết minh báo cáo tài chính năm 2017 của PVT (mục 12. ĐẦU TƯ VÀO CÔNG TY LIÊN DOANH, LIÊN KẾT):
<<<
12. ĐẦU TƯ VÀO CÔNG TY LIÊN DOANH, LIÊN KẾT
Đầu tư vào Công ty liên kết:
 | Số cuối nămVND | Số đầu nămVND
Đầu tư vào các Công ty liên kết | 150.037.720.000 | 150.037.720.000
Phần lợi nhuận phát sinh sau ngày đầu tư trừcổ tức được chia | 43.648.804.453 | 38.910.405.750
 | 193.686.524.453 | 188.948.125.750
Giá gốc khoản đầu tư và thông tin chỉ tiết về các công ty liên kết tại ngày 31 tháng 12 năm 2017 như sau:
 | Số cuối nămVND | Số đầu nămVND
Công ty Cổ phần Dịch vụ Khai thác Dầu khí PTSC | 98.000.000.000 | 98.000.000.000
Công ty Cổ phần vận tải dầu khí Cửu Long | 52.037.720.000 | 52.037.720.000
 | 150.037.720.000 | 150.037.720.000
Công ty Cổ phần Dịch vụ Khai thác Dầu khí PTSC được thành lập theo Giấy chứng nhận đăng ký doanh nghiệp số 3501811660 do Sở Kế hoạch và Đầu tư tính Bà Rịa - Vũng Tàu cấp ngày 01 tháng 4 năm 2011. Tổng Công ty đã góp 98 tỷ đồng, tương ứng với 49% tổng vốn điều lệ theo Giấy chứng nhận đăng ký doanh nghiệp. Hoạt động chính của công ty này là dịch vụ vận hành và bảo dưỡng các công trình khai thác đầu khí; hoạt động dịch vụ hỗ trợ khai thác đầu thô và khí tự nhiên; cung cấp lao động chuyên ngành đầu khí.
Công ty Cổ phần Dịch vụ Vận tải Dầu khí Cửu Long được thành lập theo Giấy chứng nhận đăng ký doanh nghiệp số 4103006914 do Sở Kế hoạch và Đầu tư Thành phố Hồ Chí Minh cấp ngày 04 tháng 6 năm 2007. Tổng Công ty đã góp 52.037.720.000 đồng, tương ứng với 22.63% tổng vốn điều lệ theo Giấy chứng nhận đăng ký doanh nghiệp. Hoạt động chính của công ty này là kinh doanh vận tải hành khách bằng taxi theo hợp đồng, theo tuyến cổ định, kinh doanh vận tải hàng hóa bằng ô tô, bằng dưỡng thủy nội địa; mua bán phương tiện, máy móc thiết bị, phụ tùng ngành giao thông vận tải, sản phẩm gas LPG, CNG, LNG; đại lý kinh doanh xăng dầu; dịch vụ hoán cải phương tiện vận tải; kinh doanh bất động sản, cho thuê văn phòng; kinh doanh nhà hàng, khách sạn; kinh doanh lữ hành nội địa, quốc tế; kinh doanh bãi đồ xe, trạm dùng; đầu tư, sản xuất, kinh doanh nhà máy thủy điện; kinh doanh vận tải khách bằng xe buýt; kinh doanh vận tải biển và mua bán phân bón.
TỔNG CÔNG TY CỔ PHẦN VÂN TẢI DẦU KHÍ
Thông tin tài chính tóm tắt về Công ty liên doanh, liên kết được trình bày như sau:
 | Số cuối nămVND | Số đầu nămVND
Tổng tài sản | 865.081.792.417 | 810.453.003.285
Tổng công nợ | (333.005.912.823) | (287.292.588.494)
Tài sản thuần | 532.075.879.594 | 523.160.414.791
Phần tài sản thuần khoản đầu tư vào công ty liên kết | 193.686.524.453 | 188.948.125.750
 | Năm nayVND | Năm trướcVND
Lợi nhuận sau thuế | 55.938.261.902 | 55.944.341.581
Lợi nhuận thuần từ khoản đầu tư vào công ty liên kết | 27.116.030.203 | 26.785.452.437
>>>

Danh sách biến được phép dùng:
- long_term_investments: Đầu tư tài chính dài hạn [VND, số dư cuối kỳ]
- investments_associates: Đầu tư vào công ty liên doanh, liên kết [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- minority_interest: Lợi ích cổ đông không kiểm soát [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- financial_income: Doanh thu hoạt động tài chính [VND, phát sinh trong kỳ]
- share_of_associates: Phần lãi lỗ trong công ty liên doanh, liên kết [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- net_income_parent: Lợi nhuận sau thuế của cổ đông công ty mẹ [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến share_of_associates. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "financial_income_share", "formula": "safe_div(financial_income, pretax_profit)", "rationale": "Lợi nhuận dựa nhiều vào thu nhập tài chính thay vì hoạt động cốt lõi thì kém bền vững.", "source": {"type": "line_item", "ref": "financial_income, pretax_profit"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}},
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Doanh nghiệp mở rộng tài sản quá nhanh thường có lợi suất sau đó thấp hơn (Cooper, Gulen, Schill 2008).", "source": {"type": "line_item", "ref": "total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F1-012 · P17-NTP17-related_party

allowed_vars (12): `short_term_receivables, receivables_customers, prepaid_to_suppliers, total_assets, payables_suppliers, equity, revenue, cogs, net_income, cfo, related_party_disclosed, market_cap`  
must_reference: `related_party_disclosed`  
context_source: `-`

````text
Doanh nghiệp: NTP - sản xuất công nghiệp (nhựa), sàn HNX.
Chủ đề: giao dịch và số dư với các bên liên quan.

Danh sách biến được phép dùng:
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến related_party_disclosed.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-017 · P17-NTP17-related_party

allowed_vars (12): `short_term_receivables, receivables_customers, prepaid_to_suppliers, total_assets, payables_suppliers, equity, revenue, cogs, net_income, cfo, related_party_disclosed, market_cap`  
must_reference: `related_party_disclosed`  
context_source: `data/sample/raw/ocr_results/NTP/2017/NTP_Baocaotaichinh_2017_Kiemtoan_Hopnhat/NTP_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1227-L1253`

````text
Doanh nghiệp: NTP - sản xuất công nghiệp (nhựa), sàn HNX.
Chủ đề: giao dịch và số dư với các bên liên quan.

Trích thuyết minh báo cáo tài chính năm 2017 của NTP (mục 30. NGHIỆP VỤ VÀ SỐ DỰ VỚI CÁC BÊN LIÊN QUAN):
<<<
30. NGHIỆP VỤ VÀ SỐ DỰ VỚI CÁC BÊN LIÊN QUAN
Danh sách các bên liên quan có giao dịch và số dư chủ yếu trong năm:
Bên liên quan | Môi quan hệ
Công ty Cổ phần Nhựa Thiếu niên Tiền Phong phía Nam | Công ty liên kết
Công ty Cổ phần Bao bì Tiền Phong | Công ty liên kết
Công ty TNHH Liên doanh Nhựa Tiền Phong - SMP | Công ty liên doanh
Công ty TNHH Thương mại Xuất nhập khẩu Minh Hải | Công ty liên quan khác
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
Trong năm, Công ty có các giao dịch chủ yếu với các bên liên quan như sau:
 | Năm nayVND | Năm trướcVND
Công ty Cổ phần Nhựa Thiểu niên Tiền Phong phía Nam | 301.063.347.138 | 195.914.529.480
Công ty TNHH Liên doanh Nhựa Tiền Phong - SMP | - | 2.257.132.201
Công ty TNHH Thương mại Xuất nhập khẩu Minh Hải | 960.703.110.883 | 905.345.844.335
Công ty Cổ phần Nhựa Thiểu niên Tiền Phong phía Nam | 373.789.161.597 | 192.228.148.045
Công ty Cổ phần Bao bì Tiền Phong | 28.243.920.029 | 10.915.966.390
Số dư chủ yếu với các bên liên quan tại ngày kết thúc năm tài chính như sau:
 | Số cuối nămVND | Số đầu nămVND
Công ty TNHH Thương mại Xuất nhập khẩu Minh Hải | 362.096.709.434 | 326.248.971.780
Công ty Cổ phần Nhựa Thiểu niên Tiền Phong phía Nam | 137.581.432.221 | 120.854.956.925
Công ty Cổ phần Bao bì Tiền Phong | 15.461.572.866 | 15.461.572.866
Công ty Cổ phần Bao bì Tiền Phong | 1.489.420.240 | 1.166.874.225
Thu nhập của Hội đồng Quản trị và Ban Tổng Giám đốc được hưởng trong năm như sau:
Năm nay | Năm trước
VND | VND
Thu nhập của Hội đồng Quản trị và Ban Tổng Giám đốc | 22.390.956.956 | 22.901.026.517
>>>

Danh sách biến được phép dùng:
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến related_party_disclosed. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-014 · P17-NTP17-related_party

allowed_vars (12): `short_term_receivables, receivables_customers, prepaid_to_suppliers, total_assets, payables_suppliers, equity, revenue, cogs, net_income, cfo, related_party_disclosed, market_cap`  
must_reference: `related_party_disclosed`  
context_source: `data/sample/raw/ocr_results/NTP/2017/NTP_Baocaotaichinh_2017_Kiemtoan_Hopnhat/NTP_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1227-L1253`

````text
Doanh nghiệp: NTP - sản xuất công nghiệp (nhựa), sàn HNX.
Chủ đề: giao dịch và số dư với các bên liên quan.

Trích thuyết minh báo cáo tài chính năm 2017 của NTP (mục 30. NGHIỆP VỤ VÀ SỐ DỰ VỚI CÁC BÊN LIÊN QUAN):
<<<
30. NGHIỆP VỤ VÀ SỐ DỰ VỚI CÁC BÊN LIÊN QUAN
Danh sách các bên liên quan có giao dịch và số dư chủ yếu trong năm:
Bên liên quan | Môi quan hệ
Công ty Cổ phần Nhựa Thiếu niên Tiền Phong phía Nam | Công ty liên kết
Công ty Cổ phần Bao bì Tiền Phong | Công ty liên kết
Công ty TNHH Liên doanh Nhựa Tiền Phong - SMP | Công ty liên doanh
Công ty TNHH Thương mại Xuất nhập khẩu Minh Hải | Công ty liên quan khác
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
Trong năm, Công ty có các giao dịch chủ yếu với các bên liên quan như sau:
 | Năm nayVND | Năm trướcVND
Công ty Cổ phần Nhựa Thiểu niên Tiền Phong phía Nam | 301.063.347.138 | 195.914.529.480
Công ty TNHH Liên doanh Nhựa Tiền Phong - SMP | - | 2.257.132.201
Công ty TNHH Thương mại Xuất nhập khẩu Minh Hải | 960.703.110.883 | 905.345.844.335
Công ty Cổ phần Nhựa Thiểu niên Tiền Phong phía Nam | 373.789.161.597 | 192.228.148.045
Công ty Cổ phần Bao bì Tiền Phong | 28.243.920.029 | 10.915.966.390
Số dư chủ yếu với các bên liên quan tại ngày kết thúc năm tài chính như sau:
 | Số cuối nămVND | Số đầu nămVND
Công ty TNHH Thương mại Xuất nhập khẩu Minh Hải | 362.096.709.434 | 326.248.971.780
Công ty Cổ phần Nhựa Thiểu niên Tiền Phong phía Nam | 137.581.432.221 | 120.854.956.925
Công ty Cổ phần Bao bì Tiền Phong | 15.461.572.866 | 15.461.572.866
Công ty Cổ phần Bao bì Tiền Phong | 1.489.420.240 | 1.166.874.225
Thu nhập của Hội đồng Quản trị và Ban Tổng Giám đốc được hưởng trong năm như sau:
Năm nay | Năm trước
VND | VND
Thu nhập của Hội đồng Quản trị và Ban Tổng Giám đốc | 22.390.956.956 | 22.901.026.517
>>>

Danh sách biến được phép dùng:
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến related_party_disclosed. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}},
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Doanh nghiệp mở rộng tài sản quá nhanh thường có lợi suất sau đó thấp hơn (Cooper, Gulen, Schill 2008).", "source": {"type": "line_item", "ref": "total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-018 · P18-MWG24-related_party

allowed_vars (12): `short_term_receivables, receivables_customers, prepaid_to_suppliers, total_assets, payables_suppliers, equity, revenue, cogs, net_income, cfo, related_party_disclosed, market_cap`  
must_reference: `related_party_disclosed`  
context_source: `data/sample/raw/ocr_results/MWG/2024/MWG_Baocaotaichinh_2024_Kiemtoan_Hopnhat/MWG_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1197-L1211;data/sample/raw/ocr_results/MWG/2024/MWG_Baocaotaichinh_2024_Kiemtoan_Hopnhat/MWG_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L734-L736`

````text
Doanh nghiệp: MWG - bán lẻ - tiêu dùng (bán lẻ), sàn HOSE.
Chủ đề: giao dịch và số dư với các bên liên quan.

Trích thuyết minh báo cáo tài chính năm 2024 của MWG (mục 33. NGHIỆP VỤ VỚI CÁC BÊN LIÊN QUAN):
<<<
33. NGHIỆP VỤ VỚI CÁC BÊN LIÊN QUAN
Danh sách các bên liên quan có quan hệ kiểm soát với Tập đoàn trong năm và tại ngày 31 tháng 12 năm 2024 như sau:
Bên liên quan | Mối quan hệ
PT Era Blu ElektronikÔng Nguyễn Đức TàiÔng Trần Huy Thanh TùngÔng Đặng Minh LượngÔng Đoàn Văn Hiểu EmÔng Thomas LanyiÔng Robert WillettÔng Đào Thế VinhÔng Nguyễn Tiến TrungÔng Đỗ Tiến SĩÔng Vũ Đăng Linh | Công ty liên doanhChủ tịch HĐQTThành viên HĐQT và Tổng Giám đốcThành viên HĐQTThành viên HĐQTThành viên HĐQT Thành viên HĐQT và Thành viên Ủy ban Kiểm toánThành viên HĐQT vàChủ tịch Ủy ban Kiểm toánThành viên HĐQTT giám đốc Tài chính
Các giao dịch trọng yếu của Công ty với các bên liên quan trong năm nay bao gồm:
Bên liên quan | Nội dung nghiệp vụ | Năm nay | VNDNăm trước
Ông Robert Willett | Chi phí tư vấn | 2.351.671.475 | 2.250.010.657
Thu nhập của các thành viên của Hội đồng Quản trị và Tổng Giám đốc:
Tên | Chức vụ | Năm nay | VNDNăm trước
Đăng Minh Lương (*) | Thành viên HĐQT | 870.808.333 | 686.250.000
Nguyễn Đức Tài (*) | Chủ tịch HĐQT | - | 230.080.000
Đoàn Văn Hiểu Em (*) | Thành viên HĐQT |  | 584.280.000
Trần Huy Thanh Tùng (*) | Thành viên HĐQT |  | 
 | và Tổng Giám đốc | - | 164.580.000
TỔNG CỘNG |  | 870.808.333 | 1.665.190.000
(*) Thu nhập từ tiền lương được trả từ Công ty Cổ phần Thế Giới Di Đông (Công ty con).

3.21 Các bên liên quan
Các bên được coi là bên liên quan của Nhóm Công ty nếu một bên có khả năng, trực tiếp hoặc gián tiếp, kiểm soát bên kia hoặc gây ảnh hưởng đáng kể tới bên kia trong việc ra các quyết định tài chính và hoạt động, hoặc khi Nhóm Công ty và bên kia cùng chịu sự kiểm soát chung hoặc ảnh hưởng đáng kể chung. Các bên liên quan có thể là các công ty hoặc các cá nhân, bao gồm các thành viên mật thiết trong gia đình mật thiết của các cá nhân được coi là liên quan.
>>>

Danh sách biến được phép dùng:
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến related_party_disclosed. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-011 · P18-MWG24-related_party

allowed_vars (12): `short_term_receivables, receivables_customers, prepaid_to_suppliers, total_assets, payables_suppliers, equity, revenue, cogs, net_income, cfo, related_party_disclosed, market_cap`  
must_reference: `related_party_disclosed`  
context_source: `-`

````text
Doanh nghiệp: MWG - bán lẻ - tiêu dùng (bán lẻ), sàn HOSE.
Chủ đề: giao dịch và số dư với các bên liên quan.

Danh sách biến được phép dùng:
- short_term_receivables: Các khoản phải thu ngắn hạn [VND, số dư cuối kỳ]
- receivables_customers: Phải thu ngắn hạn của khách hàng [VND, số dư cuối kỳ]
- prepaid_to_suppliers: Trả trước cho người bán ngắn hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- payables_suppliers: Phải trả người bán ngắn hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến related_party_disclosed.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-013 · P19-GAS17-commitments

allowed_vars (12): `cash_and_equivalents, construction_in_progress, total_assets, total_liabilities, long_term_debt, equity, revenue, net_income, cfo, capex, contingent_liabilities_disclosed, market_cap`  
must_reference: `contingent_liabilities_disclosed`  
context_source: `-`

````text
Doanh nghiệp: GAS - tiện ích - năng lượng (khí), sàn HOSE.
Chủ đề: cam kết, nợ tiềm tàng và khoản mục ngoài bảng.

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến contingent_liabilities_disclosed.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-019 · P19-GAS17-commitments

allowed_vars (12): `cash_and_equivalents, construction_in_progress, total_assets, total_liabilities, long_term_debt, equity, revenue, net_income, cfo, capex, contingent_liabilities_disclosed, market_cap`  
must_reference: `contingent_liabilities_disclosed`  
context_source: `data/sample/raw/ocr_results/GAS/2017/GAS_Baocaotaichinh_2017_Kiemtoan_Hopnhat/GAS_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1186-L1213`

````text
Doanh nghiệp: GAS - tiện ích - năng lượng (khí), sàn HOSE.
Chủ đề: cam kết, nợ tiềm tàng và khoản mục ngoài bảng.

Trích thuyết minh báo cáo tài chính năm 2017 của GAS (mục 39. CÁC KHOÀN CAM KẾT):
<<<
39. CÁC KHOÀN CAM KẾT
(i) Cam kết vốn
Tại ngày 31 tháng 12 năm 2017, Tổng Công ty có các khoản cam kết vốn liên quan tối một số dự án đầu tư xây dựng cơ bản lớn đang thực hiện chưa hoàn thành sau:
Số cuối năm | Số đầu năm
VND | VND
Kho cảng nhập khẩu LNG Sơn Mỹ | 33.502.059.832.769 | 33.583.719.522.095
Kho chứa LNG quy mô 1 triệu tấn/năm tại Thị Vải | 5.491.709.929.040 | 5.505.235.066.160
Nhà máy xử lý khí Cà Mau | 5.068.782.115.916 | 7.339.317.320.149
Dự án thu gom và phân phối khí mô Cá Rồng Đỏ | 4.046.601.152.024 | 4.079.833.332.262
Đường ống dẫn khí Nam Côn Sơn 2 | 2.537.476.166.684 | 2.559.903.218.466
Hệ thống cung cấp khí khu vực Long Thành, Đồng Nai | 257.061.143.810 | -
Hệ thống cấp khí cho Công ty TNHH Intermalt Việt Nam | - | 59.779.977.489
Khác | - | 41.888.125.812
 | 50.903.690.340.243 | 53.169.676.562.433
(ii) Cam kết khác
Các khoản cam kết liên quan đến hoạt động kinh doanh và vận chuyển khí:
Cam kết mua hàng
Cam kết mua hàng | Sản lượng cam kết | Thời gian cam kết
Cam kết mua khí từ chủ khí Lô 06.1 | Tôi thiếu là 2,7 tỷ m3/năm | Đến hết giai đoạn bình ổn của Lô 06.1
Cam kết mua khí từ chủ khí Lô 11.2 | Tôi thiếu là 1,216 tỷ m3/năm | Đến hết giai đoạn bình ổn của Lô 11.2
Cam kết mua khí từ chủ khí Lô 05.3 và 05.2 | Tôi thiếu 1,368 tỷ m3/năm | Đến hết giai đoạn bình ổn của Lô 05-2 và Lô 05-3
Cam kết mua khí từ chủ khí Lô 102 và 106 | Tôi thiếu 204 triệu m3/năm | Đến hết giai đoạn bình ổn của Lô 102 và Lô 106
Cam kết bán hàng
Cam kết bán hàng | Sản lượng cam kết | Thời gian cam kết
Bán khí Nam Côn Sơn cho Tập đoàn Điện lực Việt Nam | Tôi thiếu hàng năm là 1,85 tỷ m3 | Trong giai đoạn bình ổn theo hợp đồng GSA
Bán khí Nam Côn Sơn cho Công ty TNHH Phú Mỹ 3 BOT Power (PM3 BOT) | Tôi thiếu hàng năm là 0,85 tỷ m3 | Đến năm 2023
Bán khí Nam Côn Sơn cho Công ty TNHH Năng lượng Mekong (PM 2.2 BOT) | Tôi thiếu hàng năm là 0,85 tỷ m3 | Đến năm 2024
Bán khí Nam Côn Sơn cho Tổng Công ty Điện lực Dầu khí Việt Nam | Tôi thiếu hàng năm là 0,447 tỷ m3 | Trong giai đoạn bình ổn theo Hợp đồng
Bán khí Nam Côn Sơn cho Công ty Cổ Phăn Điện Lực Dầu Khí Nhơn Trạch 2 | Tôi thiếu hàng năm là 0,785 tỷ m3 | Đến năm 2036
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến contingent_liabilities_disclosed. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-015 · P19-GAS17-commitments

allowed_vars (12): `cash_and_equivalents, construction_in_progress, total_assets, total_liabilities, long_term_debt, equity, revenue, net_income, cfo, capex, contingent_liabilities_disclosed, market_cap`  
must_reference: `contingent_liabilities_disclosed`  
context_source: `data/sample/raw/ocr_results/GAS/2017/GAS_Baocaotaichinh_2017_Kiemtoan_Hopnhat/GAS_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1186-L1213`

````text
Doanh nghiệp: GAS - tiện ích - năng lượng (khí), sàn HOSE.
Chủ đề: cam kết, nợ tiềm tàng và khoản mục ngoài bảng.

Trích thuyết minh báo cáo tài chính năm 2017 của GAS (mục 39. CÁC KHOÀN CAM KẾT):
<<<
39. CÁC KHOÀN CAM KẾT
(i) Cam kết vốn
Tại ngày 31 tháng 12 năm 2017, Tổng Công ty có các khoản cam kết vốn liên quan tối một số dự án đầu tư xây dựng cơ bản lớn đang thực hiện chưa hoàn thành sau:
Số cuối năm | Số đầu năm
VND | VND
Kho cảng nhập khẩu LNG Sơn Mỹ | 33.502.059.832.769 | 33.583.719.522.095
Kho chứa LNG quy mô 1 triệu tấn/năm tại Thị Vải | 5.491.709.929.040 | 5.505.235.066.160
Nhà máy xử lý khí Cà Mau | 5.068.782.115.916 | 7.339.317.320.149
Dự án thu gom và phân phối khí mô Cá Rồng Đỏ | 4.046.601.152.024 | 4.079.833.332.262
Đường ống dẫn khí Nam Côn Sơn 2 | 2.537.476.166.684 | 2.559.903.218.466
Hệ thống cung cấp khí khu vực Long Thành, Đồng Nai | 257.061.143.810 | -
Hệ thống cấp khí cho Công ty TNHH Intermalt Việt Nam | - | 59.779.977.489
Khác | - | 41.888.125.812
 | 50.903.690.340.243 | 53.169.676.562.433
(ii) Cam kết khác
Các khoản cam kết liên quan đến hoạt động kinh doanh và vận chuyển khí:
Cam kết mua hàng
Cam kết mua hàng | Sản lượng cam kết | Thời gian cam kết
Cam kết mua khí từ chủ khí Lô 06.1 | Tôi thiếu là 2,7 tỷ m3/năm | Đến hết giai đoạn bình ổn của Lô 06.1
Cam kết mua khí từ chủ khí Lô 11.2 | Tôi thiếu là 1,216 tỷ m3/năm | Đến hết giai đoạn bình ổn của Lô 11.2
Cam kết mua khí từ chủ khí Lô 05.3 và 05.2 | Tôi thiếu 1,368 tỷ m3/năm | Đến hết giai đoạn bình ổn của Lô 05-2 và Lô 05-3
Cam kết mua khí từ chủ khí Lô 102 và 106 | Tôi thiếu 204 triệu m3/năm | Đến hết giai đoạn bình ổn của Lô 102 và Lô 106
Cam kết bán hàng
Cam kết bán hàng | Sản lượng cam kết | Thời gian cam kết
Bán khí Nam Côn Sơn cho Tập đoàn Điện lực Việt Nam | Tôi thiếu hàng năm là 1,85 tỷ m3 | Trong giai đoạn bình ổn theo hợp đồng GSA
Bán khí Nam Côn Sơn cho Công ty TNHH Phú Mỹ 3 BOT Power (PM3 BOT) | Tôi thiếu hàng năm là 0,85 tỷ m3 | Đến năm 2023
Bán khí Nam Côn Sơn cho Công ty TNHH Năng lượng Mekong (PM 2.2 BOT) | Tôi thiếu hàng năm là 0,85 tỷ m3 | Đến năm 2024
Bán khí Nam Côn Sơn cho Tổng Công ty Điện lực Dầu khí Việt Nam | Tôi thiếu hàng năm là 0,447 tỷ m3 | Trong giai đoạn bình ổn theo Hợp đồng
Bán khí Nam Côn Sơn cho Công ty Cổ Phăn Điện Lực Dầu Khí Nhơn Trạch 2 | Tôi thiếu hàng năm là 0,785 tỷ m3 | Đến năm 2036
>>>

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến contingent_liabilities_disclosed. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}},
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Doanh nghiệp mở rộng tài sản quá nhanh thường có lợi suất sau đó thấp hơn (Cooper, Gulen, Schill 2008).", "source": {"type": "line_item", "ref": "total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-012 · P19-GAS17-commitments

allowed_vars (12): `cash_and_equivalents, construction_in_progress, total_assets, total_liabilities, long_term_debt, equity, revenue, net_income, cfo, capex, contingent_liabilities_disclosed, market_cap`  
must_reference: `contingent_liabilities_disclosed`  
context_source: `-`

````text
Doanh nghiệp: GAS - tiện ích - năng lượng (khí), sàn HOSE.
Chủ đề: cam kết, nợ tiềm tàng và khoản mục ngoài bảng.

Danh sách biến được phép dùng:
- cash_and_equivalents: Tiền và các khoản tương đương tiền [VND, số dư cuối kỳ]
- construction_in_progress: Tài sản dở dang dài hạn [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- total_liabilities: NỢ PHẢI TRẢ [VND, số dư cuối kỳ]
- long_term_debt: Vay và nợ thuê tài chính dài hạn [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- capex: Tiền chi mua sắm, xây dựng TSCĐ và tài sản dài hạn khác [VND, phát sinh trong kỳ, ghi số âm]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến contingent_liabilities_disclosed.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-014 · P20-VNM24-segment

allowed_vars (13): `long_term_assets, total_assets, equity, gross_revenue, revenue, cogs, gross_profit, selling_expense, admin_expense, operating_profit, net_income, segment_disclosed, market_cap`  
must_reference: `gross_profit`  
context_source: `-`

````text
Doanh nghiệp: VNM - bán lẻ - tiêu dùng (sữa), sàn HOSE.
Chủ đề: cơ cấu doanh thu và lợi nhuận theo bộ phận.

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- gross_revenue: Doanh thu bán hàng và cung cấp dịch vụ [VND, phát sinh trong kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- selling_expense: Chi phí bán hàng [VND, phát sinh trong kỳ]
- admin_expense: Chi phí quản lý doanh nghiệp [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- segment_disclosed: Có thuyết minh bộ phận theo lĩnh vực hoặc khu vực [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến gross_profit.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-020 · P20-VNM24-segment

allowed_vars (13): `long_term_assets, total_assets, equity, gross_revenue, revenue, cogs, gross_profit, selling_expense, admin_expense, operating_profit, net_income, segment_disclosed, market_cap`  
must_reference: `gross_profit`  
context_source: `data/sample/raw/ocr_results/VNM/2024/VNM_Baocaotaichinh_2024_Kiemtoan_Hopnhat/VNM_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L2092-L2116;data/sample/raw/ocr_results/VNM/2024/VNM_Baocaotaichinh_2024_Kiemtoan_Hopnhat/VNM_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1274-L1276`

````text
Doanh nghiệp: VNM - bán lẻ - tiêu dùng (sữa), sàn HOSE.
Chủ đề: cơ cấu doanh thu và lợi nhuận theo bộ phận.

Trích thuyết minh báo cáo tài chính năm 2024 của VNM (mục 2. Báo cáo bộ phận):
<<<
2. Báo cáo bộ phận
Thông tin bộ phận được trình bày theo bộ phận chính yếu của Tập đoàn là bộ phận chia theo khu vực địa lý.
Kết quả của bộ phận bao gồm các khoản mục phân bổ trực tiếp cho một bộ phận cũng như phân bổ cho các bộ phận theo một cơ sở hợp lý. Các khoản mục không được phân bổ bao gồm tài sản và nợ phải trả, doanh thu hoạt động tài chính và chi phí tài chính, chi phí bán hàng và chi phí quản lý doanh nghiệp, lợi nhuận và lỗ khác, và thuế thu nhập doanh nghiệp.
Bộ phận theo khu vực địa lý
Khi trình bày thông tin bộ phận theo khu vực địa lý, doanh thu của bộ phận được trình bày dựa vào vị trí địa lý của khách hàng tại Việt Nam (“Trong nước”) hay ở các nước khác Việt Nam (“Nước ngoài”). Tài sản bộ phận và chi tiêu vốn không được trình bày do vị trí của tài sản và cơ sở sản xuất chủ yếu là ở Việt Nam.
2024VND | 2023VND | 2024VND | 2023VND | 2024VND | 2023VND
Doanh thu thuầnGiá vốn hàng bán vàdịch vụ cung cấp | 50.799.361.377.927(29.824.520.360.949) | 50.617.453.566.955(29.723.643.941.157) | 10.983.248.150.518(6.367.912.844.372) | 9.751.461.944.550(6.100.539.954.938) | 61.782.609.528.445(36.192.433.205.321) | 60.368.915.511.505(35.824.183.896.095)
Lợi nhuận gộptheo bộ phận | 20.974.841.016.978 | 20.893.809.625.798 | 4.615.335.306.146 | 3.650.921.989.612 | 25.590.176.323.124 | 24.544.731.615.410
Giám đốc Điều hành Tài chính

26. Báo cáo bộ phận
Một bộ phận là một hợp phần có thể xác định riêng biệt của Tập đoàn tham gia vào việc cung cấp các sản phẩm hoặc dịch vụ liên quan (bộ phận chia theo hoạt động kinh doanh), hoặc cung cấp sản phẩm hoặc dịch vụ trong một môi trường kinh tế cụ thể (bộ phận chia theo khu vực địa lý), mỗi bộ phận này chịu rủi ro và thu được lợi ích khác biệt với các bộ phận khác. Mẫu báo cáo bộ phận chính yếu của Tập đoàn là dựa theo bộ phận chia theo khu vực địa lý.
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- gross_revenue: Doanh thu bán hàng và cung cấp dịch vụ [VND, phát sinh trong kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- selling_expense: Chi phí bán hàng [VND, phát sinh trong kỳ]
- admin_expense: Chi phí quản lý doanh nghiệp [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- segment_disclosed: Có thuyết minh bộ phận theo lĩnh vực hoặc khu vực [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến gross_profit. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-016 · P20-VNM24-segment

allowed_vars (13): `long_term_assets, total_assets, equity, gross_revenue, revenue, cogs, gross_profit, selling_expense, admin_expense, operating_profit, net_income, segment_disclosed, market_cap`  
must_reference: `gross_profit`  
context_source: `data/sample/raw/ocr_results/VNM/2024/VNM_Baocaotaichinh_2024_Kiemtoan_Hopnhat/VNM_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L2092-L2116;data/sample/raw/ocr_results/VNM/2024/VNM_Baocaotaichinh_2024_Kiemtoan_Hopnhat/VNM_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1274-L1276`

````text
Doanh nghiệp: VNM - bán lẻ - tiêu dùng (sữa), sàn HOSE.
Chủ đề: cơ cấu doanh thu và lợi nhuận theo bộ phận.

Trích thuyết minh báo cáo tài chính năm 2024 của VNM (mục 2. Báo cáo bộ phận):
<<<
2. Báo cáo bộ phận
Thông tin bộ phận được trình bày theo bộ phận chính yếu của Tập đoàn là bộ phận chia theo khu vực địa lý.
Kết quả của bộ phận bao gồm các khoản mục phân bổ trực tiếp cho một bộ phận cũng như phân bổ cho các bộ phận theo một cơ sở hợp lý. Các khoản mục không được phân bổ bao gồm tài sản và nợ phải trả, doanh thu hoạt động tài chính và chi phí tài chính, chi phí bán hàng và chi phí quản lý doanh nghiệp, lợi nhuận và lỗ khác, và thuế thu nhập doanh nghiệp.
Bộ phận theo khu vực địa lý
Khi trình bày thông tin bộ phận theo khu vực địa lý, doanh thu của bộ phận được trình bày dựa vào vị trí địa lý của khách hàng tại Việt Nam (“Trong nước”) hay ở các nước khác Việt Nam (“Nước ngoài”). Tài sản bộ phận và chi tiêu vốn không được trình bày do vị trí của tài sản và cơ sở sản xuất chủ yếu là ở Việt Nam.
2024VND | 2023VND | 2024VND | 2023VND | 2024VND | 2023VND
Doanh thu thuầnGiá vốn hàng bán vàdịch vụ cung cấp | 50.799.361.377.927(29.824.520.360.949) | 50.617.453.566.955(29.723.643.941.157) | 10.983.248.150.518(6.367.912.844.372) | 9.751.461.944.550(6.100.539.954.938) | 61.782.609.528.445(36.192.433.205.321) | 60.368.915.511.505(35.824.183.896.095)
Lợi nhuận gộptheo bộ phận | 20.974.841.016.978 | 20.893.809.625.798 | 4.615.335.306.146 | 3.650.921.989.612 | 25.590.176.323.124 | 24.544.731.615.410
Giám đốc Điều hành Tài chính

26. Báo cáo bộ phận
Một bộ phận là một hợp phần có thể xác định riêng biệt của Tập đoàn tham gia vào việc cung cấp các sản phẩm hoặc dịch vụ liên quan (bộ phận chia theo hoạt động kinh doanh), hoặc cung cấp sản phẩm hoặc dịch vụ trong một môi trường kinh tế cụ thể (bộ phận chia theo khu vực địa lý), mỗi bộ phận này chịu rủi ro và thu được lợi ích khác biệt với các bộ phận khác. Mẫu báo cáo bộ phận chính yếu của Tập đoàn là dựa theo bộ phận chia theo khu vực địa lý.
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- gross_revenue: Doanh thu bán hàng và cung cấp dịch vụ [VND, phát sinh trong kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- selling_expense: Chi phí bán hàng [VND, phát sinh trong kỳ]
- admin_expense: Chi phí quản lý doanh nghiệp [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- segment_disclosed: Có thuyết minh bộ phận theo lĩnh vực hoặc khu vực [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến gross_profit. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "sga_intensity", "formula": "safe_div(selling_expense + admin_expense, gross_revenue)", "rationale": "Chi phí bán hàng và quản lý trên doanh thu cao làm biên lợi nhuận nhạy với biến động doanh số.", "source": {"type": "line_item", "ref": "selling_expense, admin_expense, gross_revenue"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}},
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Doanh nghiệp mở rộng tài sản quá nhanh thường có lợi suất sau đó thấp hơn (Cooper, Gulen, Schill 2008).", "source": {"type": "line_item", "ref": "total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-021 · P21-PC124-segment

allowed_vars (13): `long_term_assets, total_assets, equity, gross_revenue, revenue, cogs, gross_profit, selling_expense, admin_expense, operating_profit, net_income, segment_disclosed, market_cap`  
must_reference: `gross_profit`  
context_source: `data/sample/raw/ocr_results/PC1/2024/PC1_Baocaotaichinh_2024_Kiemtoan_Hopnhat/PC1_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L998-L1071`

````text
Doanh nghiệp: PC1 - xây dựng - vật liệu (xây lắp điện + thuỷ điện), sàn HOSE.
Chủ đề: cơ cấu doanh thu và lợi nhuận theo bộ phận.

Trích thuyết minh báo cáo tài chính năm 2024 của PC1 (mục 5. Báo cáo bộ phận):
<<<
5. Báo cáo bộ phận
(a) Bộ phận chia theo hoạt động kinh doanh
Một bộ phận là một hợp phần có thể xác định riêng biệt của Tập đoàn tham gia vào việc cung cấp các sản phẩm hoặc dịch vụ liên quan (bộ phận chia theo hoạt động kinh doanh), hoặc cung cấp sản phẩm hoặc dịch vụ trong một môi trường kinh tế cụ thể (bộ phận chia theo vùng địa lý), mỗi bộ phận này chịu rủi ro và thu được lợi ích khác biệt với các bộ phận khác. Doanh thu, chi phí và kết quả kinh doanh của các bộ phận bao gồm các giao dịch giữa các bộ phận, các giao dịch giữa các bộ phận này được loại trừ khi lập báo cáo tài chính hợp nhất. Tập đoàn có các bộ phận chia theo hoạt động kinh doanh chính như sau:
- Xây lắp và xây dựng;
- Sản xuất công nghiệp;
• Bất động sản;
- Khai thác, vận hành khu công nghiệp;
- Khai khoáng; và
• Các hoạt động khác.
 | Xây lắp và xây dựng VND | Sản xuất công nghiệp VND | Bắt động sản VND | Năng lượng VND | Thương mại VND | Khai thác, vận hành Khu Công nghiệp VND | Khai khoáng VND | Các hoạt động khác VND | Loại trừ VND | Hợp nhất VND
Doanh thu hợp nhất của bộ phận | 5.285.078.775.132 | 1.581.906.381.343 | 44.268.528.613 | 1.793.512.897.375 | 963.624.187.857 | 599.664.683.839 | 2.977.772.087.865 | 117.846.878.266 | (3.274.772.799.671) | 10.088.901.620.619
Giá vốn hàng bán bộ phân | (5.041.373.321.868) | (1.428.042.082.448) | (23.405.763.259) | (854.536.585.123) | (952.021.397.380) | (450.850.045.824) | (2.367.570.349.563) | (107.936.778.887) | 3.229.229.304.724 | (7.996.507.019.628)
Kết quả kinh doanh của bộ phân | 243.705.453.264 | 153.864.298.895 | 20.862.765.354 | 938.976.312.252 | 11.602.790.477 | 148.814.638.015 | 610.201.738.302 | 9.910.099.379 | (45.543.494.947) | 2.092.394.600.991
(78.532.757.514)
(487.725.540.156)
138.085.670.369
(881.568.197.542)
45.794.608.983
10.562.245.682
(129.035.237.083)
709.975.393.730
 | Xây lắp và xây dựng VND | Sản xuất công nghiệp VND | Bắt động sản VND | Năng lượng VND | Thương mại VND | Khai thác, vận hành Khu Công nghiệp VND | Khai khoáng VND Đã điều chỉnh lại | Các hoạt động khác VND | Loại trừ VND | Hợp nhất VND Đã điều chỉnh lại
Doanh thu hợp nhất của bộ phận | 3.828.968.348.359 | 1.218.148.180.352 | 192.537.977.998 | 1.532.041.358.298 | 1.042.889.712.645 | 614.102.201.835 | 1.297.936.440.269 | 164.182.450.358 | (2.197.025.607.450) | 7.693.781.062.664
Giá vốn hàng bán bộ phận | (3.595.376.108.331) | (1.088.309.973.617) | (143.827.157.734) | (804.734.609.638) | (1.024.318.503.004) | (475.527.762.175) | (1.176.869.402.638) | (127.032.116.211) | 2.190.380.659.834 | (6.245.614.973.514)
Kết quả kinh doanh của bộ phận | 233.592.240.028 | 129.838.206.735 | 48.710.820.264 | 727.306.748.660 | 18.571.209.641 | 138.574.439.660 | 121.067.037.631 | 37.150.334.147 | (6.644.947.616) | 1.448.166.089.150
(55.980.734.072)
(335.208.954.077)
182.694.013.188
(967.330.851.856)
1.577.383.209
(17.937.240.869)
(74.349.782.578)
181.629.922.095
\( \therefore {AO} = 3,{BN} = 2\left( {{AD} - {AB}}\right) \)
 | Xây lắp và xây dựng VND | Sản xuất công nghiệp VND | Bất động sản VND | Năng lượng VND | Thương mại VND | Khai thác, vận hành Khu Công nghiệp VND | Khai khoáng VND | Các hoạt động khác VND | Hợp nhất VND
Tải sản của bộ phận Tài sản không phân bổ | 1.902.631.794.913 | 723.731.548.075 | 1.309.608.304.859 | 9.008.063.060.286 | 241.386.683.338 | 1.399.100.103.337 | 2.170.526.667.505 | 27.819.880.071 | 16.782.868.042.3844.204.776.698.744
>>>

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- gross_revenue: Doanh thu bán hàng và cung cấp dịch vụ [VND, phát sinh trong kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- selling_expense: Chi phí bán hàng [VND, phát sinh trong kỳ]
- admin_expense: Chi phí quản lý doanh nghiệp [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- segment_disclosed: Có thuyết minh bộ phận theo lĩnh vực hoặc khu vực [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến gross_profit. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-013 · P21-PC124-segment

allowed_vars (13): `long_term_assets, total_assets, equity, gross_revenue, revenue, cogs, gross_profit, selling_expense, admin_expense, operating_profit, net_income, segment_disclosed, market_cap`  
must_reference: `gross_profit`  
context_source: `-`

````text
Doanh nghiệp: PC1 - xây dựng - vật liệu (xây lắp điện + thuỷ điện), sàn HOSE.
Chủ đề: cơ cấu doanh thu và lợi nhuận theo bộ phận.

Danh sách biến được phép dùng:
- long_term_assets: TÀI SẢN DÀI HẠN [VND, số dư cuối kỳ]
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- gross_revenue: Doanh thu bán hàng và cung cấp dịch vụ [VND, phát sinh trong kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- cogs: Giá vốn hàng bán [VND, phát sinh trong kỳ]
- gross_profit: Lợi nhuận gộp [VND, phát sinh trong kỳ]
- selling_expense: Chi phí bán hàng [VND, phát sinh trong kỳ]
- admin_expense: Chi phí quản lý doanh nghiệp [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- segment_disclosed: Có thuyết minh bộ phận theo lĩnh vực hoặc khu vực [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến gross_profit.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F2-022 · P22-PNJ17-tax

allowed_vars (12): `total_assets, equity, retained_earnings, revenue, operating_profit, other_income, pretax_profit, current_tax_expense, net_income, depreciation, cfo, market_cap`  
must_reference: `current_tax_expense`  
context_source: `data/sample/raw/ocr_results/PNJ/2017/PNJ_Baocaotaichinh_2017_Kiemtoan_Hopnhat/PNJ_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1041-L1052`

````text
Doanh nghiệp: PNJ - bán lẻ - tiêu dùng (bán lẻ trang sức), sàn HOSE.
Chủ đề: thuế thu nhập doanh nghiệp và chất lượng lợi nhuận.

Trích thuyết minh báo cáo tài chính năm 2017 của PNJ (mục 33. CHI PHÍ THUÊ THU NHẬP DOANH NGHIỆP HIỆN HÀNH):
<<<
33. CHI PHÍ THUÊ THU NHẬP DOANH NGHIỆP HIỆN HÀNH
 | Năm nayVND | Năm trướcVND
Chi phí thuế thu nhập doanh nghiệp tính trên thu nhập tính thuế năm hiện hành | 182.004.938.247 | 139.964.060.336
Điều chỉnh chi phí thuế thu nhập doanh nghiệp của các năm trước vào chi phí thuế thu nhập hiện hành năm nay | 33.945.000 | -
 | 182.038.883.247 | 139.964.060.336
Chi phí thuế thu nhập doanh nghiệp hoãn lại phát sinh từ các khoản chênh lệch tạm thời phải tính thuế | 484.064.550 | 175.856.983
 | 484.064.550 | 175.856.983
Công ty có nghĩa vụ nộp thuê thu nhập doanh nghiệp theo tỷ lệ 20% (2016:20%) trên thu nhập tính thuế.
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □
>>>

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- retained_earnings: Lợi nhuận sau thuế chưa phân phối [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- other_income: Thu nhập khác [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- current_tax_expense: Chi phí thuế TNDN hiện hành [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến current_tax_expense. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-017 · P22-PNJ17-tax

allowed_vars (12): `total_assets, equity, retained_earnings, revenue, operating_profit, other_income, pretax_profit, current_tax_expense, net_income, depreciation, cfo, market_cap`  
must_reference: `current_tax_expense`  
context_source: `data/sample/raw/ocr_results/PNJ/2017/PNJ_Baocaotaichinh_2017_Kiemtoan_Hopnhat/PNJ_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1041-L1052`

````text
Doanh nghiệp: PNJ - bán lẻ - tiêu dùng (bán lẻ trang sức), sàn HOSE.
Chủ đề: thuế thu nhập doanh nghiệp và chất lượng lợi nhuận.

Trích thuyết minh báo cáo tài chính năm 2017 của PNJ (mục 33. CHI PHÍ THUÊ THU NHẬP DOANH NGHIỆP HIỆN HÀNH):
<<<
33. CHI PHÍ THUÊ THU NHẬP DOANH NGHIỆP HIỆN HÀNH
 | Năm nayVND | Năm trướcVND
Chi phí thuế thu nhập doanh nghiệp tính trên thu nhập tính thuế năm hiện hành | 182.004.938.247 | 139.964.060.336
Điều chỉnh chi phí thuế thu nhập doanh nghiệp của các năm trước vào chi phí thuế thu nhập hiện hành năm nay | 33.945.000 | -
 | 182.038.883.247 | 139.964.060.336
Chi phí thuế thu nhập doanh nghiệp hoãn lại phát sinh từ các khoản chênh lệch tạm thời phải tính thuế | 484.064.550 | 175.856.983
 | 484.064.550 | 175.856.983
Công ty có nghĩa vụ nộp thuê thu nhập doanh nghiệp theo tỷ lệ 20% (2016:20%) trên thu nhập tính thuế.
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □
>>>

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- retained_earnings: Lợi nhuận sau thuế chưa phân phối [VND, số dư cuối kỳ]
- revenue: Doanh thu thuần [VND, phát sinh trong kỳ]
- operating_profit: Lợi nhuận thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- other_income: Thu nhập khác [VND, phát sinh trong kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- current_tax_expense: Chi phí thuế TNDN hiện hành [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- depreciation: Khấu hao tài sản cố định [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải dùng biến current_tax_expense. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "other_income_share", "formula": "safe_div(other_income, pretax_profit)", "rationale": "Tỷ trọng thu nhập khác lớn cho thấy lợi nhuận kỳ này có phần không lặp lại.", "source": {"type": "line_item", "ref": "other_income, pretax_profit"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}},
{"name": "earnings_yield", "formula": "safe_div(net_income, market_cap)", "rationale": "Lợi nhuận trên mỗi đồng vốn hoá cao cho thấy cổ phiếu đang rẻ so với khả năng sinh lời.", "source": {"type": "line_item", "ref": "net_income, market_cap"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F1-015 · P23-VCB24-bank_loans

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `-`

````text
Doanh nghiệp: VCB - ngân hàng (ngân hàng quốc doanh), sàn HOSE.
Chủ đề: chất lượng danh mục cho vay và dự phòng rủi ro tín dụng.

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-023 · P23-VCB24-bank_loans

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `data/sample/raw/ocr_results/VCB/2024/VCB_Baocaotaichinh_2024_Kiemtoan_Hopnhat/VCB_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1354-L1377`

````text
Doanh nghiệp: VCB - ngân hàng (ngân hàng quốc doanh), sàn HOSE.
Chủ đề: chất lượng danh mục cho vay và dự phòng rủi ro tín dụng.

Trích thuyết minh báo cáo tài chính năm 2024 của VCB (mục 9. Cho vay khách hàng):
<<<
9. Cho vay khách hàng
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND
Cho vay các tổ chức kinh tế, cá nhân trong nước | 1.436.710.181 | 1.258.418.586
Cho vay chiết khấu công cụ chuyển nhượng và các giấy tờ có giá | 2.831.604 | 3.396.873
Cho thuê tài chính | 7.073.712 | 6.055.394
Các khoản trả thay khách hàng | 1.770.654 | 1.646.618
Cho vay đối với các tổ chức, cá nhân nước ngoài | 812.748 | 841.547
 | 1.449.198.899 | 1.270.359.018
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND(trình bày lại)
Nợ đủ tiêu chuẩn | 1.431.299.668 | 1.252.320.285
Nợ cần chú ý | 3.935.217 | 5.421.319
Nợ dưới tiêu chuẩn | 2.153.039 | 1.821.753
Nợ nghi ngờ | 1.518.558 | 2.819.825
Nợ có khả năng mất vốn | 10.292.417 | 7.975.836
 | 1.449.198.899 | 1.270.359.018
Phân tích dư nợ theo thời hạn cho vay như sau:
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND
Nợ ngắn hạn | 915.576.792 | 790.604.807
Nợ trung hạn | 59.453.709 | 46.175.347
Nợ dài hạn | 474.168.398 | 433.578.864
 | 1.449.198.899 | 1.270.359.018
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND
Doanh nghiệp nhà nước | 96.605.199 | 80.144.585
Công ty trách nhiệm hữu hạn | 227.041.340 | 207.339.020
Doanh nghiệp có vốn đầu tư nước ngoài | 147.778.524 | 109.476.021
Hợp tác xã và công ty tư nhân | 1.371.552 | 1.212.185
Cá nhân và hộ kinh doanh cá thể | 640.003.504 | 566.326.189
Khác | 336.398.780 | 305.861.018
 | 1.449.198.899 | 1.270.359.018
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND
Sản xuất và gia công chế biến | 340.501.488 | 280.386.148
Thương mại, dịch vụ | 214.488.774 | 204.168.323
Xây dựng | 90.512.980 | 81.091.024
Sản xuất và phân phối điện, khí đốt và nước | 65.344.169 | 54.975.004
Nông, lâm, thủy hải sản | 42.722.982 | 38.732.650
Vận tải kho bãi và thông tin liên lạc | 42.626.109 | 33.448.171
Khai khoảng | 26.027.625 | 20.413.414
Nhà hàng, khách sạn | 16.356.618 | 19.622.160
Các ngành khác | 610.618.154 | 537.522.124
 | 1.449.198.899 | 1.270.359.018
\( \therefore y \leq  {a}_{1} + 3\sqrt{2} \)
>>>

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-018 · P23-VCB24-bank_loans

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `data/sample/raw/ocr_results/VCB/2024/VCB_Baocaotaichinh_2024_Kiemtoan_Hopnhat/VCB_Baocaotaichinh_2024_Kiemtoan_Hopnhat_extracted.txt#L1354-L1377`

````text
Doanh nghiệp: VCB - ngân hàng (ngân hàng quốc doanh), sàn HOSE.
Chủ đề: chất lượng danh mục cho vay và dự phòng rủi ro tín dụng.

Trích thuyết minh báo cáo tài chính năm 2024 của VCB (mục 9. Cho vay khách hàng):
<<<
9. Cho vay khách hàng
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND
Cho vay các tổ chức kinh tế, cá nhân trong nước | 1.436.710.181 | 1.258.418.586
Cho vay chiết khấu công cụ chuyển nhượng và các giấy tờ có giá | 2.831.604 | 3.396.873
Cho thuê tài chính | 7.073.712 | 6.055.394
Các khoản trả thay khách hàng | 1.770.654 | 1.646.618
Cho vay đối với các tổ chức, cá nhân nước ngoài | 812.748 | 841.547
 | 1.449.198.899 | 1.270.359.018
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND(trình bày lại)
Nợ đủ tiêu chuẩn | 1.431.299.668 | 1.252.320.285
Nợ cần chú ý | 3.935.217 | 5.421.319
Nợ dưới tiêu chuẩn | 2.153.039 | 1.821.753
Nợ nghi ngờ | 1.518.558 | 2.819.825
Nợ có khả năng mất vốn | 10.292.417 | 7.975.836
 | 1.449.198.899 | 1.270.359.018
Phân tích dư nợ theo thời hạn cho vay như sau:
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND
Nợ ngắn hạn | 915.576.792 | 790.604.807
Nợ trung hạn | 59.453.709 | 46.175.347
Nợ dài hạn | 474.168.398 | 433.578.864
 | 1.449.198.899 | 1.270.359.018
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND
Doanh nghiệp nhà nước | 96.605.199 | 80.144.585
Công ty trách nhiệm hữu hạn | 227.041.340 | 207.339.020
Doanh nghiệp có vốn đầu tư nước ngoài | 147.778.524 | 109.476.021
Hợp tác xã và công ty tư nhân | 1.371.552 | 1.212.185
Cá nhân và hộ kinh doanh cá thể | 640.003.504 | 566.326.189
Khác | 336.398.780 | 305.861.018
 | 1.449.198.899 | 1.270.359.018
 | 31/12/2024Triệu VND | 31/12/2023Triệu VND
Sản xuất và gia công chế biến | 340.501.488 | 280.386.148
Thương mại, dịch vụ | 214.488.774 | 204.168.323
Xây dựng | 90.512.980 | 81.091.024
Sản xuất và phân phối điện, khí đốt và nước | 65.344.169 | 54.975.004
Nông, lâm, thủy hải sản | 42.722.982 | 38.732.650
Vận tải kho bãi và thông tin liên lạc | 42.626.109 | 33.448.171
Khai khoảng | 26.027.625 | 20.413.414
Nhà hàng, khách sạn | 16.356.618 | 19.622.160
Các ngành khác | 610.618.154 | 537.522.124
 | 1.449.198.899 | 1.270.359.018
\( \therefore y \leq  {a}_{1} + 3\sqrt{2} \)
>>>

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "roe_change", "formula": "delta(safe_div(net_income, mean(equity, 4)), 4)", "rationale": "Cải thiện tỷ suất sinh lời trên vốn chủ so với cùng kỳ năm trước báo hiệu chất lượng hoạt động đi lên.", "source": {"type": "line_item", "ref": "net_income, equity"}},
{"name": "book_to_market", "formula": "safe_div(equity, market_cap)", "rationale": "Giá trị sổ sách cao so với vốn hoá là nhân tố giá trị kinh điển (Fama & French 1992).", "source": {"type": "line_item", "ref": "equity, market_cap"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-014 · P23-VCB24-bank_loans

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `-`

````text
Doanh nghiệp: VCB - ngân hàng (ngân hàng quốc doanh), sàn HOSE.
Chủ đề: chất lượng danh mục cho vay và dự phòng rủi ro tín dụng.

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````

### F1-016 · P24-SHB17-bank_loans

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `-`

````text
Doanh nghiệp: SHB - ngân hàng (ngân hàng tư nhân), sàn HOSE.
Chủ đề: chất lượng danh mục cho vay và dự phòng rủi ro tín dụng.

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-024 · P24-SHB17-bank_loans

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `data/sample/raw/ocr_results/SHB/2017/SHB_Baocaotaichinh_2017_Kiemtoan_Hopnhat/SHB_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1216-L1262`

````text
Doanh nghiệp: SHB - ngân hàng (ngân hàng tư nhân), sàn HOSE.
Chủ đề: chất lượng danh mục cho vay và dự phòng rủi ro tín dụng.

Trích thuyết minh báo cáo tài chính năm 2017 của SHB (mục 11. CHO VAY KHÁCH HÀNG):
<<<
11. CHO VAY KHÁCH HÀNG
 | 31/12/2017triệu VND | 31/12/2016triệu VND
Cho vay các tổ chức kinh tế, cá nhân | 196.082.946 | 161.341.033
Cho vay chiết khấu thương phiếu và các giấy tờ có giá | 7.548 | 6.299
Các khoản trả thay khách hàng | 35.359 | 47.338
Cho vay bằng vốn tài trợ, uỷ thác đầu tư | 2.164.713 | 808.887
 | 198.290.566 | 162.203.557
Các khoản phải thu giao dịch chứng khoán của SHBS | - | 172.628
 | 198.290.566 | 162.376.185
11.1 Phân tích chất lượng nợ cho vay
 | 31/12/2017triệu VND | 31/12/2016triệu VND
Nợ đủ tiêu chuẩn | 190.368.695 | 156.920.432
Nợ cần chú ý | 3.298.174 | 2.239.145
Nợ dưới tiêu chuẩn | 669.686 | 263.785
Nợ nghi ngờ | 1.088.771 | 993.341
Nợ có khả năng mất vốn | 2.865.240 | 1.786.854
 | 198.290.566 | 162.203.557
Các khoản phải thu giao dịch chứng khoán của SHBS | - | 172.628
 | 198.290.566 | 162.376.185
11.2 Phân tích dư nợ theo thời gian cho vay ban đầu
 | 31/12/2017triệu VND | 31/12/2016triệu VND
Nợ ngắn hạn | 83.106.717 | 73.797.009
Nợ trung hạn | 53.433.957 | 38.022.985
Nợ dài hạn | 61.749.892 | 50.383.563
 | 198.290.566 | 162.203.557
Các khoản phải thu giao dịch chứng khoán của SHBS | - | 172.628
 | 198.290.566 | 162.376.185
 | 31/12/2017%/năm | 31/12/2016%/năm
Tại thị trường Việt Nam |  | 
Cho vay bằng VND | 7,50 – 12,00 | 5,01 – 11,25
Cho vay bằng ngoại tệ | 1,90 – 5,01 | 1,00 – 5,03
Tại thị trường Lào |  | 
Cho vay bằng LAK | 5,00 – 14,50 | 8,00 – 14,50
Cho vay bằng ngoại tệ | 6,25 – 9,50 | 6,25 – 9,50
Tại thị trường Campuchia |  | 
Cho vay bằng ngoại tệ | 2,00 – 10,00 | 2,00 – 10,00
11.3 Phân tích dư nợ cho vay theo đối tượng khách hàng và theo loại hình doanh nghiệp
 | 31/12/2017triệu VND | % | 31/12/2016triệu VND | %
Công ty Nhà nước | 7.657.939 | 3,86 | 7.231.657 | 4,45
Công ty TNHH Nhà nước | 13.486.439 | 6,80 | 12.412.504 | 7,64
Công ty TNHH khác | 35.056.234 | 17,68 | 24.494.250 | 15,08
Công ty cổ phần vốn Nhà nước | 16.986.532 | 8,57 | 15.114.294 | 9,31
Công ty cổ phần khác | 80.842.480 | 40,77 | 69.049.630 | 42,52
Công ty hợp danh | 8.321 | 0,00 | 96.250 | 0,06
Doanh nghiệp tư nhân | 2.527.685 | 1,27 | 1.565.104 | 0,96
Doanh nghiệp có vốn đầu tư nước ngoài | 499.434 | 0,25 | 59.215 | 0,04
Hợp tác xã và liên hiệp hợp tác xã | 66.194 | 0,03 | 64.345 | 0,05
Hộ kinh doanh, cá nhân | 38.821.106 | 19,58 | 30.331.453 | 18,68
Thành phần kinh tế khác | 2.338.202 | 1,19 | 1.784.855 | 1,11
 | 198.290.566 | 100,00 | 162.203.557 | 99,90
Các khoản phải thu giao dịch chứng khoán của SHBS | - | - | 172.628 | 0,10
 | 198.290.566 | 100,00 | 162.376.185 | 100,00
11.4 Phân tích dư nợ cho vay theo ngành
 | 31/12/2017triệu VND | % | 31/12/2016triệu VND | %
Nông nghiệp, lâm nghiệp và thủy sản | 43.249.519 | 21,81 | 34.501.644 | 21,25
Khai khoáng | 7.659.777 | 3,86 | 8.483.683 | 5,22
Công nghiệp chế biến, chế tạo | 27.452.713 | 13,84 | 25.232.054 | 15,54
Sản xuất và phân phối điện, khí đốt, nước nóng, hơi nước và điều hòa không khí | 10.757.675 | 5,43 | 8.427.214 | 5,19
Cung cấp nước; hoạt động quản lý và xử lý rác thải, nước thải | 118.922 | 0,06 | 154.238 | 0,09
Xây dựng | 27.913.697 | 14,08 | 22.636.557 | 13,94
Bán buôn và bán lẻ; sửa chữa ô tô, mô tô, xe máy và xe có động cơ khác | 32.346.233 | 16,31 | 25.922.633 | 15,96
Vận tải kho bãi | 3.158.672 | 1,59 | 3.326.876 | 2,05
Dịch vụ lưu trú và ăn uống | 1.331.461 | 0,67 | 1.213.657 | 0,75
Thông tin và truyền thông | 111.063 | 0,06 | 143.909 | 0,09
Hoạt động tài chính, ngân hàng và bảo hiểm | 2.263.714 | 1,14 | 983.861 | 0,61
>>>

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F3-019 · P24-SHB17-bank_loans

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `data/sample/raw/ocr_results/SHB/2017/SHB_Baocaotaichinh_2017_Kiemtoan_Hopnhat/SHB_Baocaotaichinh_2017_Kiemtoan_Hopnhat_extracted.txt#L1216-L1262`

````text
Doanh nghiệp: SHB - ngân hàng (ngân hàng tư nhân), sàn HOSE.
Chủ đề: chất lượng danh mục cho vay và dự phòng rủi ro tín dụng.

Trích thuyết minh báo cáo tài chính năm 2017 của SHB (mục 11. CHO VAY KHÁCH HÀNG):
<<<
11. CHO VAY KHÁCH HÀNG
 | 31/12/2017triệu VND | 31/12/2016triệu VND
Cho vay các tổ chức kinh tế, cá nhân | 196.082.946 | 161.341.033
Cho vay chiết khấu thương phiếu và các giấy tờ có giá | 7.548 | 6.299
Các khoản trả thay khách hàng | 35.359 | 47.338
Cho vay bằng vốn tài trợ, uỷ thác đầu tư | 2.164.713 | 808.887
 | 198.290.566 | 162.203.557
Các khoản phải thu giao dịch chứng khoán của SHBS | - | 172.628
 | 198.290.566 | 162.376.185
11.1 Phân tích chất lượng nợ cho vay
 | 31/12/2017triệu VND | 31/12/2016triệu VND
Nợ đủ tiêu chuẩn | 190.368.695 | 156.920.432
Nợ cần chú ý | 3.298.174 | 2.239.145
Nợ dưới tiêu chuẩn | 669.686 | 263.785
Nợ nghi ngờ | 1.088.771 | 993.341
Nợ có khả năng mất vốn | 2.865.240 | 1.786.854
 | 198.290.566 | 162.203.557
Các khoản phải thu giao dịch chứng khoán của SHBS | - | 172.628
 | 198.290.566 | 162.376.185
11.2 Phân tích dư nợ theo thời gian cho vay ban đầu
 | 31/12/2017triệu VND | 31/12/2016triệu VND
Nợ ngắn hạn | 83.106.717 | 73.797.009
Nợ trung hạn | 53.433.957 | 38.022.985
Nợ dài hạn | 61.749.892 | 50.383.563
 | 198.290.566 | 162.203.557
Các khoản phải thu giao dịch chứng khoán của SHBS | - | 172.628
 | 198.290.566 | 162.376.185
 | 31/12/2017%/năm | 31/12/2016%/năm
Tại thị trường Việt Nam |  | 
Cho vay bằng VND | 7,50 – 12,00 | 5,01 – 11,25
Cho vay bằng ngoại tệ | 1,90 – 5,01 | 1,00 – 5,03
Tại thị trường Lào |  | 
Cho vay bằng LAK | 5,00 – 14,50 | 8,00 – 14,50
Cho vay bằng ngoại tệ | 6,25 – 9,50 | 6,25 – 9,50
Tại thị trường Campuchia |  | 
Cho vay bằng ngoại tệ | 2,00 – 10,00 | 2,00 – 10,00
11.3 Phân tích dư nợ cho vay theo đối tượng khách hàng và theo loại hình doanh nghiệp
 | 31/12/2017triệu VND | % | 31/12/2016triệu VND | %
Công ty Nhà nước | 7.657.939 | 3,86 | 7.231.657 | 4,45
Công ty TNHH Nhà nước | 13.486.439 | 6,80 | 12.412.504 | 7,64
Công ty TNHH khác | 35.056.234 | 17,68 | 24.494.250 | 15,08
Công ty cổ phần vốn Nhà nước | 16.986.532 | 8,57 | 15.114.294 | 9,31
Công ty cổ phần khác | 80.842.480 | 40,77 | 69.049.630 | 42,52
Công ty hợp danh | 8.321 | 0,00 | 96.250 | 0,06
Doanh nghiệp tư nhân | 2.527.685 | 1,27 | 1.565.104 | 0,96
Doanh nghiệp có vốn đầu tư nước ngoài | 499.434 | 0,25 | 59.215 | 0,04
Hợp tác xã và liên hiệp hợp tác xã | 66.194 | 0,03 | 64.345 | 0,05
Hộ kinh doanh, cá nhân | 38.821.106 | 19,58 | 30.331.453 | 18,68
Thành phần kinh tế khác | 2.338.202 | 1,19 | 1.784.855 | 1,11
 | 198.290.566 | 100,00 | 162.203.557 | 99,90
Các khoản phải thu giao dịch chứng khoán của SHBS | - | - | 172.628 | 0,10
 | 198.290.566 | 100,00 | 162.376.185 | 100,00
11.4 Phân tích dư nợ cho vay theo ngành
 | 31/12/2017triệu VND | % | 31/12/2016triệu VND | %
Nông nghiệp, lâm nghiệp và thủy sản | 43.249.519 | 21,81 | 34.501.644 | 21,25
Khai khoáng | 7.659.777 | 3,86 | 8.483.683 | 5,22
Công nghiệp chế biến, chế tạo | 27.452.713 | 13,84 | 25.232.054 | 15,54
Sản xuất và phân phối điện, khí đốt, nước nóng, hơi nước và điều hòa không khí | 10.757.675 | 5,43 | 8.427.214 | 5,19
Cung cấp nước; hoạt động quản lý và xử lý rác thải, nước thải | 118.922 | 0,06 | 154.238 | 0,09
Xây dựng | 27.913.697 | 14,08 | 22.636.557 | 13,94
Bán buôn và bán lẻ; sửa chữa ô tô, mô tô, xe máy và xe có động cơ khác | 32.346.233 | 16,31 | 25.922.633 | 15,96
Vận tải kho bãi | 3.158.672 | 1,59 | 3.326.876 | 2,05
Dịch vụ lưu trú và ăn uống | 1.331.461 | 0,67 | 1.213.657 | 0,75
Thông tin và truyền thông | 111.063 | 0,06 | 143.909 | 0,09
Hoạt động tài chính, ngân hàng và bảo hiểm | 2.263.714 | 1,14 | 983.861 | 0,61
>>>

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Ví dụ công thức (chỉ minh hoạ định dạng và mức độ, KHÔNG lặp lại):
[{"name": "roe_change", "formula": "delta(safe_div(net_income, mean(equity, 4)), 4)", "rationale": "Cải thiện tỷ suất sinh lời trên vốn chủ so với cùng kỳ năm trước báo hiệu chất lượng hoạt động đi lên.", "source": {"type": "line_item", "ref": "net_income, equity"}},
{"name": "book_to_market", "formula": "safe_div(equity, market_cap)", "rationale": "Giá trị sổ sách cao so với vốn hoá là nhân tố giá trị kinh điển (Fama & French 1992).", "source": {"type": "line_item", "ref": "equity, market_cap"}},
{"name": "accruals_to_assets", "formula": "safe_div(net_income - cfo, total_assets)", "rationale": "Phần lợi nhuận không đi kèm dòng tiền càng lớn thì chất lượng lợi nhuận càng thấp, lợi suất tương lai thường kém hơn (Sloan 1996).", "source": {"type": "line_item", "ref": "net_income, cfo, total_assets"}}]

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F1-017 · P25-BVS24-fin_assets

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `-`

````text
Doanh nghiệp: BVS - chứng khoán (chứng khoán vốn hoá nhỏ), sàn HNX.
Chủ đề: danh mục tài sản tài chính của công ty chứng khoán.

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F2-025 · P25-BVS24-fin_assets

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `data/sample/raw/ocr_results/BVS/2024/BVS_Baocaotaichinh_2024_Kiemtoan/BVS_Baocaotaichinh_2024_Kiemtoan_extracted.txt#L1178-L1247`

````text
Doanh nghiệp: BVS - chứng khoán (chứng khoán vốn hoá nhỏ), sàn HNX.
Chủ đề: danh mục tài sản tài chính của công ty chứng khoán.

Trích thuyết minh báo cáo tài chính năm 2024 của BVS (mục 7. CÁC LOẠI TÀI SẢN TÀI CHÍNH):
<<<
7. CÁC LOẠI TÀI SẢN TÀI CHÍNH
7.1 Tài sản tài chính ghi nhận thông qua lãi/lỗ (FVTPL)
Giá gốc VND | Giá trị hợp lý VND | Giá gốc VND | Giá trị hợp lý VND
Cổ phiếu niêm yết | 238.099.845.216 | 257.888.984.770 | 195.203.695.970 | 225.213.953.530
Cổ phiếu chưa niêm yết | 2.688.655.127 | 2.456.516.211 | 1.534.743.168 | 1.182.451.715
Chứng chỉ quỹ | 65.240.346.725 | 75.053.113.200 | 57.725.055.759 | 63.940.748.700
Trái phiếu niêm yết | - | - | 50.983.100.000 | 50.983.100.000
Trái phiếu chưa niêm yết | 81.164.953.403 | 81.164.953.403 | 391.602.948.464 | 391.602.948.464
TỔNG CỘNG | 387.193.800.471 | 416.563.567.584 | 697.049.543.361 | 732.923.202.409
\( \therefore {S}_{\Delta APQ} = {S}_{\Delta AQP} + {S}_{\Delta QPQ} \)
7.2 Tài sản tài chính sẵn sàng để bán (AFS)
Giá gốc VND | Giá trị ghi sổ VND | Giá trị hợp lý/ Giá trị thuần VND | Giá gốc VND | Giá trị ghi sổ VND | Giá trị hợp lý/ Giá trị thuần VND
Ghi nhận theo giá trị hợp lý | 16.576.432.682 | 81.439.670.000 | 81.439.670.000 | 16.576.432.682 | 65.607.010.000 | 65.607.010.000
Chứng chỉ quỹ | 16.576.432.682 | 81.439.670.000 | 81.439.670.000 | 16.576.432.682 | 65.607.010.000 | 65.607.010.000
Ghi nhận theo giá gốc | 83.478.822.047 | 83.478.822.047 | 32.728.401.392 | 83.978.327.067 | 83.978.327.067 | 30.923.483.472
Đầu tư tự doanh khác | 13.123.117.619 | 13.123.117.619 | - | 13.623.117.619 | 13.623.117.619 | -
Cổ phiếu chưa niêm yết | 70.355.704.428 | 70.355.704.428 | 32.728.401.392 | 70.355.209.448 | 70.355.209.448 | 30.923.483.472
TỔNG CỘNG | 100.055.254.729 | 164.918.492.047 | 114.168.071.392 | 100.554.759.749 | 149.585.337.067 | 96.530.493.472
Giá gốc VND | Giá trị ghi số VND | Giá trị hợp lý/ Giá trị thuần (*) VND | Giá gốc VND | Giá trị ghi số VND | Giá trị hợp lý/ Giá trị thuần (*) VND
Ghi nhận theo giá trị hợp lý | 93.000.000.000 | 157.408.483.109 | 157.408.483.109 | 108.285.757.806 | 162.219.417.314 | 162.219.417.314
Cổ phiếu niêm yết | - | - | - | 15.285.757.806 | 21.883.151.450 | 21.883.151.450
Chứng chỉ quỹ chưa niêm yết | 93.000.000.000 | 157.408.483.109 | 157.408.483.109 | 93.000.000.000 | 140.336.265.864 | 140.336.265.864
Ghi nhận theo giá gốc | 14.150.483.000 | 14.150.483.000 | 11.209.099.000 | 14.150.483.000 | 14.150.483.000 | 11.209.099.000
Cổ phiếu chưa niêm yết | 14.150.483.000 | 14.150.483.000 | 11.209.099.000 | 14.150.483.000 | 14.150.483.000 | 11.209.099.000
TỔNG CỘNG | 107.150.483.000 | 171.558.966.109 | 168.617.582.109 | 122.436.240.806 | 176.369.900.314 | 173.428.516.314
(*) Đối với các tài sản tài chính AFS ghi nhận theo giá gốc, giá trị thuần là giá trị ghi sổ trừ dự phòng suy giảm giá trị.
7.3 Các khoản đầu tư nấm giữ đến ngày đáo hạn (HTM)
 | Số cuối năm VND | Số đầu năm VND
Các hợp đồng tiền gửi có kỳ hạn (*) | 860.549.280.822 | 1.605.722.510.956
Trái phiếu tổ chức tín dụng (**) | 302.597.007.664 | 102.040.989.518
TỔNG CỘNG | 1.163.146.288.486 | 1.707.763.500.474
(*) Các hợp đồng tiền gửi có kỳ hạn bằng đồng Việt Nam tại các tổ chức tín dụng có kỳ hạn còn lại từ ba (03) tháng đến một (01) năm và được hưởng lãi suất từ 3,7%/năm đến 5,9%/năm; và được dùng toàn bộ để đảm bảo cho các khoản vay ngắn hạn của Công ty.
(**) Các trái phiếu tại các tổ chức tín dụng có kỳ hạn còn lại từ bày (07) năm đến tám (08) năm và được hưởng lãi suất từ 5,78%/năm đến 5,88%/năm; và được dùng toàn bộ để đảm bảo cho các khoản vay ngắn hạn của Công ty.
7.4 Các khoản cho vay
 | Số cuối năm VND | Số đầu năm VND
Cho vay margin (*) | 2.949.435.728.483 | 2.708.111.871.986
>>>

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: dựa trên nội dung đoạn thuyết minh, đề xuất 3 công thức đặc trưng khác nhau có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới. Ít nhất một công thức phải xuất phát từ thông tin trong thuyết minh: khi đó ghi source.type = "note" và source.ref trích nguyên văn một cụm tối đa 20 từ từ đoạn thuyết minh.

Trả về mảng JSON gồm đúng 3 phần tử theo định dạng đã quy định.
````

### F4-015 · P25-BVS24-fin_assets

allowed_vars (15): `total_assets, equity, pretax_profit, net_income, cfo, cfi, cff, related_party_disclosed, audit_opinion_qualified, going_concern_flag, contingent_liabilities_disclosed, market_cap, close_price, shares_outstanding, adv20`  
must_reference: `-`  
context_source: `-`

````text
Doanh nghiệp: BVS - chứng khoán (chứng khoán vốn hoá nhỏ), sàn HNX.
Chủ đề: danh mục tài sản tài chính của công ty chứng khoán.

Danh sách biến được phép dùng:
- total_assets: TỔNG CỘNG TÀI SẢN [VND, số dư cuối kỳ]
- equity: VỐN CHỦ SỞ HỮU [VND, số dư cuối kỳ]
- pretax_profit: Tổng lợi nhuận kế toán trước thuế [VND, phát sinh trong kỳ]
- net_income: Lợi nhuận sau thuế thu nhập doanh nghiệp [VND, phát sinh trong kỳ]
- cfo: Lưu chuyển tiền thuần từ hoạt động kinh doanh [VND, phát sinh trong kỳ]
- cfi: Lưu chuyển tiền thuần từ hoạt động đầu tư [VND, phát sinh trong kỳ]
- cff: Lưu chuyển tiền thuần từ hoạt động tài chính [VND, phát sinh trong kỳ]
- related_party_disclosed: Có thuyết minh giao dịch với bên liên quan [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- audit_opinion_qualified: Ý kiến kiểm toán không phải chấp nhận toàn phần [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- going_concern_flag: Thuyết minh có nêu nghi ngờ khả năng hoạt động liên tục [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- contingent_liabilities_disclosed: Có thuyết minh nợ tiềm tàng hoặc cam kết [cờ từ thuyết minh, số lần nội dung này được nhắc tới]
- market_cap: Vốn hoá thị trường [dữ liệu thị trường]
- close_price: Giá đóng cửa [dữ liệu thị trường]
- shares_outstanding: Số cổ phiếu đang lưu hành [dữ liệu thị trường]
- adv20: Giá trị giao dịch bình quân 20 phiên [dữ liệu thị trường]

Yêu cầu: đề xuất 3 công thức đặc trưng khác nhau xoay quanh chủ đề trên, có khả năng giúp xếp hạng lợi suất cổ phiếu quý tới.

ĐỊNH DẠNG BẮT BUỘC - tuân thủ tuyệt đối:
1. Câu trả lời là MỘT mảng JSON gồm đúng 3 đối tượng. Ký tự đầu tiên là "[", ký tự cuối cùng là "]".
   Không dùng markdown, không bọc trong ```, không viết giải thích trước hay sau.
2. Mỗi đối tượng có đúng 4 khoá: "name", "formula", "rationale", "source".
   - name: chữ thường, chữ số và dấu gạch dưới, bắt đầu bằng chữ cái.
   - formula: một biểu thức theo ngữ pháp ở mục 3.
   - rationale: một câu tiếng Việt, tối đa 40 từ.
   - source: {"type": "line_item", "ref": "<các biến đã dùng, cách nhau bởi dấu phẩy>"}
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
{"name": "asset_growth", "formula": "growth(total_assets, 4)", "rationale": "Tài sản tăng quá nhanh thường đi kèm lợi suất thấp hơn.", "source": {"type": "line_item", "ref": "total_assets"}}
````
