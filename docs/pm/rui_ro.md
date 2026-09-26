# Sổ rủi ro

> Sinh tự động từ Google Sheet bằng `docs/pm/xlsx_to_md.py` ngày 26/09/2026. **Đừng sửa tay** — sửa trên Sheet rồi chạy lại script.

Điểm = Khả năng × Ảnh hưởng (mỗi thứ 1–3). 🔴 ≥6: bàn mỗi buổi họp tuần · 🟡 3–5: theo dõi · 🟢 ≤2.

## Đang mở

| ID | Điểm | Rủi ro | Nhóm | Dấu hiệu sớm | Cách phòng | Nếu xảy ra thì | Người theo dõi | Trạng thái | Cập nhật |
|---|---|---|---|---|---|---|---|---|---|
| R01 | 🔴 9 | Không tìm được nguồn ngày công bố BCTC thực tế đủ phủ | Dữ liệu | Đến 30/09 (V14) chưa nguồn nào phủ >50% mã × năm | Dò nguồn ngay tuần này, thử nhiều nguồn song song, hỏi thầy 01/10 | Bỏ Bảng 2, chuyển H3 thành mục hạn chế, báo thầy trong ngày (CHỐT 1) | Thắng | Mở | 26/09 |
| R02 | 🔴 6 | Không có thuyết minh BCTC quý (API chỉ trả bảng số) | Dữ liệu | Thầy không có hướng khác ở buổi 01/10 | Đề xuất với thầy dùng thuyết minh năm | Dùng thuyết minh năm, áp cho 4 quý sau ngày công bố | Thắng | Mở | 26/09 |
| R03 | 🔴 6 | Tỷ lệ công thức hợp lệ < 60% ở CHỐT 2 (hiện tốt nhất 47,2%) | Mô hình | GCD (V25) không đưa được tỷ lệ lên ≥55% trước 17/10 | Thử GCD sớm, trước P4 | Few-shot + ràng buộc grammar, KHÔNG đổi mô hình lần nữa | Quân | Mở | 26/09 |
| R04 | 🔴 6 | Thiếu biến để tính nhân tố (parser OCR chỉ đọc trung vị 30/65 biến) | Dữ liệu | Sau khi map API, <80% biến trong variables.yaml có số | Lấy số liệu quý từ API, map variables.yaml sang tên trường API | Thu hẹp danh mục biến, ghi rõ trong phần hạn chế | Thắng | Mở | 26/09 |
| R05 | 🔴 6 | Ít điểm thời gian (~40 quý) → kết quả không có ý nghĩa thống kê | Phương pháp | t-stat của IC < 2 ở hầu hết cấu hình | Bổ sung giá tần suất ngày (Wei et al. 2022), kiểm định kỹ ở P7 | Báo cáo trung thực, nhấn mạnh đóng góp của Bảng 2 và Bảng 3 | Trung | Mở | 26/09 |
| R06 | 🔴 6 | Rò rỉ dữ liệu tương lai (point-in-time, mốc huấn luyện LLM) bị hội đồng bắt lỗi | Phương pháp | Code gán thời gian chưa ai review chéo | Theo kỷ luật README mục 6; người khác review code gán thời gian | Sửa và chạy lại trước 30/11; sau đóng băng thì ghi vào hạn chế | Trung | Mở | 26/09 |
| R07 | 🔴 6 | Quá tải 1 người: Quân vừa quản lý vừa làm ML chính (hiện mọi commit là của Quân) | Nhân sự | Việc của Quân trễ 2 tuần liên tiếp; Thắng/Trung chưa có commit | Giao việc theo tên, soi bảng Tổng quan mỗi buổi họp tuần | Chuyển bớt việc P6/P8 của Quân sang người đang ít việc | Quân | Mở | 26/09 |
| R08 | 🔴 6 | Dồn việc viết báo cáo về cuối, không đủ 10 ngày cho thầy sửa | Tiến độ | Đến 09/11 chưa có nháp Chương 1–2 | Viết Chương 1–2 từ 20/10, song song với chạy mô hình | Cắt độ dài Chương 2, ưu tiên Chương 3–4 | Quân | Mở | 26/09 |
| R09 | 🟡 4 | Thầy không chấp nhận bộ sinh 5,1B tổng (Gemma) vì muốn "vài trăm triệu" | Phạm vi | Buổi 01/10 thầy nghiêng về mô hình <1B | Tờ trình dẫn số VRAM và kết quả Qwen3.5-0.8B chỉ 16% hợp lệ | Chuyển sang Qwen3.5-2B (dự phòng đã có số) | Quân | Mở | 26/09 |
| R10 | 🟡 4 | Phạm vi phình ra sau khi khoá đề cương (thêm giả thuyết, thêm mô hình…) | Phạm vi | Có việc mới không nằm trong tab Việc | Sau 03/10, ý mới ghi vào mục "để sau", chỉ đổi khi thầy yêu cầu | Đổi phạm vi = ghi vào tab Quyết định, bỏ bớt 1 việc tương đương | Quân | Mở | 26/09 |
| R11 | 🟡 4 | Thiếu GPU: hết quota Kaggle/Colab, máy nhà chỉ có GTX 1660 Ti 6GB | Hạ tầng | Còn <10 giờ quota trong tuần có đợt chạy lớn | Lên lịch các đợt chạy lớn trước, lưu checkpoint, dùng nhiều tài khoản trong nhóm | Giảm số seed/prompt, ghi rõ trong báo cáo | Quân | Mở | 26/09 |
| R12 | 🟢 2 | Demo không chạy trên máy hội đồng | Demo | Chưa chạy thử demo trên máy nào khác máy dev | Chạy thử trên máy của người khác trong nhóm trước 30/11 | Chuẩn bị video quay màn hình dự phòng | Thắng | Mở | 26/09 |
