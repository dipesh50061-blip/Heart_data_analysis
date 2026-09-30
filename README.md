# Heart Disease Prediction & EDA

An end-to-end machine learning project for exploring heart disease data, performing exploratory data analysis (EDA), training classification models, and deploying a prediction application using Streamlit.

## Project Overview

This project analyzes a heart disease dataset and builds a machine learning classification pipeline to predict whether a patient is likely to have heart disease based on clinical features.

The project covers:

- Data exploration
- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature analysis
- Model training
- Model evaluation
- Model persistence using Joblib
- Prediction pipeline
- Streamlit application

> **Note:** This project is created for educational and machine learning demonstration purposes. It is not a medical diagnostic system.

## Dataset

The dataset contains the following features:

| Feature | Description |
|---|---|
| `age` | Age of the patient |
| `sex` | Sex of the patient |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol |
| `fbs` | Fasting blood sugar |
| `restecg` | Resting electrocardiographic results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of the peak exercise ST segment |
| `ca` | Number of major vessels |
| `thal` | Thalassemia |
| `target` | Heart disease target |

### Target

- `0` → No heart disease
- `1` → Heart disease

## Exploratory Data Analysis

The EDA process includes:

- Dataset inspection
- Data type analysis
- Missing value analysis
- Duplicate detection
- Duplicate removal
- Target distribution analysis
- Univariate analysis
- Bivariate analysis
- Correlation analysis
- Feature relationships
- Feature importance analysis

The original dataset contained **1,025 rows and 14 columns**.

Duplicate records were identified during data cleaning and removed before model training.

## Machine Learning

Three classification models were explored:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

### Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report
- ROC-AUC

### Model Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 80.33% | 80.00% | 84.85% | 82.35% |
| Decision Tree | 80.33% | 81.82% | 81.82% | 81.82% |
| Random Forest | 75.41% | 76.47% | 78.79% | 77.61% |

### Final Model

Logistic Regression was selected as the final model based on the evaluation performed during the modeling stage.

The final machine learning pipeline uses:

```text
StandardScaler
      ↓
Logistic Regression
```

The trained model is saved using Joblib at:

```text
models/heart_disease_model.pkl
```

## Prediction Pipeline

The prediction system loads the trained model and accepts the required patient features.

The prediction pipeline works as follows:

```text
User Input
    ↓
Pandas DataFrame
    ↓
Saved ML Pipeline
    ↓
StandardScaler
    ↓
Logistic Regression
    ↓
Prediction + Probability
```

The prediction function returns information such as:

```python
{
    "prediction": 1,
    "result": "Heart Disease Detected",
    "probability": 0.82
}
```

## Streamlit Application

The project includes a Streamlit web application that provides an interactive interface for entering patient information and obtaining a model prediction.

The application allows users to enter:

- Age
- Sex
- Chest pain type
- Resting blood pressure
- Cholesterol
- Fasting blood sugar
- Resting ECG
- Maximum heart rate
- Exercise-induced angina
- Oldpeak
- Slope
- Number of major vessels
- Thalassemia

The application then displays the model's prediction and estimated probability.

### Run the Application

```bash
python -m streamlit run app.py
```

## Project Structure

```text
Heart_data_analysis/
│
├── models/
│   └── heart_disease_model.pkl
│
├── notebooks/
│   ├── heart_disease_EDA.ipynb
│   └── 02_modeling.ipynb
│
├── src/
│   └── prediction.py
│
├── tests/
│   └── test_prediction.py
│
├── app.py
├── heart.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate into the Project

```bash
cd Heart_data_analysis
```

### 3. Create the Conda Environment

```bash
conda create -n heart-eda python=3.11
```

### 4. Activate the Environment

```bash
conda activate heart-eda
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python -m streamlit run app.py
```

## Requirements

The main libraries used in this project are:

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

The project uses:

```text
scikit-learn==1.6.1
```

The scikit-learn version is pinned to maintain compatibility with the trained model.

## Future Improvements

Possible future improvements include:

- Hyperparameter tuning
- Cross-validation
- Additional classification models
- ROC-AUC visualization
- Improved Streamlit UI
- Model explainability using SHAP
- FastAPI integration
- Dockerization
- Cloud deployment
- Automated testing
- CI/CD pipeline
- Model monitoring

## Disclaimer

This application is intended for educational and machine learning demonstration purposes only.

The predictions generated by this application should not be used for medical diagnosis, treatment, or clinical decision-making.

## Author

**Depesh Kumar**

**AI Engineer Intern**

## License

This project is available for educational and personal use.