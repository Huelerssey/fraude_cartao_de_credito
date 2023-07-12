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
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier


# -> CARREGANDO DATASET

# dataframe 
tabela = pd.read_csv('dataset/creditcard.csv')

# -> DATACLEANING

# verifica os tipos de dados
print(tabela.info())
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
print(tabela.Class.value_counts())
# Class
# 0    284315
# 1       492

# porcentagem de fraudes
labels = ['Não fraudolenta', 'Fraude']  # Rótulos para as fatias do gráfico
sizes = [99.8, 0.2]  # Valores correspondentes às fatias

# Plotagem do gráfico de pizza
plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90)

# Exibição do gráfico
plt.show()

# -- IA para avaliação com accuracy -- #

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
cm = confusion_matrix(y_teste, y_pred)
rs = recall_score(y_teste, y_pred)
print(f'Matriz de confusão:\n {cm} \nRecall: {rs:.2f}%')

#resultado
# Matriz de confusão:
#  [[85264    31]
#  [   39   109]]
# Recall: 0.74%

# Cria um cartão (figura) vazio
fig, ax = plt.subplots(figsize=(4, 3))

# Adiciona o texto do accuracy_formatted no cartão
ax.text(0.5, 0.5, accuracy_formatted, ha='center', va='center', fontsize=24)

# Remove os eixos e limites do gráfico
ax.axis('off')

# Exibe o cartão
plt.show()

# -- IA para avaliação com accuracy -- #

# plotar um gráfico com a nova base organizada
labels = ['Não fraudolenta', 'Fraude']  # Rótulos para as fatias do gráfico
sizes = [492, 492]  # Valores correspondentes às fatias

# Plotagem do gráfico de pizza
plt.pie(sizes, labels=labels, startangle=90)

# Exibição do gráfico
plt.show()

# -> MODELANDO ALGUNS ALGORITIMOS DE MACHINE LEARNING

# definindo dados de treino e de teste
y = tabela['Class']
x = tabela.drop('Class', axis=1)

# dividindo a base entre treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)

# função para avaliar modelos
def avaliar_modelos(modelos, x_treino, y_treino, x_teste, y_teste, resampling_methods):
    resultados = {}
    
    for nome, modelo in modelos.items():
        for resampling_method in resampling_methods:
            if resampling_method == 'Random Undersample':
                rus = RandomUnderSampler(random_state=42)
                x_res, y_res = rus.fit_resample(x_treino, y_treino)
            elif resampling_method == 'Undersample ClusterCentroid':
                cc = ClusterCentroids(estimator=MiniBatchKMeans(n_init=1, random_state=0), random_state=42)
                x_res, y_res = cc.fit_resample(x_treino, y_treino)
            elif resampling_method == 'Undersample NearMiss':
                nm = NearMiss()
                x_res, y_res = nm.fit_resample(x_treino, y_treino)
            elif resampling_method == 'Random Oversample':
                ros = RandomOverSampler(random_state=42, shrinkage=0.7)
                x_res, y_res = ros.fit_resample(x_treino, y_treino)
            elif resampling_method == 'Oversample SMOTE':
                sm = SMOTE(random_state=42)
                x_res, y_res = sm.fit_resample(x_treino, y_treino)
            elif resampling_method == 'Oversample ADASYN':
                ada = ADASYN(random_state=42)
                x_res, y_res = ada.fit_resample(x_treino, y_treino)
            elif resampling_method == 'Combined Over/Undersample':
                sme = SMOTEENN(random_state=42)
                x_res, y_res = sme.fit_resample(x_treino, y_treino)
            else:
                raise ValueError(f'Método de resampling desconhecido: {resampling_method}')
            
            modelo.fit(x_res, y_res)
            y_pred = modelo.predict(x_teste)
            cm = confusion_matrix(y_teste, y_pred)
            rs = recall_score(y_teste, y_pred)
            
            if nome not in resultados:
                resultados[nome] = {}
            
            resultados[nome][resampling_method] = {
                'Matriz de confusão': cm,
                'Recall': rs
            }
    
    return resultados

# Criar o modelo de árvore de decisão
clf = tree.DecisionTreeClassifier(random_state=42)

# Criar o modelo de Random Forest
clfrf = RandomForestClassifier(random_state=42)

# Criar o modelo de Extra Trees
clfet = ExtraTreesClassifier(random_state=42)

# Criar o dicionário com os nomes dos modelos e as instâncias correspondentes
modelos = {
    'Decision Tree': clf,
    'Random Forest': clfrf,
    'Extra Trees': clfet
}

