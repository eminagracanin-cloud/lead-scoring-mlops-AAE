from datetime import datetime
import joblib
from fastapi import FastAPI
from app.schemas import LeadInput

app = FastAPI()

model = joblib.load("model.pkl")


@app.get("/")
def read_root():
    return {"message": "Lead Scoring API is running"}


@app.post("/predict")
def predict(lead: LeadInput):
    features = [[
        lead.total_visits,
        lead.time_spent_on_website,
        lead.page_views_per_visit,
        lead.asymmetrique_activity_score,
        lead.asymmetrique_profile_score
    ]]

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }
