import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import lime
from lime.lime_tabular import LimeTabularExplainer

# ---------------------
# 1. Carregar o dataset
# ---------------------
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
colunas = [
    'Status', 'Duration', 'CreditHistory', 'Purpose', 'CreditAmount', 'Savings', 'Employment',
    'InstallmentRate', 'PersonalStatusSex', 'Debtors', 'ResidenceDuration', 'Property',
    'Age', 'OtherInstallmentPlans', 'Housing', 'ExistingCredits', 'Job',
    'NumPeopleLiable', 'Telephone', 'ForeignWorker', 'Target'
]
df = pd.read_csv(url, sep=' ', header=None, names=colunas)
df['Target'] = df['Target'].map({1: 1, 2: 0})  # 1 = bom pagador, 0 = mau pagador
print('\n----------------------')
print('2. Análise Exploratória')
print('----------------------')
# ---------------------
# Frequência das classes
sns.countplot(x='Target', data=df)
plt.title('Distribuição das Classes (1 = Bom, 0 = Mau)')
plt.show()

# Distribuição das colunas numéricas
numericas = ['Duration', 'CreditAmount', 'Age']
df[numericas].hist(bins=20, figsize=(12, 5))
plt.tight_layout()
plt.show()

# Contagem das categorias
print(df['Purpose'].value_counts())
print(df['CreditHistory'].value_counts())

print('\n----------------------')
print("2. Correlação entre variáveis")
print('----------------------')

correlacao = df[numericas + ['Target']].corr()
sns.heatmap(correlacao, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

print('\n----------------------')
print("3. Pré-processamento dos dados")
print('----------------------')

# Faz uma cópia do DataFrame original para não mexer nos dados crus
df_copia = df.copy()

# Converte colunas categóricas para números
for coluna in df_copia.columns:
    if df_copia[coluna].dtype == 'object':
        le = LabelEncoder()
        df_copia[coluna] = le.fit_transform(df_copia[coluna])

print(df_copia.head())
df_copia.to_parquet('df_copia.parquet')
print('\n----------------------')
print("Arquivo salvo como df_copia.parquetl")
print('----------------------')
