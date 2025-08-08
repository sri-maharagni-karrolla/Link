import streamlit as st
import requests

st.title("Iris Flower Species Prediction")
sl = st.sidebar.slider("Sepal_length", 0.0, 10.0, step=0.01)
sw = st.sidebar.slider("Sepal_width", 0.0, 10.0, step=0.01)
pl = st.sidebar.slider("Petal_length", 0.0, 10.0, step=0.01)
pw = st.sidebar.slider("Petal_width", 0.0, 10.0, step=0.01)


if st.button("Predict"):
    
    data = {
        "sepal_length": sl,
        "sepal_width": sw,
        "petal_length": pl,
        "petal_width": pw
    }

    res = requests.post("http://127.0.0.1:8000/prd", json=data)
    result = res.json()
    st.write(result["Predicted Species:"])