from datetime import datetime
import joblib
from fastapi import FastAPI
from app.schemas import LeadInput

app = FastAPI()

# load trained model
model = joblib.load("model.pkl")


@app.get("/")
def read_root():
    return {"message": "Lead Scoring API is running"}


@app.post("/predict")
def predict(lead: LeadInput):
    # create feature array
    features = [[
        lead.total_visits,
        lead.time_spent_on_website,
        lead.page_views_per_visit,
        lead.asymmetrique_activity_score,
        lead.asymmetrique_profile_score
    ]]

    # model prediction
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    # logging (VERY IMPORTANT)
    with open("logs.txt", "a") as f:
        f.write(
            f"{datetime.now()} | Input: {features} | Prediction: {prediction} | Probability: {probability}\n"
        )

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }
