from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from ingestion.data_loader import clean_text, load_documents

embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print(f"[INFO] Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks

def embed_query(query: str):
    return embedding.embed_query(query)

def store_in_chroma(chunks, CHROMA_PATH="vectorstore"):
    print(f"[INFO] Generating embeddings for {len(chunks)} chunks...")

    vectordb = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding
    )

    vectordb.add_documents(chunks)

    print("[INFO] Stored in ChromaDB")

if __name__ == "__main__":
    data_dir = "data"
    documents = clean_text(load_documents(data_dir))
    chunks = split_documents(documents)
    store_in_chroma(chunks)