# main.py
import os
import json
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
# Allow CORS for testing. In production set specific origins.
CORS(app, resources={r"/*": {"origins": "*"}})

API_KEY = os.environ.get("API_KEY", "supersecretkey")
MODEL_PATH = "artifacts/model.joblib"
METRICS_PATH = "artifacts/metrics.json"

@app.route("/")
def index():
    return jsonify({"message": "NASA Exoplanet ML Challenge API"})

def check_key(req):
    key = req.headers.get("x-api-key")
    if API_KEY and key != API_KEY:
        return False
    return True

@app.route("/run-pipeline", methods=["POST"])
def run_pipeline():
    # Protect endpoint with API key
    if not check_key(request):
        return jsonify({"error": "Invalid API key"}), 401

    # This runs the training script train.py in the container.
    # Ensure train.py exists in project root (we will add it later).
    try:
        proc = subprocess.run(
            ["python", "train.py"],
            capture_output=True,
            text=True,
            check=False,
            timeout=60*20  # 20 minutes max (adjust if you need more)
        )
        out = proc.stdout
        err = proc.stderr
        code = proc.returncode
        result = {"returncode": code, "stdout": out, "stderr": err}
        # If metrics.json was produced by train.py, return it too
        if os.path.exists(METRICS_PATH):
            with open(METRICS_PATH) as f:
                result["metrics"] = json.load(f)
        return jsonify(result)
    except subprocess.TimeoutExpired:
        return jsonify({"error":"Training timed out"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/metrics", methods=["GET"])
def metrics():
    if not check_key(request):
        return jsonify({"error": "Invalid API key"}), 401
    if not os.path.exists(METRICS_PATH):
        return jsonify({"error":"No metrics found. Run /run-pipeline first."}), 404
    with open(METRICS_PATH) as f:
        return jsonify(json.load(f))

@app.route("/predict", methods=["POST"])
def predict():
    if not check_key(request):
        return jsonify({"error": "Invalid API key"}), 401
    payload = request.get_json()
    if not payload:
        return jsonify({"error":"Send JSON body with features"}), 400
    if not os.path.exists(MODEL_PATH):
        return jsonify({"error":"Model not found. Train first."}), 404
    try:
        model = joblib.load(MODEL_PATH)
        df = pd.DataFrame([payload])
        preds = model.predict(df).tolist()
        probs = None
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(df).tolist()
        return jsonify({"predictions": preds, "probabilities": probs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # in container just run: python main.py
    app.run(host="0.0.0.0", port=8000)
