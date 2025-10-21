# RAGFlow
Generative AI (RAG + vector retrieval + scaling)
# RAG-Demo — Scalable Generative QA (FastAPI + Qdrant)

A minimal, production-minded demo of a RAG pipeline:
- FastAPI backend
- Qdrant vector DB
- sentence-transformers embeddings
- Redis caching & queueing
- Docker Compose for local dev

## Run locally
1. copy `.env.example` to `.env` and set variables
2. docker compose up --build
3. ingest docs: `curl -X POST http://localhost:8000/ingest ...`
4. query: `curl -X POST http://localhost:8000/query -d '{"q":"What is X?"}' -H "Content-Type: application/json"`

## Highlights
- Async batching + semaphore to avoid LLM 429 errors
- Caching (Redis) and queueing (RQ)
- Eval scripts for recall@k and latency
