# Benchmark bộ sinh công thức (P0, task 2)

Trả lời một câu: **chốt mô hình nào làm bộ sinh công thức**, bằng số đo trên phần cứng thật.
Spec: [docs/specs/P0-2-benchmark.md](../docs/specs/P0-2-benchmark.md).

## Cấu trúc thư mục

```
bench/
├─ README.md                  file này
├─ kaggle_benchmark.ipynb     chạy trên Kaggle (cách chính)
├─ config/                    ĐẦU VÀO - sửa ở đây để đổi thí nghiệm
│  ├─ models.yaml             ứng viên + revision đã ghim + cấu hình sinh chung
│  └─ system_prompt.txt       system prompt chung (sinh từ src/eval/build_prompts.py, không sửa tay)
├─ scripts/                   CODE
│  ├─ run_infer.py            chạy 1 mô hình trên bộ thử → results/raw/
│  ├─ validator.py            kiểm tra công thức (validator v0)
│  ├─ score.py                chấm điểm → results/table.md, metrics.csv, formulas.csv
│  └─ inspect_formulas.py     soi ngữ nghĩa công thức 1 mô hình → results/formulas_<model>.md
└─ results/                   ĐẦU RA - sinh lại được từ raw/, không sửa tay
   ├─ raw/                    output thô từng lượt gọi (không commit)
   ├─ logs/                   log chạy trên Kaggle
   ├─ smoke/                  lần chạy thử 2 prompt / mô hình
   ├─ table.md                BẢNG CHÍNH cho tờ trình
   ├─ metrics.csv             chỉ số theo (cách parse, mô hình, seed)
   ├─ formulas.csv            mọi công thức đã chấm
   └─ formulas_<model>.md     công thức của từng mô hình, phân loại theo chủ đề và lỗi
```

Mọi lệnh chạy từ thư mục gốc repo (`Nico-tick/`).

## Ứng viên

Cấu hình đầy đủ và lý do chọn ở [config/models.yaml](config/models.yaml). Revision ghim ngày 24/09/2026.

| Slot | key | Mô hình | Revision | Ghi chú |
|---|---|---|---|---|
| 1 | `qwen35-2b` | Qwen/Qwen3.5-2B | `15852e8c` | Lai linear + full attention; chỉ nạp phần văn bản |
| 2 | `gemma4-e2b-plecpu` | google/gemma-4-E2B-it | `3e22461f` | 5,1 tỷ tham số tổng, 2,35 tỷ là per-layer embedding → để trên CPU |
| 3 | `qwen35-0.8b` | Qwen/Qwen3.5-0.8B | `2fc06364` | Cận dưới kích thước, cùng họ với slot 1 |
| 4 | `sailor2-1b` | sail/Sailor2-1B-Chat | `51b48ecd` | Chuyên biệt tiếng Việt/ĐNA, context 4096 |
| ref | `gemma4-e2b-gpu` | google/gemma-4-E2B-it | `3e22461f` | Chỉ đo VRAM khi KHÔNG tách PLE (10 prompt, 1 seed) |

Cả 4 mô hình không gated, license Apache 2.0.

## Giao thức đo (cố định cho mọi mô hình)

| Tham số | Giá trị |
|---|---|
| Bộ thử | `eval/prompts.jsonl`: 76 prompt (F1 17, F2 25, F3 19, F4 15), 3 công thức/prompt |
| System prompt | `bench/config/system_prompt.txt`, một bản duy nhất |
| Seed | 0, 1, 2 (đặt lại trước MỖI lượt gọi) |
| Sinh | temperature 0,2 · top_p 0,9 · top_k tắt · repetition_penalty 1,0 · max_new_tokens 512 |
| Lượng tử | bitsandbytes NF4 + double quant, compute float16 |
| Mẫu chat | `enable_thinking=False` (Qwen3.5 mặc định bật thinking) |
| Phần cứng | Kaggle, GPU T4 16GB; mỗi mô hình chạy trọn trên một card |

Tham số sinh ghi đè generation_config riêng của từng mô hình (Gemma mặc định top_k=64, Sailor2
mặc định repetition_penalty=1,1). Điều kiện dừng gồm cả eos của mô hình lẫn eos của mẫu chat.

## Chỉ số

