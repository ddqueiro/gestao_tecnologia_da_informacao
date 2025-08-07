
import matplotlib.pyplot as plt
from train_model import treinar_modelo
# --------------------- 
modelo, X_train, X_test, y_train, y_test = treinar_modelo()

print('\n----------------------')
print('7.Interpretação com LIME')
print('----------------------')
from lime.lime_tabular import LimeTabularExplainer
import numpy as np


# Criar o explainer LIME
explainer = LimeTabularExplainer(
    training_data=np.array(X_train),
    feature_names=X_train.columns.tolist(),
    class_names=['Mau Pagador', 'Bom Pagador'],
    mode='classification'
)
# Índice da instância a ser explicada
while True:
    try:
        indice_cliente = int(input(f"Digite o índice do cliente (0 a {len(X_test)-1}): "))
        if 0 <= indice_cliente < len(X_test):
            break
        else:
            print("Índice fora do intervalo. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Explicação LIME para a instância selecionada

explicacao_lime = explainer.explain_instance(
    data_row=X_test.iloc[indice_cliente].values,
    predict_fn=modelo.predict_proba
)

# Probabilidades previstas pelo modelo para a instância
probabilidades_preditas = modelo.predict_proba([X_test.iloc[indice_cliente].values])[0]

# Dados da instância
dados_cliente_exp = X_test.iloc[indice_cliente]

def gerar_texto_explicativo_bonito(explicacao_lime, probabilidades):
    fatores_positivos = []
    fatores_negativos = []

    for condicao, peso in explicacao_lime.as_list():
        if peso > 0:
            fatores_positivos.append(condicao)
        else:
            fatores_negativos.append(condicao)

    texto = []
    texto.append("Fatores que influenciaram positivamente:")
    if fatores_positivos:
        for i, fator in enumerate(fatores_positivos, 1):
            texto.append(f"  {i}. {fator} contribuiu positivamente para a classificação como bom pagador.")
    else:
        texto.append("  Nenhum fator positivo identificado.")

    texto.append("\nFatores que influenciaram negativamente:")
    if fatores_negativos:
        for i, fator in enumerate(fatores_negativos, 1):
            texto.append(f"  {i}. {fator} contribuiu negativamente, indicando risco de inadimplência.")
    else:
        texto.append("  Nenhum fator negativo identificado.")

    texto.append("\nConclusão:")
    texto.append(
        f"O modelo atribuiu uma probabilidade de {probabilidades[1]:.1%} para que a pessoa seja um BOM pagador, "
        f"e {probabilidades[0]:.1%} para ser um MAU  pagador."
    )

    if probabilidades[1] > probabilidades[0]:
        texto.append("Com base nos fatores acima, considera-se que a pessoa tem maior chance de ser BOM pagador.")
    else:
        texto.append("Com base nos fatores acima, indica-se maior risco de inadimplência, chance de ser MAU pagador).")

    return "\n".join(texto)

# Exemplo de uso:
texto_formatado = gerar_texto_explicativo_bonito(explicacao_lime, probabilidades_preditas)
print(texto_formatado)
# Visualização da explicação LIME
explicacao_lime.show_in_notebook(show_table=True, show_all=False)

#Criar um grafico de pizza para fatores positivos e negativos
# Extrai os fatores e pesos da explicação LIME
explicacoes = explicacao_lime.as_list()

# Separa positivos e negativos com pesos absolutos
fatores_positivos = [(feature, peso) for feature, peso in explicacoes if peso > 0]
fatores_negativos = [(feature, peso) for feature, peso in explicacoes if peso < 0]

# Soma dos pesos absolutos de cada grupo
peso_positivo = sum([abs(peso) for _, peso in fatores_positivos])
peso_negativo = sum([abs(peso) for _, peso in fatores_negativos])

# Labels e valores para o gráfico
labels = ['Fatores Positivos', 'Fatores Negativos']
valores = [peso_positivo, peso_negativo]
cores = ['green', 'red']

# Cria o gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=labels, colors=cores, autopct='%1.1f%%', startangle=90)
plt.title("Distribuição dos Fatores na Decisão do Modelo")
plt.axis('equal')  # Mantém o círculo redondo
plt.show()

# Visualização gráfica da explicação LIME
fig = explicacao_lime.as_pyplot_figure()
fig.axes[0].set_title("")
fig.suptitle(f"Explicação da Predição para o Cliente {indice_cliente}", fontsize=14)
plt.tight_layout()
plt.show()
