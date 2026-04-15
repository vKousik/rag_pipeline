# 🚀 Agentic RAG Pipeline (Production-Ready)

An advanced **Agentic Retrieval-Augmented Generation (RAG)** system that enables intelligent querying over local documents using **multi-agent collaboration**, **vector search**, and **LLM-powered reasoning**.

This project transitions from a basic RAG system to a **production-ready API** with monitoring, CI/CD, and containerization.

---

## 📌 Features

* 🔍 Local document-based Q&A (PDF/Text)
* 🧠 Groq-powered LLM inference (low latency)
* 🧩 Multi-agent reasoning (CrewAI)
* ⚡ FastAPI REST API
* 📊 MLflow experiment tracking
* 🐳 Dockerized backend
* 🔁 CI/CD with GitHub Actions

---

## 🧱 Architecture Overview

```text
User Query
   ↓
FastAPI (/ask)
   ↓
CrewAI Agents
   ├── Researcher → retrieves context from ChromaDB
   ├── Writer → generates structured response
   └── Editor → validates & prevents hallucination
   ↓
Final grounded response
```

---

## 📂 Project Structure

```text
WEEK11/
│
├── agentic_rag/              # Main application (Dockerized)
│   ├── api/                  # FastAPI app
│   ├── agents/               # CrewAI agents
│   ├── crew/                 # Agent orchestration
│   ├── ingestion/            # Data loading & chunking
│   ├── services/             # RAG + logic layer
│   ├── vectorstore/          # ChromaDB storage
│   ├── mlflow_utils/         # MLflow tracking
│   ├── schemas/              # Pydantic models
│   ├── tools/                # Custom tools
│   ├── data/                 # Input documents
│   ├── mlruns/               # MLflow logs
│   ├── Dockerfile            # Docker config (IMPORTANT)
│   ├── .dockerignore         # Ignore heavy files
│   ├── requirements.txt
│   └── main.py               # CLI (optional)
│
├── RAG/                      # Basic RAG pipeline (Task 1)
├── .github/workflows/        # CI/CD pipeline
├── .env
└── .gitignore
```

---

## 🧠 Task 1: Knowledge Base (RAG)

* Loads PDF/Text files from `agentic_rag/data/`
* Splits documents:

  * Chunk size: **500**
  * Overlap: **50**
* Uses embedding model (sentence-transformers)
* Stores vectors in **ChromaDB**
* Retrieval ensures:

  * ❌ No hallucination
  * ✅ Only answers from documents

---

## 🤖 Task 2: Agentic Intelligence

Implemented using **CrewAI multi-agent system**:

### 👨‍🔬 Researcher Agent

* Retrieves relevant chunks from vector DB

### ✍️ Writer Agent

* Converts facts into structured response

### 🧪 Editor Agent

* Validates:

  * No hallucination
  * Only retrieved context used
* If insufficient data:

  ```text
  "I don't know based on the provided documents."
  ```

---

## ⚡ Task 3: API & Monitoring

### 🔹 FastAPI Endpoint

```http
POST /ask
```

### Request

```json
{
  "query": "What is data science?"
}
```

### Response

```json
{
  "answer": "..."
}
```

---

### 📊 MLflow Monitoring

Tracks:

* Latency
* Prompts
* Model behavior

Run UI:

```bash
mlflow ui
```

---

## 🐳 Docker Setup (IMPORTANT)

### 📍 Build Image (inside agentic_rag)

```bash
docker build -t agentic-rag:0.0.1 .
```

---

### ▶️ Run Container

```bash
docker run -p 8000:8000 \
-e GROQ_API_KEY=your_key \
agentic-rag
```

---

## 🔁 CI/CD (GitHub Actions)

Workflow file:

```text
.github/workflows/docker-build.yml
```

### What it does:

* Runs on every push to `main`
* Builds Docker image from:

```bash
./agentic_rag
```

---

## 🔐 Environment Variables

Create `.env`: 

```env
GROQ_API_KEY=your_api_key
```

---

## 🚀 Run Locally (Without Docker)

```bash
cd agentic_rag
pip install -r requirements.txt
uvicorn api.main:app --reload
```

---

## 🧪 Run Ingestion

```bash
python main.py
```

---

## ⚠️ Important Notes

* Uses **Groq API (NOT Ollama)**
* `.dockerignore` excludes:

  * `mlruns/`
  * `vectorstore/`
  * `data/`
* These should be mounted or generated at runtime

---

## 🎯 Key Highlights

* ✅ Modular architecture
* ✅ Multi-agent validation system
* ✅ No hallucination guarantee
* ✅ Production-ready API
* ✅ CI/CD integrated


## 👨‍💻 Author

Kousik Mondal
GitHub: https://github.com/vKousik