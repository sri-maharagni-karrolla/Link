import google.generativeai as genai
from transformers import pipeline

genai.configure(api_key = "AIzaSyDsMc_ZpUoL8SaURXuXTZDJdmxDaOQKWoU")
model = genai.GenerativeModel("gemini-2.0-flash")

sen_model = pipeline("sentiment-analysis")

def generate_health_info(patient_info:dict):
    prompt = f"""
    Now you are my health assistant
    Analyse following patient info:

    Name : {patient_info['name']} ,
    Age : {patient_info['Age']} ,
    Weight : {patient_info['weight']} ,
    Medical History : {patient_info['history']} ,
    Symptoms : {patient_info['symptoms']}

    provide :
    1.A detailed analysis of health pattern ,
    2.Potential risk
    3.Give a personalized recommendations for preventing this risk 
    4.Best drug to cure this which is risk free .
    """

    response = model.generate_content(prompt)

    return response    

def analyse_sentiment(text):
    sentiment=sen_model(text)
    return sentiment 


