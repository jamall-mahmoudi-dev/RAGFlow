from fastapi import APIRouter
from pydantic import BaseModel
from ..services.embeddings import embed_texts
from ..services.retriever import upsert_chunks

router = APIRouter()

class IngestRequest(BaseModel):
    collection: str
    texts: list[str]

@router.post("/")
def ingest_docs(req: IngestRequest):
    embeddings = embed_texts(req.texts)
    upsert_chunks(req.collection, req.texts, embeddings)
    return {"status": "ok", "count": len(req.texts)}
