import joblib
import pandas as pd

model = joblib.load("models/random_forest.pkl")
scaler = joblib.load("models/scaler.pkl")

def predict_score(data):
    df = pd.DataFrame([data])

    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)

    return round(prediction[0], 2)