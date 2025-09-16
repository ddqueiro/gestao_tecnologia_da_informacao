# Rota Inteligente: Otimização de Entregas com IA

## 1. Descrição do Projeto
Este projeto tem como objetivo desenvolver uma solução inteligente para otimizar as rotas de entregas de uma empresa de delivery fictícia chamada **Sabor Express**, localizada na região central de São Paulo. 

O sistema sugere **as melhores rotas** para os entregadores, considerando múltiplos pontos de entrega e agrupando pedidos próximos para eficiência logística. O projeto utiliza algoritmos de Inteligência Artificial clássicos, como **K-Means** para agrupamento e integração com a API do **OpenRouteService (ORS)** para cálculo de rotas otimizadas.

---

## 2. Objetivos
- Reduzir o tempo de entrega e consumo de combustível.  
- Agrupar entregas próximas usando **clustering**.  
- Visualizar rotas em um **mapa interativo** usando **Folium**.  
- Automatizar a sugestão de rotas, substituindo decisões manuais.

---

## 3. Estrutura do Projeto

rota_inteligente_fundamentos_da_IA/
│
├── data/
│ └── entregas.csv # Arquivo CSV com os endereços das entregas
├── rotas_otimizadas.html # Mapa gerado pelo código com rotas e marcadores
├── main.py # Código principal do projeto
├── .env # Chave da API do OpenRouteService
├── requirements.txt # Bibliotecas necessárias
└── README.md # Documentação do projeto


---

## 4. Instalação e Configuração

1. Clone este repositório:

```bash
git clone https://github.com/ddqueiro/gestao_tecnologia_da_informacao.git
cd gestao_tecnologia_da_informacao/rota_inteligente_fundamentos_da_IA
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a API do OpenRouteService:

Crie um arquivo .env na raiz do projeto:

```bash
ORS_API_KEY=SUA_CHAVE_DO_ORS
```

Substitua SUA_CHAVE_DO_ORS pela sua chave válida.

5. Como Executar

No terminal, execute:

``` bash

python main.py

```

O código irá:

- Geocodificar os endereços do CSV.

- Agrupar as entregas em clusters (opcionalmente por entregador).

- Calcular a rota otimizada para cada cluster.

- Gerar um mapa interativo rotas_otimizadas.html com as rotas e marcadores numerados.

- Abra o arquivo rotas_otimizadas.html em seu navegador para visualizar as rotas.