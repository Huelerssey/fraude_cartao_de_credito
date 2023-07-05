import streamlit as st

# Função para exibir o notebook selecionado
def exibir_notebook(caminho_arquivo):
    # Abre o arquivo HTML e lê o conteúdo como uma string
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo_html = arquivo.read()

    # Exibe o notebook no Streamlit usando a função st.components.v1.html()
    st.components.v1.html(conteudo_html, width=700, height=1700, scrolling=True)

# Exemplo de uso
caminho_arquivo = 'notebook.html'
exibir_notebook(caminho_arquivo)
