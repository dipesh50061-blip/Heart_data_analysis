from src.prediction import predict_heart_disease


sample_data = [
    55,     # age
    1,      # sex
    1,      # cp
    140,    # trestbps
    250,    # chol
    0,      # fbs
    1,      # restecg
    150,    # thalach
    0,      # exang
    1.0,    # oldpeak
    1,      # slope
    0,      # ca
    2       # thal
]


result = predict_heart_disease(sample_data)

print(result)