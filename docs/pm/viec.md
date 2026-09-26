# Bảng việc

> Sinh tự động từ Google Sheet bằng `docs/pm/xlsx_to_md.py` ngày 26/09/2026. **Đừng sửa tay** — sửa trên Sheet rồi chạy lại script.

## Theo người

| Người | Cần làm | Đang làm | Chờ duyệt | Kẹt | Xong | Trễ | Tổng |
|---|---|---|---|---|---|---|---|
| Quân | 17 | 0 | 1 | 0 | 3 | 0 | 21 |
| Thắng | 12 | 0 | 0 | 0 | 0 | 0 | 12 |
| Trung | 13 | 0 | 0 | 0 | 0 | 0 | 13 |

## PM

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V01 | Dựng bộ quản lý dự án (Google Sheet + docs/pm) | Quân |  | 26/09 | 26/09 | ✅ Xong | Sheet + docs/pm/ có đủ phân công, việc, rủi ro, quyết định, họp |  |  |
| V02 | Họp khởi động: trình bày phân công, xin ý kiến Thắng & Trung, chốt giờ họp tuần cố định | Quân | Thắng, Trung | 27/09 | 27/09 | ⬜ Cần làm · ⏰ sắp hạn | Cả 3 đồng ý phân công (hoặc đã sửa), có giờ họp tuần, Sheet đã share cho 2 bạn | V01 | Phân công hiện là ĐỀ XUẤT, chốt ở buổi này |

## P0

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V03 | Bộ thử 76 prompt, 4 họ F1–F4 | Quân |  | 19/09 | 24/09 | ✅ Xong | eval/prompts.jsonl đủ 76 dòng |  |  |
| V04 | Benchmark 4 mô hình × 76 prompt × 3 seed | Quân |  | 19/09 | 24/09 | ✅ Xong | bench/results/table.md | V03 | Kaggle T4, NF4 4-bit |
| V05 | Viết thang chấm eval/rubric.md cho tiêu chí C4 (ý nghĩa kinh tế, 1–5) | Quân | Thắng, Trung | 22/09 | ~~24/09~~ → 27/09 | 👀 Chờ duyệt · ⏰ sắp hạn | Mỗi mức 1–5 có mô tả + ví dụ; Thắng, Trung đọc và hỏi hết chỗ chưa rõ |  | Bản nháp đã có 26/09. Việc con 1.5 của P0, trễ từ 24/09 |
| V06 | Hiệu chỉnh C4: Thắng, Trung chấm độc lập C001–C010, chạy c4_merge.py --only C001-C010 | Trung | Thắng | 28/09 | 28/09 | ⬜ Cần làm · ⏰ sắp hạn | Không quá 3/10 công thức lệch ≥2 điểm; quá thì sửa rubric rồi chấm lại | V05 | Quy trình: eval/rubric.md mục 7 |
| V07 | Chấm C4 C011–C080 (2 người độc lập, mù tên mô hình) + trọng tài công thức lệch ≥2 | Trung | Thắng, Quân | 28/09 | ~~24/09~~ → 29/09 | ⬜ Cần làm | c4_scores_thang.csv + c4_scores_trung.csv đủ 80; c4_merge.py ra bench/results/c4.md | V06 | Quân làm trọng tài, không chấm (đã xem output nhiều, dễ đoán ra mô hình). Việc con 2.6, trễ từ 24/09 |
| V08 | Tờ trình 1 trang chốt mô hình | Quân |  | 22/09 | ~~24/09~~ → 29/09 | ⬜ Cần làm | docs/to_trinh_chot_mo_hinh.docx đúng 5 khối, có bảng benchmark + điểm C4 | V07 | Trễ từ 24/09 |
| V09 | Duyệt tờ trình (đọc như thầy đọc) | Thắng |  | 30/09 | 30/09 | ⬜ Cần làm | Góp ý gửi Quân, Quân sửa xong trong ngày | V08 |  |
| V10 | Gửi thầy tờ trình + 6 câu hỏi cần quyết (README mục 10) | Quân |  | 30/09 | 30/09 | ⬜ Cần làm | Email đã gửi, thầy có ≥1 ngày để đọc trước buổi họp | V09 |  |
| V11 | Họp thầy: chốt mô hình + phạm vi | Quân | Thắng, Trung | 01/10 | 01/10 | ⬜ Cần làm | Có câu trả lời cho 6 vấn đề mở | V10 | Chương trình họp: docs/pm/bien_ban/2026-10-01_hop_thay.md |
| V12 | Gửi biên bản họp thầy + cập nhật tab Quyết định | Trung | Quân | 01/10 | 02/10 | ⬜ Cần làm | Biên bản trong docs/pm/bien_ban/, các Q15–Q20 chuyển sang Đã chốt | V11 | Người ghi biên bản luân phiên, lần này Trung |
| V13 | Khoá đề cương | Quân | Thắng, Trung | 02/10 | 03/10 | ⬜ Cần làm | README cập nhật theo quyết định của thầy; từ đây không đổi phạm vi | V12 |  |

