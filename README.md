# Email Authenticity Detection

Classifies emails as legitimate or spam/phishing using an NLP pipeline, and serves the best model through a FastAPI REST API.

**Tech:** Python, Scikit-learn, TF-IDF, FastAPI, Docker

## Overview
- Text preprocessing and TF-IDF feature extraction
- Benchmarked Naive Bayes, SVM, Logistic Regression and Random Forest
- Compared models using accuracy, precision, recall and F1-score
- Best model served through a `/predict` REST endpoint

## Results
| Model | Accuracy | Precision | Recall | F1-score |
|---|---|---|---|---|
| Naive Bayes | _fill in_ | _fill in_ | _fill in_ | _fill in_ |
| SVM | _fill in_ | _fill in_ | _fill in_ | _fill in_ |
| Logistic Regression | _fill in_ | _fill in_ | _fill in_ | _fill in_ |
| Random Forest | _fill in_ | _fill in_ | _fill in_ | _fill in_ |

## Project Files
| File | Purpose |
|---|---|
| `Email_Authenticity_Detection.ipynb` | Data preprocessing, training and evaluation |
| `save_artifacts.py` | Saves the trained model and TF-IDF vectorizer |
| `app.py` | FastAPI service with the `/predict` endpoint |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container image for the API |

## How to Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Generate model files** (skip if `model.pkl` and `vectorizer.pkl` are already in the repo)
Run the notebook, then `save_artifacts.py`, to create `model.pkl` and `vectorizer.pkl`.

**3. Start the API**
```bash
uvicorn app:app --reload
```
Open `http://127.0.0.1:8000/docs` to try it in the browser.

**4. Example request**
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "Congratulations, you won a free prize, click here"}'
```
Example response:
```json
{"label": "spam/phishing", "probability": 0.97}
```

## Run with Docker
```bash
docker build -t email-api .
docker run -p 8000:8000 email-api
```

## Future Improvements
- Add automated tests and a CI/CD workflow
- Experiment with transformer-based models
