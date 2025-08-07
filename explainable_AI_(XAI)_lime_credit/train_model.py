from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

def treinar_modelo():
    df_copia = pd.read_parquet('df_copia.parquet')
    print(df_copia.head())

    print('\n----------------------')
    print("4. Divisão treino/teste")
    print('----------------------')

    # Divide os dados em treino e teste
    X = df_copia.drop('Target', axis=1)
    y = df_copia['Target']      
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)
    print(f'Tamanho do conjunto de treino: {X_train.shape[0]}')
    print(f'Tamanho do conjunto de teste: {X_test.shape[0]}')

    print('\n----------------------')
    print("5. Treinamento do modelo") 
    print('----------------------')
    
    # Treina um modelo de classificação
    from sklearn.ensemble import RandomForestClassifier
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    print(f'Precisão do modelo: {modelo.score(X_test, y_test):.2f}')
    
    # Avalia o modelo 
    print('\n----------------------')
    print("6. Avaliação do modelo") 
    print('----------------------')  
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred))
    
    print('\n----------------------')
    return modelo, X_train, X_test, y_train, y_test

if __name__ == "__main__":
    treinar_modelo()
    print("Modelo treinado e salvo com sucesso!")