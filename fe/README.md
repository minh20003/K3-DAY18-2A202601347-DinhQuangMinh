# HR Assistant - Frontend

## Setup

```bash
cd fe
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Mở browser: http://localhost:5000

## Features

- **Chat**: Hỏi đáp HR policy với citations
- **Pipeline Demo**: Xem chi tiết 5 bước RAG
- **Metrics**: Xem RAGAS scores

## Prerequisites

- Python 3.11+
- Flask
- Qdrant container running (Docker)
- OpenAI API key (optional, for full LLM support)
