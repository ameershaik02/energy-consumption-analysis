import joblib

model = joblib.load("model.pkl")

voltage = float(input("Enter Voltage: "))
prediction = model.predict([[voltage]])

print("Predicted Energy Consumption:", prediction[0])