# ==========================================
# Healthcare Data Cleaning Pipeline
# ==========================================

import pandas as pd

# Load initial processed healthcare dataset
df = pd.read_csv(
    
    "data/processed/ckd_cleaned.csv"
)

# Remove hidden spaces from column names

# Display all column names
print(df.columns)

df.columns = df.columns.str.strip()

# Display dataset shape
print("Dataset Shape:")

print(df.shape)

# Remove hidden spaces from column names
df.columns = df.columns.str.strip()

# Remove unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Standardize target labels
df['class'] = df['class'].replace({
    
    'no': 'notckd'
})

# Display first five rows
print("\nDataset Preview:")

print(df.head())

# Export cleaned dataset
df.to_csv(
    
    "data/processed/ckd_cleaned.csv",
    
    index=False
)

print("\nHealthcare data cleaning completed successfully.")