## P1

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V14 | Dò nguồn ngày công bố BCTC thực tế (HOSE/HNX, vnstock, CafeF…), thử trên 20 mã mẫu | Thắng |  | 27/09 | 30/09 | ⬜ Cần làm | Ghi chú 1 trang: nguồn nào, phủ bao nhiêu mã × năm, cách lấy, độ tin cậy |  | Mang kết quả đi họp 01/10. Xem rủi ro R01 |
| V15 | Thu thập ngày công bố thực tế ~200 DN × 10 năm, đối chiếu chéo vnstock | Thắng |  | 24/09 | 09/10 | ⬜ Cần làm | File ngày công bố cho ≥150 DN × ≥8 năm | V14 | Kế hoạch gốc bắt đầu 24/09 nhưng chưa giao → đang trễ bắt đầu |
| V16 | Crawl BCTC quý ~200 DN × 10 năm (bảng số), map về config/variables.yaml | Thắng | Quân | 24/09 | 12/10 | ⬜ Cần làm | Bảng số quý ≥150 DN × ≥8 năm, map đủ biến trong variables.yaml | V11 | Phần bảng số qua vnstock làm ngay, không chờ họp. Nguồn thuyết minh chờ thầy chốt (Q15) |
| V17 | Giá OHLCV theo ngày + mã ngành, gồm cả mã đã huỷ niêm yết | Thắng | Trung | 29/09 | 12/10 | ⬜ Cần làm | Giá ngày đủ 10 năm, có mã huỷ niêm yết, căn đúng lịch giao dịch |  | Trung quy định định dạng cần cho backtest |
| V18 | CHỐT 1 — GO/NO-GO: ≥150 DN × ≥8 năm × có ngày công bố? | Quân | Thắng, Trung | 13/10 | 13/10 | ⬜ Cần làm | Quyết định GO/NO-GO ghi vào tab Quyết định, báo thầy trong ngày | V15, V16, V17 | NO-GO → bỏ Bảng 2, H3 thành mục hạn chế |

## P2

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V19 | Pipeline backtest: xếp hạng lát cắt ngang, long-short, IC, Sharpe, turnover | Trung |  | 29/09 | 17/10 | ⬜ Cần làm | Chạy được trên dữ liệu mẫu/giả, ra IC + Sharpe + turnover |  | Kế hoạch gốc bắt đầu 06/10; kéo sớm vì Trung đang ít việc P0 |
| V20 | Mô hình chi phí VN: phí môi giới 2 chiều, thuế bán 0,1%, spread theo thanh khoản, market impact | Trung |  | 13/10 | 19/10 | ⬜ Cần làm | Hàm chi phí gắn vào backtest, có bảng tham số và nguồn trích dẫn | V19 | KHÔNG CẮT |
| V21 | Baseline nhân tố thủ công (P/E, P/B, ROE, momentum, accruals) chạy hết pipeline | Trung |  | 13/10 | 19/10 | ⬜ Cần làm | Dòng đầu Bảng 1 có số | V16, V17, V19 |  |
| V22 | Bộ tính công thức DSL → số (dùng chung parser với validator) | Trung | Quân | 06/10 | 19/10 | ⬜ Cần làm | Mọi công thức hợp lệ trong benchmark P0 tính ra được số |  | README mục 10: cầu nối khối 2 → khối 3 |

## P3

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V23 | Chunk thuyết minh + index PhoBERT-base + bộ truy xuất | Thắng | Quân | 13/10 | 26/10 | ⬜ Cần làm | Truy vấn → trả về top-k đoạn thuyết minh | V16 |  |
| V24 | Đánh giá truy xuất trên 50 truy vấn gán nhãn tay | Thắng | Quân | 22/10 | 26/10 | ⬜ Cần làm | Bảng recall@k / MRR trên 50 truy vấn | V23 | Số này để trả lời câu: sao cần 2 mô hình |

## P4

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V25 | Thử giải mã ràng buộc ngữ pháp (GCD) trên bộ benchmark | Quân |  | 06/10 | 17/10 | ⬜ Cần làm | So sánh tỷ lệ hợp lệ có GCD vs không, cùng mô hình | V13 | Phòng rủi ro R03 |
| V26 | Validator đầy đủ: loại trích dẫn bịa + khử trùng theo tương quan | Quân |  | 20/10 | 26/10 | ⬜ Cần làm | Validator có đủ 2 bước mới, có test | V22 |  |
| V27 | Sinh ~150 công thức + truy vết nguồn, log tổng số đã thử | Quân |  | 27/10 | 02/11 | ⬜ Cần làm | ~150 công thức hợp lệ, mỗi công thức có nguồn; log tổng số lần thử | V25, V26 |  |
| V28 | HITL: duyệt công thức + biên bản lý do loại từng công thức | Thắng | Trung | 27/10 | 02/11 | ⬜ Cần làm | Mỗi công thức có điểm + lý do giữ/loại | V27 | Người sinh công thức (Quân) không tự duyệt |
| V29 | CHỐT 2 — GO/NO-GO: tỷ lệ công thức hợp lệ ≥60%? | Quân | Thắng, Trung | 03/11 | 03/11 | ⬜ Cần làm | Quyết định ghi vào tab Quyết định | V27 | NO-GO → few-shot + grammar, không đổi mô hình |

