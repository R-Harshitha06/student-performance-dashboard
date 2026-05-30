import pandas as pd

ordinal_map = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

def preprocess(df):

    categorical_cols = [
        "Parental_Involvement",
        "Access_to_Resources",
        "Motivation_Level"
    ]

    for col in categorical_cols:
        df[col] = df[col].map(ordinal_map)

    bool_map = {
        "Yes": 1,
        "No": 0,
        True: 1,
        False: 0
    }

    df["Internet_Access"] = df["Internet_Access"].map(bool_map)
    df["Extracurricular_Activities"] = df["Extracurricular_Activities"].map(bool_map)

    return df