# Finance2026 — Sinh đặc trưng tài chính từ BCTC tiếng Việt bằng mô hình ngôn ngữ nhỏ

Đồ án nghiên cứu: dùng mô hình ngôn ngữ **quy mô nhỏ, tự triển khai** (1–3 tỷ tham số) để
đọc báo cáo tài chính doanh nghiệp niêm yết Việt Nam và **sinh ra công thức đặc trưng tường minh**,
phục vụ bài toán xếp hạng cổ phiếu theo lát cắt ngang, chân trời dự báo tháng đến quý.

Hạn nộp báo cáo: **14/12/2026**. Hạn đóng băng kết quả: **30/11/2026**.

---

## 1. Câu hỏi nghiên cứu

> Có thực sự cần mô hình frontier nghìn tỷ tham số để khai phá nhân tố từ báo cáo tài chính,
> hay một mô hình nhỏ chuyên biệt hoá theo lĩnh vực là đủ?

Toàn bộ nhánh khai phá nhân tố bằng LLM (AlphaCrafter, AlphaAgent, RD-Agent, QuantAgent,
Alpha-GPT, CogAlpha, FactorMAD, AlphaMemo — 2025–2026) đều mặc định dùng mô hình frontier qua API.
Giả định này chưa ai kiểm chứng, trong khi có ba bằng chứng ngược:

| Nguồn | Bằng chứng |
|---|---|
| Xiao et al. (2025) | Bộ truy xuất FinSeer 109M đánh bại E5-7B trên cả ba tập dữ liệu — chuyên biệt hoá thắng dung lượng |
| Valeyre & Aboura (2024) | Chronos-tiny 11M zero-shot đạt Sharpe 3,17 trước phí, tương đương phương pháp phức tạp hơn nhiều |
| NLP tiếng Việt | PhoBERT 135M đạt macro-F1 74,93%, GPT-4 zero-shot chỉ 60,14% trên cùng tác vụ |

### Hai khoảng trống

| | Phát biểu |
|---|---|
| **G1** | Chưa có công trình nào so sánh hệ thống sinh đặc trưng dùng SLM tự triển khai với hệ thống dùng LLM frontier qua API, **trên cùng dữ liệu, cùng giao thức đánh giá, có tính chi phí vận hành**. |
| **G2** | Chưa có công trình nào khai thác nội dung BCTC doanh nghiệp niêm yết Việt Nam bằng mô hình ngôn ngữ để sinh đặc trưng cho mô hình nhân tố. |

Với tiếng Việt, mảng nghiên cứu hiện có đều là PhoBERT phân loại cảm xúc tin tức báo chí và
dự báo giá ngày kế tiếp. **Chưa ai đọc báo cáo tài chính** — nguồn có cấu trúc ngữ nghĩa sâu hơn tin tức.

**Lợi thế riêng của dữ liệu tiếng Việt:** LLM kể cả frontier gần như không có BCTC doanh nghiệp
Việt Nam trong tập huấn luyện → đây là **thí nghiệm tự nhiên** về rò rỉ dữ liệu, thứ mà
Look-Ahead-Bench / DatedGPT / phương pháp ẩn danh hoá đang phải giả lập tốn kém.

---

## 2. Bốn giả thuyết → ba bảng kết quả

| Mã | Giả thuyết | Kiểm chứng bằng | Ra bảng |
|----|-----------|------------------|---------|
| **H1** | SLM 1–3B tự triển khai sinh đặc trưng có IC không thua kém đáng kể LLM frontier qua API | Benchmark cùng testset (P0, P6) | Bảng 1 |
| **H2** | Đặc trưng sinh từ **thuyết minh** có sức giải thích tăng thêm so với chỉ dùng chỉ tiêu có cấu trúc | Ablation bỏ RAG (P6) | Bảng 1 (ablation) |
| **H3** | Gán dữ liệu theo **ngày kết thúc quý** thổi phồng IC và Sharpe so với gán theo **ngày công bố thực tế** | Chạy song song 2 cách gán (P5) | Bảng 2 |
| **H4** | Sau chi phí giao dịch thực tế thị trường VN, lợi thế chiến lược suy giảm đáng kể so với mức 5 bps chuẩn quốc tế | Mô hình chi phí VN (P2) | Bảng 3 |

