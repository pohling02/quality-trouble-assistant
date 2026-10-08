import os
import json
import chromadb
from mcp.server.fastmcp import FastMCP

# Initialize MCP Server
mcp = FastMCP("QualityTroubleshootingAssistant")

# Initialize DB connection
db_client = chromadb.PersistentClient(path="./chroma_db")
collection = db_client.get_collection(name="troubleshooting_docs")

@mcp.tool()
def search_troubleshooting(query: str, n_results: int = 3) -> str:
    """Search the troubleshooting knowledge base for solutions to problems."""
    try:
        results = collection.query(query_texts=[query], n_results=n_results)
        
        if not results['documents'][0]:
            return "No relevant troubleshooting steps found."
            
        response = []
        for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
            response.append(f"}]\n{doc}\n")
            
        return "\n---\n".join(response)
    except Exception as e:
        return f"Error searching database: {str(e)}"

@mcp.tool()
def list_sources() -> str:
    """List all available troubleshooting documents in the knowledge base."""
    docs_dir = "docs"
    if not os.path.exists(docs_dir):
        return "Docs directory not found."
    files = [f for f in os.listdir(docs_dir) if f.endswith('.md')]
    return "Available documents:\n" + "\n".join(files)

@mcp.tool()
def create_ticket(title: str, summary: str) -> str:
    """Log a new issue ticket if the troubleshooting steps did not resolve the problem."""
    ticket = {"title": title, "summary": summary}
    try:
        with open("tickets.json", "r") as f:
            tickets = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tickets = []
        
    tickets.append(ticket)
    
    with open("tickets.json", "w") as f:
        json.dump(tickets, f, indent=4)
        
    return f"Ticket created successfully: {title}"

if __name__ == "__main__":
    # Run the server using standard I/O (required for MCP over Claude Desktop)
    mcp.run(transport='stdio')