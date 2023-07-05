import json
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


# configurações da pagina
st.set_page_config(
    page_title='Detecção de Fraude',
    page_icon='💳',
    # layout='wide'
)

# estilos de css
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# menu de seleção
opcao_selecionada = option_menu(
    menu_title=None,
    options=['Home', 'Notebook'],
    icons=['house-door', 'journal-code'],
    default_index=0,
    orientation='horizontal',
)

# Renderizar conteúdo com base na opção selecionada
if opcao_selecionada == 'Home':

    col1, col2 = st.columns(2)

    # >>animações<<

    # hello
    with open('hello.json') as source:
        hello=json.load(source)
    with open('programing.json') as source:
        programing=json.load(source)
    
    # boas vindas ao projeto
    with col2:
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
        st.subheader("Boas vindas ao projeto Detecção de Fraude")
    with col1:
        st_lottie(hello, height=400, width=300)
    
    # resumo do projeto
    with col2:
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
        st.subheader("Este é um projeto de ciência de dados utilizando um dataset público disponível na plataforma Kaggle para realizar análise e previsão de fraudes em cartões de crédito.")
    with col1:
        st_lottie(programing, height=400, width=300)

# renderiza a opção do notebook
if opcao_selecionada == 'Notebook':

    # tabela usada para exibir algumas funções na tela
    tabela = pd.read_csv('dataset/creditcard.csv')

    st.title("Notebook do Projeto")
    st.write("")

    st.header("1. Introdução")
    st.write("Bem-vindo ao projeto de detecção de fraudes em cartões de crédito! Aqui, você vai me acompanhar em uma jornada completa, explorando todos os aspectos que envolvem desde a obtenção dos dados até o compartilhamento dos resultados. Ao longo deste storytelling, vamos executar as etapas de extração, limpeza e transformação dos dados (ELT), mergulhar em técnicas de modelagem estatística e machine learning, e por fim, apresentar os insights e descobertas que nos ajudarão a combater efetivamente as fraudes nesse cenário.")
    st.image("imagens/1.png")
    st.write("")

    st.header("2. Obtenção dos dados")
    st.write("Na fase de obtenção dos dados, recorri à plataforma Kaggle, uma fonte confiável de conjuntos de dados reais para cientistas de dados. Para este projeto, utilizei dados fornecidos por uma instituição financeira europeia, disponíveis neste [link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). Esses dados representam transações de cartões de crédito e são essenciais para o desenvolvimento da análise e detecção de fraudes.")
    st.write("")

    st.header("3. Entendimento da área/negócio")
    st.write("Vamos começar entendendo a base de dados, aqui está uma tabela com as 5 primeiras linhas do nosso dataset.")
    st.dataframe(tabela.head(5), hide_index=True)
    st.write("• Coluna 'Time' (tempo): contém os segundos decorridos entre cada transação e a primeira transação.")
    st.write("• Coluna 'Amount' (valor): contém o valor da transação.")
    st.write("• Colunas 'V1, V2...V28' (caracteristicas): são as caracteristicas da transação que passaram por um processo de PCA, ou seja, os dados foram transformados de maneira que não seja possível indetificar o dono real da transação, para garantir a confidencialidade.")
    st.write("• Coluna 'Class' (classe): é a variável de resposta onde toda vez que o valor for 1, a transação é uma fraude e quando for 0, significa que a transação não é fraudolenta.")
    st.write("Então, através desses dados (Tempo, Valor e Caracteristicas), vamos desenvolver um modelo que seja capaz de prever se uma transação é ou não fraudolenta.")
    st.write("")

    st.header("4. Limpeza e tratamento dos dados")
    st.write("")

    st.header("5. Análise exploratória de dados")
    st.write("")

    st.header("6. Modelando uma inteligência artificial")
    st.write("")

    st.header("7. Resultados e considerações finais")
    st.write("")