import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("data/dataset.csv")

X = data["text"]
y = data["label"]

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)


model = LogisticRegression()
model.fit(X_vectorized, y)

joblib.dump(model, "mental_health_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully.")
