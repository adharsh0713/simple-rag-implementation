from src.embeddings import create_embeddings
from src.vector_store import VectorStore
from src.llm import generate_answer


store = VectorStore()


store.load(
    "storage/document_index"
)


question = input(
    "Ask question: "
)


query_vector = create_embeddings(
    [question]
)[0]


results = store.search(
    query_vector
)


context = "\n\n".join(
    r["text"]
    for r in results
)


answer = generate_answer(
    context,
    question
)

sources = set(
    (r["source"], r["page"])
    for r in results
)

print(answer)

print("\nSources:")
for source, page in sources:
    print(f"- {source}, Page {page}")