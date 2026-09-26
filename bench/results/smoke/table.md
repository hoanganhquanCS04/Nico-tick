# Kết quả benchmark P0

Sinh bởi `bench/scripts/score.py` từ `bench/results/smoke`. Định nghĩa chỉ số: `bench/README.md`.

## Bảng chính (đưa vào tờ trình)

| Mô hình | Tham số | **Hợp lệ / yêu cầu (%)** | Nếu cứu JSON (%) | Hợp lệ & chuẩn hoá quy mô (%) | VRAM ước tính cần (MB) | s / công thức hợp lệ | tok/s | JSON đúng (%) | Trùng (%) | Lượt |
|---|---|---|---|---|---|---|---|---|---|---|
| qwen35-2b | 2B | **16.7** | 16.7 | 16.7 | 2617 | 24.0 | 13.32 | 100.0 | 0.0 | 2 |
| gemma4-e2b-plecpu | E2B (5,1B tổng) | **50.0** | 50.0 | 50.0 | 2821 | 27.3 | 10.12 | 100.0 | 0.0 | 2 |
| qwen35-0.8b | 0,8B | **0.0** | 0.0 | 0.0 | 1698 | - | 14.56 | 50.0 | - | 2 |
| sailor2-1b | 1B | **0.0** | 0.0 | 0.0 | 1989 | - | 11.26 | 0.0 | - | 2 |

- **Hợp lệ / yêu cầu** = số công thức qua C1∧C2∧C3 / số công thức đã yêu cầu (3 × số lượt). Lượt hỏng JSON = 0 công thức hợp lệ. `a ± b` = trung bình ± độ lệch chuẩn giữa các seed.
- **Nếu cứu JSON** = như trên nhưng gom lại công thức từ output vỡ vỏ JSON (ước lượng cận trên khi có GCD).
- **Chuẩn hoá quy mô** = công thức hợp lệ có tỷ số/tăng trưởng/xếp hạng, so sánh được giữa công ty lớn và nhỏ (parse lenient).
- **VRAM ước tính cần** = đỉnh `torch.cuda.max_memory_allocated` + 604 MB ngữ cảnh CUDA (trung vị đo lúc nạp). Không dùng đỉnh NVML: trên T4 16GB bộ cấp phát giữ lại bộ nhớ nên con số đó phình to.
- **Trùng** = trung bình tỷ lệ trùng của từng seed. `*` = dòng tham chiếu, chỉ chạy 10 prompt × 1 seed.

## Theo họ prompt (hợp lệ / yêu cầu %, strict · cứu JSON)

| Mô hình | F1 chỉ biến | F2 + thuyết minh | F3 + ví dụ | F4 ép format | F2: có công thức lấy từ thuyết minh | F2: trích dẫn đúng nguyên văn |
|---|---|---|---|---|---|---|
| qwen35-2b | 0.0 · 0.0 | 33.3 · 33.3 | - · - | - · - | 100.0 | 100.0 |
| gemma4-e2b-plecpu | 0.0 · 0.0 | 100.0 · 100.0 | - · - | - · - | 0.0 | - |
| qwen35-0.8b | 0.0 · 0.0 | 0.0 · 0.0 | - · - | - · - | 100.0 | 0.0 |
| sailor2-1b | 0.0 · 0.0 | 0.0 · 0.0 | - · - | - · - | 0.0 | - |

## Theo nhóm doanh nghiệp và tuân thủ yêu cầu (strict)

| Mô hình | Phi tài chính (%) | Ngân hàng / chứng khoán (%) | Đúng 3 công thức (%) | Dùng biến bắt buộc (%, cứu JSON) | Chạm trần 512 token (%) | Độ trễ TB / lượt (s) |
|---|---|---|---|---|---|---|
| qwen35-2b | 16.7 | - | 0.0 | 100.0 | 0.0 | 12.0 |
| gemma4-e2b-plecpu | 50.0 | - | 100.0 | 100.0 | 0.0 | 40.9 |
| qwen35-0.8b | 0.0 | - | 50.0 | 50.0 | 50.0 | 33.7 |
| sailor2-1b | 0.0 | - | 0.0 | 0.0 | 50.0 | 32.6 |

## Chất lượng trong số công thức hợp lệ (cứu JSON)

| Mô hình | Số hợp lệ | Khác nhau (3 seed gộp) | Chuẩn hoá quy mô (%) | Chỉ 1 biến (%) | Có hàm chuỗi thời gian (%) | Dùng biến thuyết minh (%) |
|---|---|---|---|---|---|---|
| qwen35-2b | 1 | 1 | 100.0 | 0.0 | 0.0 | 0.0 |
| gemma4-e2b-plecpu | 3 | 3 | 100.0 | 100.0 | 66.7 | 0.0 |
| qwen35-0.8b | 0 | 0 | - | - | - | - |
| sailor2-1b | 0 | 0 | - | - | - | - |

## Lỗi hay gặp

| Mô hình | Lượt hỏng JSON (strict) | Cứu được | 6 lỗi công thức nhiều nhất (cứu JSON) |
|---|---|---|---|
| qwen35-2b | 0 | 0 | raw_division 1 |
| gemma4-e2b-plecpu | 0 | 0 | bad_arity:zscore 2, bad_arity:growth 1 |
| qwen35-0.8b | 1 | 1 | bad_arity:rank 3, unknown_var 3, syntax_error 2 |
| sailor2-1b | 2 | 0 |  |

## Điều kiện đo

| Mô hình | GPU | Lượng tử | dtype | Nạp (s) | torch sau nạp (MB) | Đỉnh torch (MB) | Đỉnh NVML (MB, tham khảo) | Module đưa ra CPU | transformers | bitsandbytes |
|---|---|---|---|---|---|---|---|---|---|---|
| qwen35-2b | Tesla T4 | nf4 | float16 | 30.9 | 1654.9 | 2013.1 | 2711.2 | - | 5.5.0 | 0.50.2 |
| gemma4-e2b-plecpu | Tesla T4 | nf4 | float16 | 56.3 | 1710.9 | 2217.4 | 7077.2 | embed_tokens_per_layer; vision_tower; embed_vision; audio_tower; embed_audio | 5.5.0 | 0.50.2 |
| qwen35-0.8b | Tesla T4 | nf4 | float16 | 15.4 | 746.6 | 1093.9 | 1791.2 | - | 5.5.0 | 0.50.2 |
| sailor2-1b | Tesla T4 | nf4 | float16 | 11.2 | 881.7 | 1384.7 | 2067.2 | - | 5.5.0 | 0.50.2 |
