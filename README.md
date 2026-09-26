# Finance2026 — Sinh đặc trưng tài chính từ BCTC tiếng Việt bằng mô hình ngôn ngữ nhỏ

Đồ án nghiên cứu: dùng mô hình ngôn ngữ **quy mô nhỏ, tự triển khai** (1–3 tỷ tham số) để
đọc báo cáo tài chính doanh nghiệp niêm yết Việt Nam và **sinh ra công thức đặc trưng tường minh**,
phục vụ bài toán xếp hạng cổ phiếu theo lát cắt ngang, chân trời dự báo tháng đến quý.

Hạn nộp báo cáo: **14/12/2026**. Hạn đóng băng kết quả: **30/11/2026**.

> **Đọc nhanh:** mục 1 (bài toán) → mục 4 (pipeline) → mục 11 (đang ở đâu). Các mục còn lại là chi tiết.

---

## 1. Bài toán

### 1.1. Chi tiết

Cho một **mô hình AI nhỏ chạy trên máy mình** đọc báo cáo tài chính (BCTC) tiếng Việt, rồi **viết ra
công thức chấm điểm cổ phiếu**. Sau đó kiểm tra xem chấm điểm như vậy có giúp chọn được cổ phiếu
tốt hơn thị trường không, **sau khi đã trừ phí giao dịch thật**.

### 1.2. Bài toán tài chính gốc: xếp hạng cổ phiếu

Mỗi kỳ (tháng hoặc quý), trên sàn có vài trăm cổ phiếu. Ta **không cố đoán giá** từng mã sẽ lên bao nhiêu,
mà chỉ cần **xếp thứ tự**: mã nào nhiều khả năng tăng tốt hơn mã nào trong kỳ tới. Sau đó mua nhóm đứng đầu
(và tránh nhóm cuối). Đây gọi là xếp hạng **theo lát cắt ngang**: so các công ty với nhau tại cùng một thời điểm.

Công cụ để xếp hạng là **nhân tố** (factor): một công thức tính ra điểm số cho mỗi công ty từ số liệu của nó.

**Ví dụ minh hoạ** (số giả định). Nhân tố *dồn tích* của Sloan (1996):
`(lợi nhuận − tiền thật thu về) / tổng tài sản`. Công ty báo lãi nhiều mà tiền không về thì lãi đó
"ảo", nên điểm càng cao càng xấu.

| Công ty | Lợi nhuận | Dòng tiền kinh doanh | Tổng tài sản | Điểm dồn tích | Xếp hạng     |
| -------- | ----------- | ---------------------- | --------------- | ----------------- | -------------- |
| A        | 100         | 120                    | 1.000           | −0,02            | 1 (tốt nhất) |
| C        | 50          | 45                     | 500             | +0,01             | 2              |
| B        | 100         | 20                     | 1.000           | +0,08             | 3 (xấu nhất) |

**Đo một nhân tố tốt hay dở bằng IC** (Information Coefficient): tương quan thứ hạng giữa điểm hôm nay
và lợi suất kỳ sau. Nếu quý sau A tăng 5%, C tăng 1%, B giảm 3% thì thứ hạng khớp hoàn toàn và IC = 1.
Thực tế IC rất nhỏ; một nhân tố có IC dương **ổn định qua nhiều kỳ**, dù chỉ cỡ vài phần trăm,
thường đã được coi là có giá trị.

### 1.3. Chỗ AI tham gia

Xưa nay công thức nhân tố do **con người** nghĩ ra, ví dụ bộ *101 Formulaic Alphas* của Kakushadze (2016).
Gần đây nhiều công trình cho **mô hình ngôn ngữ lớn** đề xuất công thức hàng loạt: AlphaAgent,
RD-Agent, AlphaCrafter… Tất cả đều dùng AI khổng lồ thuê qua API.

Đề tài này làm việc đó bằng **AI nhỏ tự chạy**, và cho nó đọc thêm **phần thuyết minh chữ** của BCTC.
Đây là chỗ con người hay bỏ qua vì quá dài, nhưng chứa thông tin mà bảng số không có: dự phòng giảm giá
tồn kho, giao dịch với bên liên quan, nợ tiềm tàng, ý kiến kiểm toán…

**AI chỉ đề xuất công thức, không ra quyết định mua bán.** Công thức phải đọc được, kiểm chứng được,
có người duyệt, rồi mới được đưa vào đánh giá. Đây là điều kiện để hệ thống **giải thích được**:
ngân hàng và quỹ không chấp nhận một hộp đen chỉ trả về "mua mã X".

### 1.4. Phát biểu chính xác

