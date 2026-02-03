from fastapi import APIRouter
from app.services.retriever import retrieve_chunks

router = APIRouter()

@router.get("/debug/retrieve")
def debug_retrieve(q: str):
    results = retrieve_chunks(q)
    return {
        "query": q,
        "results": results
    }