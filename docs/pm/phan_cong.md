# Phân công

> Sinh tự động từ Google Sheet bằng `docs/pm/xlsx_to_md.py` ngày 26/09/2026. **Đừng sửa tay** — sửa trên Sheet rồi chạy lại script.

## Ai làm gì

| Người | Vai chính | Vai phụ | Phụ trách chính (pha) | Hỗ trợ (pha) | Trách nhiệm cụ thể |
|---|---|---|---|---|---|
| Quân | Quản lý dự án (PM) · ML: bộ sinh công thức | Liên lạc GVHD · gom báo cáo | P0, P4, P6 (baseline API) · chủ trì 3 mốc GO/NO-GO | P3, P5, P8 | Kế hoạch & tiến độ, họp tuần, liên lạc thầy; benchmark, validator, GCD, sinh công thức, baseline API; gom Chương 3 và bản nộp |
| Thắng | Data | ML: RAG · Dev: demo · chủ trì Chương 1–2 | P1, P3, P6 (ablation, demo) | P0 (duyệt tờ trình), P4 (chủ trì HITL), P8 | Crawl BCTC quý, ngày công bố, giá ngày; chunk thuyết minh + PhoBERT + đánh giá truy xuất; demo Streamlit; duyệt công thức; format báo cáo |
| Trung | Quant | Chủ trì Chương 4–5 | P2, P5, P7 | P0 (chấm C4), P1 (định dạng giá), P4 (HITL), P8 | Backtest, mô hình chi phí VN, baseline thủ công, bộ tính công thức → số; point-in-time, LightGBM/MLP, Bảng 1/2/3; kiểm định thống kê |

## Ma trận theo pha

**Chính** = chịu trách nhiệm kết quả của pha · **Hỗ trợ** = làm một phần theo yêu cầu người Chính · **Duyệt** = xem và đồng ý đầu ra trước khi đóng pha. Ở mức từng việc, mỗi việc chỉ có 1 người phụ trách.

| Pha | Nội dung | Hạn | Quân | Thắng | Trung | Ghi chú |
|---|---|---|---|---|---|---|
| P0 | Chốt mô hình | 03/10 | Chính | Hỗ trợ | Hỗ trợ | Thắng duyệt tờ trình; Trung chấm C4, ghi biên bản họp thầy |
| P1 | Dữ liệu | 12/10 · CHỐT 1: 13/10 | Duyệt | Chính | Hỗ trợ | Trung quy định định dạng giá cho backtest |
| P2 | Hạ tầng đánh giá | 19/10 | Hỗ trợ | Hỗ trợ | Chính | Quân: parser DSL dùng chung; Thắng: dữ liệu giá |
| P3 | Encoder + RAG | 26/10 | Duyệt | Chính | — |  |
| P4 | Sinh công thức | 02/11 · CHỐT 2: 03/11 | Chính | Hỗ trợ | Hỗ trợ | Thắng chủ trì duyệt HITL — người sinh công thức không tự duyệt |
| P5 | Mô hình nhân tố | 16/11 | Duyệt | — | Chính |  |
| P6 | Đối chứng + demo | 23/11 | Chính | Chính | — | Quân: baseline API · Thắng: ablation, demo |
| P7 | Kiểm định | 30/11 | Duyệt | — | Chính |  |
| P8 | Báo cáo | 14/12 | Chính | Hỗ trợ | Hỗ trợ | Quân: Ch.3 + gom · Thắng: Ch.1–2, format · Trung: Ch.4–5 |
| P9 | Bảo vệ | sau 14/12 | Chính | Hỗ trợ | Hỗ trợ |  |
