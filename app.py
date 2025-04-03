
import streamlit as st
import pandas as pd
import joblib

# Load the model and encoders
model = joblib.load("health_risk_classifier.joblib")

def predict_risk(input_data):
    prediction = model.predict([input_data])
    label_map = {0: 'High', 1: 'Moderate', 2: 'Low'}
    return label_map[prediction[0]]

st.title("🏥 AI-Based Health Risk Estimator")
st.markdown("Enter your fitness tracker data to get your personalized health risk category.")

# Collect user inputs
age = st.slider("Age", 18, 80, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
weight = st.number_input("Weight (kg)", 30.0, 150.0, 70.0)
height = st.number_input("Height (m)", 1.4, 2.2, 1.75)
max_bpm = st.slider("Max BPM", 100, 210, 170)
avg_bpm = st.slider("Avg BPM", 60, 190, 130)
resting_bpm = st.slider("Resting BPM", 40, 100, 70)
session_duration = st.slider("Workout Duration (hrs)", 0.1, 3.0, 1.0)
calories = st.number_input("Calories Burned", 100, 3000, 500)
fat_percentage = st.slider("Fat %", 5.0, 50.0, 22.0)
water_intake = st.slider("Water Intake (liters)", 0.5, 5.0, 2.5)
workout_freq = st.slider("Workout Frequency (days/week)", 0, 7, 3)
experience = st.slider("Fitness Experience Level", 0, 3, 1)
bmi = st.number_input("BMI", 10.0, 40.0, 22.0)
sleep = st.slider("Sleep Duration (hours)", 3.0, 12.0, 7.0)

# Encode gender
gender_encoded = 1 if gender == "Male" else 0

# Input for model
user_input = [
    age, gender_encoded, weight, height, max_bpm, avg_bpm, resting_bpm,
    session_duration, calories, fat_percentage, water_intake,
    workout_freq, experience, bmi, sleep
]

if st.button("Predict Health Risk"):
    result = predict_risk(user_input)
    st.success(f"Your predicted health risk category is: **{result} Risk**")