```
Tại mỗi kỳ tái cân bằng t, với mỗi doanh nghiệp i trong universe:

  Đầu vào   X(i, ≤t)   bảng số BCTC ĐÃ CÔNG BỐ trước t   (theo ngày công bố thật, không theo ngày kết thúc quý)
            D(i, ≤t)   thuyết minh BCTC đã công bố trước t
            r(i, t+1)  lợi suất kỳ sau                    (chỉ dùng để đánh giá, không bao giờ đưa vào mô hình)

  B1. Sinh     SLM( danh mục biến V, đoạn thuyết minh d )  →  tập công thức F = {f1, f2, …}   (viết bằng DSL)
  B2. Lọc      validator + người duyệt                      →  F* ⊂ F
  B3. Tính     z(i, t, k) = f_k( X(i, ≤t) )                    giá trị nhân tố k của công ty i tại kỳ t
  B4. Kết hợp  s(i, t)    = h( z(i, t, 1), z(i, t, 2), … )     h = LightGBM / MLP (+ mô hình tuyến tính làm mốc)
  B5. Xếp hạng theo s(i, t)  →  danh mục nhóm đầu  →  lợi nhuận SAU PHÍ giao dịch Việt Nam

  Mục tiêu    IC(t) = tương quan thứ hạng( s(·, t) , r(·, t+1) )   cao và ổn định
              Sharpe của danh mục sau phí                           dương
```

### 1.5. Ràng buộc làm bài toán khó

| Ràng buộc                                | Nghĩa là                                                                               | Vì sao                                                                                  |
| ------------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Mô hình nhỏ**                   | 1–3 tỷ tham số, chạy trên 1 card đồ hoạ phổ thông 8GB                          | Câu hỏi nghiên cứu chính (mục 2)                                                   |
| **Không nhìn trước tương lai** | Chỉ dùng BCTC đã công bố thật trước kỳ t                                       | Dùng ngày kết thúc quý là "biết trước" 1–3 tháng → kết quả đẹp giả (H3) |
| **Phí thật**                       | Phí môi giới, thuế bán 0,1%, chênh lệch giá mua–bán                            | Nhiều chiến lược lãi trên giấy nhưng lỗ sau phí (H4)                           |
| **Giải thích được**             | Đầu ra là công thức đọc được, truy vết về dòng BCTC và đoạn thuyết minh | Tài chính không chấp nhận hộp đen                                                 |
| **Ít dữ liệu**                    | 10 năm × 4 quý ≈ 40 điểm thời gian                                                | Dễ ra kết luận do may → cần kiểm định thống kê kỹ (mục 6d)                   |

### 1.6. Đầu ra cuối cùng

1. Tập **công thức nhân tố tường minh**, mỗi công thức kèm lý do và nguồn: biến nào, đoạn thuyết minh nào.
2. **Xếp hạng cổ phiếu** cho kỳ tiếp theo, kèm phiếu giải thích vì sao mỗi mã được xếp cao.
3. **Ba bảng kết quả** trả lời 4 giả thuyết (mục 3).
4. Demo Streamlit.

### 1.7. Thuật ngữ

| Thuật ngữ              | Nghĩa                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| BCTC                     | Báo cáo tài chính: bảng cân đối, kết quả kinh doanh, lưu chuyển tiền tệ,**thuyết minh** (phần chữ) |
| Mã số VAS              | Mã số chỉ tiêu trên mẫu BCTC Việt Nam, ví dụ 270 = Tổng cộng tài sản                                         |
| Nhân tố / đặc trưng | Công thức chấm điểm công ty từ số liệu của nó                                                                  |
| IC                       | Tương quan thứ hạng giữa điểm nhân tố và lợi suất kỳ sau                                                     |
| Backtest                 | Chạy thử chiến lược trên dữ liệu quá khứ như thể đang giao dịch thật                                       |
| Point-in-time            | Tại mỗi thời điểm chỉ dùng thông tin đã công khai lúc đó                                                    |
| Walk-forward             | Huấn luyện trên quá khứ, thử trên kỳ kế tiếp, trượt dần về sau. Không bao giờ học từ tương lai        |
| SLM / LLM                | Mô hình ngôn ngữ nhỏ (vài tỷ tham số) / lớn (hàng trăm tỷ đến nghìn tỷ)                                   |
| RAG                      | Tìm đoạn văn liên quan rồi đưa cho AI đọc cùng câu hỏi                                                       |
| DSL                      | Ngôn ngữ công thức rút gọn mà AI buộc phải viết theo (mục 4.3)                                                 |
| HITL                     | Human-in-the-loop: con người duyệt đầu ra của AI                                                                    |
| Hợp lệ                 | Công thức đúng cú pháp DSL ∧ mọi biến có thật ∧ không trùng công thức đã có                            |

---

## 2. Câu hỏi nghiên cứu

