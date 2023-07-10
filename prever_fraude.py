import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from imblearn.under_sampling import ClusterCentroids
from sklearn.cluster import MiniBatchKMeans


# dataframe 
tabela = pd.read_csv('dataset/creditcard.csv')

# verifica os tipos de dados
# print(tabela.info())
# RangeIndex: 284807 entries, 0 to 284806
# Data columns (total 31 columns):
#  #   Column  Non-Null Count   Dtype
# ---  ------  --------------   -----
#  0   Time    284807 non-null  float64
#  1   V1      284807 non-null  float64
#  2   V2      284807 non-null  float64
#  3   V3      284807 non-null  float64
#  4   V4      284807 non-null  float64
#  5   V5      284807 non-null  float64
#  6   V6      284807 non-null  float64
#  7   V7      284807 non-null  float64
#  8   V8      284807 non-null  float64
#  9   V9      284807 non-null  float64
#  10  V10     284807 non-null  float64
#  11  V11     284807 non-null  float64
#  12  V12     284807 non-null  float64
#  13  V13     284807 non-null  float64
#  14  V14     284807 non-null  float64
#  15  V15     284807 non-null  float64
#  16  V16     284807 non-null  float64
#  17  V17     284807 non-null  float64
#  18  V18     284807 non-null  float64
#  19  V19     284807 non-null  float64
#  20  V20     284807 non-null  float64
#  21  V21     284807 non-null  float64
#  22  V22     284807 non-null  float64
#  23  V23     284807 non-null  float64
#  24  V24     284807 non-null  float64
#  25  V25     284807 non-null  float64
#  26  V26     284807 non-null  float64
#  27  V27     284807 non-null  float64
#  28  V28     284807 non-null  float64
#  29  Amount  284807 non-null  float64
#  30  Class   284807 non-null  int64
# dtypes: float64(30), int64(1)

# quantidade de fraudes
# print(tabela.Class.value_counts())
# Class
# 0    284315
# 1       492

# # porcentagem de fraudes
# labels = ['Não fraudolenta', 'Fraude']  # Rótulos para as fatias do gráfico
# sizes = [99.8, 0.2]  # Valores correspondentes às fatias

# # Plotagem do gráfico de pizza
# plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90)

# # Exibição do gráfico
# plt.show()

# -- IA para avaliação com accuracy -- #

# # definindo dados de treino e de teste
# y = tabela['Class']
# x = tabela.drop('Class', axis=1)

# # dividindo a base entre treino e teste
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# # criando uma IA
# clf = tree.DecisionTreeClassifier(random_state=42)

# # treina a IA
# clf = clf.fit(x_treino, y_treino)

# # previsão da IA
# y_pred = clf.predict(x_teste)

# # Avaliando a IA
# accuracy = accuracy_score(y_teste, y_pred)
# accuracy_percent = accuracy * 100
# accuracy_formatted = f"{accuracy_percent:.2f}%"

# # Cria um cartão (figura) vazio
# fig, ax = plt.subplots(figsize=(4, 3))

# # Adiciona o texto do accuracy_formatted no cartão
# ax.text(0.5, 0.5, accuracy_formatted, ha='center', va='center', fontsize=24)

# # Remove os eixos e limites do gráfico
# ax.axis('off')

# # Exibe o cartão
# plt.show()

# -- IA para avaliação com accuracy -- #

# resolvemos o problema da base desbalanceada com randomundersample da biblioteca imbalanced-learn

# definindo dados de treino e de teste
y = tabela['Class']
x = tabela.drop('Class', axis=1)

# definindo o modelo para ajustar a proporção da base
cc = ClusterCentroids(
    estimator=MiniBatchKMeans(n_init=1, random_state=0), random_state=42
)

# treinando o modelo
x_res, y_res = cc.fit_resample(x, y)

# resultado
print('Base de dados reorganizada %s' % (y_res.value_counts()))

# # plotar um gráfico com a nova base organizada
# labels = ['Não fraudolenta', 'Fraude']  # Rótulos para as fatias do gráfico
# sizes = [492, 492]  # Valores correspondentes às fatias

# # Plotagem do gráfico de pizza
# plt.pie(sizes, labels=labels, startangle=90)

# # Exibição do gráfico
# plt.show()

