import streamlit as st
import pandas as pd
import joblib


# Load the trained pipeline
model = joblib.load(r"C:\Users\Muhammad Huzifa\Desktop\AI_Course_Huawei\Week-6\code\logistic_regression\student_pass_fail_model.pkl")


st.title("Student Pass/Fail Prediction")
st.write("Enter the student's information below.")


# Numerical inputs
study_hours = st.number_input(
    "Study Hours Per Day",
    min_value=0.5,
    max_value=8.0,
    value=3.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=50,
    max_value=100,
    value=75,
    step=1
)

previous_score = st.number_input(
    "Previous Year Score",
    min_value=35,
    max_value=95,
    value=60,
    step=1
)

assignment_completion = st.number_input(
    "Assignment Completion Percentage",
    min_value=30,
    max_value=100,
    value=70,
    step=1
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=4.0,
    max_value=9.0,
    value=7.0,
    step=0.5
)


# Text inputs
internet_access = st.selectbox(
    "Internet Access",
    ["Yes", "No"]
)

extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)


if st.button("Predict Result"):

    # Create one student row
    student_data = pd.DataFrame({
        "Study_Hours_Per_Day": [study_hours],
        "Attendance_Percentage": [attendance],
        "Previous_Year_Score": [previous_score],
        "Assignment_Completion_Percentage": [assignment_completion],
        "Sleep_Hours": [sleep_hours],
        "Internet_Access": [internet_access],
        "Extracurricular_Activities": [extracurricular]
    })

    # Make prediction
    prediction = model.predict(student_data)[0]

    # Get prediction confidence
    probabilities = model.predict_proba(student_data)
     

    # Display result
    if prediction == "Pass":
        st.success(f"Prediction: {prediction}")
    else:
        st.error(f"Prediction: {prediction}")

    st.write(f"Model Confidence: {probabilities.max()} ")