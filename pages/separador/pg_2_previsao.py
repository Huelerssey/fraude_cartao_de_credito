import streamlit as st
from src.data_utility import carregar_dados


def previsao():
    st.markdown("<h1 style='text-align: center;'>📊 Modelo de Previsão de Fraude em Cartões de Crédito 📊</h1>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Bem-vindo à página de previsão de fraudes em cartões de crédito. Infelizmente, não é possível aplicar diretamente o modelo de machine learning desenvolvido para este conjunto de dados em um ambiente de produção. Permita-me explicar o motivo.")

    st.write("\n")
    st.write("O conjunto de dados que utilizamos passou por um processo de transformação chamado Análise de Componentes Principais (PCA). Esta técnica foi usada para preservar a privacidade e garantir o anonimato dos clientes. Abaixo está uma amostra dos dados após a transformação:")
    def color_columns(val):
        if val.name in [f'V{i}' for i in range(1,29)]:
            color = 'red'
        else:
            color = 'green'
        return ['background-color: %s' % color]*len(val)

    df = carregar_dados().head(5)
    st.markdown(df.style.apply(color_columns, axis=0).to_html(index=False), unsafe_allow_html=True)
    st.write("\n")

    st.write("Todas as colunas em vermelho eram características originais - como local da compra, formato da transação, titularidade do cartão, entre outros - que foram transformadas em um novo conjunto de características, rotuladas de V1 a V28. Infelizmente, as novas características não possuem um significado intuitivo, tornando impossível para você, o usuário fornecer essas informações.")
    st.write("Apesar dessas limitações, ainda somos capazes de usar este conjunto de dados para desenvolver e treinar modelos de machine learning eficazes para detectar fraudes. No entanto, a aplicação direta desses modelos em um ambiente de produção só pode ser feita com acesso aos dados bancários originais.")
