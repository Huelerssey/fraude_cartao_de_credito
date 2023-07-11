import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from imblearn.under_sampling import ClusterCentroids
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import confusion_matrix, recall_score
from imblearn.under_sampling import NearMiss
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
from imblearn.combine import SMOTEENN


# -> CARREGANDO DATASET

# dataframe 
tabela = pd.read_csv('dataset/creditcard.csv')

# -> DATACLEANING

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

# -> ANÁLISE EXPLORATÓRIA

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
# cm = confusion_matrix(y_teste, y_pred)
# rs = recall_score(y_teste, y_pred)
# print(f'Matriz de confusão:\n {cm} \nRecall: {rs:.2f}%')

#resultado
# Matriz de confusão:
#  [[85264    31]
#  [   39   109]]
# Recall: 0.74%

# # Cria um cartão (figura) vazio
# fig, ax = plt.subplots(figsize=(4, 3))

# # Adiciona o texto do accuracy_formatted no cartão
# ax.text(0.5, 0.5, accuracy_formatted, ha='center', va='center', fontsize=24)

# # Remove os eixos e limites do gráfico
# ax.axis('off')

# # Exibe o cartão
# plt.show()

# -- IA para avaliação com accuracy -- #

# # plotar um gráfico com a nova base organizada
# labels = ['Não fraudolenta', 'Fraude']  # Rótulos para as fatias do gráfico
# sizes = [492, 492]  # Valores correspondentes às fatias

# # Plotagem do gráfico de pizza
# plt.pie(sizes, labels=labels, startangle=90)

# # Exibição do gráfico
# plt.show()

# -> MODELANDO ALGUNS ALGORITIMOS DE MACHINE LEARNING

# -- IA para avaliação com randon undersample -- #

# # definindo dados de treino e de teste
# y = tabela['Class']
# x = tabela.drop('Class', axis=1)

# # dividindo a base entre treino e teste
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# # # definindo o modelo para ajustar a proporção da base
# rus = RandomUnderSampler(random_state=42)

# # # ajustando base de treino
# x_res, y_res = rus.fit_resample(x_treino, y_treino)

# # criando uma IA
# clfrus = tree.DecisionTreeClassifier(random_state=42)

# # treinando uma iA
# clfrus = clfrus.fit(x_res, y_res)

# # previsão da IA
# y_predrus = clfrus.predict(x_teste)

# # avaliando a IA
# cm_rus = confusion_matrix(y_teste, y_predrus)
# rs_rus = recall_score(y_teste, y_predrus)
# print(f'Matriz de confusão:\n {cm_rus} \nRecall: {rs_rus:.2f}%')

# resultado
# Matriz de confusão:
#  [[75628  9667]
#  [   16   132]]
# Recall: 0.89%

# -- IA para avaliação com randon undersample -- #

# -- IA para avaliação com undersample ClusterCentroid -- #

# # definindo dados de treino e de teste
# y = tabela['Class']
# x = tabela.drop('Class', axis=1)

# # dividindo a base entre treino e teste
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# # definindo o modelo para ajustar a proporção da base
# cc = ClusterCentroids(
#     estimator=MiniBatchKMeans(n_init=1, random_state=0), random_state=42
# )

# # ajustando base de treino
# x_res, y_res = cc.fit_resample(x_treino, y_treino)

# # criando uma IA
# clfcc = tree.DecisionTreeClassifier(random_state=42)

# # treinando uma iA
# clfcc = clfcc.fit(x_res, y_res)

# # previsão da IA
# y_predcc = clfcc.predict(x_teste)

# # avaliando a IA
# cm_cc = confusion_matrix(y_teste, y_predcc)
# rs_cc = recall_score(y_teste, y_predcc)
# print(f'Matriz de confusão:\n {cm_cc} \nRecall: {rs_cc:.2f}%')

# resultado
# Matriz de confusão:
#  [[42256 43039]
#  [    7   141]]
# Recall: 0.95%

# -- IA para avaliação com undersample ClusterCentroid-- #

# -- IA para avaliação com undersample NearMiss-- #

# # definindo dados de treino e de teste
# y = tabela['Class']
# x = tabela.drop('Class', axis=1)

# # dividindo a base entre treino e teste
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# # definindo o modelo para ajustar a proporção da base
# nm = NearMiss()

# # ajustando base de treino
# x_res, y_res = nm.fit_resample(x_treino, y_treino)

# # criando uma IA
# clfnm = tree.DecisionTreeClassifier(random_state=42)

# # treinando uma iA
# clfnm = clfnm.fit(x_res, y_res)

