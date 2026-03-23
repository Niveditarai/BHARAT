from fastapi import FastAPI
from rag import create_rag_chain

app = FastAPI()

qa_chain = None

# Safe initialization
try:
    qa_chain = create_rag_chain()
except Exception as e:
    print("Error initializing RAG:", e)


@app.get("/")
def home():
    return {"message": "Bharat AI running 🚀"}


@app.get("/ask")
def ask(question: str):
    if qa_chain is None:
        return {"error": "AI system not initialized. Check API key."}

    try:
        result = qa_chain(question)
        return {
            "answer": result["result"],
            "sources": [doc.page_content for doc in result["source_documents"]]
        }
    except Exception as e:
        return {"error": str(e)}