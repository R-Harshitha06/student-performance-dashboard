 import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os
from pathlib import Path

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ✅ Add error handling for missing files
try:
    model = joblib.load("models/random_forest.pkl")
    scaler = joblib.load("models/scaler.pkl")
except FileNotFoundError:
    st.error("❌ Model files not found! Please run `python train_model.py` first.")
    st.stop()

st.title("🎓 Student Performance Prediction Dashboard")

tab1, tab2 = st.tabs([
    "Prediction",
    "Dataset Analytics"
])

with tab1:

    st.header("Student Information")

    col1, col2 = st.columns(2)

    with col1:

        study_hours = st.slider(
            "Study Hours",
            0,
            12,
            5
        )

        attendance = st.slider(
            "Attendance %",
            50,
            100,
            80
        )

        parental = st.selectbox(
            "Parental Involvement",
            ["Low", "Medium", "High"]
        )

        resources = st.selectbox(
            "Access To Resources",
            ["Low", "Medium", "High"]
        )

        extracurricular = st.selectbox(
            "Extracurricular Activities",
            ["No", "Yes"]
        )

    with col2:

        sleep = st.slider(
            "Sleep Hours",
            4,
            10,
            7
        )

        previous = st.slider(
            "Previous Scores",
            50,
            100,
            75
        )

        motivation = st.selectbox(
            "Motivation Level",
            ["Low", "Medium", "High"]
        )

        internet = st.selectbox(
            "Internet Access",
            ["No", "Yes"]
        )

        tutoring = st.slider(
            "Tutoring Sessions",
            0,
            8,
            2
        )

    if st.button("Predict Exam Score"):

        # ✅ Consistent mapping with train_model.py
        mapping = {
            "Low": 1,
            "Medium": 2,
            "High": 3,
            "Yes": 1,
            "No": 0
        }

        # ✅ Create input data with correct column order matching training
        input_data = pd.DataFrame([[
            study_hours,
            attendance,
            mapping[parental],
            mapping[resources],
            mapping[extracurricular],
            sleep,
            previous,
            mapping[motivation],
            mapping[internet],
            tutoring
        ]],
        columns=[
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
        ])

        # ✅ Ensure data types match training data
        input_data = input_data.astype('float64')
        
        # ✅ Scale input before prediction
        scaled = scaler.transform(input_data)

        # ✅ Add error handling for prediction
        try:
            prediction = model.predict(scaled)[0]
            
            # ✅ Add confidence context
            if prediction < 50:
                color = "🔴"
                context = "Below Average"
            elif prediction < 75:
                color = "🟡"
                context = "Good"
            else:
                color = "🟢"
                context = "Excellent"
            
            st.success(
                f"{color} Predicted Exam Score: **{prediction:.2f}/100** ({context})"
            )
        except Exception as e:
            st.error(f"❌ Prediction failed: {str(e)}")

with tab2:

    st.header("Dataset Analytics")

    # ✅ Add error handling for data loading
    try:
        df = pd.read_csv("data/StudentPerformanceFactors.csv")
    except FileNotFoundError:
        st.error("❌ Dataset not found at `data/StudentPerformanceFactors.csv`")
        st.stop()
    
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Exam Score Distribution")

    fig = px.histogram(
        df,
        x="Exam_Score",
        nbins=20,
        title="Exam Score Distribution",
        labels={"Exam_Score": "Exam Score", "count": "Frequency"}
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Attendance vs Exam Score")

    fig2 = px.scatter(
        df,
        x="Attendance",
        y="Exam_Score",
        color="Motivation_Level",
        title="Attendance vs Exam Score by Motivation Level",
        labels={"Attendance": "Attendance %", "Exam_Score": "Exam Score"}
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("Correlation Heatmap")

    numeric_df = df.select_dtypes(
        include="number"
    )

    corr = numeric_df.corr()

    fig3 = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Feature Correlation Heatmap",
        labels=dict(color="Correlation")
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
