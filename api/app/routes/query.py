from fastapi import APIRouter
from pydantic import BaseModel
from ..services.retriever import retrieve

router = APIRouter()

class QueryRequest(BaseModel):
    collection: str
    query: str
    top_k: int = 5

@router.post("/")
def query_docs(req: QueryRequest):
    results = retrieve(req.collection, req.query, req.top_k)
    return {"query": req.query, "results": results}
