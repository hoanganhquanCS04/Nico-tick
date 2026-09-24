# SPEC — P0 Task 2: Benchmark mô hình sinh công thức

| | |
|---|---|
| **Người làm** | ML |
| **Hạn** | 24/09/2026 |
| **Phụ thuộc** | Task 1 (bộ thử). Việc 2.1–2.2 chạy song song được ngay |
| **Chặn** | Task 3 (tờ trình), họp thầy 01/10 |

> Ghi chú trong timeline: **"CĂN CỨ ĐI BÁO THẦY. Không có bảng này thì đừng họp."**

## 1. Mục tiêu

Trả lời đúng một câu hỏi: **chốt mô hình nào làm bộ sinh công thức?**
Và trả lời bằng số đo trên phần cứng thật, không bằng thông số trên model card.

**Trong phạm vi:** đo tỷ lệ công thức hợp lệ, tốc độ sinh, VRAM sau lượng tử 4-bit trên 3–4 ứng viên.
**Ngoài phạm vi:** IC, Sharpe, backtest (P5) · fine-tune (không có trong kế hoạch) ·
baseline API (P6, task #22 — mẫu con 50 DN × 3 năm).

---

## 2. Việc 2.1 — Chốt danh sách ứng viên

**Ba đến bốn mô hình, không hơn.** Thêm mô hình thứ năm không làm bảng thuyết phục hơn,
chỉ làm hết giờ.

| Vai | Mô hình | Lý do |
|---|---|---|
| Neo dưới | `Qwen2.5-1.5B-Instruct` | Đã ghi trong đề cương, mốc so sánh bắt buộc |
| Neo trên | `Qwen2.5-3B-Instruct` | Mốc trên của dải 1–3B, kiểm chứng ràng buộc 8GB |
| Tiếng Việt | `PhoGPT-4B-Chat` **hoặc** `Vistral-7B-Chat` | Đề cương nêu tên; 7B ở Q4_K_M ~4,5GB vẫn vừa 8GB |
| **Ứng viên mới** | **`<CẦN ĐIỀN>`** | Mô hình nhóm đang nhắm — task ghi "mô hình mới muốn chốt" |

**Chưa điền được ô thứ tư thì benchmark vẫn chạy được với 3 mô hình**, nhưng tờ trình sẽ yếu:
cả bảng chỉ còn là so sánh nội bộ họ Qwen. Chốt tên trong ngày 22/09.

Ghi lại **revision hash** của mỗi mô hình trên HuggingFace. Đây là điều kiện tái lập, và cũng
là luận điểm của đề tài: *mô hình tự triển khai có mốc huấn luyện biết chính xác và cố định,
khác API có thể bị cập nhật ngầm.* Không ghi hash thì mất chính luận điểm mình đang bán.

---

## 3. Việc 2.2 — Môi trường suy luận

**Lượng tử hoá 4-bit, hai đường:**

| Đường | Công cụ | Ưu | Nhược |
|---|---|---|---|
| A | `llama.cpp` + GGUF `Q4_K_M` | Đo VRAM sạch, chạy được cả khi GPU yếu | Phải tìm/convert GGUF cho từng mô hình |
| B | `transformers` + `bitsandbytes` NF4 | Cài nhanh, dùng thẳng repo HF | VRAM đo nhiễu hơn do cache của PyTorch |

Đề xuất: **đường B** cho P0 (nhanh, đủ để so sánh tương đối vì mọi mô hình đo cùng cách),
ghi rõ trong tờ trình là đo bằng NF4 của bitsandbytes. Nếu còn thời gian thì đối chiếu thêm 1 mô hình bằng đường A.

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch

bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)
```

**Đo VRAM — ghi cả hai con số:**
- `torch.cuda.max_memory_allocated()` sau khi reset đỉnh → phần model + KV-cache thực sự dùng
- đỉnh `nvidia-smi` quan sát trong lúc chạy → phần thực tế chiếm trên card, gồm cả phân mảnh

Hai số này lệch nhau là bình thường. Tờ trình dùng số `nvidia-smi` (đó mới là thứ quyết định
mô hình có chạy vừa card 8GB hay không), số PyTorch để đối chiếu.

**Bỏ lần chạy đầu (warm-up)** khỏi phép đo tốc độ.

---

## 4. Việc 2.3 — Validator v0

Đây là bản tối giản của task #15 (hạn 20/10). Làm v0 bây giờ, P4 chỉ nâng cấp, **không viết lại**.

**Đầu vào:** chuỗi công thức + `config/variables.yaml`
**Đầu ra:** `{valid: bool, reasons: [str], canonical: str, depth: int, n_vars: int}`

**Chuỗi kiểm tra:**

| # | Kiểm tra | Lỗi trả về |
|---|---|---|
| 1 | Output của mô hình parse được thành JSON | `json_parse_error` |
| 2 | Có đủ trường `name`, `formula`, `rationale`, `source` | `missing_field:<tên>` |
| 3 | `formula` parse được thành AST theo DSL | `syntax_error` |
| 4 | Mọi tên biến ∈ `variables.yaml` | `unknown_var:<tên>` |
| 5 | Mọi hàm ∈ whitelist, đúng số tham số | `unknown_func` / `bad_arity` |
| 6 | Mọi tham số `k` ∈ {1,2,4,8} | `bad_lag` |
| 7 | Không có phép `/` trần (phải dùng `safe_div`) | `raw_division` |
| 8 | Độ sâu AST ≤ 6, số biến khác nhau ≤ 6 | `too_complex` |
| 9 | Có ít nhất 1 biến (không phải hằng số thuần) | `constant_only` |
| 10 | `canonical` chưa xuất hiện trong lô | `duplicate` |

**Dạng chuẩn hoá (`canonical`)** để khử trùng: dựng lại chuỗi từ AST, sắp xếp toán hạng của
phép giao hoán (`+`, `*`) theo thứ tự chữ cái, bỏ khoảng trắng.
Nhờ vậy `a+b` và `b+a` bị coi là một.

> Bản P4 sẽ thay bước 10 bằng khử trùng **theo tương quan** (|corr| > 0,95 trên dữ liệu thật).
> P0 chưa có dữ liệu quý nên dùng trùng theo chuỗi — ghi rõ giới hạn này trong tờ trình.

Cách làm gọn nhất: dùng `ast.parse` của Python rồi duyệt cây với whitelist node type
(`Expression`, `BinOp`, `Call`, `Name`, `Constant`, `Add/Sub/Mult/Div`, `USub`), chặn tất cả node khác.
Không dùng `eval`.

---

## 5. Việc 2.4 — Giao thức chạy

**Cố định tuyệt đối giữa các mô hình** (khác một thứ là bảng mất giá trị so sánh):

| Tham số | Giá trị |
|---|---|
| Seed | 3 seed: 0, 1, 2 |
| `temperature` | 0,2 |
| `top_p` | 0,9 |
| `max_new_tokens` | 512 |
| Số công thức/prompt | 3 (`n_formulas` trong bộ thử) |
| System prompt | Một bản duy nhất, lưu ở `bench/system_prompt.txt` |
| Máy | Một máy duy nhất cho toàn bộ phép đo |

**Quy mô:** 4 mô hình × 70 prompt × 3 seed = 840 lượt gọi ≈ 2.520 công thức.
Ước tính 3–5 giờ máy. Chạy nền, đừng ngồi canh.

**Schema `bench/raw/<model>__seed<k>.jsonl`** — một dòng mỗi lượt gọi:

```json
{
  "prompt_id": "F2-007",
  "model": "Qwen2.5-3B-Instruct",
  "revision": "<hash>",
  "seed": 0,
  "raw_output": "<nguyên văn chuỗi mô hình trả về>",
  "formulas": [{"name": "...", "formula": "...", "rationale": "...", "source": {...}}],
  "validation": [{"valid": true, "reasons": [], "canonical": "..."}],
  "n_prompt_tokens": 1843,
  "n_gen_tokens": 312,
  "latency_s": 8.4,
  "vram_peak_mb": 5912
}
```

**Giữ `raw_output` nguyên văn.** Khi bảng ra kết quả lạ, thứ duy nhất cứu được là log thô.

---

## 6. Việc 2.5 — Bảng kết quả

**Định nghĩa từng chỉ số** (viết vào `bench/README.md`, đừng để người đọc đoán):

| Chỉ số | Công thức |
|---|---|
| `json_rate` | số lượt parse được JSON / tổng số lượt gọi |
| `valid_rate` | số công thức qua C1∧C2∧C3 / tổng số công thức sinh ra |
| `dup_rate` | 1 − (số `canonical` duy nhất / số công thức qua C1∧C2) |
| `tok_per_s` | tổng token sinh ra / tổng thời gian sinh |
| `s_per_valid` | tổng thời gian / số công thức **hợp lệ** |
| `vram_peak_mb` | đỉnh `nvidia-smi` trong toàn bộ lượt chạy |
| `c4_mean` | điểm nghĩa kinh tế trung bình trên 20 mẫu ngẫu nhiên |

`s_per_valid` quan trọng hơn `tok_per_s`. Một mô hình nhanh nhưng sinh 70% rác thì đắt hơn
mô hình chậm mà sạch — và đây đúng là luận điểm "chuyên biệt hoá thắng dung lượng" của đề tài.

**Bảng cuối cùng đưa vào tờ trình:**

| Mô hình | Tham số | VRAM đỉnh Q4 (MB) | tok/s | s/công thức hợp lệ | Hợp lệ (%) | Trùng (%) | Nghĩa KT (1–5) |
|---|---|---|---|---|---|---|---|

Kèm **sai số giữa 3 seed** (min–max hoặc ±sd) cho cột `valid_rate`. Báo cáo một con số trần
mà không có biến thiên là đúng lỗi mà mục 4.2.d của đề cương đã tự nhận diện —
đừng mắc ngay ở bảng đầu tiên.

**Tách riêng 2 dòng phụ:** tỷ lệ hợp lệ trên nhóm phi tài chính và trên nhóm ngân hàng/chứng khoán
(cờ `is_financial` trong `tickers.csv`).

Một biểu đồ duy nhất: trục x = VRAM, trục y = `valid_rate`, kích thước điểm = `s_per_valid`.
Nhìn phát thấy ngay mô hình nào ở biên hiệu quả.

---

## 7. Việc 2.6 — Chấm tay C4

20 công thức ngẫu nhiên/mô hình (tổng 80), 2 người chấm độc lập theo `eval/rubric.md`,
**giấu tên mô hình** khi chấm — nếu không thì thiên kiến về mô hình mình muốn chọn sẽ vào thẳng bảng.

Ghi vào `eval/manual_scores.csv`. Báo cáo cả mức đồng thuận giữa 2 người chấm.

---

## 8. Định nghĩa hoàn thành (DoD)

- [ ] `bench/README.md` ghi rõ: danh sách mô hình + revision hash, cấu hình lượng tử, phần cứng, định nghĩa từng chỉ số
- [ ] `bench/raw/` đủ file cho mọi cặp (mô hình × seed)
- [ ] `bench/results.csv` + `bench/table.md` đủ 8 cột, có sai số giữa seed
- [ ] Có 2 dòng tách nhóm tài chính / phi tài chính
- [ ] 80 công thức đã chấm C4 mù, ghi mức đồng thuận
- [ ] 1 biểu đồ VRAM × tỷ lệ hợp lệ
- [ ] Trả lời được thành câu: *"Chốt mô hình X vì …, đánh đổi là …"*

## 9. Rủi ro

| Rủi ro | Xử lý |
|---|---|
| **Chưa biết card đồ hoạ thật** | Phải xác nhận trong ngày 22/09. Nếu chạy Colab/Kaggle T4 thì số VRAM **không còn là bằng chứng cho tờ trình** — phải đo lại trên card sẽ dùng thật, hoặc nói rõ trong tờ trình là đo trên T4 16GB |
| Tỷ lệ hợp lệ cả 4 mô hình đều thấp (<30%) | Không đổi mô hình. Kiểm tra prompt F4 (constrained) trước — rất có thể là lỗi format chứ không phải lỗi năng lực. Đây chính là tình huống CHỐT 2 đã dự liệu |
| Hết giờ ngày 24/09 | Cắt xuống **2 seed**, giữ đủ 4 mô hình. Số mô hình quan trọng hơn số seed với bảng này |
| PhoGPT/Vistral không có sẵn GGUF hoặc lỗi tokenizer | Bỏ, ghi lý do vào tờ trình. "Đã thử, không chạy được trên ràng buộc phần cứng" cũng là một kết quả và thầy chấp nhận được |
| Benchmark hỏng phải chạy lại | Còn 7 ngày đệm trước họp 01/10 — nhưng chỉ dùng đệm này cho task 2, không dùng cho task 1 |
