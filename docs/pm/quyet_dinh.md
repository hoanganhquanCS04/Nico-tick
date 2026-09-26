# Nhật ký quyết định

> Sinh tự động từ Google Sheet bằng `docs/pm/xlsx_to_md.py` ngày 26/09/2026. **Đừng sửa tay** — sửa trên Sheet rồi chạy lại script.

Đổi ý thì không xoá dòng cũ: đặt nó "Đã thay đổi" và thêm dòng mới.

## ⏳ Chờ quyết

| ID | Ngày | Quyết định | Lý do | Ai quyết | Phương án đã bỏ | Ảnh hưởng tới | Nguồn |
|---|---|---|---|---|---|---|---|
| Q12 | 26/09 | Phân vai: Quân = PM + ML, Thắng = Data (+ RAG, demo), Trung = Quant | Cân tải theo pha, mỗi việc 1 người chịu trách nhiệm | Quân |  | Toàn dự án | Chốt ở họp khởi động 27/09 |
| Q14 | 26/09 | Kéo pipeline backtest (V19) bắt đầu sớm từ 29/09 thay vì 06/10 | Trung đang ít việc trong P0; backtest dựng được trên dữ liệu giả | Quân | Giữ 06/10 | P2 | Chốt ở họp khởi động 27/09 |
| Q21 | 26/09 | C4: Thắng + Trung chấm độc lập cả 80 công thức, Quân làm trọng tài; điểm cuối = trọng tài nếu lệch ≥2, không thì trung bình | Spec yêu cầu 2 người chấm độc lập và báo đồng thuận; Quân dễ đoán ra mô hình | Quân | Chia 3 người mỗi người ~27 mẫu (không đo được đồng thuận) | P0 | eval/rubric.md mục 7 — chốt ở họp khởi động 27/09 |
| Q15 |  | Thuyết minh quý lấy ở đâu? Đề xuất: dùng thuyết minh năm cho 4 quý sau ngày công bố | H2 cần thuyết minh; crawl + OCR quý quá nặng | Thầy | Crawl + OCR PDF quý | P1, P3 | README mục 10 #1 — họp 01/10 |
| Q16 |  | Số liệu quý lấy từ API hay tự OCR? Đề xuất: API | Parser OCR chỉ đọc trung vị 30/65 biến | Thầy | Tự OCR | P1 | README mục 10 #2 — họp 01/10 |
| Q17 |  | Trích con số thật từ thuyết minh thay vì đếm từ khoá? | Để chứng minh thuyết minh đóng góp gì cho H2 | Thầy | Giữ đếm từ khoá | P1, P4 | README mục 10 #3 — họp 01/10 |
| Q18 |  | Loại ngân hàng / chứng khoán khỏi universe? | Mẫu biểu BCTC khác, chỉ 15 biến áp dụng được | Thầy | Giữ và xử lý riêng | P1, P5 | README mục 10 #4 — họp 01/10 |
| Q19 |  | Định vị "giải thích được từ thiết kế" + thêm H5 (tuyến tính làm mốc)? | Ngân hàng, quỹ không chấp nhận hộp đen | Thầy | Không thêm H5 | P5, P8 | README mục 10 #5 — họp 01/10 |
| Q20 |  | Chấp nhận bộ sinh Gemma-4-E2B (5,1B tổng) hay dùng Qwen3.5-2B? | Thầy muốn mô hình "vài trăm triệu" | Thầy | Qwen3.5-2B | P4 | README mục 10 #6 — họp 01/10 |

## ✅ Đã chốt

| ID | Ngày | Quyết định | Lý do | Ai quyết | Phương án đã bỏ | Ảnh hưởng tới | Nguồn |
|---|---|---|---|---|---|---|---|
| Q01 | ≤ 22/09 | Gộp chốt mô hình + chốt phạm vi vào 1 buổi họp thầy (01/10) | Tiết kiệm thời gian của thầy, chốt sớm để khoá đề cương 03/10 | Nhóm | Họp 2 buổi riêng | P0 | Timelines.xlsx #4 |
| Q02 | ≤ 22/09 | Benchmark chỉ 3–4 mô hình ứng viên | Tránh dàn trải, kịp hạn P0 | Nhóm | Benchmark 8 mô hình | P0 | docs/P0_breakdown.md 2.1 |
| Q03 | ≤ 22/09 | Công thức chỉ viết theo DSL, cấm "/", mọi phép chia dùng safe_div | Máy kiểm tra được tự động, không chia cho 0 | Nhóm | Cho AI viết tự do | P0, P4 | README 4.3 |
| Q04 | 22/09 | Trích biến theo mã số VAS, không dò tên chỉ tiêu | Mã số không bị lỗi chính tả OCR (đã kiểm trên 40 file) | Nhóm | Dò khớp tên tiếng Việt | P1 | README mục 5 |
| Q05 | ≤ 22/09 | Giữ cả cổ phiếu đã huỷ niêm yết | Tránh survivorship bias | Nhóm | Chỉ lấy mã đang niêm yết | P1 | README mục 5 |
| Q06 | ≤ 22/09 | Baseline API chỉ chạy trên mẫu con 50 DN × 3 năm | Chi phí API và thời gian | Nhóm | Chạy full | P6 | Timelines.xlsx #22 |
| Q07 | ≤ 22/09 | Ablation chỉ 2 cấu hình: bỏ RAG, bỏ HITL | Đủ trả lời H2, tiết kiệm thời gian | Nhóm | Thêm cấu hình bỏ validator | P6 | Timelines.xlsx #23 |
| Q08 | ≤ 22/09 | Giảm số công thức sinh từ 200 xuống ~150 | Vừa sức duyệt tay (HITL) | Nhóm | 200 công thức | P4 | Timelines.xlsx #16 |
| Q09 | ≤ 22/09 | Trượt CHỐT 2 thì chuyển few-shot + ràng buộc grammar, không đổi mô hình | Đổi mô hình lần nữa sẽ phải chạy lại P0 | Nhóm | Đổi mô hình | P4 | Timelines.xlsx #18 |
| Q10 | ≤ 22/09 | 3 thứ không được cắt: mô hình chi phí VN, kiểm định thống kê, đóng băng 30/11 | Là đóng góp riêng / điều kiện để bài không bị bắt lỗi | Nhóm |  | P2, P7 | README mục 7 |
| Q11 | ≤ 26/09 | Benchmark P0 chạy trên Kaggle T4, lượng tử NF4 4-bit | Máy nhà không đủ; T4 là card phổ thông | Nhóm | Chạy trên GTX 1660 Ti | P0 | README mục 11 |
| Q13 | 26/09 | Google Sheet là bản cập nhật chính; docs/pm/*.md là bản chụp sau mỗi họp tuần | Ai cũng sửa được Sheet; md giữ lịch sử trong git | Quân | Chỉ dùng md | Quản lý |  |
