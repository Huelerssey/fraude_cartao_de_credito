import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# função que otimiza o carregamento dos dados
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("dataset/creditcard.csv")
    return tabela

def storytelling():
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
    st.dataframe(carregar_dados().head(5), hide_index=True)
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
    st.write("O trecho de código abaixo é responsável por treinar e testar um modelo de inteligência artificial utilizando a acurácia como método de avaliação.")
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

    # Cria um cartão (figura) vazio
    fig, ax = plt.subplots(figsize=(4, 3))

    # Adiciona o texto do accuracy_formatted no cartão
    ax.text(0.5, 0.5, accuracy_formatted, ha='center', va='center', fontsize=24)

    # Remove os eixos e limites do gráfico
    ax.axis('off')

    # Exibe o resultado
    plt.show()
    """
    st.code(codigo2, language='python')
    st.image("imagens/4.png")
    st.write("O resultado obtido foi de 99,92% de acurácia. Isso significa que construímos um modelo de previsão perfeito, certo? Errado! A maioria das transações não são fraudulentas, então se o modelo simplesmente considerar que todas as novas transações não são fraudes, ele terá uma alta taxa de acertos. Percebe como isso afeta nosso resultado? Afinal, cada fraude não prevista representa um impacto financeiro negativo para a empresa.")
    st.write("E como podemos resolver esse problema? Existem duas soluções baseadas no mesmo princípio: tornar os dados proporcionais, ou seja, igualar o número de fraudes e não fraudes. No entanto, essa é uma tarefa complexa e delicada. Vou te ajudar a visualizar esses cenários a seguir:")
    st.write("Se optarmos por excluir a maioria das transações não fraudulentas, corremos o risco de ter os dados restantes agrupados de uma maneira que afete nossa análise. Por exemplo: se excluirmos aleatoriamente a maioria dos dados e restarem apenas transações de alto valor. Você concorda que nem toda fraude está associada a uma compra de alto valor? Nesse caso, se o modelo tentar prever uma nova compra com valor mediano, a probabilidade de não considerá-la como fraude será alta, resultando em prejuízos desnecessários.")
    st.write("Por outro lado, se apenas adicionarmos mais fraudes, corremos o risco de duplicar tanto um determinado dado que isso pode prejudicar a tomada de decisão do modelo. Por exemplo: suponha que exista uma compra de 50 EUR registrada em nossa base de dados atual e que tenha sido classificada como fraude. Ao adotar o método de aumentar a quantidade de fraudes para equilibrar a proporção, essa transação foi duplicada 200 mil vezes. A chance de o modelo de previsão considerar todas as novas transações de 50 EUR como fraudes será extremamente alta, o que está matematicamente correto, mas não reflete nossa realidade.")
    st.write("A ideia geral da solução está representada no gráfico abaixo, e será cuidadosamente implementada com base em conhecimentos sólidos de estatística e programação. Nosso objetivo é desenvolver um modelo capaz de identificar fraudes com alta precisão, levando em consideração as características e particularidades deste contexto bancário.")
    st.image("imagens/5.png")
    st.write("")

    st.header("6. Modelando uma inteligência artificial")
    st.write("Chegamos à parte mais empolgante do projeto, onde construímos a inteligência artificial responsável por detectar fraudes em cartões de crédito. Embora seja uma etapa técnica e complexa, vou explicar de forma simplificada como tudo funciona e compartilhar os resultados obtidos. Novamente, convido você a acessar meu GitHub, por meio deste [link](https://github.com/Huelerssey/fraude_cartao_de_credito), caso queira entender detalhadamente como essas inteligências artificiais foram modeladas, linha por linha de código.")
    st.write("Ao lidar com a problemática das fraudes, temos um desafio de classificação em mãos. Para enfrentá-lo, utilizamos três principais inteligências artificiais: Decision Tree, Random Forest e Extra Trees. Em seguida, modelamos a base de dados para contornar os problemas já explicados durante a análise exploratória, garantindo que cada inteligência artificial utilize essa base de dados ajustada. Por fim, avaliamos o desempenho de cada abordagem e de cada uma das inteligências artificiais. Use a seguinte legenda:")
    st.write("Inteligência artificial - Método de reajustar base de dados")
    
    # Lista de modelos e métodos de resampling
    lista_resultados = [
        {
            'modelo': 'Decision Tree',
            'metodo_resampling': 'Random Undersample',
            'matriz_confusao': [[75628, 9667], [16, 132]],
            'recall': 0.89
        },
        {
            'modelo': 'Decision Tree',
            'metodo_resampling': 'Undersample ClusterCentroid',
            'matriz_confusao': [[42256, 43039], [7, 141]],
            'recall': 0.95
        },
        {
            'modelo': 'Decision Tree',
            'metodo_resampling': 'Undersample NearMiss',
            'matriz_confusao': [[33992, 51303], [7, 141]],
            'recall': 0.95
        },
        {
            'modelo': 'Decision Tree',
            'metodo_resampling': 'Random Oversample',
            'matriz_confusao': [[84787, 508], [25, 123]],
            'recall': 0.83
        },
        {
            'modelo': 'Decision Tree',
            'metodo_resampling': 'Oversample SMOTE',
            'matriz_confusao': [[85142, 153], [39, 109]],
            'recall': 0.74
        },
        {
            'modelo': 'Decision Tree',
            'metodo_resampling': 'Oversample ADASYN',
            'matriz_confusao': [[85151, 144], [42, 106]],
            'recall': 0.72
        },
        {
            'modelo': 'Decision Tree',
            'metodo_resampling': 'Combined Over/Undersample',
            'matriz_confusao': [[85109, 186], [36, 112]],
            'recall': 0.76
        },
        {
            'modelo': 'Random Forest',
            'metodo_resampling': 'Random Undersample',
            'matriz_confusao': [[83647, 1648], [18, 130]],
            'recall': 0.88
        },
        {
            'modelo': 'Random Forest',
            'metodo_resampling': 'Undersample ClusterCentroid',
            'matriz_confusao': [[34241, 51054], [2, 146]],
            'recall': 0.99
        },
        {
            'modelo': 'Random Forest',
            'metodo_resampling': 'Undersample NearMiss',
            'matriz_confusao': [[69222, 16073], [8, 140]],
            'recall': 0.95
        },
        {
            'modelo': 'Random Forest',
            'metodo_resampling': 'Random Oversample',
            'matriz_confusao': [[85131, 164], [26, 122]],
            'recall': 0.82
        },
        {
            'modelo': 'Random Forest',
            'metodo_resampling': 'Oversample SMOTE',
            'matriz_confusao': [[85278, 17], [30, 118]],
            'recall': 0.80
        },
        {
            'modelo': 'Random Forest',
            'metodo_resampling': 'Oversample ADASYN',
            'matriz_confusao': [[85274, 21], [29, 119]],
            'recall': 0.80
        },
        {
            'modelo': 'Random Forest',
            'metodo_resampling': 'Combined Over/Undersample',
            'matriz_confusao': [[85268, 27], [27, 121]],
            'recall': 0.82
        },
        {
            'modelo': 'Extra Trees',
            'metodo_resampling': 'Random Undersample',
            'matriz_confusao': [[84320, 975], [22, 126]],
            'recall': 0.85
        },
        {
            'modelo': 'Extra Trees',
            'metodo_resampling': 'Undersample ClusterCentroid',
            'matriz_confusao': [[38421, 46874], [0, 148]],
            'recall': 1.00
        },
        {
            'modelo': 'Extra Trees',
            'metodo_resampling': 'Undersample NearMiss',
            'matriz_confusao': [[78545, 6750], [10, 138]],
            'recall': 0.93
        },
        {
            'modelo': 'Extra Trees',
            'metodo_resampling': 'Random Oversample',
            'matriz_confusao': [[85206, 89], [26, 122]],
            'recall': 0.82
        },
        {
            'modelo': 'Extra Trees',
            'metodo_resampling': 'Oversample SMOTE',
            'matriz_confusao': [[85281, 14], [29, 119]],
            'recall': 0.80
        },
        {
            'modelo': 'Extra Trees',
            'metodo_resampling': 'Oversample ADASYN',
            'matriz_confusao': [[85280, 15], [29, 119]],
            'recall': 0.80
        },
        {
            'modelo': 'Extra Trees',
            'metodo_resampling': 'Combined Over/Undersample',
            'matriz_confusao': [[85278, 17], [28, 120]],
            'recall': 0.81
        },
    ]

    # Opções disponíveis no seletor
    opcoes = [f"{resultado['modelo']} - {resultado['metodo_resampling']}" for resultado in lista_resultados]

    # Seletor de opções
    opcao_selecionada = st.selectbox("Selecione uma opção:", opcoes)

    # Encontrar o resultado correspondente à opção selecionada
    resultado_selecionado = None
    for resultado in lista_resultados:
        if f"{resultado['modelo']} - {resultado['metodo_resampling']}" == opcao_selecionada:
            resultado_selecionado = resultado
            break

    # Verificar se um resultado válido foi selecionado
    if resultado_selecionado is not None:
        # Dados da matriz de confusão
        matriz_confusao = resultado_selecionado['matriz_confusao']

        # Cores das fatias para cada gráfico
        cores_fatias1 = ['#00FF00', '#FF0000']
        cores_fatias2 = ['#FF0000', '#00FF00']

        # Legendas
        legenda1 = ['Errou - Modelo não classificou como Fraude', 'Acertou - Modelo classificou como Fraude']
        legenda2 = ['Acertou - Modelo não classificou como Fraude', 'Errou - Modelo classificou como Fraude']

        st.subheader("Tentando prever Dados que eram Fraude")
        # Gráfico dos dados que eram fraude
        plt.figure(figsize=(6, 6))
        plt.pie(matriz_confusao[1], colors=cores_fatias2, autopct='%1.1f%%', startangle=90)
        plt.legend(legenda1, loc='upper left', bbox_to_anchor=(0.80, 0.80), bbox_transform=plt.gcf().transFigure)
        plt.axis('equal')

        # Exibir o gráfico no Streamlit
        st.pyplot(plt)

        st.subheader("Tentando prever Dados que não eram Fraude")
        # Gráfico dos dados que não eram fraude
        plt.figure(figsize=(6, 6))
        plt.pie(matriz_confusao[0], colors=cores_fatias1, autopct='%1.1f%%', startangle=90)
        plt.legend(legenda2, loc='upper left', bbox_to_anchor=(0.80, 0.80), bbox_transform=plt.gcf().transFigure)
        plt.axis('equal')

        # Exibir o gráfico no Streamlit
        st.pyplot(plt)
    st.write("")

    st.header("7. Resultados")
    st.write("Chegamos ao momento de apresentar os resultados obtidos deste projeto de detecção de fraudes em cartões de crédito. Com base na aplicação das diferentes inteligências artificiais e na análise dos dados. Vamos começar respondendo a pergunta mais importante: 'Então afinal, os resultados obtidos nos gráficos a cima, são bons ou ruins ?' E a resposta é: Depende!")
    st.write("Para facilitar o entendimento, vamos utilizar exemplos práticos para ilustrar os resultados obtidos. A seguir, apresentamos três modelos aleatórios selecionados entre todos os utilizados para a demonstração.")
    st.write("")

    # modelo 1
    st.subheader("Decision Tree - Random Undersample")

    # Cria um DataFrame
    data1 = {'': ['O dado Não era Fraude', 'O dado Era Fraude'],
            'Modelo previu como: Não é Fraude': [75628, 16],
            'Modelo previu como: É Fraude': [9667, 132]}

    df1 = pd.DataFrame(data1)

    # Aplica a formatação condicional para colorir células específicas
    def highlight_value(val):
        if val == 75628 or val == 132:  # Valores para destacar em verde
            return 'background-color: green'
        elif val == 16 or val == 9667:  # Valores para destacar em vermelho
            return 'background-color: red'
        else:
            return ''

    # Exibe a tabela com a formatação condicional
    st.table(df1.style.applymap(highlight_value, subset=['Modelo previu como: Não é Fraude', 'Modelo previu como: É Fraude']))
    st.write("Neste modelo, observamos uma alta eficácia na classificação de transações fraudulentas. Das 148 totais, o modelo identificou corretamente 132 delas, o que representa uma ótima taxa de acerto. No entanto, qual o preço disso?")
    st.write("Ao analisar as transações que não eram fraudulentas, o modelo classificou 9667 delas como fraude. Esses falsos positivos resultam em clientes insatisfeitos com compras negadas, gerando um alto volume de contatos com o banco e exigindo um aumento no tamanho da equipe de atendimento ao cliente e toda a infraestrutura em volta disso. Se o custo de manter uma equipe maior ultrapassar muito a economia das fraudes previstas, a utilização desse modelo pode se tornar inviável para a empresa.")
    st.write("")

    # modelo 2
    st.subheader("Random Forest - Oversample SMOTE")

    # Cria um DataFrame
    data2 = {'': ['O dado Não era Fraude', 'O dado Era Fraude'],
            'Modelo previu como: Não é Fraude': [85278, 30],
            'Modelo previu como: É Fraude': [17, 118]}

    df2 = pd.DataFrame(data2)

    # Aplica a formatação condicional para colorir células específicas
    def highlight_value(val):
        if val == 85278 or val == 118:  # Valores para destacar em verde
            return 'background-color: green'
        elif val == 30 or val == 17:  # Valores para destacar em vermelho
            return 'background-color: red'
        else:
            return ''

    # Exibe a tabela com a formatação condicional
    st.table(df2.style.applymap(highlight_value, subset=['Modelo previu como: Não é Fraude', 'Modelo previu como: É Fraude']))
    st.write("Neste outro modelo, temos  o exato oposto, com foco na redução dos falsos positivos. Isso significa que o modelo é mais cauteloso na classificação de transações como fraudes, evitando assim o problema do alto volume de contatos com o banco. No entanto, essa redução de falsos positivos vem com o custo de uma diminuição na precisão na detecção de fraudes.")
    st.write("Observamos que, nesse modelo, o número de transações fraudulentas não previstas é quase o dobro do modelo anterior. Caso uma ou mais dessas 30 fraudes não detectadas sejam de alto valor, o impacto financeiro pode ser considerável. É importante ressaltar que mesmo com 16 fraudes não detectadas, o risco de prejuízo ainda existe, mas quanto maior o número de fraudes não identificadas, maior é a possibilidade de prejuízos.")
    st.write("")

    # modelo 3
    st.subheader("Extra Trees - Undersample ClusterCentroid")

    # Cria um DataFrame
    data3 = {'': ['O dado Não era Fraude', 'O dado Era Fraude'],
            'Modelo previu como: Não é Fraude': [38421, 0],
            'Modelo previu como: É Fraude': [46874, 148]}

    df3 = pd.DataFrame(data3)

    # Aplica a formatação condicional para colorir células específicas
    def highlight_value(val):
        if val == 38421 or val == 148 or val == 0:  # Valores para destacar em verde
            return 'background-color: green'
        elif val == 46874:  # Valores para destacar em vermelho
            return 'background-color: red'
        else:
            return ''

    # Exibe a tabela com a formatação condicional
    st.table(df3.style.applymap(highlight_value, subset=['Modelo previu como: Não é Fraude', 'Modelo previu como: É Fraude']))
    st.write("E se você está se perguntando se é possível atingir um modelo 'perfeito', aqui está o resultado. Essa inteligência artificial é capaz de prever 100% das fraudes, porém, o custo disso é classificar erroneamente transações que não são fraudes como fraude, 46 mil vezes.")
    st.write("")

    st.header("8. Considerações finais")
    st.write("Deu para perceber que é crucial encontrar um equilíbrio entre a quantidade de falsos positivos e falsos negativos nas previsões, certo? No entanto, é importante ressaltar que, decidir se o resultado do modelo é bom ou não, só depende da área de negócio ou empresa em questão, pois cada uma possui suas próprias necessidades e restrições.")
    st.write("Vale lembrar também que não é necessário usar apenas um modelo. Seria uma estratégia interessante por exemplo, agrupar as transações ocorridas em transações de alto, médio e pequeno porte. E utilizar um modelo específico para cada grupo. Assim, para transações de grande porte utilizar modelos mais precisos e conservadores e se caso o modelo erre, exista um time responsável por entrar em contato com o titular para verificar se a compra é mesmo verídica. Enquanto nas compras de pequeno porte, usar modelos mais flexíveis na detecção e em caso de falso positivo, dar a liberdado para o próprio usuário resolver o problema da compra bloqueada pelo aplicativo do banco sem precisar entrar em contato.")
    st.write("Além disso, é fundamental destacar a importância contínua da atualização e monitoramento dos modelos de detecção de fraudes, uma vez que os métodos utilizados pelos fraudadores estão em constante evolução.")
    st.write("Por fim, este projeto proporcionou uma experiência prática e aprofundada na área de detecção de fraudes em cartões de crédito, consolidando os conhecimentos adquiridos em estatística, programação e inteligência artificial.")
    st.write("")
    st.image("imagens/6.png")
