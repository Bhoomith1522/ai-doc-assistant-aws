import numpy as np
import pickle
import os


class VectorStore:
    def __init__(self, dim, persist_path="vector_store.pkl"):
        self.dim = dim
        self.vectors = []
        self.texts = []
        self.persist_path = persist_path

        # auto load if exists
        if os.path.exists(self.persist_path):
            self.load()

    def add(self, embeddings, texts):
        self.vectors.extend(embeddings)
        self.texts.extend(texts)
        self.save()

    def search(self, query_vector, top_k=3):
        if len(self.vectors) == 0:
            return []

        mat = np.array(self.vectors)
        sims = mat @ query_vector
        idxs = np.argsort(sims)[-top_k:][::-1]
        return [self.texts[i] for i in idxs]

    def save(self):
        with open(self.persist_path, "wb") as f:
            pickle.dump((self.vectors, self.texts), f)

    def load(self):
        with open(self.persist_path, "rb") as f:
            self.vectors, self.texts = pickle.load(f)


vector_store = VectorStore(dim=384)
