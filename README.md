# 🎓 Student Performance Prediction Dashboard

A Machine Learning-powered dashboard built with **Python**, **Scikit-Learn**, and **Streamlit** to predict student exam performance based on academic, behavioral, and environmental factors.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>
</p>

---

## 📌 Project Overview

This project analyzes factors that influence student academic performance and predicts exam scores using machine learning models.

The dashboard allows users to:
- ✅ Enter student information and predict exam scores
- ✅ Explore dataset analytics and trends
- ✅ Visualize performance patterns interactively
- ✅ Understand key factors affecting student success

---

## 📸 Dashboard Screenshots

### Prediction Tab
<img width="1857" alt="Prediction Dashboard" src="https://github.com/user-attachments/assets/8d983cec-af7f-4b90-87a5-3ed0b8efbf79" />

### Dataset Analytics
<img width="1843" alt="Dataset Analytics" src="https://github.com/user-attachments/assets/9963fb5b-3461-4e1a-b096-7d3770d763fd" />

### Score Distribution
<img width="1868" alt="Score Distribution" src="https://github.com/user-attachments/assets/c3388bbf-a9d6-4b2b-9ead-cd43a9047da0" />

### Attendance vs Exam Score
<img width="1820" alt="Attendance vs Score" src="https://github.com/user-attachments/assets/99733142-dbf7-44ec-a814-6c5d9765c7c7" />

### Correlation Heatmap
<img width="1773" alt="Correlation Heatmap" src="https://github.com/user-attachments/assets/5952a00b-e1b8-46b0-838b-0edced1a1baf" />

---

## 🚀 Features

### 🎯 Student Score Prediction
Predicts student exam scores using a trained **Random Forest Regression** model with real-time inputs.

### 📊 Interactive Dashboard
Built with **Streamlit** for an intuitive and responsive user experience.

### 📈 Data Analytics
- Dataset preview
- Score distribution analysis
- Attendance vs Exam Score visualization
- Correlation heatmap

### 🤖 Machine Learning Pipeline
- Data preprocessing & feature encoding
- Feature selection
- Model training & evaluation
- Saved model deployment

---

## 📦 Dataset

**Dataset:** Student Performance Factors  
**Source:** [Kaggle — Student Performance Factors](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)

### Features Used

| Feature | Description |
|---|---|
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

**Target Variable:** `Exam_Score`

---

## 🛠️ Technology Stack

| Category | Tools |
|---|---|
| Language | Python |
| Dashboard | Streamlit |
| Visualization | Plotly |
| ML Models | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Model Saving | Joblib |

### ML Models Used
- Linear Regression
- Decision Tree Regressor
- ✅ **Random Forest Regressor** (Best performer — deployed)

---

## 📁 Project Structure

```
student-performance-dashboard/
│
├── data/
│   └── StudentPerformanceFactors.csv
│
├── models/
│   ├── random_forest.pkl       ← trained model (gitignored)
│   └── scaler.pkl              ← preprocessor (gitignored)
│
├── app.py                      ← main Streamlit dashboard
├── train_model.py              ← model training script
├── requirements.txt            ← dependencies
├── runtime.txt                 ← Python version
├── .gitignore                  ← git ignore rules
└── README.md                   ← documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/R-Harshitha06/student-performance-dashboard.git
cd student-performance-dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model
```bash
python train_model.py
```
This generates:
```
models/random_forest.pkl
models/scaler.pkl
```

### 4. Run Dashboard
```bash
streamlit run app.py
```
Open: **http://localhost:8501**

---

## 📊 Model Evaluation

| Metric | Description |
|---|---|
| R² Score | Variance explained by model |
| RMSE | Root Mean Squared Error |
| MAE | Mean Absolute Error |

### 🔍 Most Important Features
1. Previous Scores
2. Attendance
3. Hours Studied
4. Motivation Level
5. Tutoring Sessions

---

## 🔮 Future Enhancements

- [ ] Feature Importance Visualization
- [ ] SHAP Explainability
- [ ] Student Risk Classification
- [ ] Downloadable Prediction Reports
- [ ] Cloud Deployment (Streamlit Cloud)
- [ ] Model Comparison Dashboard

---

## 👩‍💻 Author

**Harshitha R**  
🎓 B.Tech CSE (AI & ML) | SVCET, Chittoor  
📧 rharshitha1103@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/harshitha-r-6017a8347) | [GitHub](https://github.com/R-Harshitha06)

---

<p align="center">⭐ If you found this project useful, please give it a star!</p>
