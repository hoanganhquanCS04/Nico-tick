# Quản lý dự án

**Google Sheet (bản cập nhật hằng ngày):** _dán link vào đây sau khi tải `Nico-tick_QuanLyDuAn.xlsx` lên Drive_

| Người | Vai |
|---|---|
| **Quân** | Quản lý dự án · ML (bộ sinh công thức) |
| **Thắng** | Data · ML (RAG) · Dev (demo) |
| **Trung** | Quant (backtest, mô hình nhân tố, kiểm định) |

Phân công đang là **đề xuất**, sẽ chốt ở [họp khởi động 27/09](bien_ban/2026-09-27_khoi_dong.md).

## Có gì ở đây

| File | Nội dung | Ai sửa |
|---|---|---|
| [phan_cong.md](phan_cong.md) | Ai làm gì, ma trận Chính / Hỗ trợ / Duyệt theo pha | sinh từ Sheet |
| [viec.md](viec.md) | Toàn bộ việc: người phụ trách, hạn, trạng thái, "xong khi" | sinh từ Sheet |
| [rui_ro.md](rui_ro.md) | Sổ rủi ro: dấu hiệu sớm, cách phòng, phương án | sinh từ Sheet |
| [quyet_dinh.md](quyet_dinh.md) | Nhật ký quyết định: đã chốt gì, ai chốt, vì sao | sinh từ Sheet |
| [hop.md](hop.md) | Nhật ký các buổi họp | sinh từ Sheet |
| [bien_ban/](bien_ban/) | Chương trình và biên bản từng buổi họp | viết tay |
| `Nico-tick_QuanLyDuAn.xlsx` | Bản khởi tạo của Google Sheet, chỉ dùng để tải lên Drive lần đầu | — |
| `xlsx_to_md.py` | Sinh các file .md ở trên từ Sheet | — |

`docs/Timelines.xlsx` giữ nguyên làm **kế hoạch gốc**. Theo dõi hằng ngày dùng Sheet; cột **Hạn** trên
Sheet không bao giờ sửa, trễ thì điền **Hạn mới**, để luôn đo được mình lệch bao nhiêu so với kế hoạch gốc.

## Nhịp làm việc

**Hằng ngày.** Mỗi người check-in 3 câu (tab Check-in hoặc nhóm chat): hôm qua xong gì, hôm nay làm gì,
đang vướng gì. Quân đọc phần "vướng" và gỡ trong ngày.

**Hằng tuần (30 phút, giờ cố định).**
1. Tab Tổng quan: mốc nào sắp tới, ai đang có việc trễ hoặc kẹt.
2. Từng việc trễ / kẹt: vì sao, cần gì, hạn mới.
3. Chia việc tuần tới. Mỗi việc có đủ **1 người phụ trách · hạn · xong khi**.
4. Rủi ro đỏ (điểm ≥6): dấu hiệu sớm đã xuất hiện chưa.
5. Ghi 1 dòng vào tab Họp. Sau đó Quân đồng bộ sang repo (xem dưới).

**Họp thầy.** Gửi tài liệu và câu hỏi trước 1–2 ngày. Gửi biên bản trong 24 giờ sau họp, cập nhật tab
Quyết định. Người ghi biên bản luân phiên.

## Luật chơi

1. Mỗi việc đúng **1 người phụ trách**. Người khác là Hỗ trợ. Không có việc giao cho "cả nhóm".
2. Việc dài hơn 3 ngày thì tách nhỏ.
3. Đổi trạng thái ngay khi đổi, không đợi họp.
4. Kẹt quá 1 ngày: đặt **Kẹt**, ghi lý do, nhắn nhóm.
5. Không kịp hạn: điền **Hạn mới** + lý do, báo sớm. Trễ 2 ngày báo ngay thì còn xoay được.
6. Sau khoá đề cương 03/10: ý tưởng mới ghi "để sau". Chỉ thêm việc khi thầy yêu cầu hoặc cả nhóm
   đồng ý, và ghi vào tab Quyết định.
7. Đổi quyết định thì không xoá dòng cũ: đặt "Đã thay đổi" và thêm dòng mới.

## Đồng bộ Sheet → repo

Sau mỗi buổi họp tuần:

```
Google Sheet → Tệp → Tải xuống → Microsoft Excel (.xlsx)
python docs/pm/xlsx_to_md.py <file vừa tải>
git add docs/pm && git commit -m "pm: cập nhật sau họp tuần dd/mm"
```

Script chỉ dùng thư viện chuẩn. Nó tính lại cột Trễ và Điểm rủi ro theo ngày chạy
(`--today YYYY-MM-DD` để chạy cho ngày khác).
