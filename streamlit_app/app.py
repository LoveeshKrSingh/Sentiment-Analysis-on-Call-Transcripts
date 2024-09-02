import streamlit as st
from PIL import Image

st.set_page_config(page_title="Call Transcript Sentiment Analysis", page_icon=":speech_balloon:")

st.title("Call Transcript Sentiment Analysis")
st.write("Upload your call transcript files to analyze sentiment.")

uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file:
    st.write("Uploaded file: ", uploaded_file.name)
    # Display the uploaded transcript
    st.write("Transcript: ")
    st.text_area(uploaded_file.read().decode("utf-8"), height=300)