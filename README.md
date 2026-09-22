# LangChain RAG — EduAI Thesis Q&A

A document-based Retrieval-Augmented Generation (RAG) system built with LangChain.

This project rebuilds a RAG pipeline that was previously implemented from scratch, using LangChain abstractions for document loading, text splitting, embeddings, vector storage, retrieval, prompting, and LLM interaction.

The system uses an academic thesis as its knowledge source and allows users to ask questions about the document through an interactive terminal interface.

## Architecture

```text
PDF Document
     ↓
PyPDFLoader
     ↓
RecursiveCharacterTextSplitter
     ↓
HuggingFace Embeddings
     ↓
Chroma Vector Store
     ↓
LangChain Retriever
     ↓
Top 10 Candidates
     ↓
Cross-Encoder Reranking
     ↓
Top 5 Documents
     ↓
Prompt Template
     ↓
Ollama LLM
     ↓
Answer

Features
PDF document loading
Recursive text splitting
Local HuggingFace embeddings
Chroma vector database
Semantic similarity retrieval
Top-k retrieval
Cross-Encoder reranking
Prompt templates
Local Ollama LLM
Interactive terminal question answering
LangChain LCEL chain composition
Tech Stack
Python 3.12
LangChain
LangChain Community
LangChain Chroma
LangChain HuggingFace
LangChain Text Splitters
PyPDF
Sentence Transformers
ChromaDB
Ollama
Project Structure:

RAG_LangChain/
│
├── data/
│   └── thesis.pdf
│
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── reranker.py
│   ├── prompt.py
│   ├── generator.py
│   └── chain.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md

The PDF inside data/ is excluded from Git through .gitignore.

Setup
1. Clone the repository
git clone <repository-url>
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama

Install Ollama separately and make sure a compatible local chat model is available.

The current development environment uses a custom local Ollama model:

eduai-finetuned:latest

This model is not included in the repository.

If using another Ollama model, update:

src/generator.py

and change the model name accordingly.

6. Add a document

Place a PDF document at:

data/thesis.pdf

The application expects this filename by default.

Run
python main.py

The application will start an interactive terminal session:

EduAI RAG Assistant
Ask questions about the thesis.
Type 'exit' or 'quit' to quit.

Ask a question:

Enter questions about the document.

Type exit or quit to stop the application.

Retrieval Pipeline

The application retrieves the top 10 candidate documents from Chroma.

A Cross-Encoder then evaluates the relevance of the query against those candidates and selects the top 5 documents.

The selected documents are combined into the context supplied to the language model.

This provides a two-stage retrieval process:

Semantic Retrieval
       ↓
    Top 10
       ↓
Cross-Encoder
    Reranking
       ↓
     Top 5
LangChain Abstractions

The project intentionally keeps the individual stages visible to demonstrate what LangChain abstracts.

Document Loading

PyPDFLoader replaces manually handling PDF extraction.

Text Splitting

RecursiveCharacterTextSplitter handles chunk creation and overlap.

Embeddings

HuggingFaceEmbeddings provides a standardized LangChain interface around the embedding model.

Vector Store

Chroma provides the vector database integration.

Retriever

The Chroma vector store is exposed through LangChain's retriever interface:

retriever.invoke(question)
Prompt

ChatPromptTemplate handles structured prompt construction.

LLM

ChatOllama provides a standardized interface for interacting with the local Ollama model.

LCEL

The prompt and model are composed using LangChain's expression language:

prompt | llm
Custom Component

The Cross-Encoder reranker remains a custom component because LangChain is not responsible for the specific reranking strategy used in this project.

Learning Purpose

This project was created to learn LangChain by rebuilding an existing RAG system.

The original RAG implementation was built from scratch using Python, Sentence Transformers, ChromaDB, Cross-Encoder reranking, and Ollama.

This version uses LangChain abstractions where appropriate while keeping the underlying RAG architecture understandable and visible.

The goal is not to hide the implementation behind a framework, but to understand what the framework simplifies.

Limitations
The document must currently be provided as a PDF.
The PDF must be placed at data/thesis.pdf.
The application uses a local Ollama model.
The current vector store is created when the application starts.
Retrieval quality depends on the chunks returned by the vector search and reranker.
The application does not maintain conversational memory between questions.

---

# 4. Check the project files

Run this **one command**:

```powershell
Get-ChildItem -Recurse -File | Select-Object FullName

You should see the important files roughly like:

.gitignore
README.md
main.py
requirements.txt

src\chain.py
src\chunker.py
src\embeddings.py
src\generator.py
src\loader.py
src\prompt.py
src\reranker.py
src\vectorstore.py

You may also see Python cache files. That's fine; .gitignore will prevent them from being committed.