# P0: CHỐT MÔ HÌNH — Bóc tách công việc

Cửa sổ thời gian: 19/09 → **24/09/2026** (hôm nay 22/09, còn 3 ngày).
Họp thầy: 01/10 (task #4) → có 7 ngày đệm nếu benchmark hỏng phải chạy lại.
Nguồn: `docs/GAP_research.pdf` (mục 3.3, 3.4, 6), `docs/Timelines.xlsx` (task 1–3, 15).

---

## TASK 1 — Bộ thử: 15–20 BCTC mẫu + 60–80 prompt  (ML)

| # | Việc | Ước lượng | Đầu ra | Xong khi |
|---|------|-----------|--------|----------|
| 1.1 | Chọn mẫu 15–20 mã, phân tầng theo ngành × vốn hoá | 1h | `data/sample/tickers.csv` (mã, sàn, ngành, vốn hoá, lý do chọn) | Có ≥4 ngành phi tài chính + 2–3 mã ngân hàng/chứng khoán đánh dấu riêng |
| 1.2 | Tải BCTC mẫu từ HF `tinixai/ocr_annual_financials` | 1–2h | `data/sample/raw/<ticker>/<year>/*.txt` (+3–5 PDF để đối chiếu) | Kéo đúng mẫu đã chọn, **không** tải cả 194GB |
| 1.3 | Chuẩn hoá danh mục biến (bảng số + đoạn thuyết minh) | 3–4h | **`config/variables.yaml`** ~40–60 biến: tên canonical, mô tả, đơn vị, nguồn dòng BCTC | Mỗi biến map được về ít nhất 12/20 DN mẫu |
| 1.4 | Viết 60–80 prompt, chia 4 họ | 4h | `eval/prompts.jsonl` | Đủ 60–80 dòng, mỗi dòng có `id, family, ticker, context, instruction, allowed_vars` |
| 1.5 | Rubric chấm + bộ chấm tay | 1–2h | `eval/rubric.md` + `eval/manual_scores.csv` | Rubric có 4 tiêu chí, 2 người chấm thử 10 mẫu lệch ≤1 điểm |

**Chi tiết 1.3 — đây là task quan trọng nhất của cả P0.** `variables.yaml` là thứ mà prompt (1.4), validator (task #15) và mô hình nhân tố (P5) đều ăn theo. Làm ẩu ở đây thì hỏng dây chuyền. Đặt tên biến bằng tiếng Anh snake_case (`total_assets`, `cfo`, `inventory`, `receivables`, `interest_expense`, `ebit`...), mỗi biến ghi rõ lấy từ dòng nào của BCTC Việt Nam (mã số chỉ tiêu VAS).

**Chi tiết 1.4 — 4 họ prompt** (mỗi họ 15–20 prompt):
- **F1 — Structured-only**: chỉ đưa danh mục biến, yêu cầu sinh công thức. Đây là nhánh đối chứng cho H2.
- **F2 — Notes-augmented**: đưa kèm 1–2 đoạn thuyết minh thật. Đây là nhánh chính, nuôi giả thuyết H2 (giá trị gia tăng của thuyết minh).
- **F3 — Few-shot**: 2–3 ví dụ công thức mẫu (ví dụ `accruals = (net_income - cfo) / total_assets`).
- **F4 — Constrained format**: ép output đúng JSON/DSL, để đo mô hình nhỏ có giữ được format không. Nếu task #18 (GO/NO-GO tỷ lệ hợp lệ ≥60%) trượt, đây là phương án cứu — nên phải có số từ bây giờ.

**Chi tiết 1.5** — không có ground-truth công thức, nên chấm theo 4 tiêu chí: (a) parse được AST, (b) biến tồn tại trong `variables.yaml`, (c) không trùng công thức đã sinh, (d) có nghĩa kinh tế (người chấm 1–5). (a)(b)(c) tự động, (d) chấm tay.

---

## TASK 2 — Benchmark mô hình  (ML) — *căn cứ đi báo thầy*

| # | Việc | Ước lượng | Đầu ra | Xong khi |
|---|------|-----------|--------|----------|
| 2.1 | Chốt danh sách ứng viên (3–4 mô hình, không hơn) | 30′ | 1 dòng trong `bench/README.md` | Có bản neo Qwen2.5-1.5B + 3B |
| 2.2 | Dựng môi trường suy luận + lượng tử 4-bit | 2–3h | `bench/run_infer.py` | Sinh được 1 công thức từ mỗi mô hình, log VRAM |
| 2.3 | **Validator v0** (bản tối giản của task #15) | 2h | `bench/validator.py` | Parse AST + kiểm tra biến + khử trùng theo chuỗi chuẩn hoá |
| 2.4 | Chạy benchmark: N mô hình × 60–80 prompt × 3 seed | 3–5h máy | `bench/raw/*.jsonl` | Log đủ: output thô, thời gian, token, VRAM đỉnh |
| 2.5 | Tổng hợp bảng + 1 biểu đồ | 1–2h | `bench/results.csv` + `bench/table.md` | Đúng 4 cột thầy cần xem |
| 2.6 | Chấm tay tiêu chí (d) trên 20 output ngẫu nhiên/mô hình | 1h | cập nhật `manual_scores.csv` | Đủ để nói mô hình nào "sinh công thức có nghĩa" |

**Cột bắt buộc của bảng kết quả** (đây là thứ thầy nhìn vào):

| Mô hình | Tham số | VRAM đỉnh (Q4) | Tốc độ (tok/s, s/công thức) | Tỷ lệ hợp lệ (%) | Tỷ lệ trùng (%) | Điểm nghĩa KT (1–5) |
|---|---|---|---|---|---|---|

**2.1 — đề xuất danh sách** (chốt gọn, đừng benchmark 8 mô hình):
- `Qwen2.5-1.5B-Instruct` — mốc neo dưới, đã ghi trong đề cương
- `Qwen2.5-3B-Instruct` — mốc neo trên, giới hạn 8GB VRAM sau Q4
- 1 mô hình tiếng Việt: `PhoGPT-4B-Chat` **hoặc** `Vistral-7B` (7B Q4 ~4.5GB, vẫn vừa 8GB)
- 1 mô hình mới nhóm đang nhắm — **cần điền tên**

**Kỷ luật đo** (thiếu là bảng mất giá trị): cố định seed, `temperature=0.2`, `max_new_tokens` như nhau, cùng 1 template prompt, cùng 1 máy. VRAM đo bằng `torch.cuda.max_memory_allocated()` **và** `nvidia-smi` đỉnh, ghi cả hai.

---

## TASK 3 — Tờ trình 1 trang  (cả nhóm)

| # | Việc | Ước lượng | Đầu ra |
|---|------|-----------|--------|
| 3.1 | Dựng khung 1 trang (làm trước khi có số) | 1h | `docs/to_trinh_chot_mo_hinh.docx` |
| 3.2 | Điền bảng benchmark từ `bench/table.md` | 30′ | — |
| 3.3 | Gộp câu hỏi phạm vi cho buổi họp 01/10 | 1h | mục cuối tờ trình |

**Bố cục 1 trang — đúng 5 khối:**
1. 3 dòng bối cảnh: cần bộ sinh công thức decoder-only, không thể dùng encoder.
2. **Bảng benchmark** (chiếm nửa trang).
3. 3 dòng lý do chốt mô hình X.
4. 1 đoạn đánh đổi tham số: vì sao vượt ngưỡng "vài trăm triệu" thầy nêu → dẫn số VRAM đo được để chứng minh vẫn chạy trên 1 card 8GB; dẫn tiền lệ FinSeer 109M thắng E5-7B (chuyên biệt hoá > dung lượng) để cho thấy nhóm hiểu lập luận của thầy, nhưng encoder không sinh được công thức.
5. **Câu hỏi cần thầy quyết** — gom từ mục 6 của `GAP_research.pdf` để họp 01/10 chỉ mất 1 buổi:
   - Chấp nhận bộ sinh 1–3B, hay chuyển sang trích embedding (mất tính diễn giải)?
   - Giữ hay bỏ nhánh văn bản (thuyết minh)?
   - Giới hạn 1 nhóm ngành?
   - Nguồn nào lưu **ngày công bố thực tế** BCTC? (điều kiện tiên quyết của Bảng 2 / H3)

---

## Lịch 3 ngày

| Ngày | ML | Cả nhóm |
|------|----|---------|
| **22/09 (hôm nay)** | 1.1, 1.2 · song song 2.1, 2.2 (tải model, dựng môi trường — không phụ thuộc bộ thử) | 3.1 dựng khung tờ trình |
| **23/09** | 1.3 (`variables.yaml`) → 1.4 (prompt) → 2.3 (validator v0) | 3.3 soạn câu hỏi cho thầy |
| **24/09** | 2.4 chạy → 2.5 bảng → 2.6 + 1.5 chấm tay | 3.2 điền số, duyệt chéo, chốt |

Đường găng: **1.3 → 1.4 → 2.4**. Nếu 1.3 trượt sang 23/09 chiều thì cắt prompt xuống 60 (mức sàn), đừng cắt số mô hình.

---

## Cảnh báo cần biết trước khi bắt tay

1. **Dataset HF là báo cáo NĂM, không phải QUÝ.** `tinixai/ocr_annual_financials`: 18.231 báo cáo, 1.491 mã, 2015–2025, PDF + TXT OCR, 194GB, có thuyết minh, OCR ~95% với số liệu. Dùng tốt cho P0 (mẫu để viết prompt) nhưng **không thay được P1** (BCTC quý ~200 DN × 10 năm, task #6). Đừng để cả nhóm tưởng P1 đã xong.
2. **Không có ngày công bố thực tế** trong dataset này → task #7 vẫn phải làm, và nó là điều kiện sống còn của Bảng 2 / giả thuyết H3.
3. **License CC BY-NC 4.0** — dùng cho đồ án học thuật thì được, nhưng phải trích nguồn trong báo cáo và không được thương mại hoá demo.
4. **Validator là dependency ẩn.** Task #15 hạn 21/10, nhưng task 2 cần nó ngay hôm nay → phải làm bản v0 (mục 2.3). Task #15 sau này chỉ là nâng cấp (khử trùng theo tương quan), không viết lại.
5. **Phần cứng.** Cần xác nhận card thật đang có. 3B ở Q4_K_M ~2GB trọng số nhưng tốn thêm KV-cache; 8GB là vừa. Không có GPU thì lên Colab/Kaggle T4, nhưng khi đó **số VRAM đo được không còn là bằng chứng cho tờ trình** — phải đo trên đúng card sẽ dùng.
