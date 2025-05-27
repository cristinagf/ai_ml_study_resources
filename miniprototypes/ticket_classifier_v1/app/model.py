import joblib

model = joblib.load("/home/cristina/mine/code/cristigf/ticket_classifier/model/ticket_model.joblib")

def predict(text: str) -> str:
    return model.predict([text])[0]

