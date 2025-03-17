import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", 
                             json={'input': {'topic': input_text}})
    
    return response.json().get('output', {}).get('content', 'No content found.')

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", 
                             json={'input': {'topic': input_text}})

    return response.json().get('output', 'No output found.')

# Streamlit framework
st.title("AI Poetry and Essay Generator")
st.write("This is a simple web app that uses the Hugging Face Transformers library to generate poetry")
st.write("and essays based on user input.")

input_text1 = st.text_input("Write an essay on:")
input_text2 = st.text_input("Write a poem on:")

if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))