## P5

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V30 | Gán point-in-time theo ngày công bố + bản ngây thơ theo ngày cuối quý | Trung |  | 03/11 | 09/11 | ⬜ Cần làm | 2 bộ giá trị nhân tố song song → Bảng 2 | V15, V22 |  |
| V31 | LightGBM + MLP (+ tuyến tính nếu thầy duyệt H5), walk-forward | Trung |  | 03/11 | 16/11 | ⬜ Cần làm | Mô hình huấn luyện walk-forward, chọn tham số chỉ trên quá khứ | V30 | Không dùng LLM chọn feature theo kết quả |
| V32 | Backtest đầy đủ, xuất Bảng 1 / 2 / 3 | Trung | Quân | 10/11 | 16/11 | ⬜ Cần làm | 3 bảng kết quả có số | V20, V31 | Xương sống của bài |

## P6

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V33 | Baseline API trên mẫu con 50 DN × 3 năm | Quân |  | 17/11 | 23/11 | ⬜ Cần làm | Dòng baseline API trong Bảng 1 | V32 |  |
| V34 | Ablation 2 cấu hình: bỏ RAG, bỏ HITL | Thắng | Quân | 17/11 | 23/11 | ⬜ Cần làm | Dòng ablation trong Bảng 1 | V32 |  |
| V35 | Demo Streamlit 1 màn hình: nhập mã → công thức + đoạn nguồn + xếp hạng | Thắng |  | 17/11 | 30/11 | ⬜ Cần làm | Thầy bấm thử được trên máy khác | V32 |  |

## P7

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V36 | Kiểm định: t-stat, sai số chuẩn, giai đoạn con, hiệu chỉnh đa giả thuyết | Trung |  | 24/11 | 30/11 | ⬜ Cần làm | Mọi số trong Bảng 1/2/3 có t-stat + sai số chuẩn | V32 | KHÔNG CẮT |
| V37 | ĐÓNG BĂNG KẾT QUẢ | Quân | Thắng, Trung | 30/11 | 30/11 | ⬜ Cần làm | Không chạy thí nghiệm mới sau mốc này | V36 |  |

## P8

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V38 | Chương 1–2: tổng quan, khoảng trống, cơ sở lý thuyết | Thắng | Quân | 20/10 | 09/11 | ⬜ Cần làm | Bản nháp đủ 2 chương |  | Nguồn chính: docs/GAP_research.pdf |
| V39 | Chương 3: phương pháp — mỗi người viết phần mình làm, Quân gom | Quân | Thắng, Trung | 03/11 | 16/11 | ⬜ Cần làm | Bản nháp Chương 3 |  | Căn cứ chọn mô hình lấy từ tờ trình |
| V40 | Chương 4–5: kết quả, thảo luận, hạn chế | Trung | Quân | 17/11 | 30/11 | ⬜ Cần làm | Khung viết trước, số điền ngay khi có | V32 |  |
| V41 | CHỐT 3: nộp bản nháp đầy đủ cho GVHD | Quân | Thắng, Trung | 30/11 | 30/11 | ⬜ Cần làm | Thầy nhận bản nháp, còn đủ 10 ngày để sửa | V38, V39, V40 |  |
| V42 | Sửa theo góp ý thầy (vòng 1) | Quân | Thắng, Trung | 04/12 | 09/12 | ⬜ Cần làm | Mọi góp ý đã xử lý hoặc có lý do không sửa | V41 |  |
| V43 | Format, mục lục, danh mục bảng/hình, kiểm tra đạo văn, trích dẫn APA | Thắng |  | 09/12 | 12/12 | ⬜ Cần làm | Bản đúng mẫu trình bày, báo cáo đạo văn đạt | V42 |  |
| V44 | Bản cuối sẵn sàng, in / đóng quyển | Trung |  | 12/12 | 13/12 | ⬜ Cần làm | Có bản in trước hạn 1 ngày | V43 |  |
| V45 | NỘP BÁO CÁO | Quân | Thắng, Trung | 14/12 | 14/12 | ⬜ Cần làm | Đã nộp | V44 | HẠN CHỐT |

## P9

| ID | Việc | Phụ trách | Hỗ trợ | Bắt đầu | Hạn | Trạng thái | Xong khi | Phụ thuộc | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| V46 | Slide + tập phản biện + chạy thử demo trên máy hội đồng | Quân | Thắng, Trung | 14/12 |  | ⬜ Cần làm | Mỗi người trả lời trôi 5 câu về rò rỉ dữ liệu | V45 |  |
