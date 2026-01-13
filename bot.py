import joblib

model = joblib.load("models/mental_health_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def get_response(user_input):
    input_vec = vectorizer.transform([user_input])
    prediction = model.predict(input_vec)[0]

    advice = {
        "depression": "You may be experiencing depression. Please talk to someone you trust and consider professional support.",
        "anxiety": "This seems like anxiety. Try deep breathing and relaxing exercises.",
        "stress": "Stress detected. Take breaks, rest well, and manage your workload.",
        "normal": "You seem to be in a healthy mental state. Keep maintaining a positive lifestyle!"
    }

    return advice[prediction]
