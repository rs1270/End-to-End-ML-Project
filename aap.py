import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Set the page title
st.set_page_config(page_title="Student Performance Predictor")

# Title of the web app
st.title("Student Performance Predictor")

# Sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.write("Use this form to predict student performance based on various features.")

# Create a form for input
with st.form("prediction_form"):
    st.subheader("Enter Student Details:")

    gender = st.selectbox("Gender:", options=["male", "female"])
    ethnicity = st.selectbox("Race/Ethnicity:", options=[
        "group A", "group B", "group C", "group D", "group E"
    ])
    parental_level_of_education = st.selectbox("Parental Level of Education:", options=[
        "high school", "some high school", "associate's degree", "some college", "bachelor's degree", "master's degree"
    ])
    lunch = st.selectbox("Lunch Type:", options=["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course:", options=["completed","none"])

    reading_score = st.number_input("Reading Score:", min_value=0.0, max_value=100.0, step=5.0)
    writing_score = st.number_input("Writing Score:", min_value=0.0, max_value=100.0, step=5.0)

    # Submit button
    submitted = st.form_submit_button("Predict")

# Handle form submission
if submitted:
    # Create a data object using the CustomData class
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    # Convert the input data to a DataFrame
    pred_df = data.get_data_as_data_frame()

    # Make a prediction using the PredictPipeline
    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(pred_df)

    # Display the prediction result
    st.success(f"The predicted math score is: {prediction[0]:.2f}")