> Có thực sự cần mô hình frontier nghìn tỷ tham số để khai phá nhân tố từ báo cáo tài chính,
> hay một mô hình nhỏ chuyên biệt hoá theo lĩnh vực là đủ?

Toàn bộ nhánh khai phá nhân tố bằng LLM (AlphaCrafter, AlphaAgent, RD-Agent, QuantAgent,
Alpha-GPT, CogAlpha, FactorMAD, AlphaMemo — 2025–2026) đều mặc định dùng mô hình frontier qua API.
Giả định này chưa ai kiểm chứng, trong khi có ba bằng chứng ngược:

| Nguồn                  | Bằng chứng                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Xiao et al. (2025)      | Bộ truy xuất FinSeer 109M đánh bại E5-7B trên cả ba tập dữ liệu — chuyên biệt hoá thắng dung lượng |
| Valeyre & Aboura (2024) | Chronos-tiny 11M zero-shot đạt Sharpe 3,17 trước phí, tương đương phương pháp phức tạp hơn nhiều   |
| NLP tiếng Việt        | PhoBERT 135M đạt macro-F1 74,93%, GPT-4 zero-shot chỉ 60,14% trên cùng tác vụ                                |

### Hai khoảng trống

|              | Phát biểu                                                                                                                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **G1** | Chưa có công trình nào so sánh hệ thống sinh đặc trưng dùng SLM tự triển khai với hệ thống dùng LLM frontier qua API,**trên cùng dữ liệu, cùng giao thức đánh giá, có tính chi phí vận hành**. |
| **G2** | Chưa có công trình nào khai thác nội dung BCTC doanh nghiệp niêm yết Việt Nam bằng mô hình ngôn ngữ để sinh đặc trưng cho mô hình nhân tố.                                                                  |

Với tiếng Việt, mảng nghiên cứu hiện có đều là PhoBERT phân loại cảm xúc tin tức báo chí và
dự báo giá ngày kế tiếp. **Chưa ai đọc báo cáo tài chính** — nguồn có cấu trúc ngữ nghĩa sâu hơn tin tức.

**Lợi thế riêng của dữ liệu tiếng Việt:** LLM kể cả frontier gần như không có BCTC doanh nghiệp
Việt Nam trong tập huấn luyện → đây là **thí nghiệm tự nhiên** về rò rỉ dữ liệu, thứ mà
Look-Ahead-Bench / DatedGPT / phương pháp ẩn danh hoá đang phải giả lập tốn kém.

---

## 3. Bốn giả thuyết → ba bảng kết quả

| Mã          | Giả thuyết                                                                                                                         | Kiểm chứng bằng                | Ra bảng           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | ------------------ |
| **H1** | SLM 1–3B tự triển khai sinh đặc trưng có IC không thua kém đáng kể LLM frontier qua API                                  | Benchmark cùng testset (P0, P6)  | Bảng 1            |
| **H2** | Đặc trưng sinh từ**thuyết minh** có sức giải thích tăng thêm so với chỉ dùng chỉ tiêu có cấu trúc           | Ablation bỏ RAG (P6)             | Bảng 1 (ablation) |
| **H3** | Gán dữ liệu theo**ngày kết thúc quý** thổi phồng IC và Sharpe so với gán theo **ngày công bố thực tế**  | Chạy song song 2 cách gán (P5) | Bảng 2            |
| **H4** | Sau chi phí giao dịch thực tế thị trường VN, lợi thế chiến lược suy giảm đáng kể so với mức 5 bps chuẩn quốc tế | Mô hình chi phí VN (P2)        | Bảng 3            |

Cả bốn giả thuyết đặt ở cuối Chương 1 (sau câu hỏi nghiên cứu) và mở đầu Chương 4.

**Vì sao H4 quan trọng:** Valeyre & Aboura (2024) cho thấy chỉ với trượt giá 3 bps,
Sharpe rơi từ +3,17 xuống −1,49. Chi phí thật ở VN cao hơn nhiều lần mức 5 bps mà các
công trình quốc tế dùng. Riêng việc trình bày Bảng 3 đã là đóng góp.

**Đề xuất thêm H5 (chờ thầy duyệt 01/10):** mô hình kết hợp tuyến tính, đọc được trọng số trực tiếp,
không thua đáng kể LightGBM/MLP. Nghĩa là đo cái giá của việc giải thích được.

---

## 4. Pipeline

### 4.1. Sơ đồ tổng thể

Ba khối: **Dữ liệu → Sinh nhân tố → Đánh giá**.
Ký hiệu trạng thái: ✅ đã có · 🟡 có nhưng chưa ổn · ❌ chưa làm · 💡 đề xuất, chờ thầy duyệt.

