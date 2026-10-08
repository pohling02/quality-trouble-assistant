import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="troubleshooting_docs")

results = collection.query(
    query_texts=["My computer screen is black after updating"],
    n_results=2
)

print("--- Search Results ---")
for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
    print(f"Source: {meta['source']}\nContent: {doc}\n")