import json
from datetime import datetime
from pathlib import Path

import chromadb
from mcp.server.mcpserver import MCPServer

BASE = Path(__file__).resolve().parent
mcp = MCPServer("QualityTroubleshootingAssistant")

_client = chromadb.PersistentClient(path="/home/pohling/quality-trouble-assistant/chroma_db")
_collection = _client.get_collection("troubleshooting")


@mcp.tool()
def search_troubleshooting(query: str, n_results: int = 3, source_type: str = "") -> str:
    """Search troubleshooting notes and docs by meaning.
    source_type can be 'notes' or 'public' (leave empty for all)."""
    where = {"source_type": source_type} if source_type else None
    res = _collection.query(query_texts=[query], n_results=n_results, where=where)
    out = []
    for doc, meta in zip(res["documents"][0], res["metadatas"][0]):
        out.append(f"[Source: {meta['source']}]\n{doc}")
    return "\n\n---\n\n".join(out) or "No results found."


@mcp.tool()
def list_sources() -> str:
    """List the documents available in the knowledge base."""
    data = _collection.get(include=["metadatas"])
    sources = sorted({m["source"] for m in data["metadatas"]})
    return "\n".join(sources)


@mcp.tool()
def create_ticket(title: str, summary: str) -> str:
    """Log a troubleshooting ticket to tickets.json."""
    path = BASE / "tickets.json"
    tickets = json.loads(path.read_text()) if path.exists() else []
    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "summary": summary,
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    tickets.append(ticket)
    path.write_text(json.dumps(tickets, indent=2))
    return f"Created ticket #{ticket['id']}: {title}"


if __name__ == "__main__":
    mcp.run()