```
╔═══════════════════════════════ KHỐI 1 · DỮ LIỆU ═══════════════════════════════╗

 [1] THU THẬP                                                             P1
     BCTC năm (HuggingFace, bản OCR)            ✅ mẫu 20 mã × 2 năm (data/sample/)
     BCTC QUÝ ~200 DN × 10 năm                  ❌
     Ngày công bố thật của từng BCTC            ❌  ← điều kiện sống còn của H3
     Giá cổ phiếu hằng ngày (cả mã đã huỷ)      ❌
                            │
                            ▼
 [2] TRÍCH SỐ LIỆU                        src/data/parse_statements.py
     bảng HTML trong OCR → đọc theo MÃ SỐ VAS → 65 biến chuẩn    config/variables.yaml
     🟡 trung vị 30/65 biến mỗi báo cáo; KQKD chỉ đọc được 9/17 DN
                            │
                            ▼
 [3] CẮT THUYẾT MINH                      src/eval/build_prompts.py       P3
     hiện tại: cắt theo tiêu đề mục ("10. Hàng tồn kho")         ✅
     kế hoạch: PhoBERT tìm đoạn liên quan nhất (RAG)             ❌

╠═══════════════════════════ KHỐI 2 · SINH NHÂN TỐ ══════════════════════════════╣

 [4] AI VIẾT CÔNG THỨC                    bench/run_infer.py              P4
     vào : danh sách biến + đoạn thuyết minh + vài ví dụ mẫu
     ra  : JSON { tên, công thức, lý do, nguồn }
     ✅ đã benchmark 4 mô hình — Gemma-4-E2B dẫn đầu (mục 11)
                            │
                            ▼
 [5] MÁY KIỂM TRA                         bench/validator.py
     cú pháp DSL · biến có thật · đúng số tham số · không chia trần · không trùng
     ✅ 10 bước    ❌ loại trích dẫn bịa    ❌ khử trùng theo tương quan (P4)
                            │
                            ▼
 [6] NGƯỜI DUYỆT (HITL)                   eval/c4_blind.csv
     chấm "có nghĩa kinh tế không" thang 1–5, giấu tên mô hình
     ❌ chưa có thang chấm eval/rubric.md, chưa chấm (0/80)

╠═════════════════════════════ KHỐI 3 · ĐÁNH GIÁ ════════════════════════════════╣

 [7] TÍNH GIÁ TRỊ NHÂN TỐ                 ❌ chưa có code                 P5
     công thức → con số cho từng mã, từng quý
     gán theo NGÀY CÔNG BỐ  ∥  song song bản gán "ngây thơ"  →  Bảng 2 (H3)
                            │
                            ▼
 [8] MÔ HÌNH XẾP HẠNG                     ❌                              P5
     LightGBM / MLP, walk-forward
     💡 + mô hình tuyến tính làm mốc (H5)  💡 + SHAP: nhân tố nào đẩy mã nào lên
                            │
                            ▼
 [9] DANH MỤC + BACKTEST SAU PHÍ VN       ❌                              P2
     mua nhóm đầu → trừ phí môi giới, thuế 0,1%, chênh lệch giá  →  Bảng 3 (H4)
     💡 phiếu giải thích cho từng mã được chọn
                            │
                            ▼
 [10] KIỂM CHỨNG                          ❌                         P6 · P7
     đối chứng: AI lớn qua API (H1) · bỏ RAG (H2) · bỏ người duyệt
     thống kê: t-stat, sai số chuẩn, chia giai đoạn, hiệu chỉnh vì thử nhiều công thức

╚════════════════════════════════════════════════════════════════════════════════╝
```

### 4.2. Từng bước làm gì, vì sao

