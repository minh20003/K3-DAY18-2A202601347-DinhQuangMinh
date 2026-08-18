from __future__ import annotations

"""Module 4: RAGAS Evaluation — 4 metrics + failure analysis."""

import os, sys, json
from dataclasses import dataclass

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import TEST_SET_PATH


@dataclass
class EvalResult:
    question: str
    answer: str
    contexts: list[str]
    ground_truth: str
    faithfulness: float
    answer_relevancy: float
    context_precision: float
    context_recall: float


def load_test_set(path: str = TEST_SET_PATH) -> list[dict]:
    """Load test set from JSON. (Đã implement sẵn)"""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def evaluate_ragas(questions: list[str], answers: list[str],
                   contexts: list[list[str]], ground_truths: list[str]) -> dict:
    """Run RAGAS evaluation."""
    try:
        from ragas import evaluate
        from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
        from datasets import Dataset

        dataset = Dataset.from_dict({
            "question": questions,
            "answer": answers,
            "contexts": contexts,
            "ground_truth": ground_truths,
        })

        result = evaluate(
            dataset,
            metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
        )

        df = result.to_pandas()

        per_question = []
        for _, row in df.iterrows():
            per_question.append(EvalResult(
                question=str(row["question"]),
                answer=str(row["answer"]),
                contexts=list(row["contexts"]) if row["contexts"] else [],
                ground_truth=str(row["ground_truth"]),
                faithfulness=float(row.get("faithfulness", 0.0)),
                answer_relevancy=float(row.get("answer_relevancy", 0.0)),
                context_precision=float(row.get("context_precision", 0.0)),
                context_recall=float(row.get("context_recall", 0.0))
            ))

        # Calculate aggregate scores
        n = len(per_question) if per_question else 1
        return {
            "faithfulness": sum(e.faithfulness for e in per_question) / n if per_question else 0.0,
            "answer_relevancy": sum(e.answer_relevancy for e in per_question) / n if per_question else 0.0,
            "context_precision": sum(e.context_precision for e in per_question) / n if per_question else 0.0,
            "context_recall": sum(e.context_recall for e in per_question) / n if per_question else 0.0,
            "per_question": per_question
        }

    except Exception as e:
        print(f"  ⚠️  RAGAS evaluation failed: {e}")
        return {
            "faithfulness": 0.0,
            "answer_relevancy": 0.0,
            "context_precision": 0.0,
            "context_recall": 0.0,
            "per_question": []
        }


def failure_analysis(eval_results: list[EvalResult], bottom_n: int = 10) -> list[dict]:
    """Analyze bottom-N worst questions using Diagnostic Tree."""
    # Diagnostic tree mapping metric -> (diagnosis, suggested_fix)
    diagnostic_tree = {
        "faithfulness": (
            "LLM hallucinating - generated answer doesn't match retrieved context",
            "Tighten prompt, lower temperature, add citation requirements"
        ),
        "context_recall": (
            "Missing relevant chunks - retrieval failed to capture all necessary context",
            "Improve chunking strategy, add BM25 fallback, adjust embedding model"
        ),
        "context_precision": (
            "Too many irrelevant chunks - retrieved context includes noisy content",
            "Add reranking, metadata filtering, improve chunk boundaries"
        ),
        "answer_relevancy": (
            "Answer doesn't match question - query understanding or answer generation issue",
            "Improve prompt template, check for multi-hop reasoning, verify context"
        ),
    }

    # Compute average score and find worst metric for each result
    scored_results = []
    for result in eval_results:
        metrics = {
            "faithfulness": result.faithfulness,
            "answer_relevancy": result.answer_relevancy,
            "context_precision": result.context_precision,
            "context_recall": result.context_recall,
        }
        avg_score = sum(metrics.values()) / len(metrics)
        worst_metric = min(metrics, key=metrics.get)
        scored_results.append({
            "result": result,
            "avg_score": avg_score,
            "worst_metric": worst_metric,
            "worst_score": metrics[worst_metric]
        })

    # Sort by average score ascending (worst first) and take bottom_n
    scored_results.sort(key=lambda x: x["avg_score"])
    bottom_results = scored_results[:bottom_n]

    # Build failure analysis
    failures = []
    for item in bottom_results:
        diag = diagnostic_tree.get(item["worst_metric"], ("Unknown issue", "Review manually"))
        failures.append({
            "question": item["result"].question,
            "worst_metric": item["worst_metric"],
            "score": item["worst_score"],
            "avg_score": item["avg_score"],
            "diagnosis": diag[0],
            "suggested_fix": diag[1],
            "all_metrics": {
                "faithfulness": item["result"].faithfulness,
                "answer_relevancy": item["result"].answer_relevancy,
                "context_precision": item["result"].context_precision,
                "context_recall": item["result"].context_recall,
            }
        })

    return failures


def save_report(results: dict, failures: list[dict], path: str = "ragas_report.json"):
    """Save evaluation report to JSON. (Đã implement sẵn)"""
    report = {
        "aggregate": {k: v for k, v in results.items() if k != "per_question"},
        "num_questions": len(results.get("per_question", [])),
        "failures": failures,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"Report saved to {path}")


if __name__ == "__main__":
    test_set = load_test_set()
    print(f"Loaded {len(test_set)} test questions")
    print("Run pipeline.py first to generate answers, then call evaluate_ragas().")