Cả bốn giả thuyết đặt ở cuối Chương 1 (sau câu hỏi nghiên cứu) và mở đầu Chương 4.

**Vì sao H4 quan trọng:** Valeyre & Aboura (2024) cho thấy chỉ với trượt giá 3 bps,
Sharpe rơi từ +3,17 xuống −1,49. Chi phí thật ở VN cao hơn nhiều lần mức 5 bps mà các
công trình quốc tế dùng. Riêng việc trình bày Bảng 3 đã là đóng góp.

---

## 3. Kiến trúc hệ thống

```
   [BÁO CÁO TÀI CHÍNH TIẾNG VIỆT]
   (bảng số + thuyết minh + ý kiến kiểm toán)
              |
     +--------+--------+
     |                 |
 [PhoBERT 135M]   [Chỉ tiêu tài chính
  ENCODER-ONLY     có cấu trúc]
  -> embeddings         |
  -> truy xuất đoạn     |
     liên quan (RAG)    |
     |                  |
     +--------+---------+
              |
   [SLM SINH VĂN BẢN 1-3B]  <-- P0 đang chốt mô hình nào
    DECODER-ONLY
    -> sinh công thức đặc trưng
              |
   [KIỂM TRA TỰ ĐỘNG]  cú pháp / biến tồn tại / không trùng
              |
   [HITL - CHUYÊN GIA DUYỆT]
              |
   [GÁN DỮ LIỆU POINT-IN-TIME]  <-- theo ngày công bố thực tế
              |
   [MÔ HÌNH NHÂN TỐ NHỎ]  LightGBM / MLP
              |
   [XẾP HẠNG -> DANH MỤC -> BACKTEST SAU PHÍ]
```

**Đầu ra của hệ thống:** tập công thức đặc trưng tường minh kèm truy vết về chỉ tiêu hoặc đoạn văn nguồn;
xếp hạng cổ phiếu lát cắt ngang cho kỳ tiếp theo; danh mục và kết quả kiểm định ngược sau chi phí.

### Căn cứ chọn từng mô hình

| Thành phần | Lựa chọn | Tham số | Căn cứ |
|---|---|---|---|
| Bộ mã hoá, truy xuất | PhoBERT-base | 135M | Encoder-only, đúng thế mạnh sinh embedding. Tiền lệ trực tiếp: FinSeer trong Xiao et al. (2025) |
| Bộ sinh công thức | **Đang chốt** (P0) | 1–3B | Decoder-only, chạy được trên GPU phổ thông sau lượng tử 4-bit |
| Mô hình nhân tố | MLP hoặc LightGBM | ~1.000 | Các công trình hàng đầu đều dùng mô hình rất nhỏ: GPZ vài trăm tham số, Epstein chiều ẩn 32 |
| Baseline đối chứng | GPT-4o hoặc Claude qua API | Rất lớn | Đại diện cách làm hiện hành của AlphaCrafter, Kou et al. |

**Phân vai phải nêu tường minh trong báo cáo:** PhoBERT **chỉ** mã hoá và truy xuất, không sinh văn bản.
Gán nhầm vai encoder-only / decoder-only là lỗi kiến trúc bị bắt nhiều nhất trong nhánh này.
Thí nghiệm ablation (P6) là để chứng minh mỗi mô-đun có đóng góp thực, chặn trước câu hỏi
"vì sao phải dùng hai mô hình".

**Đánh đổi đã biết:** bộ sinh 1–3B vượt ngưỡng "vài trăm triệu" GVHD đã nêu. Đây là đánh đổi bắt buộc —
encoder-only không sinh được công thức, mà công thức tường minh là điều kiện của tính diễn giải.
Với lượng tử 4-bit, mô hình 3B chạy trên card 8GB. Cần thầy xác nhận (họp 01/10).

