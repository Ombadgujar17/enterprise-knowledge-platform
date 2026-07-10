
# Enterprise Knowledge Platform

Lightweight retrieval-augmented knowledge platform for enterprise document search, question answering, and agent orchestration.

## Overview

- Purpose: Ingest, index, and query enterprise documents using embeddings, vector stores, and a graph layer to support retrieval-augmented generation (RAG) workflows.
- Core components:
	- `app/api`: FastAPI application and routers
	- `app/rag`: Retriever, vector store, and chunking/embeddings utilities
	- `app/graph`: Graph builder, state, and node models
	- `app/services`: Business logic (chat/document/tool orchestration)
	- `app/agents`: Higher-level agent implementations (intent classification, response generation)
	- `app/models`: Request/response and document schemas
	- `data/`: Raw, processed, and vector store data

## Quickstart

1. Create and activate a Python 3.12+ virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

2. Run the FastAPI app (development):

```bash
uvicorn app.api.app:app --reload
```

3. Open the API docs at http://localhost:8000/docs

## Notes

- `pyproject.toml` contains project metadata and dependencies. The `description` field is a placeholder.
- Several modules are present as implementation stubs (for example, `app/services/chat_service.py` and `app/rag/retriever.py`). Fill these with project-specific logic.

## Contributing

PRs, issues, and suggestions welcome. Run tests with:

```bash
pytest -q
```

