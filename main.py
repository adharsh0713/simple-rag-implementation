from src.utils import extract_text, split_text
from src.embeddings import create_embeddings
from src.vector_store import VectorStore
from src.llm import generate_answer

text = extract_text("data/rag_test_document.pdf")

chunks = split_text(text)

vectors = create_embeddings(chunks)

store = VectorStore()

store.add(
    vectors,
    chunks
)

question = "Types of machine learning?"

query_vector = create_embeddings(
    [question]
)[0]

results = store.search(
    query_vector,
    k=3
)

context = "\n\n".join(results)

answer = generate_answer(
    context,
    question
)

print("\nAnswer:")
print(answer)