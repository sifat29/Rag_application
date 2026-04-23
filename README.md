# 📚 RAG Application with Groq + FAISS

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows users to load custom documents and ask questions based on their content. The system retrieves relevant context using vector search and generates accurate answers using a Large Language Model (LLM). I have only loaded the PDF files, but any kind of file excel or word or text file can be given as well.

---

## 🚀 Features

- 🔍 Load and process custom documents
- ✂️ Smart text chunking
- 🧠 Embeddings using `all-MiniLM-L6-v2`
- 📦 Vector database using FAISS
- ⚡ Fast inference using Groq LLM (`llama-3.1-8b-instant`)
- 💬 Ask questions directly from command line (no code editing required)
- 🔗 End-to-end modular RAG pipeline

---

## 🧠 Models Used

| Component      | Model                   |
|----------------|------------------------|
| Embeddings     | all-MiniLM-L6-v2       |
| LLM            | llama-3.1-8b-instant   |
| Vector Store   | FAISS                  |

---

## 📂 Project Structure
RAG_project/
│
├── src/
│ ├── data_loader.py # Load documents
│ ├── vectorstore.py # FAISS vector DB
│ ├── search.py # RAG pipeline logic
│
├── data/ # Input documents
├── faiss_store/ # Saved FAISS index
├── app.py # Main script
├── requirements.txt
└── README.md


## 📸 Example Output
![image alt](https://github.com/sifat29/Rag_application/blob/c750c057c70ab1621cfb16adfcef68d52e9137bb/Rag_application_git/assets/output.png)

-------------------------------------------------------------------------------------------------------------
📚 Inspiration

This project was inspired by:
https://github.com/krishnaik06/RAG-Tutorials

Enhancements include:

Updated models and dependencies
Improved usability
Optimized pipeline design

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Create virtual environment (recommended)
pip install -r requirements.txt

🔑 Setup API Key

This project uses Groq API.
Set your API key as an environment variable:
set GROQ_API_KEY=your_api_key_here   # Windows

Run with a query from command line:
python main.py What is YOLOv5?

⚠️ Notes
First run may take longer due to embedding generation
Ensure faiss_store is created before querying
Do NOT expose your API key publicly

📌 Future Improvements
Add Streamlit UI
Add conversational memory
Implement hybrid search (BM25 + embeddings)
Add source citations in responses

🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.
