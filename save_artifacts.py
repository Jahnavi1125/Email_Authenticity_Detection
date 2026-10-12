# Run this ONCE at the end of your training notebook/script.
# Replace `best_model` and `tfidf` with your own variable names.
import joblib

joblib.dump(best_model, "model.pkl")   # your best classifier
joblib.dump(tfidf, "vectorizer.pkl")   # your fitted TfidfVectorizer
print("Saved model.pkl and vectorizer.pkl")
