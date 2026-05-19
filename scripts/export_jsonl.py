import pandas as pd
import json

# Load merged dataset
df = pd.read_csv("data/merged_dataset.csv")


# Export to JSONL
with open("data/dataset.jsonl", "w") as f:

    for _, row in df.iterrows():

        record = {
            "sample_id": row["sample_id"],
            "prompt": row["prompt"],
            "model_output": row["model_output"],
            "primary_label": row["primary_label"],
            "severity": row["severity"],
            "rationale": row["rationale"],
            "confidence": row["confidence"],
            "edge_case": row["edge_case"]
        }

        f.write(json.dumps(record) + "\n")

print("JSONL export completed!")