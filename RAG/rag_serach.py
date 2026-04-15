import os
from groq import Groq
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
# Initialize embedding (same as ingestion)
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load Chroma DB
vectordb = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding
)

# Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
    )

def build_prompt(context: str, query: str) -> str:
    return f"""You are a strict document-based assistant. 
You must answer ONLY using the context provided below.

Rules:
- If the answer is not in the context, say "I don't know based on the provided documents."
- Do NOT use any external knowledge or make assumptions.
- Do NOT hallucinate or guess.
- Be concise and precise.
- Explain the full source of the information and don't miss any information.

Context:
---------
{context}
---------

Question: {query}

Answer:"""

def retrieve_docs(query: str, top_k: int = 3, threshold: float = 1.0) :
    results = vectordb.similarity_search_with_score(query, k=top_k)

    if not results:
        return []

    filtered = []
    for doc, score in results:
        print(f"[DEBUG] Score: {score:.4f}")
        if score < threshold:
            filtered.append(doc.page_content)

    print(f"[DEBUG] Docs after filtering: {len(filtered)}/{len(results)}")
    return filtered

def generate_answer(
    query: str,
    top_k: int = 3,
    threshold: float = 1.0,
    temperature: float = 0.2,
) -> dict:
    print(f"[INFO] Query: {query}")

    docs = retrieve_docs(query, top_k=top_k, threshold=threshold)
    if not docs:
        return "No relevant information found in the provided documents."

    context = "\n\n".join(docs)
    prompt = build_prompt(context, query)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        answer = response.choices[0].message.content

    except Exception as e:
        print(f"[ERROR] LLM call failed: {e}")
        return "Failed to generate a response. Please try again."

    return answer

