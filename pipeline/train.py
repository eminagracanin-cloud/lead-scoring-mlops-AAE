import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train_model():
    # 1. Load dataset
    df = pd.read_csv("Lead Scoring.csv")

    # 2. Select relevant features
    df = df[[
        "TotalVisits",
        "Total Time Spent on Website",
        "Page Views Per Visit",
        "Asymmetrique Activity Score",
        "Asymmetrique Profile Score",
        "Converted"
    ]]

    # 3. Handle missing values
    df = df.dropna()

    # 4. Split features and target
    X = df.drop("Converted", axis=1)
    y = df["Converted"]

    # 5. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 6. Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 7. Evaluate model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy:.4f}")

    # 8. Save model
    joblib.dump(model, "model.pkl")

    return model
