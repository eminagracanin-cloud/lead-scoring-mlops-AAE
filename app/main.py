from fastapi import FastAPI
from app.schemas import LeadInput

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Lead Scoring API is running"}


@app.post("/predict")
def predict(lead: LeadInput):
    # simple dummy logic (for now)
    if lead.time_spent_on_website > 100:
        prediction = 1
    else:
        prediction = 0

    return {
        "prediction": prediction,
        "message": "This is a dummy prediction (will be replaced by model later)"
    }
