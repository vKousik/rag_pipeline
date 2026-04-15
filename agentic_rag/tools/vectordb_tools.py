from crewai.tools import tool
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding
)

@tool("Vector DB Search Tool")
def search_vector_db(query: str):
    """Search the vector database and return relevant context."""
    k = 3
    threshold = 1.0
    results = vectordb.similarity_search_with_score(query, k=k)

    context = []

    for doc, score in results:
        print(f"[DEBUG] Score: {score:.4f}")

        if score < threshold:
            context.append(doc.page_content.strip())

    if not context:
        return "NO_RELEVANT_CONTEXT"

    return "\n---\n".join(context)

