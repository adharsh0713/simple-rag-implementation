from src.embeddings import create_embeddings
from src.vector_store import VectorStore
from src.llm import generate_answer


class RAG:

    def __init__(self):

        self.store = VectorStore()

        self.store.load(
            "storage/document_index"
        )


    def ask(self, question):

        query_vector = create_embeddings(
            [question]
        )[0]


        results = self.store.search(
            query_vector
        )


        if not results:
            return {
                "answer": "No relevant information found.",
                "sources": []
            }


        context = "\n\n".join(
            [
                item["chunk"]["text"]
                for item in results
            ]
        )


        answer = generate_answer(
            context,
            question
        )


        sources = [
            {
                "source": item["chunk"]["source"],
                "page": item["chunk"]["page"],
                "score": item["score"]
            }
            for item in results
        ]

        for item in results:

            print(
                {
                    "score": item["score"],
                    "source": item["chunk"]["source"],
                    "page": item["chunk"]["page"]
                }
            )

        return {
            "answer": answer,
            "sources": sources
        }