---

## 4. Dữ liệu

| Nguồn | Nội dung | Trạng thái |
|---|---|---|
| [`tinixai/ocr_annual_financials`](https://huggingface.co/datasets/tinixai/ocr_annual_financials) | 18.231 BCTC **năm**, 1.491 mã, 2015–2025, PDF + TXT OCR, có thuyết minh, 194GB, CC BY-NC 4.0 | Có sẵn — dùng cho **P0** |
| vnstock / API công ty chứng khoán | BCTC **quý** ~200 DN × 10 năm (bảng số + thuyết minh) | Chưa tải — **P1** |
| HOSE / HNX | **Ngày công bố thực tế** | Chưa kiểm tra có sẵn hay không — **P1, điều kiện tiên quyết của H3** |
| HOSE / HNX | OHLCV theo ngày + mã ngành, gồm cả mã đã huỷ niêm yết | Chưa thu thập — **P1** |

> **Cảnh báo:** dataset HuggingFace là báo cáo **năm**, không phải **quý**. Nó đủ dùng làm mẫu
> cho P0 nhưng **không thay thế được P1**, và **không có ngày công bố**.
> License CC BY-NC 4.0 → trích nguồn trong báo cáo, demo không thương mại hoá.

**Format OCR (đã xác minh trên 40 file mẫu, 22/09):** file `_extracted.txt` không phải text thuần
mà là **bảng HTML** — `<tr><td>Tên chỉ tiêu</td><td>Mã số VAS</td><td>Thuyết minh</td><td>Số cuối kỳ</td><td>Số đầu kỳ</td></tr>`.
Trung vị 73 bảng / ~700 dòng / 74 mã số VAS mỗi file; phần thuyết minh dạng văn xuôi nằm ngoài bảng,
trung vị ~65.000 ký tự. 40/40 file có bảng và có mã số VAS.
Nghĩa là **trích biến theo mã số chỉ tiêu, không phải dò khớp tên tiếng Việt** — chính xác hơn hẳn
và miễn nhiễm với sai khác chính tả OCR. Riêng ngân hàng ít mã VAS hơn nhiều (VCB 28–31, SHB 38–49
so với trung vị 74) do mẫu biểu khác.

**Giữ cả cổ phiếu đã huỷ niêm yết.** Bỏ đi là survivorship bias.

### Vấn đề số quan sát (rủi ro lớn nhất của đề tài)

Dữ liệu quý × 10 năm chỉ cho ~40 điểm thời gian. Chia train/val/test thì test còn ~10 điểm —
quá mỏng để rút kết luận thống kê.

**Giải pháp:** bổ sung giá theo **tần suất ngày** (~2.500 điểm) để tăng số quan sát huấn luyện,
vẫn tái cân bằng danh mục theo tháng/quý. Cách này theo Wei et al. (2022).

**Ngưỡng tối thiểu:** ~200 DN để lát cắt ngang đủ rộng, ~10 năm dữ liệu.
Mốc GO/NO-GO ngày 13/10 kiểm tra đúng điều này.

---

## 5. Kỷ luật nghiên cứu — không được vi phạm

Đây là phần dễ bị hội đồng bắt lỗi nhất, và cũng là lỗi phần lớn công trình trong nhánh đều mắc.

**a) Rò rỉ point-in-time**
- Dùng **ngày công bố thực tế**, không dùng ngày kết thúc kỳ báo cáo.
- Xử lý các trường hợp đính chính theo nguyên tắc Wei et al. (2022).
- Trình bày Bảng 2 như **kết quả độc lập** — biến việc kiểm soát thành đóng góp thay vì thủ tục.

**b) Rò rỉ qua mốc dữ liệu huấn luyện của LLM**
- Mô hình tự triển khai có mốc huấn luyện **biết chính xác và cố định** — khác API có thể bị cập nhật ngầm.
- **Nguyên tắc cách ly:** LLM chỉ dùng để **sinh** công thức, **không** dùng để chọn lọc phụ thuộc thời điểm.
  Việc chọn do kiểm định trên dữ liệu trước thời điểm đánh giá quyết định.
