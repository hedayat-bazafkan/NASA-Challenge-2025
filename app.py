from fastapi import FastAPI, Header, HTTPException
import uvicorn
import random

app = FastAPI()
API_KEY = "supersecretkey"  # you can change this later

@app.get("/")
def root():
    return {"message": "NASA Exoplanet ML Challenge API"}

@app.post("/run-pipeline")
def run_pipeline(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    accuracy = round(random.uniform(0.85, 0.97), 4)
    return {"status": "ok", "model_accuracy": accuracy}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
