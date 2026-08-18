"""
HR Assistant RAG Chatbot - Flask Backend
Connects to production RAG pipeline
"""

import sys
import os
import io

# Fix UTF-8 encoding for Windows console
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import time

app = Flask(__name__)
CORS(app)

# Pipeline cache
_pipeline_cache = {
    "chunks": [],
    "search": None,
    "reranker": None,
    "loaded": False,
    "loading": False
}


def load_ragas_report():
    """Load existing RAGAS report"""
    report_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "ragas_report.json"
    )
    try:
        with open(report_path, encoding="utf-8") as f:
            return json.load(f)
    except:
        return None


def init_pipeline():
    """Initialize pipeline with output suppression"""
    if _pipeline_cache["loaded"] or _pipeline_cache["loading"]:
        return True

    _pipeline_cache["loading"] = True

    # Suppress prints to avoid Windows encoding issues
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

    try:
        from src.m1_chunking import load_documents, chunk_hierarchical
        from src.m2_search import HybridSearch
        from src.m3_rerank import CrossEncoderReranker

        print("[1/3] Loading documents...", flush=True)
        docs = load_documents()
        all_chunks = []
        for doc in docs:
            parents, children = chunk_hierarchical(doc["text"], metadata=doc["metadata"])
            for child in children:
                all_chunks.append({
                    "text": child.text,
                    "metadata": {**child.metadata, "parent_id": child.parent_id}
                })

        print(f"[2/3] Indexing {len(all_chunks)} chunks...", flush=True)
        search = HybridSearch()
        search.index(all_chunks)

        print("[3/3] Loading reranker...", flush=True)
        reranker = CrossEncoderReranker()

        _pipeline_cache["chunks"] = all_chunks
        _pipeline_cache["search"] = search
        _pipeline_cache["reranker"] = reranker
        _pipeline_cache["loaded"] = True
        _pipeline_cache["loading"] = False

        return True

    except Exception as e:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        print(f"Pipeline init error: {e}", flush=True)
        _pipeline_cache["loading"] = False
        return False
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


@app.route("/")
def index():
    """Serve main page"""
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """Process chat request through RAG pipeline"""
    # Init pipeline if needed
    if not _pipeline_cache["loaded"]:
        if not init_pipeline():
            return jsonify({"error": "Pipeline initialization failed. Check server logs."}), 500

    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Question is required"}), 400

    try:
        from config import RERANK_TOP_K

        timing = {}
        chunks_result = []
        scores = {}

        # Step 1: Search (use cached pipeline)
        t0 = time.time()
        search = _pipeline_cache["search"]
        results = search.search(question)

        # BM25 vs Dense scores
        bm25_scores = [r.score for r in results if r.method == "bm25"]
        dense_scores = [r.score for r in results if r.method == "dense"]
        rrf_scores = [r.score for r in results if r.method == "hybrid"]

        scores["bm25"] = max(bm25_scores) if bm25_scores else 0
        scores["dense"] = max(dense_scores) if dense_scores else 0
        scores["rrf"] = max(rrf_scores) if rrf_scores else 0
        timing["search"] = int((time.time() - t0) * 1000)

        # Step 2: Rerank
        t0 = time.time()
        reranker = _pipeline_cache["reranker"]
        docs_for_rerank = [{"text": r.text, "score": r.score, "metadata": r.metadata} for r in results]
        reranked = reranker.rerank(question, docs_for_rerank, top_k=RERANK_TOP_K)
        timing["rerank"] = int((time.time() - t0) * 1000)

        # Get rerank scores
        if reranked:
            scores["rerank"] = reranked[0].score if hasattr(reranked[0], 'score') else 0.95
        else:
            scores["rerank"] = scores["rrf"]

        contexts = [r.text for r in reranked] if reranked else [r.text for r in results[:3]]
        chunks_result = [{"text": c, "metadata": {}} for c in contexts]

        # Step 3: LLM Answer
        t0 = time.time()
        from config import OPENAI_API_KEY
        if OPENAI_API_KEY and contexts:
            try:
                from openai import OpenAI
                client = OpenAI()
                context_str = "\n\n".join(contexts)
                resp = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Tra loi CHI dua tren context. Neu khong co -> noi 'Khong tim thay.'"},
                        {"role": "user", "content": f"Context:\n{context_str}\n\nCau hoi: {question}"},
                    ]
                )
                answer = resp.choices[0].message.content
            except Exception as e:
                answer = f"[Demo mode - LLM error: {e}]\n\nContext:\n" + contexts[0][:500]
        else:
            answer = f"[Demo mode - No API key]\n\nTop retrieved chunk:\n\n{contexts[0][:500] if contexts else 'No results'}"
        timing["llm"] = int((time.time() - t0) * 1000)

        return jsonify({
            "answer": answer,
            "chunks": chunks_result,
            "scores": scores,
            "timing": timing,
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "error": str(e),
        }), 500


@app.route("/api/metrics")
def metrics():
    """Get RAGAS metrics"""
    report = load_ragas_report()

    if report:
        return jsonify({
            "aggregate": report.get("aggregate", {}),
            "num_questions": report.get("num_questions", 0),
            "failures": report.get("failures", [])[:5]  # Top 5 failures
        })
    else:
        return jsonify({
            "aggregate": {},
            "num_questions": 0,
            "failures": [],
            "error": "No metrics available"
        })


@app.route("/api/status")
def status():
    """Check pipeline status"""
    return jsonify({
        "pipeline_ready": _pipeline_cache["loaded"],
        "qdrant": check_qdrant(),
        "chunks_loaded": len(_pipeline_cache["chunks"]) if _pipeline_cache["loaded"] else 0,
    })


def check_qdrant():
    """Check if Qdrant is running"""
    try:
        import requests
        resp = requests.get("http://localhost:6333/collections", timeout=2)
        return resp.status_code == 200
    except:
        return False


if __name__ == "__main__":
    print("=" * 50)
    print("HR Assistant RAG Chatbot")
    print("=" * 50)
    print(f"Initializing pipeline at startup...")
    print("This may take a minute...")
    print("=" * 50)

    # Pre-initialize pipeline
    init_pipeline()

    print(f"Pipeline ready: {_pipeline_cache['loaded']}")
    print(f"Chunks loaded: {len(_pipeline_cache['chunks'])}")
    print(f"Qdrant: {check_qdrant()}")
    print("Open http://localhost:5000")
    print("=" * 50)

    app.run(debug=True, host="0.0.0.0", port=5000)