| Chỉ số | Cách tính |
|---|---|
| `yield` (**chỉ số chính**) | số công thức qua C1∧C2∧C3 / số công thức **đã yêu cầu** (3 × số lượt). Lượt hỏng JSON = 0, không bị loại khỏi mẫu số. Báo trung bình ± độ lệch chuẩn giữa 3 seed |
| `yield` (cứu JSON) | như trên, nhưng gom lại công thức từ output vỡ vỏ JSON (`extract_json_lenient`). Tách năng lực viết công thức khỏi lỗi định dạng |
| `valid_of_parsed` | hợp lệ / số công thức **đọc được**. Chỉ để tham khảo: mô hình hỏng format càng nhiều càng được lợi |
| `usable_yield` | hợp lệ **và** có chuẩn hoá quy mô (tỷ số, tăng trưởng, xếp hạng) / yêu cầu. `total_assets + total_liabilities` hợp lệ cú pháp nhưng chỉ đo quy mô |
| `json_rate` | số lượt parse được JSON đúng yêu cầu / tổng số lượt gọi |
| `dup_rate` | 1 − (số `canonical` duy nhất / số công thức qua C1∧C2), trong từng lượt chạy (mô hình × seed); dòng gộp = trung bình các seed |
| `tok_per_s` | tổng token sinh ra / tổng thời gian sinh (gồm cả prefill) |
| `s_per_valid` | tổng thời gian / số công thức **hợp lệ**. Quan trọng hơn tok/s: nhanh mà sinh rác thì vẫn đắt |
| VRAM ước tính cần | đỉnh `torch.cuda.max_memory_allocated()` + ngữ cảnh CUDA đo lúc nạp (~600 MB). **Con số đưa vào tờ trình** |
| `vram_nvml_peak_mb` | đỉnh bộ nhớ cả card (NVML). Chỉ tham khảo: trên T4 16GB bộ cấp phát PyTorch giữ lại bộ nhớ nên con số phình theo prompt dài nhất |
| `c4_mean` | điểm nghĩa kinh tế 1–5, chấm tay mù 20 công thức/mô hình (`eval/c4_blind.csv`) |

**Hợp lệ** = C1 (parse được theo DSL: đúng hàm, đúng số tham số, k ∈ {1,2,4,8}, không có `/` trần,
độ sâu ≤ 6, ≤ 6 biến, không phải hằng số) ∧ C2 (mọi biến có trong `config/variables.yaml`)
∧ C3 (không trùng dạng chuẩn hoá; chép lại ví dụ mẫu của F3 cũng tính là trùng). Mã lỗi: `scripts/validator.py`.

Giới hạn cần ghi trong tờ trình: C3 hiện khử trùng theo chuỗi chuẩn hoá. P4 sẽ thay bằng khử trùng
theo tương quan (|corr| > 0,95) khi có dữ liệu quý.

## Chạy

**Kaggle** (cách chính): mở [kaggle_benchmark.ipynb](kaggle_benchmark.ipynb), chọn GPU T4 x2 và bật
Internet. Notebook clone nhánh `quan_dev`, nên phải **push `bench/` + `eval/` lên trước**.
Chạy thử 2 prompt/mô hình trước (ô 3), sau đó chạy thật với 2 hàng đợi song song trên 2 card.

**Máy local:**

```bash
python bench/scripts/run_infer.py --model qwen35-2b                       # đủ bộ thử x 3 seed
python bench/scripts/run_infer.py --model qwen35-2b --seeds 0 --limit 2   # chạy thử
python bench/scripts/run_infer.py --model qwen35-0.8b --quant none        # máy chưa có bitsandbytes
python bench/scripts/score.py --c4-sample                                 # chấm + bảng + mẫu chấm tay mù
python bench/scripts/inspect_formulas.py --model gemma4-e2b-plecpu        # soi công thức 1 mô hình
```

Chạy lại cùng lệnh sẽ tự bỏ qua các lượt đã có trong `bench/results/raw/`, nên bị ngắt giữa chừng thì cứ chạy lại.
Trên Windows mà HF không tạo được symlink thì tải trước bằng `snapshot_download(..., local_dir=...)`
rồi truyền `--local-path`.

## Đầu ra

| File | Nội dung |
|---|---|
| `results/raw/<key>__seed<k>.jsonl` | Một dòng / lượt gọi: output thô nguyên văn, token, thời gian, VRAM. Không commit |
| `results/raw/<key>__meta.json` | GPU, phiên bản thư viện, VRAM sau nạp, module đưa ra CPU |
| `results/table.md` | Bảng chính cho tờ trình + bảng theo họ prompt, theo nhóm ngành, lỗi hay gặp |
| `results/metrics.csv` | Chỉ số theo (cách parse, mô hình, seed) và gộp |
| `results/formulas.csv` | Mọi công thức đã chấm, kèm lý do không hợp lệ |
| `results/formulas_<model>.md` | Công thức của 1 mô hình theo chủ đề: dạng, họ nhân tố, lỗi ngữ nghĩa |
| `eval/c4_blind.csv`, `eval/c4_key.csv` | Mẫu chấm tay đã giấu tên mô hình và khoá giải mã |

## Rủi ro đã biết

- **Gemma trên T4 với float16:** họ Gemma từng bị tràn số ở fp16. Nếu lần chạy thử ra chuỗi rỗng hoặc
  ký tự lặp vô nghĩa, đổi `compute_dtype: float32` riêng cho Gemma trong `config/models.yaml` và ghi rõ vào tờ trình.
- **Tốc độ Qwen3.5:** không cài `flash-linear-attention` thì transformers chạy nhánh torch cho các lớp
  linear attention. Số tok/s là cận dưới, ghi rõ khi báo cáo.
- **Sailor2 context 4096:** prompt dài nhất 3.448 token + 512 sinh = 3.960 token. Nếu sửa bộ thử cho dài
  thêm, runner sẽ ghi `context_overflow` thay vì cắt ngầm.