- Tham chiếu Look-Ahead-Bench, DatedGPT, phương pháp ẩn danh hoá.

**c) Chi phí giao dịch và trượt giá** — phí môi giới mỗi chiều, thuế bán 0,1% trên giá trị bán
(không phụ thuộc lãi lỗ), chênh lệch giá mua bán cao hơn đáng kể với cổ phiếu thanh khoản thấp,
market impact (chưa công trình nào khảo sát mô hình hoá).

**d) Kiểm định thống kê** — báo cáo t-stat và sai số chuẩn (không chỉ điểm ước lượng),
phân tích theo giai đoạn con, **nêu rõ tổng số công thức đã thử** và hiệu chỉnh đa giả thuyết.

---

## 6. Lộ trình

| Pha | Nội dung | Hạn | Người |
|-----|----------|-----|-------|
| **P0** | Chốt mô hình: bộ thử, benchmark, tờ trình | **24/09** | ML, cả nhóm |
| | Họp thầy (gộp 1 buổi: mô hình + phạm vi) | 01/10 | Cả nhóm |
| | **Khoá đề cương** — sau mốc này không đổi phạm vi | 03/10 | Cả nhóm |
| **P1** | Dữ liệu: crawl BCTC quý, ngày công bố, OHLCV theo ngày | 12/10 | Data |
| | **CHỐT 1 — GO/NO-GO:** đủ ≥150 DN × ≥8 năm × có ngày công bố? | 13/10 | Cả nhóm |
| **P2** | Hạ tầng đánh giá: pipeline backtest, mô hình chi phí VN, baseline nhân tố thủ công | 19/10 | Quant |
| **P3** | Encoder + RAG: chunk thuyết minh, index PhoBERT, đánh giá trên 50 truy vấn gán nhãn tay | 26/10 | ML |
| **P4** | Sinh công thức: validator đầy đủ, ~150 công thức + truy vết nguồn, HITL duyệt | 02/11 | ML, cả nhóm |
| | **CHỐT 2 — GO/NO-GO:** tỷ lệ công thức hợp lệ ≥60%? | 03/11 | Cả nhóm |
| **P5** | Mô hình nhân tố: gán point-in-time + bản ngây thơ, LightGBM + MLP walk-forward, xuất Bảng 1/2/3 | 16/11 | Quant |
| **P6** | Đối chứng: baseline API (mẫu con 50 DN × 3 năm), ablation (bỏ RAG, bỏ HITL), demo Streamlit | 23/11 | ML, Dev |
| **P7** | Kiểm định: t-stat, sai số chuẩn, giai đoạn con, hiệu chỉnh đa giả thuyết | 30/11 | Quant |
| | **ĐÓNG BĂNG KẾT QUẢ** — không chạy thí nghiệm mới | **30/11** | Cả nhóm |
| **P8** | Báo cáo: Ch.1–2 → Ch.3 → Ch.4–5 → nộp nháp GVHD (30/11) → sửa → format → **nộp 14/12** | 14/12 | Cả nhóm |
| **P9** | Bảo vệ: slide, tập phản biện, chạy thử demo trên máy hội đồng | sau 14/12 | Cả nhóm |

**Ba thứ không được cắt:** mô hình chi phí VN (P2), kiểm định thống kê (P7), đóng băng kết quả (30/11).
Chừa đúng 10 ngày cho thầy sửa bản nháp — không chừa ít hơn.

**Hai mốc GO/NO-GO có phương án dự phòng sẵn:**
- Trượt CHỐT 1 → bỏ Bảng 2, chuyển H3 thành mục hạn chế, báo thầy trong ngày.
- Trượt CHỐT 2 → chuyển few-shot có ràng buộc grammar, **không đổi mô hình lần nữa**.

---

