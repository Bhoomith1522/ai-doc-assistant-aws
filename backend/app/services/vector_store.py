import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.vectors = []
        self.texts = []

    def add(self, embeddings, texts):
        self.vectors.extend(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding, top_k=3):
        if not self.vectors:
            return []

        vectors = np.array(self.vectors)
        query = np.array(query_embedding)

        similarities = np.dot(vectors, query) / (
            np.linalg.norm(vectors, axis=1) * np.linalg.norm(query)
        )

        top_indices = similarities.argsort()[-top_k:][::-1]
        return [self.texts[i] for i in top_indices]
    
    
    
    
    
    

vector_store = VectorStore(dim=384)
