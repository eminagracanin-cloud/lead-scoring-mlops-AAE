import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib


def train_model():
    # load data
    df = pd.read_csv("Lead Scoring.csv")

    # select features
    df = df[[
        "TotalVisits",
        "Total Time Spent on Website",
        "Page Views Per Visit",
        "Asymmetrique Activity Score",
        "Asymmetrique Profile Score",
        "Converted"
    ]]

    # remove missing values
    df = df.dropna()

    # split features + target
    X = df.drop("Converted", axis=1)
    y = df["Converted"]

    # train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # save model
    joblib.dump(model, "model.pkl")

    return model
