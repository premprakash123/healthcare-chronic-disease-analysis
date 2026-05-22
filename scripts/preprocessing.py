# ==========================================
# Healthcare Preprocessing Pipeline
# ==========================================

import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Load cleaned dataset
df = pd.read_csv("data/processed/ckd_scaled.csv")

# Initialize label encoder
label_encoder = LabelEncoder()

# Encode categorical columns
for col in df.select_dtypes(include='object').columns:
    
    df[col] = label_encoder.fit_transform(df[col])

# Separate features and target
X = df.drop("class", axis=1)

y = df["class"]

# Apply feature scaling
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Convert to DataFrame
X_scaled = pd.DataFrame(
    X_scaled,
    columns=X.columns
)

# Add target back
X_scaled["class"] = y.values

# Export ML-ready dataset
X_scaled.to_csv(
    "data/processed/ckd_ml_ready.csv",
    index=False
)

# Save scaler
joblib.dump(
    scaler,
    "models/standard_scaler.pkl"
)

print("Preprocessing completed successfully.")