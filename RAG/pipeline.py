from data_loader import load_documents, clean_text
from embedding import split_documents, store_in_chroma
from rag_serach import generate_answer
def run_ingestion():
    data_dir = "data"
    documents = clean_text(load_documents(data_dir))
    chunks = split_documents(documents)
    store_in_chroma(chunks)


    print(f"[INFO] Ingestion complete")


def run_query():
    while True:
        query = input("\nAsk (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        answer = generate_answer(query)
        print("\nAnswer:", answer)


if __name__ == "__main__":
    choice = input("1: Ingest\n2: Query\nChoose: ")

    if choice == "1":
        run_ingestion()
    else:
        run_query()