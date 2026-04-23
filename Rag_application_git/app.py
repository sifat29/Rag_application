from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
import sys

if __name__ == "__main__":
    
    # Get query from command line
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("Enter your question: ")

    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)
    store.load()

    rag_search = RAGSearch()
    summary = rag_search.search_and_summarize(query, top_k=3)

    print("Summary:", summary)