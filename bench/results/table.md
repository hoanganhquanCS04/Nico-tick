# Kết quả benchmark P0

Sinh bởi `bench/scripts/score.py` từ `bench/results/raw`. Định nghĩa chỉ số: `bench/README.md`.

## Bảng chính (đưa vào tờ trình)

| Mô hình | Tham số | **Hợp lệ / yêu cầu (%)** | Nếu cứu JSON (%) | Hợp lệ & chuẩn hoá quy mô (%) | VRAM ước tính cần (MB) | s / công thức hợp lệ | tok/s | JSON đúng (%) | Trùng (%) | Lượt |
|---|---|---|---|---|---|---|---|---|---|---|
| qwen35-2b | 2B | **13.3 ± 2.4** | 30.3 | 30.3 | 3291 | 49.0 | 13.73 | 61.4 | 6.7 | 228 |
| gemma4-e2b-gpu * | E2B (5,1B tổng) | **26.7** | 33.3 | 33.3 | 7984 | 47.3 | 10.16 | 90.0 | 33.3 | 10 |
| gemma4-e2b-plecpu | E2B (5,1B tổng) | **47.2 ± 2.6** | 49.9 | 46.5 | 3660 | 27.9 | 9.91 | 92.1 | 12.2 | 228 |
| qwen35-0.8b | 0,8B | **12.0 ± 1.1** | 16.2 | 13.3 | 2363 | 77.9 | 14.06 | 55.7 | 41.7 | 228 |
| sailor2-1b | 1B | **3.8 ± 2.4** | 11.3 | 2.5 | 3119 | 376.6 | 10.6 | 31.1 | 6.7 | 228 |

- **Hợp lệ / yêu cầu** = số công thức qua C1∧C2∧C3 / số công thức đã yêu cầu (3 × số lượt). Lượt hỏng JSON = 0 công thức hợp lệ. `a ± b` = trung bình ± độ lệch chuẩn giữa các seed.
- **Nếu cứu JSON** = như trên nhưng gom lại công thức từ output vỡ vỏ JSON (ước lượng cận trên khi có GCD).
- **Chuẩn hoá quy mô** = công thức hợp lệ có tỷ số/tăng trưởng/xếp hạng, so sánh được giữa công ty lớn và nhỏ (parse lenient).
- **VRAM ước tính cần** = đỉnh `torch.cuda.max_memory_allocated` + 605 MB ngữ cảnh CUDA (trung vị đo lúc nạp). Không dùng đỉnh NVML: trên T4 16GB bộ cấp phát giữ lại bộ nhớ nên con số đó phình to.
- **Trùng** = trung bình tỷ lệ trùng của từng seed. `*` = dòng tham chiếu, chỉ chạy 10 prompt × 1 seed.

## Theo họ prompt (hợp lệ / yêu cầu %, strict · cứu JSON)

| Mô hình | F1 chỉ biến | F2 + thuyết minh | F3 + ví dụ | F4 ép format | F2: có công thức lấy từ thuyết minh | F2: trích dẫn đúng nguyên văn |
|---|---|---|---|---|---|---|
| qwen35-2b | 7.8 · 9.8 | 8.4 · 18.2 | 21.1 · 55.6 | 17.8 · 41.5 | 93.3 | 38.9 |
| gemma4-e2b-gpu | 11.1 · 11.1 | 55.6 · 55.6 | 16.7 · 50.0 | 16.7 · 16.7 | 33.3 | 100.0 |
| gemma4-e2b-plecpu | 37.9 · 37.9 | 50.7 · 51.6 | 60.2 · 65.5 | 35.6 · 40.7 | 92.0 | 70.7 |
| qwen35-0.8b | 1.3 · 2.6 | 2.7 · 3.1 | 29.2 · 32.8 | 17.8 · 32.6 | 98.7 | 36.4 |
| sailor2-1b | 1.3 · 2.6 | 0.0 · 1.3 | 0.6 · 1.2 | 17.0 · 50.4 | 16.0 | 0.0 |

## Theo nhóm doanh nghiệp và tuân thủ yêu cầu (strict)

