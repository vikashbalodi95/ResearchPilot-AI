# 🔬 ResearchPilot AI

**An AI-powered research assistant that uses Retrieval-Augmented Generation (RAG) to answer questions from research documents.**

ResearchPilot AI is a GenAI application designed to process research documents, retrieve relevant information through semantic search, and generate context-aware responses using Large Language Models (LLMs).

## 🎯 Problem Statement

Research papers and technical documents contain large amounts of information. Finding relevant information manually can be time-consuming.

ResearchPilot AI aims to simplify this process by combining document processing, vector search, and LLM-based response generation.

## ✨ Key Features

- **PDF Text Extraction:** Extract text from PDF research documents.
- **Document Processing:** Process extracted content into smaller text chunks.
- **Text Embeddings:** Convert text into numerical vector representations.
- **Semantic Search:** Retrieve relevant document chunks using similarity search.
- **Vector Storage:** Store embeddings using ChromaDB.
- **RAG Pipeline:** Generate responses using retrieved document context.
- **Research Agent:** Coordinate multi-step research operations.
- **Tool Architecture:** Separate document processing and retrieval operations.
- **LLM Integration:** Generate responses using the Groq API.

## 🏗️ System Architecture

```text
              User Question
                   |
                   v
             Research Agent
                   |
                   v
              Tool Selector
              /           \
             v             v
       Retrieval Tool   Document Tool
             |             |
             v             v
      Embedding Service  PDF Service
             |
             v
          ChromaDB
             |
             v
      Relevant Context
             |
             v
       Research Analysis
             |
             v
          Groq LLM
             |
             v
        Final Response
```

## 🔄 RAG Pipeline

```text
Research PDF
     |
     v
Text Extraction
     |
     v
Text Chunking
     |
     v
Embedding Generation
     |
     v
ChromaDB Storage
     |
     v
User Query
     |
     v
Semantic Similarity Search
     |
     v
Relevant Document Chunks
     |
     v
LLM Response Generation
     |
     v
Grounded Answer
```

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Backend | FastAPI, Pydantic |
| LLM Integration | Groq API |
| AI Architecture | Retrieval-Augmented Generation |
| Vector Database | ChromaDB |
| Document Processing | PyPDF |
| Embeddings | Text Embeddings |
| Development | Git, GitHub, VS Code |

## 📁 Project Structure

```text
ResearchPilot-AI/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   └── research_agent.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── logger.py
│   │   │   └── prompts.py
│   │   │
│   │   ├── services/
│   │   │   ├── embedding_service.py
│   │   │   ├── vector_store_service.py
│   │   │   ├── groq_service.py
│   │   │   └── pdf_service.py
│   │   │
│   │   └── tools/
│   │       ├── retrieval_tool.py
│   │       ├── document_tool.py
│   │       └── tool_selector.py
│   │
│   ├── test_retrieval.py
│   ├── test_document_tool.py
│   └── test_research_agent.py
│
├── frontend/
│
├── .gitignore
├── README.md
├── requirements.txt
└── package-lock.json
```

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10+
- Node.js and npm (for frontend development)
- Git
- Groq API key

### 1. Clone the repository

```bash
git clone https://github.com/vikashbalodi95/ResearchPilot-AI.git

cd ResearchPilot-AI
```

### 2. Create a Python virtual environment

```powershell
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install backend dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the backend directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your actual API keys or `.env` file to GitHub.

### 5. Start the backend

Navigate to the backend directory:

```powershell
cd backend
```

Start FastAPI:

```powershell
uvicorn app.main:app --reload
```

### 6. Access API documentation

Once the backend server is running, open:

```text
http://127.0.0.1:8000/docs
```

## 🧪 Testing

The backend includes focused tests for individual components and research workflows.

Run the tests from the backend directory:

```powershell
python test_retrieval.py

python test_document_tool.py

python test_research_agent.py
```

## 🚧 Development Status

### Implemented

- FastAPI backend foundation
- PDF text extraction
- Document processing and chunking
- Text embedding generation
- ChromaDB integration
- Semantic similarity search
- RAG workflow
- Research Agent
- Retrieval Tool
- Document Tool
- Basic tool selection
- Groq LLM integration

### Remaining Development

- Conversation memory
- Follow-up question handling
- Frontend PDF upload
- Chat interface integration
- Frontend–backend integration
- Error and edge-case handling
- Production hardening
- Application deployment

## 🔮 Future Improvements

- Improved conversational context management
- Better document retrieval and ranking
- Research answer evaluation
- Improved user experience
- Production deployment

## 👨‍💻 Author

**Vikash Balodi**

B.Tech – Computer Science and Engineering

- GitHub: [vikashbalodi95](https://github.com/vikashbalodi95)
- LinkedIn: [Vikash Balodi](https://www.linkedin.com/in/vikash-balodi-17824b398)

---

*ResearchPilot AI — Making research document exploration more efficient through Generative AI and Retrieval-Augmented Generation.*
