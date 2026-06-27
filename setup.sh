#!/bin/bash

# 🚀 Student Performance Dashboard - Quick Setup Script

echo "🎓 Student Performance Dashboard Setup"
echo "========================================"

# Step 1: Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Step 2: Train the model
echo "🤖 Training the model..."
python train_model.py

# Step 3: Run the dashboard
echo "🚀 Starting Streamlit dashboard..."
echo "📊 Dashboard will open at: http://localhost:8501"
streamlit run app.py
