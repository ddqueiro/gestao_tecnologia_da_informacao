
# 📊 Previsão de Vendas com Regressão Linear - Wave Surfboards

Este projeto é um estudo de caso que aplica regressão linear e conceitos de matemática aplicada à ciência de dados para resolver um problema realista de previsão de vendas na empresa fictícia Wave Surfboards, especializada na fabricação e comercialização de pranchas de surf. O projeto foi desenvolvido para a disciplina Applied Math for Data Science.


---

## 🏄 Sobre a Empresa

A **Wave Surfboards** é uma empresa fictícia do setor esportivo, especializada em pranchas de surf. Possui forte atuação em regiões litorâneas e sua demanda é diretamente impactada por fatores sazonais, como:

- Condições climáticas (ex: temperatura)
- Fluxo turístico
- Investimentos em campanhas de marketing

---

## ❗ O Problema

A empresa apresenta **dificuldades na previsão de vendas mensais**, o que impacta negativamente:

- 📦 Gestão de estoque (excesso ou ruptura)
- 🏭 Planejamento da produção
- 📣 Efetividade de campanhas publicitárias
- 📉 Perdas de oportunidade em períodos de alta demanda
- 💸 Custos elevados por decisões baseadas em intuição

Esses problemas são agravados por **variações sazonais mal geridas** e a **ausência de um modelo preditivo estruturado**.

---

## 🎯 Objetivo do Projeto

Desenvolver um **modelo preditivo com regressão linear (simples e múltipla)** que permita:

- Estimar as vendas mensais de pranchas
- Antecipar picos e quedas de demanda
- Melhorar o alinhamento entre produção, estoque e marketing
- Reduzir desperdícios e melhorar a lucratividade

---

## 🔧 Ferramentas e Tecnologias

- **Linguagem:** Python 3.10+
- **Ambiente:** Google Colab
- **Bibliotecas utilizadas:**
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `scikit-learn`
- **Modelos aplicados:**
  - Regressão Linear Simples
  - Regressão Linear Múltipla

---

## 📂 Estrutura do Projeto

```bash
📁 wave-surfboards-vendas
│
├── estudo_de_caso_wave.pdf                 # Estudo de caso completo com contextualização e análise
├── regressão_linear_wave_surfboard.ipynb   # Notebook com o modelo preditivo em Python
└── README.md                               # Este arquivo
```

---

## 🧠 Metodologia

1. Levantamento e contextualização do problema  
2. Importação e limpeza dos dados fictícios  
3. Análise estatística descritiva (EDA)  
4. Implementação da regressão linear simples (Temperatura)  
5. Implementação da regressão linear múltipla (Temperatura + Marketing)  
6. Validação com métricas como R² e RMSE  
7. Previsão de vendas para novos cenários  

---

## 📈 Exemplo de Previsão

Com temperatura de 25°C e investimento de R$ 6.000, o modelo previu:

```
Vendas ≈ 153 pranchas
```

---

## ✅ Benefícios Esperados

A adoção do modelo preditivo baseado em regressão linear traz impactos positivos significativos para a gestão da Wave Surfboards. Entre os principais benefícios estão:

### 📦 1. Melhoria no Controle de Estoque
- Evita excesso de produtos parados que ocupam espaço e geram custo.
- Reduz o risco de ruptura de estoque em períodos de alta demanda.
- Exemplo: prever baixa demanda em meses frios evita a superprodução de pranchas.

### 🏭 2. Otimização do Planejamento da Produção
- Permite ajustar a produção de acordo com a demanda prevista.
- Evita ociosidade de equipamentos ou sobrecarga de turnos.
- Reduz desperdício de matéria-prima e melhora a eficiência operacional.

### 📣 3. Campanhas de Marketing mais Estratégicas
- Ajuda a identificar os melhores períodos para investir em divulgação.
- Permite alocar orçamento publicitário de forma mais eficaz.
- Exemplo: em meses com previsão de queda nas vendas, campanhas promocionais podem ser antecipadas.

### 💰 4. Redução de Custos Operacionais
- Minimiza gastos com armazenamento e logística desnecessária.
- Evita investimentos em marketing e produção que não geram retorno.
- Aumenta a rentabilidade e libera capital de giro.

### 🎯 5. Decisões Mais Assertivas e Ágeis
- Com previsões baseadas em dados, decisões deixam de ser feitas por "achismo".
- A diretoria e os gestores ganham mais confiança para planejar o futuro.

### 📊 6. Cultura Organizacional Orientada por Dados (Data-Driven)
- Estimula todos os setores a usar dados para embasar ações e estratégias.
- Torna a empresa mais competitiva e preparada para o crescimento sustentável.

### 🚀 7. Escalabilidade e Evolução Contínua
- O modelo pode ser facilmente atualizado com novos dados.
- Pode ser expandido futuramente com técnicas de machine learning (ex: árvores de decisão ou redes neurais).

---
