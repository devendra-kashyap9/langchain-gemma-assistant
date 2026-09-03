import os
from dotenv import load_dotenv

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


## This function will load all the variable from .env file and will make them available
## os.environ directory (env_variablea)
load_dotenv()

## for langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

## Prompt template
prompt = ChatPromptTemplate(
    [
        ('system', 'You are a helpful assistant please provide the solutions to the problem asked'),
        ('user', 'Question:{question}')
    ]
)

## streamlit Framewrok
st.title("Langchain demo with Gemma Model")
input_text = st.text_input("What do you have in mind?")

## Ollama Llama2 model
llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write((chain.invoke({'question':input_text})))