# Definir os métodos de resampling a serem utilizados
resampling_methods = ['Random Undersample', 'Undersample ClusterCentroid', 'Undersample NearMiss',
                      'Random Oversample', 'Oversample SMOTE', 'Oversample ADASYN',
                      'Combined Over/Undersample']

# Chamar a função para avaliar os modelos
resultados = avaliar_modelos(modelos, x_treino, y_treino, x_teste, y_teste, resampling_methods)

# Imprimir os resultados
for nome, resultado in resultados.items():
    print(f"Modelo: {nome}")
    for resampling_method, res in resultado.items():
        print(f"Método de resampling: {resampling_method}")
        print(f"Matriz de confusão:\n {res['Matriz de confusão']}")
        print(f"Recall: {res['Recall']:.2f}%")

# -> RESULTADOS

#                       -- DECISION TREE --

# Modelo: Decision Tree
# Método de resampling: Random Undersample
# Matriz de confusão:
#  [[75628  9667]
#  [   16   132]]
# Recall: 0.89%

# Modelo: Decision Tree
# Método de resampling: Undersample ClusterCentroid
# Matriz de confusão:
#  [[42256 43039]
#  [    7   141]]
# Recall: 0.95%

# Modelo: Decision Tree
# Método de resampling: Undersample NearMiss
# Matriz de confusão:
#  [[33992 51303]
#  [    7   141]]
# Recall: 0.95%

# Modelo: Decision Tree
# Método de resampling: Random Oversample
# Matriz de confusão:
#  [[84787   508]
#  [   25   123]]
# Recall: 0.83%

# Modelo: Decision Tree
# Método de resampling: Oversample SMOTE
# Matriz de confusão:
#  [[85142   153]
#  [   39   109]]
# Recall: 0.74%

# Modelo: Decision Tree
# Método de resampling: Oversample ADASYN
# Matriz de confusão:
#  [[85151   144]
#  [   42   106]]
# Recall: 0.72%

# Modelo: Decision Tree
# Método de resampling: Combined Over/Undersample
# Matriz de confusão:
#  [[85109   186]
#  [   36   112]]
# Recall: 0.76%

#                       -- RANDOM FOREST --

# Modelo: Random Forest
# Método de resampling: Random Undersample
# Matriz de confusão:
#  [[83647  1648]
#  [   18   130]]
# Recall: 0.88%

# Modelo: Random Forest
# Método de resampling: Undersample ClusterCentroid
# Matriz de confusão:
#  [[34241 51054]
#  [    2   146]]
# Recall: 0.99%

# Modelo: Random Forest
# Método de resampling: Undersample NearMiss
# Matriz de confusão:
#  [[69222 16073]
#  [    8   140]]
# Recall: 0.95%

# Modelo: Random Forest
# Método de resampling: Random Oversample
# Matriz de confusão:
#  [[85131   164]
#  [   26   122]]
# Recall: 0.82%

# Modelo: Random Forest
# Método de resampling: Oversample SMOTE
# Matriz de confusão:
#  [[85278    17]
#  [   30   118]]
# Recall: 0.80%

# Modelo: Random Forest
# Método de resampling: Oversample ADASYN
# Matriz de confusão:
#  [[85274    21]
#  [   29   119]]
# Recall: 0.80%

# Modelo: Random Forest
# Método de resampling: Combined Over/Undersample
# Matriz de confusão:
#  [[85268    27]
#  [   27   121]]
# Recall: 0.82%

#                       -- EXTRA TREES --

# Modelo: Extra Trees
# Método de resampling: Random Undersample
# Matriz de confusão:
#  [[84320   975]
#  [   22   126]]
# Recall: 0.85%

# Modelo: Extra Trees
# Método de resampling: Undersample ClusterCentroid
# Matriz de confusão:
#  [[38421 46874]
#  [    0   148]]
# Recall: 1.00%

# Modelo: Extra Trees
# Método de resampling: Undersample NearMiss
# Matriz de confusão:
#  [[78545  6750]
#  [   10   138]]
# Recall: 0.93%

# Modelo: Extra Trees
# Método de resampling: Random Oversample
# Matriz de confusão:
#  [[85206    89]
#  [   26   122]]
# Recall: 0.82%

# Modelo: Extra Trees
# Método de resampling: Oversample SMOTE
# Matriz de confusão:
#  [[85281    14]
#  [   29   119]]
# Recall: 0.80%

# Modelo: Extra Trees
# Método de resampling: Oversample ADASYN
# Matriz de confusão:
#  [[85280    15]
#  [   29   119]]
# Recall: 0.80%

# Modelo: Extra Trees
# Método de resampling: Combined Over/Undersample
# Matriz de confusão:
#  [[85278    17]
#  [   28   120]]
# Recall: 0.81%
