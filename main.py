#Integrate openAI API code

import os
from constant import openai_key
from langchain.llms import OpenAI

import streamlit as st
os.environ["OPENAI_API_KEY"] = openai_key

#strealit framework

st.title("Lanchain demo with OpenAI")
input_text = st.text_input("Serach any topic you want")

#OPENAI LLMs

llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))