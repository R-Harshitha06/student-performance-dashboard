import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import os

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/StudentPerformanceFactors.csv")

# -----------------------------
# Features & target
# -----------------------------
X = df[[
    "Hours_Studied",
    "Attendance",
    "Parental_Involvement",
    "Access_to_Resources",
    "Extracurricular_Activities",
    "Sleep_Hours",
    "Previous_Scores",
    "Motivation_Level",
    "Internet_Access",
    "Tutoring_Sessions"
]]

y = df["Exam_Score"]

# -----------------------------
# Encode categorical values
# -----------------------------
mapping = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Yes": 1,
    "No": 0
}

for col in X.columns:
    X[col] = X[col].replace(mapping)

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Scale data
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# Train model
# -----------------------------
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train_scaled, y_train)

# -----------------------------
# Create models folder
# -----------------------------
os.makedirs("models", exist_ok=True)

# -----------------------------
# Save model + scaler
# -----------------------------
joblib.dump(model, "models/random_forest.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Model and scaler saved successfully in /models")
