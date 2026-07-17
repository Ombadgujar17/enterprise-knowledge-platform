# Enterprise Knowledge Platform

A lightweight retrieval-augmented knowledge platform (RAG) for enterprise document search, question answering, and agent orchestration. This repository provides a minimal, extensible foundation for ingesting documents, creating embeddings, storing vectors, and building graph-aware retrieval workflows for downstream conversational agents and tools.

Why this project

- Enables fast prototyping of RAG applications for internal knowledge, policies, and documentation.
- Combines vector search with a graph layer to represent relationships between documents and entities.
- Designed to be adaptable to different embedding providers, vector stores, and LLM backends.

Key features

- Document ingestion and chunking utilities
- Configurable embedding and vector-store adapters
- Retriever and RAG orchestration layer
- Graph builder and node models to capture relationships
- FastAPI-based HTTP API with interactive docs
- Modular services and agents for chat, classification, and tool orchestration

Repository layout

- app/api: FastAPI application, routers, and API models
- app/rag: Chunking, embedding, retriever and vector store utilities
- app/graph: Graph builder, state management, and node models
- app/services: Business logic (chat/document orchestration)
- app/agents: Higher-level agent patterns (intent classification, response generation)
- app/models: Pydantic schemas for requests/responses and documents
- data/: Raw inputs, processed artifacts, and vector store files

Quickstart (development)

Prerequisites

- Python 3.12+
- Git
- (Optional) an embeddings provider and vector store for production use

Create a virtual environment and install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

Configure environment

- Copy the example environment file (if present) or set required environment variables for your embedding provider, LLM endpoint, and vector store connection.
- Common variables:
  - EMBEDDING_PROVIDER_URL / EMBEDDING_API_KEY
  - VECTOR_STORE_PATH or VECTOR_STORE_URL
  - OPENAI_API_KEY or other LLM credentials

Run the app (development)

```bash
uvicorn app.api.app:app --reload
```

Open the interactive API docs at http://localhost:8000/docs

Notes on architecture

- The `app/rag` layer handles document chunking, embedding calls, and abstract vector-store operations so you can swap providers with minimal changes.
- `app/graph` builds a lightweight graph of nodes and edges that can be used to contextualize retrieval results and support follow-up Q&A.
- `app/services` contains the orchestration logic that ties together retrieval, prompt construction, and agent execution.

Implementation status

- Several modules are scaffolds/stubs and require project-specific integration (for example: `app/services/chat_service.py`, `app/rag/retriever.py`). Treat this repository as a starting point — plug in your chosen embedding provider, vector store, and LLM backend.

Testing

Run tests with:

```bash
pytest -q
```

Contributing

Contributions, issue reports, and PRs are welcome. When contributing:

- Open an issue to discuss larger changes before writing code
- Follow the existing code style and add tests for new behavior
- Keep changes small and focused

License

Specify a license in the repository (e.g., MIT) — this project currently does not include a license file.

Contact

Open issues or PRs on GitHub for questions, feature requests, or assistance.
