from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load trained model
ml = joblib.load("C:/Users/hp/Desktop/Python/demo_iriss.pkl")

# Input format for POST /prd
class IrisInput(BaseModel):
    septal_length: float
    septal_width: float
    petal_length: float
    petal_width: float

# GET endpoint
@app.get("/prd")
def read_load():
    return {"message": "Welcome to the Iris flower species prediction API"}

# POST endpoint
@app.post("/prd")
def predict_species(data: IrisInput):
    spec_cls = ["setosa", "versicolor", "virginica"]
    input_data = [[
        data.septal_length,
        data.septal_width,
        data.petal_length,
        data.petal_width
    ]]
    prediction = ml.predict(input_data)
    return {"predicted_species": spec_cls[int(prediction[0])]}
