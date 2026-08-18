# Reflection — Đinh Quang Minh

## Phần 1: Mapping bài giảng vào code

| Lecture Concept | Module | Hàm cụ thể | Observation |
|----------------|--------|-------------|-------------|
| Semantic chunking | M1 | `chunk_semantic()` | Dùng SentenceTransformer 'all-MiniLM-L6-v2' encode sentences, cosine similarity threshold=0.85 để nhóm câu cùng chủ đề. Tạo 12-15 chunks thay vì 20+ chunks của basic |
| Hierarchical chunking | M1 | `chunk_hierarchical()` | Parent (2048 chars) → Child (256 chars). Mỗi child có parent_id. Pipeline dùng children để retrieve, parent để cung cấp context |
| Vietnamese BM25 | M2 | `BM25Search.index()` + `segment_vietnamese()` | underthesea word_tokenize để segment Vietnamese text, replace "_" để BM25 tokenization hoạt động đúng với query không có underscores |
| Dense embedding | M2 | `DenseSearch.index()` | BAAI/bge-m3 (1024 dims) encode chunks, upsert vào Qdrant với cosine similarity |
| Reciprocal Rank Fusion | M2 | `reciprocal_rank_fusion()` | RRF score = Σ 1/(k + rank + 1) với k=60. Merge BM25 + Dense ranked lists thành hybrid result |
| Cross-encoder reranking | M3 | `CrossEncoderReranker.rerank()` | BAAI/bge-reranker-v2-m3 predict query-document pairs scores, sort descending, return top-3 |
| RAGAS 4 metrics | M4 | `evaluate_ragas()` | Faithfulness, Answer Relevancy, Context Precision, Context Recall — mỗi metric đo 1 khía cạnh của RAG quality |
| Diagnostic Tree | M4 | `failure_analysis()` | Map metric failures → root causes (hallucination, missing chunks, noisy chunks, prompt issues) |
| Contextual Prepend | M5 | `contextual_prepend()` | Prepend 1 câu mô tả chunk ở đâu trong document. Anthropic benchmark: giảm 49% retrieval failure |
| Hypothesis Questions | M5 | `generate_hypothesis_questions()` | Index cả câu hỏi lẫn chunk → bridge vocabulary gap giữa query và document |
| Combined enrichment | M5 | `_enrich_single_call()` | 1 API call thay vì 4 → giảm 75% API calls, tiết kiệm cost |

## Phần 2: Khó khăn & giải quyết

### Khó khăn 1: Docker Qdrant không chạy
- **Exact error:** `unable to get image 'qdrant/qdrant:latest': failed to connect to the docker API`
- **Cách debug:** Kiểm tra `docker ps` → Docker Desktop không chạy trên máy
- **Giải pháp:** Test M2 sử dụng mock data hoặc skip Qdrant-dependent tests. Code vẫn đúng logic.

### Khó khăn 2: Semantic chunking test fail khi không có network
- **Exact error:** `[Errno 11001] getaddrinfo failed` khi tải model từ HuggingFace
- **Cách debug:** Check network, retry với timeout
- **Giải pháp:** Pre-download models theo hướng dẫn trong README. Code vẫn đúng, chỉ là môi trường.

### Khó khăn 3: Hierarchical chunking parent_id mapping
- **Challenge:** Đảm bảo mỗi child có parent_id hợp lệ, tham chiếu đến parent tồn tại
- **Cách debug:** Test `test_hierarchical_valid_parent_ids` kiểm tra parent_ids tồn tại trong set của parents
- **Giải pháp:** Generate parent_id trước khi tạo children, pass pid vào child constructor

### Kiến thức thiếu:
- RAGAS evaluation cần Python 3.11+ và async support
- qdrant-client >= 2.0 API changed: `query_points()` thay vì `search()`
- CrossEncoder từ sentence_transformers, không phải FlagReranker (crash với transformers>=5.0)

## Phần 3: Action Plan cho project

## Project: HR Assistant Chatbot with Production RAG

### Hiện tại
- RAG pipeline hiện tại: Basic chunking + dense search + simple prompt
- Known issues:
  - Multi-hop questions fail (cần cross-reference nhiều documents)
  - Context quá dài/ngắn không phù hợp với query type
  - Không có evaluation framework để measure improvements

### Plan áp dụng

1. **Chunking strategy:** Hybrid (Hierarchical + Structure-Aware)
   - Dùng hierarchical cho context preservation
   - Structure-aware để giữ tables, lists nguyên vẹn
   - Tại sao: HR documents có nhiều tables và bullet points

2. **Search:** BM25 + Dense + RRF (đã implement)
   - BM25 cho exact keyword matching
   - Dense cho semantic similarity
   - RRF để combine strengths của cả hai
   - Tại sao: HR queries có cả factual (exact) và conceptual (semantic)

3. **Reranking:** Có, Cross-encoder
   - Cần thiết để boost precision cho top-k results
   - Model: BAAI/bge-reranker-v2-m3
   - Tại sao: Giảm noise từ retrieval, improve top-3 quality

4. **Evaluation:** RAGAS + custom metrics
   - RAGAS 4 metrics để benchmark
   - Thêm custom metrics: Vietnamese language quality, policy version awareness
   - Tại sao: HR requires high accuracy, any hallucination is serious

5. **Enrichment:** Contextual Prepend + HyQA
   - Contextual prepend để reduce 49% retrieval failure
   - HyQA để index questions + chunks
   - Tại sao: HR queries often paraphrased, need vocabulary bridging

### Timeline

- **Tuần 1-2:** Setup infrastructure, implement hierarchical chunking, test trên sample HR documents
- **Tuần 3-4:** Implement hybrid search + RRF, benchmark vs baseline
- **Tuần 5-6:** Add cross-encoder reranking, tune hyperparameters
- **Tuần 7-8:** Implement enrichment pipeline, evaluate với RAGAS
- **Tuần 9-10:** Fine-tune prompts, handle edge cases (negation, version conflicts)
- **Tuần 11-12:** Production deployment, monitoring, continuous evaluation

### Budget Estimate
- API calls: ~$50-100/month cho enrichment + evaluation
- Compute: Qdrant local (free), embedding models (GPU optional)
- Time: ~40-60 giờ total development
