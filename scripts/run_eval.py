import pandas as pd


# Load multiple raw output datasets
raw_v1 = pd.read_csv("data/raw_outputs_v1.csv")
raw_v2 = pd.read_csv("data/raw_outputs_v2.csv")

# Combine datasets
raw_outputs = pd.concat(
    [raw_v1, raw_v2],
    ignore_index=True
)
annotations = pd.read_csv("data/annotations.csv")


# Merge datasets on sample_id
merged = pd.merge(
    raw_outputs,
    annotations,
    on="sample_id"
)

# Save merged dataset
merged.to_csv("data/merged_dataset.csv", index=False)

# Print basic evaluation statistics
print("\n=== LABEL DISTRIBUTION ===")
print(merged["primary_label"].value_counts())

print("\n=== SEVERITY DISTRIBUTION ===")
print(merged["severity"].value_counts())

print("\n=== EDGE CASE COUNT ===")
print(merged["edge_case"].value_counts())

print("\nMerged dataset saved to data/merged_dataset.csv")