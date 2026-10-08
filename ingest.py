import os
import chromadb

# Initialize ChromaDB persistent client
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="troubleshooting_docs")

def chunk_text(text, chunk_size=400, overlap=50):
    """Splits text into chunks of `chunk_size` with `overlap` characters."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks

def main():
    docs_dir = "docs"
    for filename in os.listdir(docs_dir):
        if not filename.endswith(".md"):
            continue
            
        file_path = os.path.join(docs_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        chunks = chunk_text(content)
        
        for i, chunk in enumerate(chunks):
            chunk_id = f"{filename}_chunk_{i}"
            # Add to vector database
            collection.add(
                documents=[chunk],
                metadatas=[{"source": filename, "chunk_index": i}],
                ids=[chunk_id]
            )
            print(f"Ingested: {chunk_id}")
            
    print("Ingestion complete!")

if __name__ == "__main__":
    main()