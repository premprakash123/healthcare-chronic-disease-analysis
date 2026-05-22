# ==========================================
# Healthcare Model Evaluation Pipeline
# ==========================================

import pandas as pd
import joblib

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("data/processed/ckd_ml_ready.csv")

# Load trained model
model = joblib.load(
    "models/random_forest_model.pkl"
)

print("Model evaluation pipeline ready.")