from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "ML API Running"}

@app.post("/predict")
def predict(
    age: int,
    hours_per_week: int
):
    data = pd.DataFrame([[
    age,
    hours_per_week
]], columns=[
    "age",
    "hours-per-week"
])

    prediction = model.predict(data)

    return {"prediction": str(prediction[0])}