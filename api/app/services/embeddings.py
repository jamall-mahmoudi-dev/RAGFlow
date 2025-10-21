from sentence_transformers import SentenceTransformer
import os

model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
model = SentenceTransformer(model_name)

def embed_texts(texts: list[str]) -> list[list[float]]:
    return model.encode(texts, show_progress_bar=False).tolist()
