import re
def chunk_text(text: str, chunk_size=500, overlap=50):
    tokens = re.split(r'\s+', text)
    chunks = []
    i = 0
    while i < len(tokens):
        chunk = tokens[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks
