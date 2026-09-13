from fastapi import FastAPI
from pydantic import BaseModel

from src.rag import RAG


app = FastAPI()


rag = RAG()


class Question(BaseModel):
    question: str



@app.get("/")
def home():

    return {
        "status": "RAG API running"
    }



@app.post("/ask")
def ask(data: Question):

    try:

        return rag.ask(
            data.question
        )

    except Exception as e:

        return {
            "error": str(e)
        }