| #  | Bước               | Làm gì                                                                     | Vì sao làm như vậy                                                                                                                                                                                                 |
| -- | -------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Thu thập            | BCTC quý, ngày công bố, giá ngày                                       | Không có ngày công bố thì không kiểm soát được việc "nhìn trước tương lai". Giữ mã đã huỷ niêm yết để tránh survivorship bias                                                              |
| 2  | Trích số liệu     | Đọc bảng theo mã số VAS, không dò tên chỉ tiêu                     | Mã số không bị lỗi chính tả OCR. Cùng mã số có nghĩa khác nhau giữa các báo cáo (mã 20 = lợi nhuận gộp ở KQKD, nhưng = dòng tiền kinh doanh ở LCTT) nên phải xác định báo cáo trước |
| 3  | Cắt thuyết minh    | Lấy mục thuyết minh riêng của công ty, bỏ mục chính sách kế toán | Mục chính sách là văn mẫu, công ty nào cũng giống nhau, không có thông tin                                                                                                                                |
| 4  | AI viết công thức | SLM đọc danh sách biến + thuyết minh → đề xuất công thức          | Đây là chỗ kiểm chứng H1 (nhỏ vs lớn) và H2 (có thuyết minh vs không)                                                                                                                                      |
| 5  | Máy kiểm tra       | Loại công thức sai cú pháp, dùng biến không có, trùng lặp         | AI nhỏ sinh sai nhiều. Lọc tự động rẻ hơn người đọc                                                                                                                                                        |
| 6  | Người duyệt       | Chấm ý nghĩa kinh tế                                                     | Công thức đúng cú pháp vẫn có thể vô nghĩa, ví dụ`tổng tài sản + tổng nợ`                                                                                                                          |
| 7  | Tính giá trị      | Chạy công thức trên số liệu từng quý                                 | Cầu nối công thức → con số. Chạy song song 2 cách gán thời gian để đo mức thổi phồng (H3)                                                                                                              |
| 8  | Mô hình xếp hạng | Kết hợp nhiều nhân tố thành 1 điểm                                   | Mô hình rất nhỏ (~1.000 tham số) vì chỉ có ~40 điểm thời gian; mô hình to sẽ học thuộc                                                                                                                 |
| 9  | Backtest sau phí    | Giả lập mua bán, trừ phí thật                                          | Lãi trên giấy khác lãi thật (H4)                                                                                                                                                                                 |
| 10 | Kiểm chứng         | So với AI lớn, bỏ từng bộ phận, kiểm định thống kê                | Chứng minh kết quả không do may và mỗi bộ phận đều có đóng góp                                                                                                                                           |

### 4.3. Ngôn ngữ công thức (DSL) mà AI phải viết theo

AI **không được viết tự do**, chỉ được dùng:

| Loại                                      | Được dùng                                                                                                          |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Biến                                      | Đúng tên trong`config/variables.yaml`, ví dụ `net_income`, `cfo`, `total_assets`, `inventory_writedown` |
| Toán tử                                  | `+  -  *  ( )`. **Cấm `/`**, mọi phép chia viết `safe_div(a, b)` để không chia cho 0                |
| Theo thời gian (k = số quý: 1, 2, 4, 8) | `lag(x,k)` · `delta(x,k)` · `growth(x,k)` · `mean(x,k)` · `std(x,k)`                                     |
| So giữa các công ty                     | `rank(x)` · `zscore(x)`                                                                                           |
| Khác                                      | `log(x)` · `abs(x)`                                                                                               |
| Giới hạn                                 | ≤ 6 biến, lồng ≤ 6 tầng, không được là hằng số                                                             |

Nhờ ràng buộc này máy kiểm tra được tự động, và công thức luôn tính ra số được.

### 4.4. Một công thức đi hết pipeline (ví dụ minh hoạ)

```
[3] Thuyết minh HPG 2024, mục "10. Hàng tồn kho":
      "… có 671 tỷ VND hàng tồn kho được ghi nhận theo giá trị thuần có thể thực hiện được …"
[4] AI đề xuất:
      { "name": "inventory_writedown_ratio",
        "formula": "safe_div(abs(inventory_writedown), inventory_gross)",
        "rationale": "Tỷ lệ dự phòng giảm giá trên giá gốc tồn kho cao → rủi ro hàng ế, lợi suất kém",
        "source": { "type": "note", "ref": "giá trị thuần có thể thực hiện được" } }
[5] Máy kiểm tra: đúng cú pháp ✓  biến có thật ✓  không trùng ✓  trích dẫn có trong thuyết minh ✓
[6] Người duyệt: 4/5 — hợp lý, giải thích được
[7] Tính cho ~200 mã × 40 quý, mỗi quý chỉ dùng BCTC đã công bố trước ngày tái cân bằng
[8] Mô hình xếp hạng học cách kết hợp nhân tố này với các nhân tố khác
[9] Mã X đứng top 10 → phiếu giải thích: "X xếp cao vì tỷ lệ dự phòng tồn kho thấp nhất ngành
    (công thức …, lấy từ thuyết minh mục …)"
```

### 4.5. Căn cứ chọn từng mô hình

| Thành phần             | Lựa chọn                                                                   | Tham số                      | Căn cứ                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Bộ mã hoá, truy xuất | PhoBERT-base                                                                 | 135M                          | Encoder-only, đúng thế mạnh sinh embedding. Tiền lệ trực tiếp: FinSeer trong Xiao et al. (2025)       |
| Bộ sinh công thức     | **Gemma-4-E2B-it** (dự phòng: Qwen3.5-2B) — chờ thầy duyệt 01/10 | 2,3B hiệu dụng / 5,1B tổng | Dẫn đầu benchmark P0 (mục 11). Decoder-only, chạy trên card phổ thông sau lượng tử 4-bit           |
| Mô hình nhân tố      | MLP hoặc LightGBM (💡 + tuyến tính làm mốc)                             | ~1.000                        | Các công trình hàng đầu đều dùng mô hình rất nhỏ: GPZ vài trăm tham số, Epstein chiều ẩn 32 |
| Baseline đối chứng    | LLM frontier qua API: GPT-4o / Claude, hoặc 💡 Qwen3.8-Max                  | Rất lớn                     | Đại diện cách làm hiện hành. Qwen3.8-Max cùng họ với Qwen3.5 nên cô lập được yếu tố quy mô |

