# 🚀 Bharat AI – Multilingual RAG-Based Assistant

An AI-powered assistant built using **Retrieval Augmented Generation (RAG)** that provides accurate, context-aware answers based on custom knowledge sources.

---

## 🌟 Features

✨ Intelligent Question Answering using LLM
🌍 Multilingual-ready (Hindi + English support)
📚 RAG Pipeline for accurate and grounded responses
⚡ FastAPI backend for real-time interaction
🧠 Vector Database (Chroma) for semantic search
🎤 Voice input with fallback to text (robust design)
🔍 Source-based answers (Explainable AI)

---

## 🧠 How It Works

```text
User Query → FastAPI → RAG Pipeline → Vector DB → LLM → Response
```

1. User asks a question
2. System retrieves relevant data from vector database
3. LLM generates a context-aware answer
4. Response is returned with sources

---

## 🏗️ Tech Stack

### 🔹 Backend

* Python
* FastAPI
* Uvicorn

### 🔹 AI / ML

* LangChain
* OpenAI GPT Models
* Embeddings

### 🔹 Database

* Chroma (Vector Database)

### 🔹 Additional Tools

* SpeechRecognition (Voice Input)
* Pyttsx3 (Text-to-Speech)
* LangDetect (Language Detection)

---

## 📂 Project Structure

```
bharat-ai/
│── main.py          # FastAPI backend
│── rag.py           # RAG pipeline logic
│── test_voice.py    # Voice input module
│── data.txt         # Knowledge base
│── venv/            # Virtual environment (ignored)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/bharat-ai.git
cd bharat-ai
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set API Key

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

Restart terminal after this.

---

## ▶️ Run the Project

```bash
python -m uvicorn main:app --reload
```

---

## 🌐 API Endpoints

### 🔹 Health Check

```
GET /
```

### 🔹 Ask Question

```
GET /ask?question=Your Question Here
```

---

## 💡 Example

```
http://127.0.0.1:8000/ask?question=PM Awas Yojana kya hai
```

---

## 🎯 Key Highlights

✔ Reduced hallucination using RAG
✔ Context-aware AI responses
✔ Scalable backend architecture
✔ Fault-tolerant design (voice fallback system)

---

## 🚀 Future Enhancements

* 🎤 Full voice assistant support
* 🌍 Advanced multilingual responses
* 💻 Frontend UI (React-based)
* 📱 Mobile app integration
* ☁️ Cloud deployment

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

## 📌 Author

👩‍💻 Nivi
AI/ML Enthusiast | Developer

---

## ⭐ If you like this project, give it a star!
