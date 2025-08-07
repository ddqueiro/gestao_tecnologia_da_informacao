# Decifrando a Caixa Preta: Tornando Modelos de IA Explicáveis com LIME

## Descrição do projeto

Este projeto foi desenvolvido para a disciplina *Explainable AI (XAI)* da faculdade Unifecaf. O objetivo principal é construir um modelo preditivo para classificação de risco de crédito bancário utilizando o dataset Statlog (German Credit Data) da UCI. 

O desafio proposto consiste em lidar com uma situação realista na qual uma empresa que desenvolve modelos preditivos para crédito bancário já possui um modelo com alta precisão, porém clientes, gerentes e órgãos regulatórios questionam "por que" o modelo toma determinadas decisões, especialmente em casos de negação de crédito. 

Para além da precisão, a empresa necessita explicar de forma transparente, clara e tecnicamente fundamentada cada decisão individual, tanto para o cliente quanto para fins de compliance. 

Neste cenário, a missão do projeto é aplicar técnicas de Explainable AI (XAI), utilizando a biblioteca LIME (Local Interpretable Model-agnostic Explanations), para gerar explicações locais que indiquem quais características (como idade, renda, histórico de inadimplência, entre outras) mais impactaram a decisão do modelo para cada cliente analisado.

O dataset Statlog (German Credit Data) da UCI contém 1.000 amostras com 20 atributos, incluindo informações como idade, tipo de conta e histórico de crédito, classificando clientes em bom ou mau risco de crédito. Ele é recomendado por sua simplicidade e por representar um problema balanceado de classificação binária, sendo amplamente utilizado em estudos introdutórios e aplicações práticas.

Este trabalho une a aplicação de modelos de machine learning com técnicas de interpretabilidade para garantir que decisões automatizadas sejam compreensíveis, transparentes e confiáveis.


## Contextualização

No contexto dos sistemas financeiros, a análise de crédito desempenha um papel fundamental para instituições bancárias e financeiras, pois permite avaliar o risco associado à concessão de empréstimos e financiamentos. Modelos preditivos de crédito são amplamente utilizados para estimar a probabilidade de inadimplência dos clientes, ajudando a decidir se um crédito deve ser aprovado ou negado.

Entretanto, muitos dos modelos preditivos mais precisos atualmente disponíveis, como Random Forests e redes neurais, são considerados “caixas-pretas”, pois suas decisões são baseadas em processos complexos e não lineares que dificultam a interpretação direta dos fatores que levaram a determinada predição. Essa falta de transparência pode gerar desconfiança por parte dos clientes e dificultar o processo de auditoria e compliance pelas instituições financeiras, além de levantar questionamentos por órgãos regulatórios que exigem explicações claras para decisões automatizadas que impactam direitos dos consumidores.

Neste projeto acadêmico, buscamos abordar esse desafio por meio da aplicação de técnicas de Explainable AI (XAI), com foco no uso do LIME (Local Interpretable Model-agnostic Explanations). O objetivo é tornar o modelo preditivo não apenas preciso, mas também capaz de fornecer explicações locais e compreensíveis sobre suas decisões, aumentando a transparência e facilitando a comunicação entre a equipe técnica, os gestores e os clientes finais.

A interpretabilidade dos modelos é, portanto, essencial para:

- Garantir transparência e confiança para os clientes, que têm o direito de entender os motivos das decisões de crédito que os afetam diretamente;
- Facilitar a revisão e aprovação das decisões por gerentes, auditores internos e externos, que precisam assegurar que os processos estejam em conformidade com políticas internas e regulamentações legais;
- Atender às exigências regulatórias de compliance, que têm se tornado cada vez mais rigorosas em relação ao uso de inteligência artificial e automação em decisões financeiras;
- Identificar possíveis vieses e inconsistências nos modelos, promovendo um uso ético e justo da inteligência artificial na análise de crédito.

Este trabalho acadêmico visa, portanto, integrar a precisão do machine learning com a explicabilidade necessária para aplicação prática e responsável no setor financeiro.


### Por que escolhemos o modelo Random Forest?

O algoritmo Random Forest foi escolhido para este projeto por vários motivos importantes:

- **Alta precisão e robustez**  
  O Random Forest combina múltiplas árvores de decisão para formar um modelo mais forte. Cada árvore é treinada em uma amostra diferente dos dados e com um subconjunto aleatório das variáveis disponíveis. Isso faz com que cada árvore tenha “visões” ligeiramente diferentes do problema. Ao agregar as decisões de todas essas árvores (geralmente por votação na classificação), o modelo final corrige erros individuais das árvores simples, evitando que o modelo aprenda detalhes específicos demais dos dados de treino (overfitting). Isso resulta em maior precisão e melhor capacidade de generalização, ou seja, o modelo consegue fazer previsões confiáveis mesmo em dados novos que não viu antes.

- **Capacidade de lidar com dados mistos**  
  O dataset usado neste projeto contém variáveis numéricas (como idade e duração do crédito) e variáveis categóricas (como tipo de emprego e estado civil). O Random Forest lida muito bem com esse tipo de dados mistos sem a necessidade de transformações complexas, como one-hot encoding para variáveis categóricas. Isso simplifica o pré-processamento e mantém a integridade das informações.

- **Facilidade de uso**  
  Diferentemente de alguns modelos que requerem ajuste fino de muitos parâmetros, o Random Forest costuma funcionar bem com configurações padrão ou com poucas modificações. Isso facilita a implementação, reduz o tempo de desenvolvimento e a necessidade de conhecimento avançado em tuning de hiperparâmetros para obter bons resultados.

- **Interpretabilidade relativa**  
  Embora o Random Forest seja um modelo mais complexo do que uma única árvore de decisão (que é facilmente interpretável), ele ainda permite extrair informações importantes, como a importância relativa de cada variável para as decisões do modelo. Além disso, técnicas como LIME podem ser aplicadas para gerar explicações locais, ou seja, mostrar quais características influenciaram a decisão do modelo para um cliente específico, trazendo transparência para a análise.

- **Suporte consolidado**  
  O Random Forest é um dos algoritmos mais populares e amplamente utilizados em machine learning. Ele possui ampla documentação, bibliotecas maduras (como a implementação do scikit-learn usada aqui) e uma grande comunidade ativa que contribui para sua evolução, o que garante confiabilidade e facilidade para encontrar soluções em caso de dúvidas ou problemas.


## Dataset

- Nome: Statlog (German Credit Data)
- Fonte: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29)
- Descrição: O dataset contém 1000 amostras de clientes com 20 atributos, incluindo variáveis numéricas e categóricas, que indicam o perfil financeiro e histórico do cliente, e uma variável alvo binária (bom ou mau pagador).

### Principais variáveis do dataset

| Variável            | Tipo       | Descrição                                     |
|---------------------|------------|-----------------------------------------------|
| Status              | Categórica | Status da conta existente                      |
| Duration            | Numérica   | Duração do crédito (em meses)                  |
| CreditHistory       | Categórica | Histórico de crédito                           |
| Purpose             | Categórica | Propósito do crédito                           |
| CreditAmount        | Numérica   | Quantidade do crédito                          |
| Savings             | Categórica | Poupança                                      |
| Employment          | Categórica | Tempo de emprego                              |
| InstallmentRate     | Numérica   | Taxa de parcelamento                           |
| PersonalStatusSex   | Categórica | Estado civil e sexo                            |
| Debtors             | Categórica | Outras pessoas devedoras                       |
| ResidenceDuration   | Numérica   | Tempo de residência atual                      |
| Property            | Categórica | Tipo de propriedade                            |
| Age                 | Numérica   | Idade do cliente                              |
| OtherInstallmentPlans | Categórica | Outros planos de parcelamento                  |
| Housing             | Categórica | Tipo de habitação                              |
| ExistingCredits     | Numérica   | Créditos existentes                            |
| Job                 | Categórica | Tipo de emprego                                |
| NumPeopleLiable     | Numérica   | Número de pessoas a cargo                      |
| Telephone           | Categórica | Presença de telefone                           |
| ForeignWorker       | Categórica | Indicador de trabalhador estrangeiro          |
| Target              | Binária    | 1 = Bom pagador; 0 = Mau pagador              |

