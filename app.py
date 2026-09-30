import streamlit as st

from src.prediction import predict_heart_disease


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("❤️ Heart Disease Prediction")

st.write(
    "Enter the patient's information below "
    "to generate a machine learning prediction."
)


# -----------------------------
# Input Features
# -----------------------------

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=50
)

sex = st.selectbox(
    "Sex",
    [0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

cp = st.selectbox(
    "Chest Pain Type",
    [0, 1, 2, 3]
)

trestbps = st.number_input(
    "Resting Blood Pressure",
    min_value=50,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Cholesterol",
    min_value=50,
    max_value=700,
    value=200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

restecg = st.selectbox(
    "Resting ECG",
    [0, 1, 2]
)

thalach = st.number_input(
    "Maximum Heart Rate",
    min_value=50,
    max_value=250,
    value=150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope = st.selectbox(
    "Slope",
    [0, 1, 2]
)

ca = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thal",
    [0, 1, 2, 3]
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict", type="primary"):

    data = [
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]

    result = predict_heart_disease(data)

    st.subheader("Prediction Result")

    if result["prediction"] == 1:
        st.error(result["result"])
    else:
        st.success(result["result"])

    st.metric(
        "Prediction Probability",
        f"{result['probability']:.2%}"
    )

    st.info(
        "This application is for educational purposes "
        "and is not a medical diagnostic tool."
    )