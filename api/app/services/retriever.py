from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import os

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def upsert_chunks(collection_name: str, texts: list[str], embeddings: list[list[float]]):
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config={"size": len(embeddings[0]), "distance": "Cosine"}
    )
    points = [
        PointStruct(id=i, vector=embeddings[i], payload={"text": texts[i]})
        for i in range(len(texts))
    ]
    client.upsert(collection_name=collection_name, points=points)

def retrieve(collection_name: str, query: str, top_k: int = 5):
    query_emb = client.openapi_client.vectorize_texts([query])[0] if hasattr(client, "openapi_client") else None
    if not query_emb:
        from .embeddings import embed_texts
        query_emb = embed_texts([query])[0]
    hits = client.search(collection_name=collection_name, query_vector=query_emb, limit=top_k)
    return [hit.payload for hit in hits]
