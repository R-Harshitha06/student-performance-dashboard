# 🎓 Student Performance Prediction Dashboard

A Machine Learning-powered dashboard built with **Python**, **Scikit-Learn**, and **Streamlit** to predict student exam performance based on academic, behavioral, and environmental factors.

## 📌 Project Overview

This project analyzes factors that influence student academic performance and predicts exam scores using machine learning models.

The dashboard allows users to:

- Enter student information
- Predict exam scores
- Explore dataset analytics
- Visualize performance trends
- Understand key factors affecting student success

---

## 🚀 Features

### Student Score Prediction
Predicts student exam scores using a trained Random Forest Regression model.

### Interactive Dashboard
Built with Streamlit for an intuitive user experience.

### Data Analytics
Includes:
- Dataset preview
- Score distribution analysis
- Attendance vs Exam Score visualization
- Correlation analysis

### Machine Learning Pipeline
- Data preprocessing
- Feature encoding
- Feature selection
- Model training
- Model evaluation

---

## 📊 Dataset

Dataset: **Student Performance Factors**

Source:
https://www.kaggle.com/datasets/lainguyn123/student-performance-factors

### Features Used

| Feature | Description |
|----------|-------------|
| Hours_Studied | Daily study hours |
| Attendance | Attendance percentage |
| Parental_Involvement | Academic support from parents |
| Access_to_Resources | Learning resource availability |
| Extracurricular_Activities | Participation in activities |
| Sleep_Hours | Average sleep duration |
| Previous_Scores | Historical academic performance |
| Motivation_Level | Student motivation level |
| Internet_Access | Internet availability |
| Tutoring_Sessions | Number of tutoring sessions |

### Target Variable

```text
Exam_Score
```

---

## 🛠️ Technology Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Plotly
- Joblib

### Machine Learning Models
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## 📂 Project Structure

```text
student-performance-dashboard/
│
├── data/
│   └── StudentPerformanceFactors.csv
│
├── models/
│   ├── random_forest.pkl
│   └── scaler.pkl
│
├── src/
│   ├── preprocess.py
│   ├── predict.py
│   └── train_model.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/R-Harshitha06/student-performance-dashboard.git
```

### Navigate to Project

```bash
cd student-performance-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Train the Model

```bash
python src/train_model.py
```

Generated files:

```text
models/random_forest.pkl
models/scaler.pkl
```

---

## ▶️ Run Dashboard

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📈 Model Evaluation

Evaluation metrics used:

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

### Expected Important Features

- Previous Scores
- Attendance
- Hours Studied
- Motivation Level
- Tutoring Sessions

---

## 📸 Dashboard Screenshots

Add screenshots here after deployment.

Example:

```markdown
![Dashboard Screenshot](images/dashboard.png)
```

---

## 🔮 Future Enhancements

- Feature Importance Visualization
- SHAP Explainability
- Student Risk Classification
- Downloadable Prediction Reports
- Cloud Deployment
- Model Comparison Dashboard

---

## 👩‍💻 Author

**Harshitha R**

GitHub:
https://github.com/R-Harshitha06

---

## ⭐ Repository

If you found this project useful, consider giving it a star.

