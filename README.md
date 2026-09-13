# Simple RAG System

A from-scratch implementation of a Retrieval Augmented Generation (RAG) system.

This project demonstrates the complete RAG pipeline:

- Document ingestion
- Text extraction
- Recursive chunking
- Embedding generation
- Vector similarity search
- Context retrieval
- LLM-based answer generation
- REST API
- Web interface
- Basic evaluation dashboard

---

# Architecture

```
                INGESTION PIPELINE

PDF Documents
      |
      v
Text Extraction (PyMuPDF)
      |
      v
Recursive Chunking
      |
      v
Embedding Generation
(Sentence Transformers)
      |
      v
FAISS Vector Database
      |
      v
Persistent Storage



                QUERY PIPELINE

User Question
      |
      v
Generate Query Embedding
      |
      v
FAISS Similarity Search
      |
      v
Retrieve Relevant Chunks
      |
      v
Context + Question
      |
      v
LLM (Ollama)
      |
      v
Generated Answer
```

---

# Features

## Document Processing

- Extract text from PDF documents
- Split documents into meaningful chunks
- Preserve metadata:
  - Source document
  - Page number

Example:

```json
{
  "text": "Machine learning enables computers to learn patterns...",
  "source": "document.pdf",
  "page": 1
}
```

---

## Embedding Generation

Uses:

```
Sentence Transformers
all-MiniLM-L6-v2
```

Text is converted into numerical vectors:

```
"Machine learning"

        ↓

[0.21, 0.84, -0.12, ...]
```

Similar meanings produce similar vectors.

---

## Vector Search

Uses:

```
FAISS
```

Features:

- Vector indexing
- Similarity search
- Top-k retrieval
- Similarity threshold filtering

---

## LLM Generation

Uses:

```
Ollama + Llama 3.2
```

The LLM receives:

```
Retrieved Context

+

User Question

↓

Final Answer
```

The model generates answers using retrieved document context.

---

# Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| PDF Processing | PyMuPDF |
| Chunking | LangChain Text Splitters |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| LLM | Ollama |
| Backend API | FastAPI |
| Frontend | Streamlit |
| Evaluation | Streamlit + Matplotlib |

---

# Project Structure

```
simple-rag/

├── app.py                    # Streamlit frontend
│
├── src/
│   ├── api.py                # FastAPI server
│   ├── rag.py                # RAG pipeline
│   ├── llm.py                # LLM generation
│   ├── embeddings.py         # Embedding generation
│   ├── vector_store.py       # FAISS operations
│   ├── chunking.py           # Document chunking
│   └── utils.py              # PDF utilities
│
├── data/
│   └── sample.pdf
│
├── storage/
│   ├── document_index.faiss
│   └── document_index.pkl
│
├── evaluation/
│   ├── questions.json
│   ├── evaluate.py
│   ├── results.json
│   └── dashboard.py
│
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd simple-rag
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup Ollama

Install Ollama:

```
https://ollama.com
```

Download model:

```bash
ollama pull llama3.2
```

Verify:

```bash
ollama list
```

---

# Create Knowledge Base

Place PDFs inside:

```
data/
```

Run ingestion:

```bash
python src/ingest.py
```

This creates:

```
storage/

document_index.faiss
document_index.pkl
```

---

# Run Application

## Start FastAPI

Terminal 1:

```bash
uvicorn src.api:app --reload
```

API:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit

Terminal 2:

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# API Usage

Endpoint:

```
POST /ask
```

Request:

```json
{
    "question": "What is machine learning?"
}
```

Response:

```json
{
    "answer": "Machine learning is...",
    "sources": [
        {
            "source": "document.pdf",
            "page": 1,
            "score": 0.85
        }
    ]
}
```

---

# Evaluation

The evaluation system measures retrieval quality.

Workflow:

```
Questions Dataset
        |
        v
RAG System
        |
        v
Store Results
        |
        v
Visualization Dashboard
```

Run evaluation:

```bash
python evaluation/evaluate.py
```

Results are saved:

```
evaluation/results.json
```

Run dashboard:

```bash
streamlit run evaluation/dashboard.py
```

Dashboard shows:

- Retrieved similarity scores
- Average retrieval score
- Query performance

---

# Example

Question:

```
What is Machine Learning?
```

Retrieved:

```
Source:
rag_test_document.pdf

Page:
1

Score:
0.85
```

Generated answer:

```
Machine Learning is a branch of Artificial Intelligence
that enables computers to learn patterns from data...
```

---

# Learning Goals

This project was built to understand:

- How RAG works internally
- Why embeddings are needed
- How vector search works
- How retrieval affects LLM accuracy
- How production RAG systems are structured

---

# Future Improvements

Possible extensions:

- Multiple document upload
- Better evaluation metrics
- Hybrid search (BM25 + vectors)
- Reranking models
- Streaming responses
- Authentication
- Docker deployment
- Cloud deployment

---

# License

MIT License