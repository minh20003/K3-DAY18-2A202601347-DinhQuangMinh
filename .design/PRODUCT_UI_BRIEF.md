# PRODUCT UI BRIEF

## Mode
FAST LAB

## Product summary
HR Assistant Chatbot với Production RAG Pipeline. Demo trực quan để show RAG system hoạt động: chunking → search → rerank → answer → evaluation.

## Target user
- Sinh viên/thầy review demo
- Người học muốn hiểu RAG pipeline hoạt động thế nào

## Primary job-to-be-done
Gõ câu hỏi về HR policy → nhận câu trả lời kèm debug info (chunks retrieved, scores, ranking)

## Core workflows
1. User nhập câu hỏi HR
2. Backend xử lý: enrich → hybrid search → rerank → LLM answer
3. Frontend hiển thị: câu trả lời + citations + pipeline stats
4. (Optional) User xem chi tiết từng bước

## Product archetype
Primary: RAG / AI Assistant
Secondary: Chat / Messaging

## Demo story
User hỏi "Nhân viên mới được nghỉ bao nhiêu ngày phép?" → System trả lời + show chunks đã retrieve + scores từng bước (BM25, Dense, RRF, Rerank)

## Information objects
- Question (input)
- Answer (output)
- Retrieved Chunks (debug)
- Search Scores (BM25, Dense, RRF)
- Reranked Results
- RAGAS Metrics (sidebar)

## Critical states
- loading: streaming answer với progress indicator
- empty: prompt starter questions
- error: connection error hoặc LLM fail
- streaming: partial answer hiển thị

## Assumptions
- Backend Flask chạy local
- Qdrant đang chạy trong Docker
- Không có auth
- Mobile-friendly nhưng desktop-first

## Non-goals
- Không cần authentication
- Không cần lưu conversation history
- Không cần deploy lên cloud
