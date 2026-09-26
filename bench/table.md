# Kết quả benchmark P0

Sinh bởi `bench/score.py` từ `bench/raw`. Định nghĩa chỉ số: `bench/README.md`.

## Bảng chính (đưa vào tờ trình)

| Mô hình | Tham số | VRAM đỉnh card (MB) | VRAM torch (MB) | tok/s | s/công thức hợp lệ | Hợp lệ (%) | Trùng (%) | JSON (%) | Seed | Lượt |
|---|---|---|---|---|---|---|---|---|---|---|
| qwen35-2b | 2B | 5429 (nền 451) | 2685.5 | 13.73 | 49.03 | 50.6 ± 8.4 | 22.7 | 61.4 | 3 | 228 |
| gemma4-e2b-gpu * | E2B (5,1B tổng) | 8761 (nền 451) | 7378.7 | 10.16 | 47.26 | 29.6 | 33.3 | 90.0 | 1 | 10 |
| gemma4-e2b-plecpu | E2B (5,1B tổng) | 7083 (nền 451) | 3054.7 | 9.91 | 27.9 | 51.2 ± 2.1 | 42.5 | 92.1 | 3 | 228 |
| qwen35-0.8b | 0,8B | 4505 (nền 451) | 1757.6 | 14.06 | 77.89 | 21.6 ± 1.7 | 64.1 | 55.7 | 3 | 228 |
| sailor2-1b | 1B | 7257 (nền 451) | 2513.7 | 10.6 | 305.97 | 22.1 ± 7.9 | 9.8 | 31.1 | 3 | 228 |

Hợp lệ = parse được theo DSL ∧ mọi biến có trong danh mục ∧ không trùng (dạng chuẩn hoá). Giá trị `a ± b` = trung bình ± độ lệch chuẩn giữa các seed. `*` = dòng tham chiếu VRAM, không chạy đủ bộ thử.

## Theo họ prompt (tỷ lệ hợp lệ %, gộp seed)

| Mô hình | F1 chỉ biến | F2 + thuyết minh | F3 + ví dụ | F4 ép format | F2: có dùng thuyết minh | F2: trích dẫn đúng nguyên văn |
|---|---|---|---|---|---|---|
| qwen35-2b | 27.9 | 30.6 | 92.3 | 66.7 | 69.3 | 32.8 |
| gemma4-e2b-gpu | 11.1 | 55.6 | 33.3 | 16.7 | 33.3 | 100.0 |
| gemma4-e2b-plecpu | 38.7 | 52.0 | 66.0 | 45.7 | 89.3 | 71.2 |
| qwen35-0.8b | 2.8 | 5.8 | 32.0 | 50.0 | 46.7 | 42.2 |
| sailor2-1b | 10.5 | 0.0 | 2.2 | 61.7 | 9.3 | 0.0 |

## Theo nhóm doanh nghiệp (tỷ lệ hợp lệ %)

| Mô hình | Phi tài chính | Ngân hàng / chứng khoán | Đúng số công thức (%) | Dùng biến bắt buộc (%) | Chạm trần 512 token (%) |
|---|---|---|---|---|---|
| qwen35-2b | 52.2 | 38.1 | 8.3 | 57.9 | 11.4 |
| gemma4-e2b-gpu | 29.6 | - | 90.0 | 90.0 | 0.0 |
| gemma4-e2b-plecpu | 52.3 | 44.8 | 92.1 | 86.0 | 1.8 |
| qwen35-0.8b | 22.4 | 16.7 | 55.3 | 28.5 | 23.2 |
| sailor2-1b | 25.4 | 0.0 | 8.3 | 19.3 | 62.3 |

## Lỗi hay gặp (số công thức)

| Mô hình | 5 lỗi nhiều nhất |
|---|---|
| qwen35-2b | json_parse_error 88, raw_division 64, syntax_error 13, bad_arity 10, duplicate 8 |
| gemma4-e2b-gpu | bad_arity 7, syntax_error 5, duplicate 5, raw_division 2, constant_only 1 |
| gemma4-e2b-plecpu | bad_arity 110, syntax_error 98, raw_division 55, duplicate 50, json_parse_error 18 |
| qwen35-0.8b | syntax_error 155, json_parse_error 101, copied_fewshot 100, bad_arity 20, raw_division 12 |
| sailor2-1b | json_parse_error 157, syntax_error 46, missing_field 27, not_object 21, unknown_var 21 |

## Điều kiện đo

| Mô hình | GPU | Lượng tử | dtype | Nạp (s) | VRAM sau nạp (MB) | Module đưa ra CPU | transformers | bitsandbytes |
|---|---|---|---|---|---|---|---|---|
| qwen35-2b | Tesla T4 | nf4 | float16 | 18.5 | 2245.1875 | - | 5.5.0 | 0.50.2 |
| gemma4-e2b-gpu | Tesla T4 | nf4 | float16 | 11.8 | 7109.1875 | - | 5.5.0 | 0.50.2 |
| gemma4-e2b-plecpu | Tesla T4 | nf4 | float16 | 18.4 | 7045.1875 | embed_tokens_per_layer; vision_tower; embed_vision; audio_tower; embed_audio | 5.5.0 | 0.50.2 |
| qwen35-0.8b | Tesla T4 | nf4 | float16 | 8.9 | 1349.1875 | - | 5.5.0 | 0.50.2 |
| sailor2-1b | Tesla T4 | nf4 | float16 | 9.7 | 1487.1875 | - | 5.5.0 | 0.50.2 |
