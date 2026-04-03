# Lead Scoring MLOps Pipeline

This project implements an end-to-end MLOps pipeline for predicting whether a lead is likely to convert into a customer.

## Project Structure

- `app/` – FastAPI application (API endpoints)
- `pipeline/` – Data processing and model pipeline
- `requirements.txt` – Python dependencies
- `Dockerfile` – Containerization setup

## Features

- Modular pipeline design
- API for real-time predictions
- Basic preprocessing and model structure
- Docker-ready for deployment

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the API:
uvicorn app.main:app --reload


## Endpoint

- `GET /` – Health check
- `POST /predict` – Predict lead conversion

---

This project focuses on system design, reproducibility, and deployment in an MLOps context.
