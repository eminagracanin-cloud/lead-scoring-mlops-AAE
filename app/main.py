from fastapi import FastAPI
from app.schemas import LeadInput

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Lead Scoring API is running"}


@app.post("/predict")
def predict(lead: LeadInput):
    # simulate preprocessing + model logic

    features = [
        lead.total_visits,
        lead.time_spent_on_website
    ]

    if features[1] > 100:
        prediction = 1
    else:
        prediction = 0

    return {
        "prediction": prediction,
        "features_used": features
    }
