import streamlit as st
import google.generativeai as genai
st.title("SUBRAMANI")
genai.configure(api_key="AIzaSyC08vN5RCWso96-JAnaUbVa5YRYJSrPa3s")
text = st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("EXPLORE"):
    response = chat.send_message(text)
    st.write(response.text)
