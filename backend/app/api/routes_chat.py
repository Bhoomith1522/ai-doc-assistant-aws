from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.retriever import retrieve_chunks
from app.services.llm import generate_answer

router = APIRouter()

@router.post("/chat")
def chat(query: str):
    results = retrieve_chunks(query)

    if not results:
        return {
            "answer": "No documents indexed yet",
            "sources": []
        }

    answer = generate_answer(query, results)

    sources = list({r["meta"].get("source", "unknown") for r in results})

    return {
        "answer": answer,
        "sources": sources
}