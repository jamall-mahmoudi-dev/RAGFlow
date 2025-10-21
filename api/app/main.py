from fastapi import FastAPI
from .routes import ingest, query

app = FastAPI(
    title="RAGFlow API",
    description="Retrieval-Augmented Generation Demo Backend",
    version="0.1.0"
)

app.include_router(ingest.router, prefix="/ingest", tags=["Ingestion"])
app.include_router(query.router, prefix="/query", tags=["Query"])

@app.get("/")
def health_check():
    return {"status": "ok", "message": "RAGFlow API running"}