# # previsão da IA
# y_prednm = clfnm.predict(x_teste)

# # avaliando a IA 
# cm_nm = confusion_matrix(y_teste, y_prednm)
# rs_nm = recall_score(y_teste, y_prednm)
# print(f'Matriz de confusão:\n {cm_nm} \nRecall: {rs_nm:.2f}%')

#resultado
# Matriz de confusão:
#  [[33992 51303]
#  [    7   141]]
# Recall: 0.95%

# -- IA para avaliação com undersample NearMiss -- #

# -- IA para avaliação com randon oversample -- #

# # definindo dados de treino e de teste
# y = tabela['Class']
# x = tabela.drop('Class', axis=1)

# # dividindo a base entre treino e teste
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# # definindo o modelo para ajustar a proporção da base
# ros = RandomOverSampler(random_state=42, shrinkage=0.7)

# # ajustando base de treino
# x_res, y_res = ros.fit_resample(x_treino, y_treino)

# # criando uma IA
# clfros = tree.DecisionTreeClassifier(random_state=42)

# # treinando uma iA
# clfros = clfros.fit(x_res, y_res)

# # previsão da IA
# y_predros = clfros.predict(x_teste)

# # avaliando a IA 
# cm_ros = confusion_matrix(y_teste, y_predros)
# rs_ros = recall_score(y_teste, y_predros)
# print(f'Matriz de confusão:\n {cm_ros} \nRecall: {rs_ros:.2f}%')

# resultado
# Matriz de confusão:
#  [[84787   508]
#  [   25   123]]
# Recall: 0.83%

# -- IA para avaliação com randon oversample -- #

# -- IA para avaliação com oversample SMOTE -- #

# # definindo dados de treino e de teste
# y = tabela['Class']
# x = tabela.drop('Class', axis=1)

# # dividindo a base entre treino e teste
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# # definindo o modelo para ajustar a proporção da base
# sm = SMOTE(random_state=42)

# # ajustando base de treino
# x_res, y_res = sm.fit_resample(x_treino, y_treino)

# # criando uma IA
# clfsm = tree.DecisionTreeClassifier(random_state=42)

# # treinando uma iA
# clfsm = clfsm.fit(x_res, y_res)

# # previsão da IA
# y_predsm = clfsm.predict(x_teste)

# # avaliando a IA 
# cm_sm = confusion_matrix(y_teste, y_predsm)
# rs_sm = recall_score(y_teste, y_predsm)
# print(f'Matriz de confusão:\n {cm_sm} \nRecall: {rs_sm:.2f}%')

# resultado
# Matriz de confusão:
#  [[85142   153]
#  [   39   109]]
# Recall: 0.74%

# -- IA para avaliação com oversample SMOTE -- #

# -- IA para avaliação com oversample ADASYN -- #

# # definindo dados de treino e de teste
# y = tabela['Class']
# x = tabela.drop('Class', axis=1)

# # dividindo a base entre treino e teste
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# # definindo o modelo para ajustar a proporção da base
# ada = ADASYN(random_state=42)

# # ajustando base de treino
# x_res, y_res = ada.fit_resample(x_treino, y_treino)

# # criando uma IA
# clfada = tree.DecisionTreeClassifier(random_state=42)

# # treinando uma iA
# clfada = clfada.fit(x_res, y_res)

# # previsão da IA
# y_predada = clfada.predict(x_teste)

# # avaliando a IA 
# cm_ada = confusion_matrix(y_teste, y_predada)
# rs_ada = recall_score(y_teste, y_predada)
# print(f'Matriz de confusão:\n {cm_ada} \nRecall: {rs_ada:.2f}%')

# resultado
# Matriz de confusão:
#  [[85151   144]
#  [   42   106]]
# Recall: 0.72%

# -- IA para avaliação com oversample ADASYN -- #

# -- IA para avaliação combinando over com undersample SMOTEENN -- #

# # definindo dados de treino e de teste
# y = tabela['Class']
# x = tabela.drop('Class', axis=1)

# # dividindo a base entre treino e teste
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# # definindo o modelo para ajustar a proporção da base
# sme = SMOTEENN(random_state=42)

# # ajustando base de treino
# x_res, y_res = sme.fit_resample(x_treino, y_treino)

# # criando uma IA
# clfsme = tree.DecisionTreeClassifier(random_state=42)

# # treinando uma iA
# clfsme = clfsme.fit(x_res, y_res)

# # previsão da IA
# y_predsme = clfsme.predict(x_teste)

