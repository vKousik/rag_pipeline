import os
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader

def load_documents(data_dir : str) -> List[Any]:
    documents = []
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)

        if file.endswith(".pdf"):
            print(f"[DEBUG] Loading PDF: {file}")
            try:
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())
            except Exception as e:
                print(f"[ERROR] Failed to load PDF: {file}, exception: {e}")
    print(f"[DEBUG] Total loaded documents: {len(documents)}")
    return documents
def clean_text(documents):
    for doc in documents:
        text = doc.page_content
        text = text.replace("\n", " ")
        text = " ".join(text.split())

        doc.page_content = text
    print(f"[DEBUG] Total cleaned documents: {len(documents)}")
    return documents