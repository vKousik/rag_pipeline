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
* 🧪 Includes **both Basic RAG and Agentic RAG pipelines**

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
├── agentic_rag/              # Production Agentic RAG (Dockerized)
│   ├── api/
│   ├── agents/
│   ├── crew/
│   ├── ingestion/
│   ├── services/
│   ├── vectorstore/
│   ├── mlflow_utils/
│   ├── schemas/
│   ├── tools/
│   ├── data/
│   ├── mlruns/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   └── main.py
│
├── RAG/                      # Basic RAG (Task 1)
│   ├── pipeline.py
│   ├── embedding.py
│   ├── data_loader.py
│   ├── rag_search.py
│   ├── data/
│   └── vectorstore/
│
├── .github/workflows/
├── .env
└── .gitignore
```

---

## 🧠 Task 1: Basic RAG Pipeline

Located in: `RAG/`

### 🔹 What it does

* Loads documents from `RAG/data/`
* Splits into chunks:

  * Chunk size: **500**
  * Overlap: **50**
* Generates embeddings using open-source models
* Stores vectors in **ChromaDB**
* Retrieves relevant context and answers queries

---

### ▶️ Run Basic RAG

```bash
cd RAG
python pipeline.py
```

---

### ⚙️ Flow

```text
Load Documents → Clean Text → Split → Embed → Store → Retrieve → Answer
```

---

### ⚠️ Limitation

* Single-step retrieval
* No validation layer
* May hallucinate if context is weak

---

## 🤖 Task 2: Agentic RAG (Advanced)

Located in: `agentic_rag/`

### 🔹 Improvements over Basic RAG

| Feature               | Basic RAG | Agentic RAG |
| --------------------- | --------- | ----------- |
| Retrieval             | ✅         | ✅           |
| Multi-agent reasoning | ❌         | ✅           |
| Hallucination control | ❌         | ✅           |
| Confidence validation | ❌         | ✅           |
| Structured output     | ❌         | ✅           |

---

### 🧠 Multi-Agent System (CrewAI)

#### 👨‍🔬 Researcher

* Fetches relevant chunks from vector DB

#### ✍️ Writer

* Generates structured answer

#### 🧪 Editor

* Validates:

  * No hallucination
  * Only retrieved facts used
* Returns fallback:

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
  "query": "What is AI?"
}
```

### Response

```json
{
  "query": "...",
  "answer": "...",
  "latency": 3.41,
  "model_used": "groq/llama-3.3-70b-versatile"
}
```

---

### 📊 MLflow Monitoring

Tracks:

* Latency
* Prompts
* Model usage

Run:

```bash
mlflow ui
```

---

## 🐳 Docker Setup

### 📍 Build (inside agentic_rag)

```bash
cd agentic_rag
docker build -t agentic-rag:0.0.1 .
```

---

### ▶️ Run

```bash
docker run -d -p 8000:8000 \
-e GROQ_API_KEY=your_api_key \
--name agentic-rag-container \
agentic-rag:0.0.1
```

---

## 🔁 CI/CD (GitHub Actions)

Workflow:

```text
.github/workflows/docker-build.yml
```

### ✔ On every push:

* Builds Docker image from `agentic_rag/`
* Verifies build success

---

## 🔐 Environment Variables

```env
GROQ_API_KEY=your_api_key
```

---

## 🚀 Run Locally

```bash
cd agentic_rag
pip install -r requirements.txt
uvicorn api.main:app --reload
```

---

## 🧪 Ingestion (Agentic Pipeline inside agentic_rag)

```bash
python main.py (choose ingestion in cli)
```

---

## ⚠️ Notes

* Uses **Groq API (instead of Ollama)**
* `.dockerignore` excludes:

  * `mlruns/`
  * `vectorstore/`
  * `data/`
* These are generated at runtime

---

## 🎯 Key Highlights

* ✅ Dual pipeline (Basic + Agentic)
* ✅ Multi-agent validation system
* ✅ No hallucination guarantee
* ✅ Production-ready API
* ✅ CI/CD integrated
* ✅ Monitoring with MLflow

---

## 👨‍💻 Author

Kousik Mondal
GitHub: https://github.com/vKousik

