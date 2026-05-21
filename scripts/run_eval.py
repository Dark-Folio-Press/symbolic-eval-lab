import pandas as pd

# Load datasets
raw_outputs = pd.read_csv("data/raw_outputs.csv")
annotations = pd.read_csv("data/annotations.csv")

# Normalize sample_id formatting
raw_outputs["sample_id"] = raw_outputs["sample_id"].astype(str).str.strip()
annotations["sample_id"] = annotations["sample_id"].astype(str).str.strip()

# Merge datasets
merged = pd.merge(
    raw_outputs,
    annotations,
    on="sample_id"
)

# Save merged dataset
merged.to_csv("data/merged_dataset.csv", index=False)

# Print stats
print("\nMerged Records:", len(merged))

print("\n=== LABEL DISTRIBUTION ===")
print(merged["primary_label"].value_counts())

print("\n=== SEVERITY DISTRIBUTION ===")
print(merged["severity"].value_counts())

print("\n=== EDGE CASE COUNT ===")
print(merged["edge_case"].value_counts())

print("\nMerged dataset saved to data/merged_dataset.csv")