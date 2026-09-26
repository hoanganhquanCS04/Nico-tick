# Kết quả benchmark P0

Sinh bởi `bench/score.py` từ `bench/smoke`. Định nghĩa chỉ số: `bench/README.md`.

## Bảng chính (đưa vào tờ trình)

| Mô hình | Tham số | VRAM đỉnh card (MB) | VRAM torch (MB) | tok/s | s/công thức hợp lệ | Hợp lệ (%) | Trùng (%) | JSON (%) | Seed | Lượt |
|---|---|---|---|---|---|---|---|---|---|---|
| qwen35-2b | 2B | 2711 (nền 451) | 2013.1 | 13.32 | 23.95 | 50.0 | 0.0 | 100.0 | 1 | 2 |
| gemma4-e2b-plecpu | E2B (5,1B tổng) | 7077 (nền 451) | 2217.4 | 10.12 | 27.27 | 50.0 | 0.0 | 100.0 | 1 | 2 |
| qwen35-0.8b | 0,8B | 1791 (nền 451) | 1093.9 | 14.56 | - | 0.0 | - | 50.0 | 1 | 2 |
| sailor2-1b | 1B | 2067 (nền 451) | 1384.7 | 11.26 | - | - | - | 0.0 | 1 | 2 |

Hợp lệ = parse được theo DSL ∧ mọi biến có trong danh mục ∧ không trùng (dạng chuẩn hoá). Giá trị `a ± b` = trung bình ± độ lệch chuẩn giữa các seed. `*` = dòng tham chiếu VRAM, không chạy đủ bộ thử.

## Theo họ prompt (tỷ lệ hợp lệ %, gộp seed)

| Mô hình | F1 chỉ biến | F2 + thuyết minh | F3 + ví dụ | F4 ép format | F2: có dùng thuyết minh | F2: trích dẫn đúng nguyên văn |
|---|---|---|---|---|---|---|
| qwen35-2b | 0.0 | 100.0 | - | - | 100.0 | 100.0 |
| gemma4-e2b-plecpu | 0.0 | 100.0 | - | - | 0.0 | - |
| qwen35-0.8b | - | 0.0 | - | - | 100.0 | 0.0 |
| sailor2-1b | - | - | - | - | 0.0 | - |

## Theo nhóm doanh nghiệp (tỷ lệ hợp lệ %)

| Mô hình | Phi tài chính | Ngân hàng / chứng khoán | Đúng số công thức (%) | Dùng biến bắt buộc (%) | Chạm trần 512 token (%) |
|---|---|---|---|---|---|
| qwen35-2b | 50.0 | - | 0.0 | 100.0 | 0.0 |
| gemma4-e2b-plecpu | 50.0 | - | 100.0 | 100.0 | 0.0 |
| qwen35-0.8b | 0.0 | - | 50.0 | 50.0 | 50.0 |
| sailor2-1b | - | - | 0.0 | 0.0 | 50.0 |

## Lỗi hay gặp (số công thức)

| Mô hình | 5 lỗi nhiều nhất |
|---|---|
| qwen35-2b | raw_division 1 |
| gemma4-e2b-plecpu | bad_arity 3 |
| qwen35-0.8b | bad_arity 3, unknown_var 3, json_parse_error 1 |
| sailor2-1b | json_parse_error 2 |

## Điều kiện đo

| Mô hình | GPU | Lượng tử | dtype | Nạp (s) | VRAM sau nạp (MB) | Module đưa ra CPU | transformers | bitsandbytes |
|---|---|---|---|---|---|---|---|---|
| qwen35-2b | Tesla T4 | nf4 | float16 | 30.9 | 2245.1875 | - | 5.5.0 | 0.50.2 |
| gemma4-e2b-plecpu | Tesla T4 | nf4 | float16 | 56.3 | 7045.1875 | embed_tokens_per_layer; vision_tower; embed_vision; audio_tower; embed_audio | 5.5.0 | 0.50.2 |
| qwen35-0.8b | Tesla T4 | nf4 | float16 | 15.4 | 1349.1875 | - | 5.5.0 | 0.50.2 |
| sailor2-1b | Tesla T4 | nf4 | float16 | 11.2 | 1487.1875 | - | 5.5.0 | 0.50.2 |
