# 🚀 Enterprise Knowledge Platform

> An AI-powered Enterprise Knowledge Assistant built with **LangGraph**, **LangChain**, **FastAPI**, **ChromaDB**, and **Groq LLM** that enables intelligent document retrieval, agentic workflows, and real-world tool execution.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-orange)
![LangChain](https://img.shields.io/badge/LangChain-RAG-blueviolet)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

Enterprise Knowledge Platform is a production-oriented AI assistant designed to help organizations interact with internal knowledge bases using Retrieval-Augmented Generation (RAG) and Agentic AI workflows.

Instead of performing simple semantic search, the platform intelligently:

- Understands user intent
- Retrieves relevant enterprise documents
- Generates grounded responses
- Executes real-world actions through tools
- Integrates with external services such as Gmail

The architecture follows modern software engineering principles including clean architecture, modular services, reusable AI components, and separation of concerns.

---

# ✨ Features

## 🤖 Agentic AI Workflow

- LangGraph-powered multi-node workflow
- Intent classification
- Dynamic routing
- Tool execution
- Retrieval-Augmented Generation (RAG)

---

## 📚 Retrieval-Augmented Generation (RAG)

- PDF document ingestion
- Intelligent chunking
- Embedding generation
- ChromaDB vector storage
- Semantic similarity search
- Context-aware answer generation

---

## 🧠 LLM Integration

- Groq LLM
- LangChain abstraction
- Provider-independent architecture
- Structured Output using Pydantic
- Prompt engineering

---

## 🛠 AI Tools

### 📧 Intelligent Email Assistant

Supports natural language email requests such as:

> Send an email to john@example.com informing him that the deployment has completed successfully.

The agent automatically:

- extracts recipient
- generates subject
- generates email body
- validates data using Pydantic
- sends the email through the Gmail API

---

## 🌐 REST API

FastAPI backend exposing endpoints for:

- Chat
- Document Upload
- Retrieval
- Tool Execution
- Health Monitoring

---

## 🖥 Frontend

Streamlit interface including:

- Chat interface
- PDF upload
- Document management
- Backend status monitoring

---

# 🏗 Architecture

```
                        User
                          │
                          ▼
                  Streamlit Frontend
                          │
                          ▼
                     FastAPI Backend
                          │
                          ▼
                     LangGraph Agent
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
 Intent Classifier   General Chat      Tool Execution
        │                                  │
        ▼                                  ▼
      RAG Pipeline                     Email Tool
        │                                  │
        ▼                                  ▼
     ChromaDB                        Gmail API
```

---

# 🧠 Agent Workflow

```
User Query
     │
     ▼
Intent Classification
     │
     ├───────────────┐
     ▼               ▼
Knowledge Query   Tool Request
     │               │
     ▼               ▼
Retrieve Docs    Email Tool
     │               │
     ▼               ▼
Build Context   Gmail Service
     │               │
     ▼               ▼
Generate Answer Gmail API
```

---

# 📂 Project Structure

```
app/
│
├── api/
├── config/
├── graph/
├── integrations/
├── models/
├── rag/
├── services/
├── tools/
├── utils/
│
frontend/
│
tests/
│
docker/
```

---

# ⚙ Tech Stack

## Backend

- Python 3.12
- FastAPI
- LangChain
- LangGraph

## AI

- Groq LLM
- ChromaDB
- HuggingFace Embeddings

## Frontend

- Streamlit

## Development

- Docker
- uv
- Ruff
- MyPy
- Pytest

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Ombadgujar17/enterprise-knowledge-platform.git
cd enterprise-knowledge-platform
```

---

## Install Dependencies

```bash
uv sync
```

---

## Configure Environment

Create a `.env`

```env
GROQ_API_KEY=your_key

LLM_MODEL=llama-3.3-70b-versatile
```

---

## Start Backend

```bash
uv run uvicorn app.api.app:app --reload
```

---

## Start Frontend

```bash
streamlit run frontend/app.py
```

---

# 📸 Screenshots

> Add screenshots of:

- Chat Interface
- Document Upload
- RAG Responses
- Email Tool
- LangGraph Workflow

---

# 🧪 Testing

Run all tests

```bash
pytest
```

---

# 🔮 Future Enhancements

- Microsoft Outlook Integration
- Google Calendar Integration
- GitHub Issue Creation
- HRMS Integration
- Jira Integration
- Slack Notifications
- Microsoft Teams
- Authentication & RBAC
- PostgreSQL Persistence
- LangSmith Observability
- CI/CD Pipeline
- Kubernetes Deployment

---

# 📚 Key Concepts Demonstrated

- Agentic AI
- Retrieval-Augmented Generation
- LangGraph
- LangChain
- Tool Calling
- Structured Output
- Vector Databases
- Embeddings
- FastAPI
- OAuth2
- Gmail API
- Software Architecture
- Clean Code
- Modular Design

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Om Badgujar**

Aspiring AI Engineer passionate about building production-ready AI systems using Agentic AI, RAG, LLMs, and modern software engineering practices.

- GitHub: https://github.com/Ombadgujar17
- LinkedIn: *Add your LinkedIn profile here*
