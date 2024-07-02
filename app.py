# Databricks notebook source
import streamlit as st
#from langchain.llms import HuggingFaceHub
from langchain_community.llms import HuggingFaceHub
import os
from dotenv import load_dotenv
from huggingface_hub import login
load_dotenv()
#from huggingface_hub import login
#login("HUGGINGFACEHUB_API_TOKEN")

#os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('HUGGINGFACEHUB_API_TOKEN')
huggingface_api_key  = os.getenv('HUGGINGFACEHUB_API_TOKEN')


st.set_page_config(page_title='LangChain Demo', page_icon=':robot:')
st.header('LangChain Demo')

#user input 
def get_text():
    input_text = st.text_input("You: ", value="input")
    return input_text

def load_answer(question):
    llm = HuggingFaceHub(repo_id = "google/flan-t5-large")
    answer=llm.invoke(question)
    return answer

user_input = get_text()
response = load_answer(user_input)

submit = st.button("Generate")


if submit:
    #st.text_area("Answer: ", value=response, height=50)
    st.write(response)