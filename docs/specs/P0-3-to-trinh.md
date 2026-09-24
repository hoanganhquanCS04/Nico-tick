# SPEC — P0 Task 3: Tờ trình chốt mô hình (1 trang)

| | |
|---|---|
| **Người làm** | Cả nhóm |
| **Hạn** | 24/09/2026 |
| **Phụ thuộc** | Task 2 (bảng benchmark) cho khối 2; khối 1, 3, 5 viết trước được ngay |
| **Dùng cho** | Họp thầy 01/10 (task #4) · Chương 3 báo cáo (task #28 ghi rõ: *"phần căn cứ chọn mô hình lấy thẳng từ tờ trình task 3"*) |

> Ghi chú trong timeline: **"1 trang thôi. Bảng số + 3 dòng lý do."**

## 1. Mục tiêu

Đưa thầy **một trang A4** đủ để ra quyết định trong buổi họp 01/10, không phải một bản báo cáo con.
Tờ trình này phải làm được hai việc: chốt mô hình, và **gom hết câu hỏi phạm vi vào một buổi**
để không phải họp lần hai (timeline ghi rõ: *"Gộp 1 buổi, đừng tách 2 lần họp"*).

Viết xong tờ trình là gần như viết xong mục 3.3 của Chương 3. Đừng coi đây là việc hành chính.

---

## 2. Bố cục — đúng 5 khối, 1 trang

### Khối 1 — Bối cảnh (3 dòng, ~60 từ)

Nội dung phải có:
- Hệ thống cần một bộ **sinh** công thức, tức decoder-only. PhoBERT là encoder-only, không sinh được.
- Công thức tường minh là điều kiện của tính diễn giải — thứ phân biệt đề tài này với phương án trích embedding.
- Vì vậy cần một mô hình 1–3B, vượt ngưỡng "vài trăm triệu" thầy đã nêu.

Đặt vấn đề thẳng ngay dòng đầu. Thầy biết trước mình định xin gì thì đọc bảng sẽ nhanh hơn.

### Khối 2 — Bảng benchmark (nửa trang, phần chính)

Lấy thẳng từ `bench/table.md`:

| Mô hình | Tham số | VRAM đỉnh Q4 (MB) | tok/s | s/công thức hợp lệ | Hợp lệ (%) | Trùng (%) | Nghĩa KT (1–5) |
|---|---|---|---|---|---|---|---|

Dưới bảng, đúng 2 dòng chú thích:
1. Điều kiện đo: bộ thử N prompt × 3 seed, temperature 0,2, lượng tử NF4 4-bit, card `<tên card>`.
2. Định nghĩa "hợp lệ": parse được theo DSL ∧ mọi biến tồn tại ∧ không trùng dạng chuẩn hoá.

**Phải có sai số giữa các seed ở cột tỷ lệ hợp lệ.** Mục 4.2.d của đề cương tự cam kết
"báo cáo t-stat và sai số chuẩn, không chỉ báo cáo điểm ước lượng" — bảng đầu tiên mà đã
đưa một con số trần thì mất uy tín cho toàn bộ phần sau.

### Khối 3 — Lý do chốt (đúng 3 dòng)

Mỗi dòng một trục, mỗi dòng dẫn một con số **từ bảng phía trên**:
1. **Chất lượng:** tỷ lệ hợp lệ X% và điểm nghĩa kinh tế Y — cao nhất/đủ ngưỡng trong nhóm.
2. **Khả thi phần cứng:** VRAM đỉnh Z MB, vừa card 8GB sau lượng tử 4-bit.
3. **Chi phí và tái lập:** chi phí truy vấn bằng 0, revision hash cố định — không bị nhà cung cấp cập nhật ngầm làm mất tính tái lập.

Không viết dòng nào không dẫn được về số trong bảng.

### Khối 4 — Đánh đổi số tham số (1 đoạn, ~100 từ)

Đây là khối thầy sẽ đọc kỹ nhất. Phải cho thấy nhóm **hiểu** lập luận của thầy chứ không phải
đang lách nó:

- Thừa nhận: 1–3B vượt ngưỡng vài trăm triệu.
- Dẫn tiền lệ ủng hộ **quan điểm của thầy**: FinSeer 109M đánh bại E5-7B trên cả ba tập
  (Xiao et al. 2025); PhoBERT 135M đạt macro-F1 74,93% trong khi GPT-4 zero-shot chỉ 60,14%.
  Chuyên biệt hoá thắng dung lượng — nhóm đồng ý, và đó là lý do PhoBERT vẫn giữ vai encoder.
- Nêu ràng buộc kỹ thuật: encoder-only **không sinh được chuỗi**. Muốn có công thức tường minh
  thì bắt buộc phải có một decoder ở đâu đó trong kiến trúc.
- Chốt bằng số đo: sau lượng tử 4-bit, mô hình chạy hết Z MB trên card 8GB — chi phí thực tế
  của đánh đổi này là Z MB, không phải là một con số tham số trừu tượng.
- Nêu phương án thay thế đã cân nhắc và lý do loại: trích embedding thay vì sinh công thức →
  đúng ràng buộc quy mô nhưng **mất tính diễn giải**, mà diễn giải là điều kiện của HITL (task #17)
  và của truy vết nguồn.

### Khối 5 — Câu hỏi cần thầy quyết (gạch đầu dòng, để cuối trang)

Gom từ mục 6 của `GAP_research.pdf` — đây là phần biến tờ trình thành chương trình nghị sự
cho buổi 01/10:

**Kiến trúc**
- Chấp nhận bộ sinh 1–3B, hay chuyển sang trích embedding (mất tính diễn giải)?
- Có nên bỏ hẳn nhánh xử lý văn bản, chỉ dùng chỉ tiêu có cấu trúc, để giảm độ phức tạp?

**Phạm vi**
- Gộp ba nội dung (so sánh quy mô mô hình + kiểm soát rò rỉ + mô hình chi phí VN) có quá tải
  cho một đồ án không? Nếu cần tách, giữ nội dung nào làm chính?
- Có nên giới hạn ở một nhóm ngành?

**Dữ liệu** (câu hỏi gấp nhất — chặn CHỐT 1 ngày 13/10)
- Nguồn nào tại Việt Nam lưu **ngày công bố thực tế** của BCTC? Đây là điều kiện tiên quyết
  của toàn bộ nhánh point-in-time và của Bảng 2.
- Dữ liệu quý cho quá ít điểm thời gian (~40). Phương án bổ sung giá theo ngày (~2.500 điểm)
  có hợp lý không?

**Đánh giá**
- Mức chi phí giao dịch nào là hợp lý để mô phỏng thị trường VN?
- Khâu chuyên gia duyệt công thức nên để nhóm tự làm hay mời người có chuyên môn thực tế?

---

## 3. Quy tắc trình bày

| | |
|---|---|
| Độ dài | **1 trang A4**. Tràn sang trang 2 là hỏng mục đích |
| Font | Times New Roman 12 hoặc 13, giãn dòng 1,15 |
| Bảng | Chiếm khoảng nửa trang, là thứ đập vào mắt đầu tiên |
| Văn phong | Câu ngắn. Không tính từ. Mỗi khẳng định dẫn được về một con số hoặc một trích dẫn |
| Trích dẫn | Ghi số arXiv trực tiếp trong ngoặc, không cần mục tài liệu tham khảo riêng |

**Nếu phải cắt cho vừa 1 trang, cắt theo thứ tự này:** khối 1 → khối 4 → khối 5.
**Không bao giờ cắt khối 2 và khối 3.**

---

## 4. Trình tự làm

| Khi nào | Việc | Ai |
|---|---|---|
| 22/09 | Dựng khung `.docx` đủ 5 khối, viết khối 1 + khối 4 + khối 5 (không cần chờ số) | Cả nhóm |
| 23/09 | Rà soát khối 5 với `GAP_research.pdf` mục 6, bổ sung câu hỏi phát sinh từ task 1 | Cả nhóm |
| 24/09 sáng | Bảng benchmark xong → dán vào khối 2 | ML |
| 24/09 chiều | Viết khối 3 (3 dòng lý do, dẫn số từ bảng) | Cả nhóm |
| 24/09 chiều | Duyệt chéo, ép về 1 trang, xuất PDF | Cả nhóm |

Khối 4 viết trước được vì lập luận không phụ thuộc kết quả — chỉ có con số VRAM là chờ.
Chừa sẵn chỗ trống dạng `___ MB`.

---

## 5. Định nghĩa hoàn thành (DoD)

- [ ] Đúng 1 trang A4, xuất cả `.docx` và `.pdf` tại `docs/to_trinh_chot_mo_hinh.*`
- [ ] Bảng benchmark có sai số giữa seed, có 2 dòng chú thích điều kiện đo
- [ ] 3 dòng lý do, mỗi dòng dẫn được về một con số trong bảng
- [ ] Khối đánh đổi có dẫn FinSeer và PhoBERT — chứng minh nhóm hiểu lập luận của thầy
- [ ] Khối câu hỏi phủ đủ 4 nhóm: kiến trúc, phạm vi, dữ liệu, đánh giá
- [ ] Toàn nhóm đã đọc và thống nhất — người thuyết trình trả lời được câu *"vì sao không dùng mô hình nhỏ hơn?"* mà không cần mở tờ trình

## 6. Chuẩn bị thêm cho buổi họp 01/10

Không nằm trong 1 trang, nhưng mang theo — thầy hỏi thì mở ra:

- `bench/table.md` bản đầy đủ (gồm dòng tách nhóm tài chính/phi tài chính)
- 5–10 công thức mẫu đẹp nhất mà mô hình được chọn sinh ra, kèm truy vết nguồn.
  **Đây là thứ thuyết phục nhất.** Một bảng số nói mô hình chạy được; một công thức đọc lên
  thấy có nghĩa kinh tế nói mô hình *dùng được*.
- Danh sách lỗi hay gặp nhất của mô hình (từ trường `reasons` của validator) — trả lời trước
  câu hỏi "mô hình nhỏ sinh sai nhiều thì xử lý sao", và dẫn thẳng sang validator + HITL trong kiến trúc.
- Mốc 03/10 khoá đề cương: nhắc thầy rằng sau buổi này nhóm sẽ không đổi phạm vi nữa,
  nên mọi điều chỉnh cần nói trong hôm nay.
