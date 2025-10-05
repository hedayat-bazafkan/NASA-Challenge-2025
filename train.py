# train.py (simple example — saves a tiny dummy model and metrics)
import os, json
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
import pandas as pd

ARTIFACTS = "artifacts"
os.makedirs(ARTIFACTS, exist_ok=True)

# Create a tiny fake dataset and train a model as a placeholder.
def train_dummy():
    # fake data
    X = pd.DataFrame({
        "f1": np.random.randn(200),
        "f2": np.random.randn(200)
    })
    y = (X["f1"] + X["f2"] > 0).astype(int)
    clf = RandomForestClassifier(n_estimators=10, random_state=0)
    clf.fit(X, y)
    model_path = os.path.join(ARTIFACTS, "model.joblib")
    joblib.dump(clf, model_path)
    metrics = {
        "n_samples": len(X),
        "note": "This is a dummy model. Replace train.py with your real training code."
    }
    with open(os.path.join(ARTIFACTS, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
    print("Training done. Model saved to", model_path)

if __name__ == "__main__":
    train_dummy()
