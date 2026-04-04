def preprocess_data(df):
    df = df[[
        "TotalVisits",
        "Total Time Spent on Website",
        "Page Views Per Visit",
        "Asymmetrique Activity Score",
        "Asymmetrique Profile Score",
        "Converted"
    ]]

    df = df.dropna()

    X = df.drop("Converted", axis=1)
    y = df["Converted"]

    return X, y
