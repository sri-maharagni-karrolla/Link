import streamlit as st 
import requests
import google.generativeai as genai
genai.configure(api_key="AIzaSyCBqWS8IZ0wb9Jmp9TCm7to1wni3-c2XTM")
model=genai.GenerativeModel(model_name="gemini-2.0-flash")

st.title("📚Edutech Learning Platform")
selection=st.sidebar.selectbox("Choose the page",["Submit Learning Data","Recommendation","Feedback","chat tutor"])

if selection == "Submit Learning Data":
    st.header("Submit Learning form ")
    with st.form("submit form"):
        id=st.number_input("Enter user_id")
        topic=st.selectbox("Topic",["Algebra","Trigonometry","probability","Statistics","Calculus","Functions","Limits","Geometry","Derivatives","Linear Equations"])
        tp=st.slider("Enter time spent",1,100)
        qs=st.slider("Enter quiz score",0,100)
        pref=st.selectbox("Preference",["Visual","Text","Audio","interactive"])
        fb=st.text_area("Feedback")
        rate=st.slider("Ratings",0,5)

        sub=st.form_submit_button("Submit")
        if sub:
            data={
                "user_id":id,
                "topic":topic,
                "time_spent":tp,
                "quiz_score":qs,
                "preference":pref,
                "feedback":fb,
                "rating":rate
            }
            res=requests.post("http://127.0.0.1:8000/submit",json=data)
            st.success(res.json()["Message"])

elif(selection=="Feedback"):
    st.header("Feedback Sentiment Analysis")
    feedback=st.text_area("Feedback: ")
    if st.button("submit feedback"):
        res=requests.post("http://127.0.0.1:8000/feedback",json={"feedback":feedback})
        st.write(res.json()["Feedback"])

elif(selection=="chat tutor"):
    st.header("🤖 AI Tutor ChatBot")
    prmt=st.text_input("Ask Your Doubts : ")
    chat=model.start_chat(history=[])
    if st.button("Clear the Doubts"):
        res=chat.send_message(prmt)
        st.write("Tutor Response")
        st.write(res.text)

elif(selection == "Recommendation"):
    userid = st.number_input("Enter the User Id", min_value=1, step=1)
    if st.button("Recomend"):
        res = requests.get(f"http://127.0.0.1:8000/get_recomend?userid={userid}")
        response = res.json()
        st.write("Recommended Topics !")
        st.write(response["recomend"])

        selected_topic = st.selectbox("Choose one topic to generate questions:", response["recomend"])
        if st.button("Generate Questions"):
            gen_res = requests.post("http://127.0.0.1:8000/gen_qns", json={"topic": selected_topic})
            qns = gen_res.json()
            st.subheader("Generated Questions:")
            for q in qns["questions"]:
                st.write("➤", q)
