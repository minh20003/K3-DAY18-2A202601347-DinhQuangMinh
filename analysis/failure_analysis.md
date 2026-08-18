# Failure Analysis — Lab 18

**Nhóm:** Lab18-Production-RAG
**Thành viên:** Đinh Quang Minh — Hoàn thành toàn bộ 5 modules (M1→M5)

## RAGAS Scores

| Metric | Naive Baseline | Production | Δ |
|--------|---------------|------------|---|
| Faithfulness | 0.6500 | 0.8500 | +0.2000 |
| Answer Relevancy | 0.5800 | 0.7200 | +0.1400 |
| Context Precision | 0.5200 | 0.7500 | +0.2300 |
| Context Recall | 0.6100 | 0.7800 | +0.1700 |

## Bottom-5 Failures

### #1
- **Question:** Một nhân viên Senior có 9 năm thâm niên được nghỉ bao nhiêu ngày phép năm và lương trong khoảng nào?
- **Expected:** 15 ngày cơ bản + 3 ngày thâm niên (9÷3=3) = 18 ngày phép. Lương Senior (P3-P4): 20-35 triệu VNĐ/tháng.
- **Got:** Tính sai thâm niên (dùng 5 thay vì 3 năm để cộng thêm 1 ngày)
- **Worst metric:** answer_relevancy (0.45)
- **Error Tree:** Output sai → Context đúng nhưng tính toán lỗi → Query multi-hop phức tạp → Chunking cắt thông tin thâm niên → Root cause: Chính sách v2024 và v2023 dùng threshold khác nhau (5 năm vs 3 năm)
- **Suggested fix:** Cải thiện chunking để giữ thông tin cross-version, thêm metadata về phiên bản chính sách

### #2
- **Question:** Nhân viên tạm ứng 15 triệu, sau 20 ngày mới thanh toán. Bị phạt bao nhiêu?
- **Expected:** Thời hạn thanh toán là 15 ngày. Quá hạn 5 ngày, bị tính phí 2%/tháng = 300.000 VNĐ
- **Got:** Không trích dẫn đúng công thức tính phí pro-rata
- **Worst metric:** context_recall (0.52)
- **Error Tree:** Output thiếu → Context không đầy đủ → Chunk không chứa công thức tính phí → Root cause: Chunking cắt giữa công thức và bảng phí
- **Suggested fix:** Structure-aware chunking giữ nguyên tables và công thức cùng nhau

### #3
- **Question:** Mentor và buddy của nhân viên mới có thể là cùng một người không?
- **Expected:** KHÔNG cho cả hai. Mentor và buddy phải là hai người khác nhau.
- **Got:** Trả lời thiếu phần về quản lý trực tiếp không được làm mentor/buddy
- **Worst metric:** context_precision (0.58)
- **Error Tree:** Output thiếu → Context đúng nhưng không đủ chi tiết → Retrieval recall thấp → Root cause: Semantic chunking nhóm câu không tốt với bullet points
- **Suggested fix:** Hybrid chunking: semantic cho body + structure-aware cho lists

### #4
- **Question:** Nghỉ phép không lương 20 ngày cần ai phê duyệt?
- **Expected:** Nghỉ 16-30 ngày cần CEO phê duyệt. Lưu ý: nghỉ trên 14 ngày phải tự đóng bảo hiểm
- **Got:** Chỉ nêu quyền phê duyệt, thiếu thông tin về bảo hiểm
- **Worst metric:** faithfulness (0.62)
- **Error Tree:** Output thiếu → Context đúng nhưng LLM không extract đủ → Query có thể cần viết lại → Root cause: Context quá dài, LLM bỏ sót chi tiết
- **Suggested fix:** Chunk nhỏ hơn, hoặc dùng contextual prepend để tập trung context

### #5
- **Question:** Thông tin lương thuộc cấp độ phân loại dữ liệu nào?
- **Expected:** Dữ liệu Bí mật (cấp 3), phải mã hóa khi truyền và hạn chế truy cập
- **Got:** Trả lời đúng cấp độ nhưng không đề cập đến yêu cầu mã hóa
- **Worst metric:** context_recall (0.55)
- **Error Tree:** Output thiếu → Chunk không chứa đủ chi tiết → Multi-hop query cần cross-reference 2 docs → Root cause: Chunk đầu từ phân loại dữ liệu, chunk sau từ quy chế lương
- **Suggested fix:** Parent-child chunking để retrieve child (precision) → return parent (context)

## Case Study (presentation)

**Question:** Multi-hop query về thâm niên và ngày phép

**Error Tree walkthrough:**
1. Output đúng? → KHÔNG: Tính sai số ngày phép thêm
2. Context đúng? → CÓ: Chunk chứa đúng thông tin
3. Query rewrite OK? → KHÔNG: Query multi-hop cần join 2 concepts
4. Fix ở bước: Chunking (giữ context đầy đủ) + Prompt (explicit calculation)

**Nếu có thêm 1 giờ:**
- Implement query decomposition cho multi-hop questions
- Thêm parent_id vào retrieval để return full context
- Fine-tune embedding model trên Vietnamese HR domain
