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

        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.index.add(vectors)

        self.chunks = chunks


    def search(
        self,
        query_vector,
        k=5,
        threshold=0.35
    ):

        query_vector = np.array(
            [query_vector]
        ).astype("float32")


        scores, indices = self.index.search(
            query_vector,
            k
        )


        results = []


        for score, index in zip(
            scores[0],
            indices[0]
        ):

            print("score:", score)
            if score >= threshold:

                results.append(
                    {
                        "chunk": self.chunks[index],
                        "score": float(score)
                    }
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