## Estrutura do projeto

/explainable_AI_(XAI)_lime_credit
├── data_analysis.py            # Script para análise exploratória, pré-processamento e salvamento do dataset
├── train_model.py             # Script para treinamento do modelo Random Forest e avaliação
├── explain_client.py          # Script para gerar explicações locais com LIME para um cliente específico
├── requirements.txt           # Arquivo com as dependências Python do projeto
├── README.md                  # Documentação detalhada do projeto
├── df_copia.parquet           # Arquivo gerado pelo data_analysis.py com os dados pré-processados
├── outputs/                   # Diretório para armazenar imagens e gráficos gerados
│   └── lime_explanation_cliente_<indice>.png  # Exemplo de gráfico salvo com explicação LIME para cliente


## Como executar

### Pré-requisitos

- Python 3.7 ou superior  
- Acesso à internet para download do dataset via URL  
- Ambiente com permissões para instalar pacotes Python  

### Passo a passo

1. **Clone o repositório:**

```bash
git clone <link-do-repositorio>
cd xai-lime-credit
```


2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute o script data_analysis:**

```bash
python data_analysis.py
```

4. **Execute o script train_model:**

```bash
python train_model.py
```
5. **Execute o script explain_client:**

```bash
python explain_client.py
```

6. **Uso interativo:**

O script explain_client.py solicitará um índice do cliente para gerar uma explicação local da predição.

Digite um número entre 0 e o tamanho do conjunto de teste menos 1.

Será exibida a explicação em texto e um gráfico será aberto mostrando a influência das variáveis.

7. **Resultados:**

## Resultados obtidos

- Modelo Random Forest com acurácia aproximada de 75-80% no conjunto de teste, exibida ao executar o script `train_model.py`.
- Explicações locais geradas pelo `explain_client.py` que identificam quais características influenciaram positivamente ou negativamente a classificação para cada cliente.
- Visualizações intuitivas que facilitam a compreensão do modelo para usuários não técnicos.


## Tecnologias e bibliotecas utilizadas

- Pandas — manipulação e análise de dados  
- NumPy — operações numéricas  
- Scikit-learn — modelagem de machine learning (Random Forest, pré-processamento, métricas)  
- LIME — geração de explicações locais para modelos de caixa-preta  
- Matplotlib e Seaborn — visualização de dados  

## Resultados obtidos

- Modelo Random Forest com acurácia aproximada de 75-80% no conjunto de teste.  
- Explicações locais que identificam quais características influenciaram positivamente ou negativamente a classificação para cada cliente.  
- Visualizações intuitivas que facilitam a compreensão do modelo para usuários não técnicos.  

## Possíveis melhorias e extensões

- Testar outros modelos preditivos, como Gradient Boosting ou redes neurais.  
- Implementar explicações globais com técnicas como SHAP.  
- Adicionar validação cruzada e otimização de hiperparâmetros.  
- Automatizar geração de relatórios e dashboards interativos.  

## Referências

- Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). Why Should I Trust You? Explaining the Predictions of Any Classifier. [Link](https://arxiv.org/abs/1602.04938)  
- Documentação oficial do LIME: https://marcotcr.github.io/lime/tutorials.html  
- Dataset Statlog (German Credit Data) — UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29  

## Contato

Para dúvidas, sugestões ou contribuições, entre em contato:

- Email: seuemail@exemplo.com  
- GitHub: https://github.com/seunomeusuario
