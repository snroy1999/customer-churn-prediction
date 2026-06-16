import pickle
import pandas as pd

with open("models/churn_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

print("Customer Churn Model Loaded Successfully")