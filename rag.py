from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
import os


def create_rag_chain():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("⚠️ WARNING: API key missing")
        return None   # crash nahi karega

    loader = TextLoader("data.txt", encoding="utf-8")
    documents = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory="db"
    )

    retriever = db.as_retriever()

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=api_key
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain