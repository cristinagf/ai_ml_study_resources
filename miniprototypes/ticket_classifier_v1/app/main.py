from fastapi import FastAPI

from app.schema import TicketRequest, TicketResponse
from app.model import predict


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Ticket Classifier API is live"}


@app.post("/predict", response_model=TicketResponse)
def classify_ticket(req: TicketRequest):
    category = predict(req.text)
    return TicketResponse(category=category)
