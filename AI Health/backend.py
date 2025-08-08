from fastapi import FastAPI
from pydantic import BaseModel
from llm_response import generate_health_info,analyse_sentiment

app = FastAPI()

class Patientdata(BaseModel):
    Name : str
    Age : int
    Weight : float
    history : str
    symptoms : str

@app.post('/predict')
def prediction(data:Patientdata):
    datas = data.dict()
    generated_res = generate_health_info(datas)

    sentiment_res = analyse_sentiment(data.history + " " + data.symptoms )
    
    return 
    {
        "Ai Response":generated_res,
        "conditional Status":sentiment_res
    }


    