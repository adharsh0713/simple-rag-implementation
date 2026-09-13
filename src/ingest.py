from src.utils import extract_pages
from src.chunking import create_chunks
from src.embeddings import create_embeddings
from src.vector_store import VectorStore


pages = extract_pages(
    "data/rag_test_document.pdf"
)


chunks = create_chunks(
    pages,
    "rag_test_document.pdf"
)


vectors = create_embeddings(
    chunks
)


store = VectorStore()


store.add(
    vectors,
    chunks
)


store.save(
    "storage/document_index"
)


print("Indexed", len(chunks), "chunks")