import streamlit as st
from streamlit_lottie import st_lottie
import json


def home():
    col1, col2 = st.columns(2)

    # >>animações<<

    # hello
    with open('animacoes/hello.json') as source:
        hello=json.load(source)
    
    # programing
    with open('animacoes/programing.json') as source:
        programing=json.load(source)
    
    # boas vindas ao projeto
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Boas vindas a apresentação do projeto de Detecção de Fraude")
    with col2:
        st_lottie(hello, height=400, width=300)
    
    # resumo do projeto
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Este é um projeto de ciência de dados utilizando um dataset público disponível na plataforma Kaggle para apresentar uma solução proposta pelo case da #DadosFera.")
    with col2:
        st_lottie(programing, height=400, width=300)
