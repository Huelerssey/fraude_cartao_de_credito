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
    st.image("imagens/2.png")
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
    st.write("Começando com a visualisação estatística da base de dados:")
    codigo1 = """
    print(tabela.info())
    RangeIndex: 284807 entries, 0 to 284806
    Data columns (total 31 columns):
    #   Column  Non-Null Count   Dtype
    ---  ------  --------------   -----
    0   Time    284807 non-null  float64
    1   V1      284807 non-null  float64
    2   V2      284807 non-null  float64
    3   V3      284807 non-null  float64
    4   V4      284807 non-null  float64
    5   V5      284807 non-null  float64
    6   V6      284807 non-null  float64
    7   V7      284807 non-null  float64
    8   V8      284807 non-null  float64
    9   V9      284807 non-null  float64
    10  V10     284807 non-null  float64
    11  V11     284807 non-null  float64
    12  V12     284807 non-null  float64
    13  V13     284807 non-null  float64
    14  V14     284807 non-null  float64
    15  V15     284807 non-null  float64
    16  V16     284807 non-null  float64
    17  V17     284807 non-null  float64
    18  V18     284807 non-null  float64
    19  V19     284807 non-null  float64
    20  V20     284807 non-null  float64
    21  V21     284807 non-null  float64
    22  V22     284807 non-null  float64
    23  V23     284807 non-null  float64
    24  V24     284807 non-null  float64
    25  V25     284807 non-null  float64
    26  V26     284807 non-null  float64
    27  V27     284807 non-null  float64
    28  V28     284807 non-null  float64
    29  Amount  284807 non-null  float64
    30  Class   284807 non-null  int64
    dtypes: float64(30), int64(1)
    """
    st.code(codigo1, language='python')
    st.write("Ao analisar o código, é possível constatar que a base de dados inicial está uniforme, o que é algo relativamente raro e extremamente positivo. Essa uniformidade nos dados economiza um tempo valioso durante as etapas de pré-processamento e limpeza, permitindo um foco maior na análise e detecção de padrões e fraudes.")
    st.write("")

    st.header("5. Análise exploratória de dados")
    st.write("Nesta etapa, aplicarei meus conhecimentos em estatística e programação para preparar os dados e torná-los prontos para serem utilizados em um modelo de previsão. Como este é um projeto de portfólio, vou compartilhar a parte mais visual e explicativa do processo. Caso tenha interesse, você pode acessar o código-fonte completo da aplicação no meu GitHub, disponível neste [link](https://github.com/Huelerssey/fraude_cartao_de_credito).")
    st.write("Vamos iniciar exibindo um gráfico que apresenta a porcentagem de transações fraudulentas em nossa base de dados:")
    st.image("imagens/3.png")
    st.write("É evidente que há uma porcentagem mínima de fraudes, o que impacta diretamente na maneira como avaliaremos nosso modelo de machine learning e nada melhor do que um exemplo prático para demonstrar isso.")
    st.write("O trecho de código abaixo é responsável por treinar e testar um modelo de inteligência artificial utilizando a acurácia como método de avaliação. O resultado foi de 99.92%, então isso quer dizer que acabamos de construir um modelo de previsão perfeito, certo? Errado!")
    codigo2 = """
    # definindo dados de treino e de teste
    y = tabela['Class']
    x = tabela.drop('Class', axis=1)

    # dividindo a base entre treino e teste
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

    # criando uma IA
    clf = tree.DecisionTreeClassifier(random_state=42)

    # treina a IA
    clf = clf.fit(x_treino, y_treino)

    # previsão da IA
    y_pred = clf.predict(x_teste)

    # Avaliando a IA
    accuracy = accuracy_score(y_teste, y_pred)
    accuracy_percent = accuracy * 100
    accuracy_formatted = f"{accuracy_percent:.2f}%"
    print(accuracy_formatted)
    """
    st.code(codigo2, language='python')
    st.write("A maioria das transações não são fraudolentas, então basta que o modelo considere que todos as novas transações que ele tenta prever também não são, assim ele terá uma alta taxa de acerto. Percebe como isso acaba afetando o nosso resultado ? Afinal, a cada fraude não prevista, isso representa um impacto financeiro negativo para a empresa.")
    st.write("")

    st.header("6. Modelando uma inteligência artificial")
    st.write("")

    st.header("7. Resultados e considerações finais")
    st.write("")