from pathlib import Path
import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "heart_disease_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_heart_disease(data):

    columns = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal"
    ]

    input_data = pd.DataFrame(
        [data],
        columns=columns
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(
        input_data
    )[0][1]

    result = (
        "Heart Disease Detected"
        if prediction == 1
        else "No Heart Disease Detected"
    )

    return {
        "prediction": int(prediction),
        "result": result,
        "probability": float(probability)
    }