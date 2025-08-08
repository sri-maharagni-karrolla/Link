from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import random 
from transformers import pipeline


app = FastAPI()

df = pd.read_csv("C:\\Users\\hp\\Desktop\\Edutech\\edtech_adaptive_learning_dataset.csv")

class form_inp(BaseModel) :
    user_id : int
    topic : str
    time_spent : int
    quiz_score : int
    preference : str
    feedback : str
    rating : int 

@app.post("/submit")
def form_submit(data:form_inp) :
    global df
    new_data = pd.DataFrame([data.dict()])
    df = pd.concat([df,new_data],ignore_index = True)
    df.to_csv("C:\\Users\\hp\\Desktop\\Edutech\\edtech_adaptive_learning_dataset.csv")
    return {"Message":"Data Submited"}
@app.get("/get_recomend/{userid}")
def recomend(userid : int):
    user = df[df["user_id"]==userid]
    if user.empty :
        return {"message":"User Not Found"}
    visited_topics = user["topic"].unique().tolist()
    All_topics = df["topic"].unique().tolist()
    Notvisited = list(set(All_topics)-set(visited_topics))

    rec = random.sample(Notvisited,k = min(3,len(Notvisited)))
    return {"recomend":rec}

class feedback(BaseModel):
    feedback: str

@app.post("/feedback")
def feedback_analysis(fb: feedback):
    ml = pipeline("sentiment-analysis")
    res = ml(fb.feedback)
    return {"Feedback": res[0]}





generator = pipeline("text-generation", model="gpt2") 

class TopicRequest(BaseModel):
    topic: str

@app.post("/gen_qns")
def generate_questions(req: TopicRequest):
    topic = req.topic
    prompt = f"Generate 3 simple questions about {topic}:\n1."
    output = generator(prompt, max_length=200, num_return_sequences=1)
    text = output[0]["generated_text"]

    # Extract only the lines starting with number (1,2,3)
    lines = text.strip().split("\n")
    questions = [line.strip() for line in lines if line.strip() and line.strip()[0] in "123"]

    return {"questions": questions}

