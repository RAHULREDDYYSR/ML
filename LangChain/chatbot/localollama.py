from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv('../.env')

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. please response to the user queries"),
        ("user","Question:{question}")
    ]
)


st.title("Langchain with ollama API")
input_text = st.text_input("Search the topic you want:")

llm = Ollama(model="gemma3:1b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))