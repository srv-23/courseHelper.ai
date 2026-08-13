# CourseHelper.ai

CourseHelper.ai is a Retrieval-Augmented Generation (RAG) project for answering questions from course documents, study material, and PDFs using AI. The project combines document loading, chunking, vector storage, retrieval, and LLM-based answering to provide context-aware answers based only on the uploaded content.

This repository contains both the main command-line version and a Streamlit UI version, along with experimental modules that explore different document loading and retrieval strategies.

---

## Overview

The core idea is simple:

1. Load a document or PDF
2. Split it into smaller text chunks
3. Convert chunks into embeddings
4. Store them in a vector database
5. Retrieve the most relevant chunks for a user question
6. Send the retrieved context to an LLM
7. Generate a grounded answer based only on the document content

This is a classic RAG pipeline, and the project is designed to work with educational documents and reading material.

---

## Main Project Flow

The actual working project is centered around these two entry points:

- `main.py` — terminal-based RAG application
- `UImain.py` — Streamlit user interface for PDF upload and Q&A

These are the primary application files. The other folders in the project are mostly experimental or alternative implementations used while exploring different approaches.

---

## Repository Structure

```text
courseHelper.ai/
├── main.py                          # Main CLI-based RAG assistant
├── UImain.py                       # Streamlit UI version of the app
├── create_database.py              # Database creation script for a PDF
├── pyproject.toml                  # Python project metadata and dependencies
├── requirements.txt                # Dependency list
├── README.md                       # Project documentation
├── .env                            # Local environment variables (API keys)
├── .python-version                 # Python version pin
├── .venv/                          # Local virtual environment
├── uv.lock                         # lockfile for uv
├── chroma_db/                      # Generated vector database (created after indexing)
├── document_loader/                # Experimental document loaders and test examples
│   ├── notes.txt
│   ├── page.py
│   ├── pdf.py
│   ├── test.pdf
│   └── test.py
├── retrievers/                     # Alternative retrieval strategies and experiments
│   ├── arixv.py
│   ├── mmr.py
│   └── multiquery.py
├── src/
│   └── coursehelper_ai/
│       └── __init__.py
├── vector_store/
│   └── DB.py
└── .gitignore
```

### What each area is for

- `main.py`  
  The main local project flow. It builds or loads a Chroma vector database, retrieves similar chunks using MMR, and answers questions with an LLM.

- `UImain.py`  
  A browser-based UI built with Streamlit. It lets the user upload a PDF, create a vector DB, and ask questions from the document.

- `create_database.py`  
  A direct database-building script that creates a Chroma vector store from a PDF document.

- `document_loader/`  
  Small experiments around loading documents from PDF, text files, and web pages. These are useful to test different document ingestion methods.

- `retrievers/`  
  Alternative retrieval strategies, including similarity search, MMR search, and MultiQuery retrieval. These are exploration files rather than the main app.

- `vector_store/`  
  Early database-related experiments and prototype logic.

- `src/coursehelper_ai/`  
  Packaging scaffold for the project, though the core logic is still concentrated in the root scripts.

---

## Tech Stack

This project uses:

- Python
- LangChain
- Chroma vector database
- Hugging Face embeddings
- Mistral AI
- Streamlit
- PyMuPDF / PDF loaders
- Python-dotenv

The app uses embeddings to transform document text into vectors and stores them in Chroma, which makes semantic retrieval possible.

---

## How the RAG Pipeline Works

The project follows this pattern:

```text
Document PDF / notes
        ↓
Document Loader
        ↓
Text Splitter
        ↓
Embedding Model
        ↓
Chroma Vector Store
        ↓
Retriever (MMR / similarity)
        ↓
Prompt + Context
        ↓
Mistral LLM
        ↓
Answer to user
```

### Important details

- Context is retrieved from the most relevant document chunks.
- The prompt instructs the model to answer only from the provided context.
- If the answer is not in the source material, the app explicitly says it could not find it in the document.
- The retrieval strategy uses MMR by default for better diversity in search results.

---

## Installation

### Prerequisites

- Python 3.13 (as defined in `pyproject.toml`)
- A Mistral API key

### Option 1: pip

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Option 2: uv

```bash
uv sync
```

---

## Environment Setup

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

This key is used by the LangChain Mistral integration.

> Keep your API key private and do not commit the `.env` file to source control.

---

## Running the Main App

### 1) Terminal version

Run:

```bash
python main.py
```

Then enter your question in the terminal. The app will:

- retrieve relevant chunks from the vector database
- build the prompt with the context
- generate an answer
- repeat until you type `0` to exit

### 2) Streamlit UI version

Run:

```bash
streamlit run UImain.py
```

Then:

1. Upload a PDF
2. Click “Create Vector Database”
3. Ask questions in the interface

This is the most user-friendly version for real usage.

---

## Creating the Vector Database

The project stores embeddings in a local Chroma database directory named `chroma_db`.

You can create it in two ways:

- Through the UI in `UImain.py`
- Through the script `create_database.py`

Example:

```bash
python create_database.py
```

This script builds a vector store from a PDF and saves it locally for later retrieval.

---

## Alternative and Experimental Modules

A number of folders in this repo are not the main app, but they show alternative ways the project was explored.

### `document_loader/`

Contains experiments for:

- loading text files
- loading PDFs
- testing splitting logic
- parsing pages

These files help understand how documents should be chunked and preprocessed before indexing.

### `retrievers/`

Contains experiments with different retrieval methods:

- `mmr.py` — Maximum Marginal Relevance retrieval
- `multiquery.py` — multi-query retrieval using LLM-generated reformulations
- `arixv.py` — research-paper retrieval from arXiv via ArxivRetriever

These are useful for understanding how retrieval quality changes with different search strategies.

### `vector_store/DB.py`

This file represents a prototype or early DB experimentation layer and is not the main live app flow.

---

## Notes on Project Status

This repository is more of a research and prototype project than a polished production package. The most important app files are:

- `main.py`
- `UImain.py`
- `create_database.py`

The remaining folders are useful examples of different approaches and alternatives used during development.

The package entry in `pyproject.toml` is present, but the actual app logic is still primarily contained in the root-level scripts rather than a fully structured library module.

---

## Recommended Usage

For a normal user workflow, the best route is:

1. Install dependencies
2. Add your `MISTRAL_API_KEY` to `.env`
3. Run the Streamlit app:

```bash
streamlit run UImain.py
```

4. Upload a PDF
5. Create the vector database
6. Ask questions about the document

This is the easiest and most practical way to use the project.

---

## License

This project does not currently declare a formal license in the repository metadata. Please check the repository settings or contact the maintainer if you need explicit licensing information.

---

## Summary

CourseHelper.ai is a lightweight RAG-based document assistant built for educational content and PDF-based Q&A. It shows both a terminal interface and a Streamlit UI, while also containing multiple experimental retrieval and loading approaches. The core product flow is clear: load documents, create embeddings, store them in Chroma, retrieve context, and answer accurately with a language model.

If you want a simple, working setup for local knowledge Q&A, start with `UImain.py` and the `main.py` CLI as your main entry points.
