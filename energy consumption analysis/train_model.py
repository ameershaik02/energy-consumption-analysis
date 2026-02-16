import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data using pandas (small sample for ML)
df = pd.read_csv("data/energy.csv", sep=';', low_memory=False)
df = df.dropna()

df["Voltage"] = df["Voltage"].astype(float)
df["Global_active_power"] = df["Global_active_power"].astype(float)

X = df[["Voltage"]]
y = df["Global_active_power"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Model trained and saved!")