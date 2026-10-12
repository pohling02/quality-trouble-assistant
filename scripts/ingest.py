from pathlib import Path
import re
import chromadb

DOCS_DIR = Path("docs")
CHUNK_SIZE = 800
OVERLAP = 100

def split_by_heading(text):
    parts = re.split(r"\n(?=#{1,3} )", text)
    return [p.strip() for p in parts if p.strip()]

def split_by_size(text):
    if len(text) <= CHUNK_SIZE:
        return [text]
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start:start + CHUNK_SIZE])
        start += CHUNK_SIZE - OVERLAP
    return chunks

def clean(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)   # front matter
    text = re.sub(r"```.{800,}?```", "", text, flags=re.DOTALL)     # very long code blocks
    return text

client = chromadb.PersistentClient(path="chroma_db")
try:
    client.delete_collection("troubleshooting")
except Exception:
    pass
collection = client.create_collection("troubleshooting")

ids, documents, metadatas = [], [], []
for path in sorted(DOCS_DIR.rglob("*.md")):
    text = clean(path.read_text(encoding="utf-8", errors="ignore"))
    
    title_match = re.search(r"^# (.+)$", text, flags=re.MULTILINE)
    title = title_match.group(1) if title_match else path.stem
    n = 0
    
    for section in split_by_heading(text):
        for chunk in split_by_size(section):
            if len(chunk) < 50:
                continue
            if not chunk.startswith(f"# {title}"):
                chunk = f"{title}\n\n{chunk}"
            
            ids.append(f"{path}:{n}")
            documents.append(chunk)
            metadatas.append({
                "source": str(path),
                "source_type": "notes" if path.parts[1] == "notes" else "public",
                "title": title,
                "chunk": n,
            })
            n += 1

for i in range(0, len(ids), 100):
    collection.add(ids=ids[i:i+100], documents=documents[i:i+100], metadatas=metadatas[i:i+100])

print(f"Ingested {len(ids)} chunks from {len(set(m['source'] for m in metadatas))} files")