**Phân vai phải nêu tường minh trong báo cáo:** PhoBERT **chỉ** mã hoá và truy xuất, không sinh văn bản.
Gán nhầm vai encoder-only / decoder-only là lỗi kiến trúc bị bắt nhiều nhất trong nhánh này.
Thí nghiệm ablation (P6) là để chứng minh mỗi mô-đun có đóng góp thực, chặn trước câu hỏi
"vì sao phải dùng hai mô hình".

**Đánh đổi đã biết:** bộ sinh vượt ngưỡng "vài trăm triệu" GVHD đã nêu. Đây là đánh đổi bắt buộc —
encoder-only không sinh được công thức, mà công thức tường minh là điều kiện của tính diễn giải.
Benchmark P0 cho thấy Qwen3.5-0.8B (dưới 1 tỷ) chỉ đạt ~16% công thức hợp lệ, so với ~30% của
Qwen3.5-2B cùng họ khi đã bỏ lỗi định dạng. Riêng Gemma-4-E2B: 5,1 tỷ tham số tổng, trong đó 2,35 tỷ
là bảng tra PLE đặt ở RAM; phần tính toán chạy trên GPU và chỉ cần ~3,7GB VRAM.

---

## 5. Dữ liệu

| Nguồn                                                                                            | Nội dung                                                                                              | Trạng thái                                                                          |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| [`tinixai/ocr_annual_financials`](https://huggingface.co/datasets/tinixai/ocr_annual_financials) | 18.231 BCTC**năm**, 1.491 mã, 2015–2025, PDF + TXT OCR, có thuyết minh, 194GB, CC BY-NC 4.0 | Có sẵn — dùng cho**P0**                                                     |
| vnstock / API công ty chứng khoán                                                              | BCTC**quý** ~200 DN × 10 năm — bảng số                                                     | Chưa tải —**P1**                                                             |
| ?                                                                                                 | Thuyết minh BCTC**quý** (phần chữ)                                                           | **Chưa rõ nguồn** — xem mục 10, vấn đề #1                               |
| HOSE / HNX                                                                                        | **Ngày công bố thực tế**                                                                    | Chưa kiểm tra có sẵn hay không —**P1, điều kiện tiên quyết của H3** |
| HOSE / HNX                                                                                        | OHLCV theo ngày + mã ngành, gồm cả mã đã huỷ niêm yết                                       | Chưa thu thập —**P1**                                                        |

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

## 6. Kỷ luật nghiên cứu — không được vi phạm

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

**e) Không tin lời giải thích của AI** — phần `rationale` AI viết có thể bịa: benchmark P0 cho thấy
Qwen3.5-2B có 61% trích dẫn thuyết minh không khớp nguyên văn. Chỉ tin thứ kiểm chứng được:
công thức, trích dẫn có thật trong văn bản gốc, kết quả backtest.

---

## 7. Lộ trình

| Pha          | Nội dung                                                                                                                                 | Hạn            | Người       |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------- |
| **P0** | Chốt mô hình: bộ thử, benchmark, tờ trình                                                                                          | **24/09** | ML, cả nhóm |
|              | Họp thầy (gộp 1 buổi: mô hình + phạm vi)                                                                                           | 01/10           | Cả nhóm     |
|              | **Khoá đề cương** — sau mốc này không đổi phạm vi                                                                       | 03/10           | Cả nhóm     |
| **P1** | Dữ liệu: crawl BCTC quý, ngày công bố, OHLCV theo ngày                                                                             | 12/10           | Data          |
|              | **CHỐT 1 — GO/NO-GO:** đủ ≥150 DN × ≥8 năm × có ngày công bố?                                                          | 13/10           | Cả nhóm     |
| **P2** | Hạ tầng đánh giá: pipeline backtest, mô hình chi phí VN, baseline nhân tố thủ công,**bộ tính công thức DSL → số** | 19/10           | Quant         |
| **P3** | Encoder + RAG: chunk thuyết minh, index PhoBERT, đánh giá trên 50 truy vấn gán nhãn tay                                           | 26/10           | ML            |
| **P4** | Sinh công thức: validator đầy đủ, ~150 công thức + truy vết nguồn, HITL duyệt                                                  | 02/11           | ML, cả nhóm |
|              | **CHỐT 2 — GO/NO-GO:** tỷ lệ công thức hợp lệ ≥60%?                                                                        | 03/11           | Cả nhóm     |
| **P5** | Mô hình nhân tố: gán point-in-time + bản ngây thơ, LightGBM + MLP walk-forward, xuất Bảng 1/2/3                                 | 16/11           | Quant         |
| **P6** | Đối chứng: baseline API (mẫu con 50 DN × 3 năm), ablation (bỏ RAG, bỏ HITL), demo Streamlit                                       | 23/11           | ML, Dev       |
| **P7** | Kiểm định: t-stat, sai số chuẩn, giai đoạn con, hiệu chỉnh đa giả thuyết                                                      | 30/11           | Quant         |
|              | **ĐÓNG BĂNG KẾT QUẢ** — không chạy thí nghiệm mới                                                                        | **30/11** | Cả nhóm     |
| **P8** | Báo cáo: Ch.1–2 → Ch.3 → Ch.4–5 → nộp nháp GVHD (30/11) → sửa → format →**nộp 14/12**                                 | 14/12           | Cả nhóm     |
| **P9** | Bảo vệ: slide, tập phản biện, chạy thử demo trên máy hội đồng                                                                 | sau 14/12       | Cả nhóm     |

**Ba thứ không được cắt:** mô hình chi phí VN (P2), kiểm định thống kê (P7), đóng băng kết quả (30/11).
Chừa đúng 10 ngày cho thầy sửa bản nháp — không chừa ít hơn.

**Hai mốc GO/NO-GO có phương án dự phòng sẵn:**

- Trượt CHỐT 1 → bỏ Bảng 2, chuyển H3 thành mục hạn chế, báo thầy trong ngày.
- Trượt CHỐT 2 → chuyển few-shot có ràng buộc grammar, **không đổi mô hình lần nữa**.

---

## 8. Cấu trúc thư mục

```
Nico-tick/
├─ README.md
├─ config/
│  ├─ variables.yaml          ✅ danh mục 65 biến chuẩn hoá — xương sống cả dự án
│  └─ sample_universe.csv     ✅ pool ứng viên chọn mẫu P0
├─ data/
│  ├─ sample/                 ✅ 20 mã × 2 năm cho P0 (tickers.csv, manifest.csv, extracted.json)
│  ├─ raw/                    ❌ P1: BCTC quý, OHLCV, ngày công bố
│  └─ processed/              ❌
├─ eval/
│  ├─ prompts.jsonl           ✅ bộ thử 76 prompt (F1–F4), sinh bằng src/eval/build_prompts.py
│  ├─ prompts_preview.md      ✅ bản dễ đọc của bộ thử
│  ├─ c4_blind.csv            ✅ 80 công thức chờ chấm tay (giấu tên mô hình)
│  └─ rubric.md               ❌ thang chấm
├─ bench/                     ✅ benchmark P0 — hướng dẫn trong bench/README.md
│  ├─ models.yaml             4 ứng viên + revision đã ghim
│  ├─ run_infer.py            chạy mô hình (Kaggle / local)
│  ├─ validator.py            validator v0, nâng cấp ở P4
│  ├─ score.py                chấm điểm → table.md, results.csv, formulas.csv
│  └─ kaggle_benchmark.ipynb
├─ src/
│  ├─ data/                   ✅ tải mẫu, parse BCTC, dựng danh mục biến
│  ├─ eval/                   ✅ sinh bộ thử
│  ├─ retrieval/              ❌ P3: PhoBERT + RAG
│  ├─ generation/             ❌ P4: sinh công thức
│  ├─ factor/                 ❌ P5: bộ tính DSL, LightGBM / MLP
│  └─ backtest/               ❌ P2: pipeline, mô hình chi phí VN
├─ docs/                      GAP_research.pdf, Timelines.xlsx, P0_breakdown.md, specs/
└─ report/                    ❌
```

---

## 9. Yêu cầu tính toán

| Thành phần        | Yêu cầu                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| Tinh chỉnh PhoBERT | Một card đồ hoạ phổ thông                                                                         |
| Suy luận SLM 1–3B | Một card 8GB với lượng tử hoá 4-bit.**Đo được ở P0: ≤3,7GB VRAM khi chạy** (T4, NF4) |
| Mô hình nhân tố | Chạy được trên CPU                                                                                 |
| Baseline qua API    | Chi phí truy vấn, ước tính thấp                                                                   |

Đối chiếu: Valeyre & Aboura tinh chỉnh Chronos 11M trên hai card RTX 4060 Ti trong khoảng một tuần.
Quy mô tính toán của đề tài này tương đương hoặc nhẹ hơn.

---

