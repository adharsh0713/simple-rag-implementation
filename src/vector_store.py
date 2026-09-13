import faiss
import numpy as np
import pickle


class VectorStore:

    def __init__(self):
        self.index = None
        self.chunks = []


    def add(self, vectors, chunks):

        vectors = np.array(vectors).astype("float32")

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(vectors)

        self.chunks = chunks


    def search(self, query_vector, k=3):

        query_vector = np.array(
            [query_vector]
        ).astype("float32")


        distances, indices = self.index.search(
            query_vector,
            k
        )


        results = []

        for index in indices[0]:
            results.append(
                self.chunks[index]
            )

        return results


    def save(self, path):

        faiss.write_index(
            self.index,
            path + ".faiss"
        )

        with open(path + ".pkl", "wb") as f:
            pickle.dump(
                self.chunks,
                f
            )


    def load(self, path):

        self.index = faiss.read_index(
            path + ".faiss"
        )

        with open(path + ".pkl", "rb") as f:
            self.chunks = pickle.load(f)