import streamlit as st
import pandas as pd

from src.logger import logging
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

# Page title
st.title("Student Exam Performance Indicator")

st.header("Student Exam Performance Prediction")

# Form inputs
gender = st.selectbox(
    "Gender",
    ["Select your Gender", "male", "female"]
)

ethnicity = st.selectbox(
    "Race or Ethnicity",
    ["Select Ethnicity", "group A", "group B", "group C", "group D", "group E"]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "Select Parent Education",
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ["Select Lunch Type", "free/reduced", "standard"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["Select Test Course", "none", "completed"]
)

reading_score = st.number_input(
    "Reading Score out of 100",
    min_value=0,
    max_value=100,
    step=1
)

writing_score = st.number_input(
    "Writing Score out of 100",
    min_value=0,
    max_value=100,
    step=1
)

# Predict button
if st.button("Predict your Maths Score"):

    # Collect input data
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    # Convert into DataFrame
    pred_df = data.get_data_as_data_frame()

    logging.info("Before Prediction")

    preict_pipeline=PredictPipeline()
    prediction=preict_pipeline.predict(pred_df)

    logging.info("After Prediction")

    st.success(f"The predicted Maths Score is: {prediction}")