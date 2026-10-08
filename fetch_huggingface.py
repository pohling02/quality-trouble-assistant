import os
from datasets import load_dataset

# Output directory matching your structure
output_dir = os.path.join("docs", "huggingfaces")
os.makedirs(output_dir, exist_ok=True)

# Example using a public IT / tech QA dataset:
# 'neural-bridge/rag-dataset-12' or 'sentence-transformers/natural-questions'
print("Loading dataset from Hugging Face...")
dataset = load_dataset("neural-bridge/rag-dataset-12", split="train", streaming=True)

count = 0
max_docs = 15  # Limit to 10-15 quality troubleshooting notes

for item in dataset:
    # Inspect or format the fields from the dataset
    # (Adjust field keys depending on your chosen dataset's schema)
    question = item.get("question") or item.get("instruction") or "Troubleshooting Issue"
    answer = item.get("answer") or item.get("response") or item.get("context") or ""
    
    # Filter for meaningful troubleshooting content
    if not answer or len(answer) < 50:
        continue

    filename = f"hf_issue_{count + 1:02d}.md"
    filepath = os.path.join(output_dir, filename)

    markdown_content = f"""# {question}

**Symptoms & Inquiry:**
{question}

**Resolution / Fix:**
{answer}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Created: {filepath}")
    count += 1
    if count >= max_docs:
        break

print(f"Finished writing {count} documents to {output_dir}")