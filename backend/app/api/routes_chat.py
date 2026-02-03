from fastapi import APIRouter
from app.services.retriever import retrieve_chunks

router = APIRouter()

@router.post("/chat")
def chat(query: str):
    chunks = retrieve_chunks(query)

    context = "\n".join(chunks)

    return {
        "query": query,
        "context_used": context
    }