## 10. Vấn đề mở — cần chốt ở buổi họp 01/10

| # | Vấn đề                                                                                                                 | Vì sao quan trọng                                                          | Đề xuất                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 1 | **Thuyết minh quý lấy ở đâu?** API thường chỉ trả bảng số; HuggingFace chỉ có báo cáo năm          | H2 cần thuyết minh. Crawl + OCR PDF quý cho ~200 DN × 40 quý rất nặng | Dùng thuyết minh**năm**, áp dụng cho 4 quý sau ngày công bố                           |
| 2 | **Số liệu quý lấy từ API hay tự OCR?** Parser hiện tại chỉ đọc được trung vị 30/65 biến             | Thiếu số thì bước [7] không tính được nhân tố, P5 bị chặn      | Lấy từ API, map`variables.yaml` sang tên trường của API                                      |
| 3 | **Thông tin thuyết minh chưa đi vào con số.** 5 biến "từ thuyết minh" chỉ là đếm từ khoá, quá lỏng | Nếu H2 thắng cũng khó nói thuyết minh đóng góp gì                  | Trích vài con số thật từ thuyết minh (phải thu bên liên quan, loại ý kiến kiểm toán…) |
| 4 | **Có giữ ngân hàng / chứng khoán?** Chỉ 15 biến áp dụng được; mô hình yếu rõ ở nhóm này         | Mẫu biểu BCTC khác hẳn doanh nghiệp thường                            | Loại khỏi universe, như thông lệ nghiên cứu nhân tố                                         |
| 5 | **Định vị "giải thích được ngay từ thiết kế" + thêm H5?**                                               | Ngân hàng và quỹ không chấp nhận hộp đen                            | Có: tuyến tính làm mốc, SHAP, phiếu giải thích                                               |
| 6 | **Chấp nhận bộ sinh 5,1B tổng (Gemma) hay dùng 2B (Qwen3.5)?**                                                 | Thầy muốn mô hình "vài trăm triệu"                                    | Trình số liệu benchmark để thầy quyết                                                         |

Ngoài ra còn một việc kỹ thuật: **chưa có bộ tính công thức → số**. Đây là cầu nối khối 2 → khối 3,
nên viết ngay trong P2 và dùng chung bộ phân tích cú pháp với validator.

---

## 11. Trạng thái hiện tại — 26/09/2026

**P0 gần xong.** Còn: tờ trình 1 trang, chấm C4, họp thầy 01/10.

| Việc                                                              | Trạng thái             |
| ------------------------------------------------------------------ | ------------------------ |
| Bộ thử 76 prompt (4 họ F1–F4, thiết kế theo cặp)            | ✅`eval/prompts.jsonl` |
| Benchmark 4 mô hình × 76 prompt × 3 seed, Kaggle T4, NF4 4-bit | ✅`bench/table.md`     |
| Chấm tay ý nghĩa kinh tế (C4)                                  | ❌ 0/80                  |
| Tờ trình chốt mô hình                                         | ❌                       |

**Kết quả benchmark** (công thức hợp lệ / công thức yêu cầu; chi tiết và định nghĩa trong `bench/table.md`):

| Mô hình                | Hợp lệ               | Nếu cứu JSON vỡ | VRAM cần | Nhận xét ngắn                                                                                          |
| ------------------------ | ---------------------- | ------------------ | --------- | --------------------------------------------------------------------------------------------------------- |
| **Gemma-4-E2B-it** | **47,2% ± 2,6** | 49,9%              | ~3,7GB    | Ổn định, đúng định dạng 92%, duy nhất làm được ngân hàng. Nhiều công thức 1 biến (37%) |
| Qwen3.5-2B               | 13,3% ± 2,4           | 30,3%              | ~3,3GB    | Công thức "ra dáng" nhất nhưng hỏng vỏ JSON và dùng`/` dù bị cấm                            |
| Qwen3.5-0.8B             | 12,0% ± 1,1           | 16,2%              | ~2,4GB    | Quá nhỏ: không có ví dụ mẫu thì gần như không làm được                                     |
| Sailor2-1B               | 3,8% ± 2,4            | 11,3%              | ~3,1GB    | Không hiểu đề, nên loại                                                                             |

**Chưa mô hình nào đạt ngưỡng CHỐT 2 (≥60%)**, nhưng phần lớn lỗi là lỗi cơ học (định dạng, dấu `/`,
thừa tham số), loại lỗi mà giải mã ràng buộc ngữ pháp (GCD) chặn được → thử GCD sớm, trước P4.

- Bóc tách công việc P0: [docs/P0_breakdown.md](docs/P0_breakdown.md)
- Spec từng task: [docs/specs/](docs/specs/)
- Hướng dẫn chạy benchmark: [bench/README.md](bench/README.md)