# # avaliando a IA 
# cm_sme = confusion_matrix(y_teste, y_predsme)
# rs_sme = recall_score(y_teste, y_predsme)
# print(f'Matriz de confusão:\n {cm_sme} \nRecall: {rs_sme:.2f}%')

# resultado
# Matriz de confusão:
#  [[85109   186]
#  [   36   112]]
# Recall: 0.76%

# -- IA para avaliação combinando over com undersample SMOTEENN -- #

# definindo dados de treino e de teste
y = tabela['Class']
x = tabela.drop('Class', axis=1)

# dividindo a base entre treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# função para avaliar modelos
def avaliar_modelos(modelos, x_treino, y_treino, x_teste, y_teste):
    resultados = {}
    
    for nome, modelo in modelos.items():
        if nome == 'Random Undersample':
            rus = RandomUnderSampler(random_state=42)
            x_res, y_res = rus.fit_resample(x_treino, y_treino)
        elif nome == 'Undersample ClusterCentroid':
            cc = ClusterCentroids(estimator=MiniBatchKMeans(n_init=1, random_state=0), random_state=42)
            x_res, y_res = cc.fit_resample(x_treino, y_treino)
        elif nome == 'Undersample NearMiss':
            nm = NearMiss()
            x_res, y_res = nm.fit_resample(x_treino, y_treino)
        elif nome == 'Random Oversample':
            ros = RandomOverSampler(random_state=42, shrinkage=0.7)
            x_res, y_res = ros.fit_resample(x_treino, y_treino)
        elif nome == 'Oversample SMOTE':
            sm = SMOTE(random_state=42)
            x_res, y_res = sm.fit_resample(x_treino, y_treino)
        elif nome == 'Oversample ADASYN':
            ada = ADASYN(random_state=42)
            x_res, y_res = ada.fit_resample(x_treino, y_treino)
        elif nome == 'Combined Over/Undersample':
            sme = SMOTEENN(random_state=42)
            x_res, y_res = sme.fit_resample(x_treino, y_treino)
        else:
            raise ValueError(f'Modelo desconhecido: {nome}')
        
        modelo.fit(x_res, y_res)
        y_pred = modelo.predict(x_teste)
        cm = confusion_matrix(y_teste, y_pred)
        rs = recall_score(y_teste, y_pred)
        
        resultados[nome] = {
            'Matriz de confusão': cm,
            'Recall': rs
        }
    
    return resultados

# Criar os modelos
clfrus = tree.DecisionTreeClassifier(random_state=42)
clfcc = tree.DecisionTreeClassifier(random_state=42)
clfnm = tree.DecisionTreeClassifier(random_state=42)
clfros = tree.DecisionTreeClassifier(random_state=42)
clfsm = tree.DecisionTreeClassifier(random_state=42)
clfada = tree.DecisionTreeClassifier(random_state=42)
clfsme = tree.DecisionTreeClassifier(random_state=42)

# Criar o dicionário com os nomes dos modelos
modelos = {
    'Random Undersample': clfrus,
    'Undersample ClusterCentroid': clfcc,
    'Undersample NearMiss': clfnm,
    'Random Oversample': clfros,
    'Oversample SMOTE': clfsm,
    'Oversample ADASYN': clfada,
    'Combined Over/Undersample': clfsme
}

# Chamar a função para avaliar os modelos
resultados = avaliar_modelos(modelos, x_treino, y_treino, x_teste, y_teste)

# Imprimir os resultados
for nome, resultado in resultados.items():
    print(f"Modelo: {nome}")
    print(f"Matriz de confusão:\n {resultado['Matriz de confusão']}")
    print(f"Recall: {resultado['Recall']:.2f}%")

## RESULTADO ##
"""
Modelo: Random Undersample
Matriz de confusão:
 [[75628  9667]
 [   16   132]]
Recall: 0.89%

Modelo: Undersample ClusterCentroid
Matriz de confusão:
 [[42256 43039]
 [    7   141]]
Recall: 0.95%

Modelo: Undersample NearMiss
Matriz de confusão:
 [[33992 51303]
 [    7   141]]
Recall: 0.95%

Modelo: Random Oversample
Matriz de confusão:
 [[84787   508]
 [   25   123]]
Recall: 0.83%

Modelo: Oversample SMOTE
Matriz de confusão:
 [[85142   153]
 [   39   109]]
Recall: 0.74%

Modelo: Oversample ADASYN
Matriz de confusão:
 [[85151   144]
 [   42   106]]
Recall: 0.72%

Modelo: Combined Over/Undersample
Matriz de confusão:
 [[85109   186]
 [   36   112]]
Recall: 0.76%
"""