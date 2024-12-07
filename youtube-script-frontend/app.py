import streamlit as st
import requests

st.title("YouTube Script Writing Assistant")

# User inputs
topic = st.text_input("Enter the video topic:")
tone = st.text_input("Select the tone:")
audience = st.text_input("Describe your target audience:")
format = st.text_input("Choose the script format:")

if st.button("Generate Script"):
    # Call the FastAPI backend
    backend_url = "http://localhost:8000/generate-script/"
    payload = {
        "topic": topic,
        "tone": tone,
        "audience": audience,
        "format": format,
    }
    response = requests.post(backend_url, json=payload)
    if response.status_code == 200:
        st.subheader("Generated Script:")
        st.write(response.json()["script"])
    else:
        st.error("Error generating script. Please try again.")
