from datasets import load_dataset
import pandas as pd

df = pd.read_csv("docs/huggingfaces/customer_support_tickets_sample.csv")
for _, r in df.head(8).iterrows():
    print("SUBJECT:", r["subject"])
    print("BODY:", r["body"][:300])
    print("ANSWER:", r["answer"][:300])
    print("-" * 60)