## 7. Cấu trúc thư mục (đề xuất, dựng dần)

```
Finance2026/
├─ README.md
├─ config/
│  └─ variables.yaml        # danh mục biến chuẩn hoá — P0, xương sống cả dự án
├─ data/
│  ├─ sample/               # 15-20 BCTC mẫu cho P0
│  ├─ raw/                  # P1: BCTC quý, OHLCV, ngày công bố
│  └─ processed/
├─ eval/
│  ├─ prompts.jsonl         # 60-80 prompt bộ thử
│  ├─ rubric.md
│  └─ manual_scores.csv
├─ bench/                   # P0 task 2
│  ├─ run_infer.py
│  ├─ validator.py          # v0, nâng cấp thành bản đầy đủ ở P4
│  ├─ raw/
│  └─ results.csv
├─ src/
│  ├─ retrieval/            # P3: PhoBERT + RAG
│  ├─ generation/           # P4: sinh công thức
│  ├─ factor/               # P5: LightGBM / MLP
│  └─ backtest/             # P2: pipeline, mô hình chi phí VN
├─ docs/
│  ├─ GAP_research.pdf
│  ├─ Timelines.xlsx
│  ├─ P0_breakdown.md
│  └─ specs/
└─ report/
```

---

## 8. Yêu cầu tính toán

| Thành phần | Yêu cầu |
|---|---|
| Tinh chỉnh PhoBERT | Một card đồ hoạ phổ thông |
| Suy luận SLM 1–3B | Một card 8GB với lượng tử hoá 4-bit |
| Mô hình nhân tố | Chạy được trên CPU |
| Baseline qua API | Chi phí truy vấn, ước tính thấp |

Đối chiếu: Valeyre & Aboura tinh chỉnh Chronos 11M trên hai card RTX 4060 Ti trong khoảng một tuần.
Quy mô tính toán của đề tài này tương đương hoặc nhẹ hơn.

---

## 9. Tài liệu tham khảo chính

1. Wei, Z., Dai, B., Lin, D. (2022). *Factor Investing with a Deep Multi-Factor Model.* arXiv:2210.12462
2. Xiao, M., Jiang, Z., Qian, L., et al. (2025). *Retrieval-augmented Large Language Models for Financial Time Series Forecasting.* arXiv:2502.05878
3. Valeyre, S., Aboura, S. (2024). *LLMs for Time Series: an Application for Single Stocks and Statistical Arbitrage.* arXiv:2412.09394
4. Kou, Z., Yu, H., Luo, J., et al. (2025). *Automate Strategy Finding with LLM in Quant Investment.* arXiv:2409.06289
5. *AlphaCrafter: A Full-Stack Multi-Agent Framework for Cross-Sectional Quantitative Trading* (2026). arXiv:2605.05580
6. *Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?* (FINSABER, 2025). arXiv:2505.07078
7. *Look-Ahead-Bench: a Standardized Benchmark of Look-ahead Bias in Point-in-Time LLMs for Finance* (2026). arXiv:2601.13770
8. Nguyen, D. Q., Nguyen, A. T. (2020). *PhoBERT: Pre-trained language models for Vietnamese.* Findings of EMNLP
9. Guijarro-Ordonez, J., Pelger, M., Zanotti, G. (2022). *Deep Learning Statistical Arbitrage.* arXiv:2106.04028
10. Epstein, E. L., Wang, R., Choi, J., Pelger, M. (2025). *Attention Factors for Statistical Arbitrage.* arXiv:2510.11616

---

## 10. Trạng thái hiện tại — 22/09/2026

Đang ở **P0**, còn 2 ngày tới hạn 24/09. Chưa task nào thực hiện.

- Bóc tách công việc: [docs/P0_breakdown.md](docs/P0_breakdown.md)
- Spec từng task: [docs/specs/](docs/specs/)

**Hai thứ chưa xác định, đang chặn P0:** tên mô hình ứng viên thứ ba muốn chốt,
và card đồ hoạ thật sẽ dùng để đo VRAM.
