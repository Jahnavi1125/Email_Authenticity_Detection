import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Email Authenticity Detection API")

# Load once at startup
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Change this if your labels are different (e.g. 1 = spam, 0 = legitimate)
LABELS = {0: "legitimate", 1: "spam/phishing"}


class EmailRequest(BaseModel):
    text: str


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(req: EmailRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="text must not be empty")

    features = vectorizer.transform([req.text])
    pred = model.predict(features)[0]

    result = {"label": LABELS.get(pred, str(pred))}
    if hasattr(model, "predict_proba"):
        result["probability"] = round(float(model.predict_proba(features).max()), 4)
    return result
