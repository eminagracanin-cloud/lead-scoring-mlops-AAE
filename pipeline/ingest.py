import pandas as pd

def load_data():
    df = pd.read_csv("Lead Scoring.csv")
    return df
