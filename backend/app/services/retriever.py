from app.services.embedding import embed_texts
from app.services.vector_store import vector_store

def retrieve_chunks(query: str, top_k: int = 3):
    query_embedding = embed_texts([query])[0]
    results = vector_store.search(query_embedding, top_k=top_k)
    return results
