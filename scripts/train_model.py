# ==========================================
# Healthcare Model Training Pipeline
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load ML-ready dataset
df = pd.read_csv("data/processed/ckd_ml_ready.csv")

# Separate features and target
X = df.drop("class", axis=1)

y = df["class"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    
    X,
    y,
    
    test_size=0.2,
    
    random_state=42,
    
    stratify=y
)

# Initialize model
model = RandomForestClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Save trained model
joblib.dump(
    model,
    "models/random_forest_model.pkl"
)

print("Model training completed successfully.")