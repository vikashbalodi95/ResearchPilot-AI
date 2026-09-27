# 🔬 ResearchPilot AI

> An AI-powered research assistant that helps users understand and query information from research documents using Retrieval-Augmented Generation (RAG).

ResearchPilot AI is a full-stack GenAI application designed to simplify document-based research. Users can upload research documents, ask questions in natural language, and receive AI-generated answers based on relevant information retrieved from those documents.

---

## 🚀 Project Overview

ResearchPilot AI combines:

- Document processing
- PDF text extraction
- Text chunking
- Embeddings
- Vector database search
- Retrieval-Augmented Generation (RAG)
- LLM-powered answer generation
- Multi-step research workflows
- AI tools and tool selection
- Conversation context
- FastAPI backend
- Interactive frontend

The application is designed around a modular architecture where the frontend communicates with the FastAPI backend, while the backend manages document processing, retrieval, AI workflows, and LLM interactions.

---

## ✨ Features

### 📄 Document Upload
- Upload research documents through the web interface.
- Extract text from PDF documents.
- Process documents for semantic search.

### 🔎 Semantic Search
- Convert document content into embeddings.
- Store embeddings in ChromaDB.
- Retrieve relevant document chunks using similarity search.

### 🤖 RAG-Based Question Answering
- Ask natural-language questions about uploaded documents.
- Retrieve relevant context before generating an answer.
- Generate responses using an LLM.

### 🧠 AI Research Agent
The `ResearchAgent` coordinates the research workflow:

```text
User Question
      ↓
Question Analysis
      ↓
Information Retrieval
      ↓
Retrieved Information Analysis
      ↓
Final Answer Generation

## 🏗️ Architecture

