import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings: np.ndarray, texts: list[str]):
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding: np.ndarray, k=3):
        distances, indices = self.index.search(query_embedding, k)
        return [self.texts[i] for i in indices[0]]
