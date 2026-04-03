import pandas as pd


def preprocess_data(df: pd.DataFrame):
    df = df.copy()

    # remove missing values for now
    df = df.dropna()

    return df
