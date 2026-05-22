import streamlit as st
import requests

st.title("ML Prediction App")

f1 = st.number_input("age")
f2 = st.number_input("hours_per_week")

if st.button("Predict"):

    r = requests.post(
        "http://127.0.0.1:8000/predict",
        params={
            "age": f1,
            "hours_per_week": f2,
        }
    )

    st.write(r.text)