| Mô hình | Phi tài chính (%) | Ngân hàng / chứng khoán (%) | Đúng 3 công thức (%) | Dùng biến bắt buộc (%, cứu JSON) | Chạm trần 512 token (%) | Độ trễ TB / lượt (s) |
|---|---|---|---|---|---|---|
| qwen35-2b | 14.0 | 8.9 | 8.3 | 86.4 | 11.4 | 19.6 |
| gemma4-e2b-gpu | 26.7 | - | 90.0 | 100.0 | 0.0 | 37.8 |
| gemma4-e2b-plecpu | 47.8 | 43.3 | 92.1 | 92.5 | 1.8 | 39.5 |
| qwen35-0.8b | 12.5 | 8.9 | 55.3 | 37.3 | 23.2 | 28.0 |
| sailor2-1b | 4.4 | 0.0 | 8.3 | 25.0 | 62.3 | 42.9 |

## Chất lượng trong số công thức hợp lệ (cứu JSON)

| Mô hình | Số hợp lệ | Khác nhau (3 seed gộp) | Chuẩn hoá quy mô (%) | Chỉ 1 biến (%) | Có hàm chuỗi thời gian (%) | Dùng biến thuyết minh (%) |
|---|---|---|---|---|---|---|
| qwen35-2b | 207 | 151 | 100.0 | 10.6 | 24.1 | 4.8 |
| gemma4-e2b-gpu | 10 | 10 | 100.0 | 60.0 | 60.0 | 0.0 |
| gemma4-e2b-plecpu | 341 | 221 | 93.3 | 36.7 | 49.0 | 11.4 |
| qwen35-0.8b | 111 | 79 | 82.0 | 41.4 | 33.3 | 7.2 |
| sailor2-1b | 94 | 81 | 18.1 | 25.5 | 9.6 | 12.8 |

## Lỗi hay gặp

| Mô hình | Lượt hỏng JSON (strict) | Cứu được | 6 lỗi công thức nhiều nhất (cứu JSON) |
|---|---|---|---|
| qwen35-2b | 88 | 76 | raw_division 125, duplicate 49, bad_arity:safe_div 21, syntax_error 15, unknown_var 9, bad_lag 6 |
| gemma4-e2b-gpu | 1 | 1 | bad_arity:zscore 5, syntax_error 5, duplicate 5, raw_division 3, bad_arity:growth 2, constant_only 1 |
| gemma4-e2b-plecpu | 18 | 18 | syntax_error 102, bad_arity:zscore 77, raw_division 61, duplicate 54, bad_arity:growth 18, bad_arity:rank 14 |
| qwen35-0.8b | 101 | 99 | syntax_error 278, copied_fewshot 104, duplicate 58, bad_arity:rank 36, unknown_var 33, bad_arity:zscore 30 |
| sailor2-1b | 157 | 80 | syntax_error 147, missing_field 66, unknown_var 43, copied_fewshot 31, duplicate 28, not_object 21 |

## Điều kiện đo

| Mô hình | GPU | Lượng tử | dtype | Nạp (s) | torch sau nạp (MB) | Đỉnh torch (MB) | Đỉnh NVML (MB, tham khảo) | Module đưa ra CPU | transformers | bitsandbytes |
|---|---|---|---|---|---|---|---|---|---|---|
| qwen35-2b | Tesla T4 | nf4 | float16 | 18.5 | 1654.9 | 2685.5 | 5429.2 | - | 5.5.0 | 0.50.2 |
| gemma4-e2b-gpu | Tesla T4 | nf4 | float16 | 11.8 | 6449.4 | 7378.7 | 8761.2 | - | 5.5.0 | 0.50.2 |
| gemma4-e2b-plecpu | Tesla T4 | nf4 | float16 | 18.4 | 1710.9 | 3054.7 | 7083.2 | embed_tokens_per_layer; vision_tower; embed_vision; audio_tower; embed_audio | 5.5.0 | 0.50.2 |
| qwen35-0.8b | Tesla T4 | nf4 | float16 | 8.9 | 746.6 | 1757.6 | 4505.2 | - | 5.5.0 | 0.50.2 |
| sailor2-1b | Tesla T4 | nf4 | float16 | 9.7 | 881.7 | 2513.7 | 7257.2 | - | 5.5.0 | 0.50.2 |
