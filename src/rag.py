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
            query_vector,
            k=3
        )


        context = "\n\n".join(
            [
                r["text"]
                for r in results
            ]
        )


        answer = generate_answer(
            context,
            question
        )


        sources = [
            {
                "source": r["source"],
                "page": r["page"]
            }
            for r in results
        ]


        return {
            "answer": answer,
            "sources": sources
        }