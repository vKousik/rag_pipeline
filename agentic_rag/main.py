from crew.crew_setup import run_crew
from ingestion.embedding import split_documents, store_in_chroma
from ingestion.data_loader import load_documents, clean_text

def run_ingestion():
    data_dir = "data"
    documents = clean_text(load_documents(data_dir))
    chunks = split_documents(documents)
    store_in_chroma(chunks)

    print(f"[INFO] Ingestion complete")

def run_query():
    print("\n[INFO] Enter your queries (type 'exit' to go back)\n")

    while True:
        query = input("Query or 'exit': ")

        if query.lower() == "exit":
            print("[INFO] Returning to main menu...")
            break

        print("\nAnswer:", run_crew(query))
    

def main():
    while True:
        print("\n1: Ingest")
        print("2: Query")
        print("3: Exit")

        choice = input("Choose: ")

        if choice == "1":
            run_ingestion()

        elif choice == "2":
            run_query()

        elif choice == "3":
            print("[INFO] Exiting program...")
            break

        else:
            print("[ERROR] Invalid choice")


if __name__ == "__main__":
    main()