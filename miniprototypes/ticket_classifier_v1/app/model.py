import joblib

model = joblib.load("./model/ticket_model.joblib")

def predict(text: str) -> str:
    return model.predict([text])[0]

