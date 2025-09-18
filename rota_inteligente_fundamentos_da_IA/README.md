
# 🚚 Rota Inteligente: Otimização de Entregas com Algoritmos de IA

Sistema de otimização de rotas para a empresa fictícia **Sabor Express**, desenvolvido como parte da disciplina *Artificial Intelligence Fundamentals*.  
A solução utiliza algoritmos clássicos de Inteligência Artificial para agrupar entregas e encontrar rotas mais eficientes em uma cidade representada como grafo.

---

## 📋 Descrição do Problema

A Sabor Express, uma pequena empresa de delivery, enfrenta dificuldades para gerenciar suas entregas em horários de pico.  
Atualmente, os percursos são definidos manualmente, resultando em rotas ineficientes, atrasos, aumento de custos e insatisfação dos clientes.

O objetivo do projeto é criar uma solução inteligente que:
- Sugira automaticamente as melhores rotas para entregadores.
- Agrupe entregas próximas, otimizando tempo e distância.
- Reduza custos operacionais e aumente a satisfação dos clientes.

---

## 🎯 Objetivos da Solução

- Representar a cidade como um **grafo** (nós = bairros/endereços, arestas = ruas com pesos).
- Agrupar entregas usando **clustering (K-Means)**.
- Encontrar rotas otimizadas usando **A*** para menor caminho entre pontos e **TSP (vizinho mais próximo)** para sequência de entregas.
- Gerar **visualizações gráficas** das rotas e clusters.

---

## 🧠 Abordagem Adotada

### 1. Representação da Cidade
A cidade é gerada como uma grade 15x15. Cada nó representa um ponto da cidade (rua ou bairro), e o restaurante é fixado no centro.

### 2. Agrupamento das Entregas (K-Means)
As entregas são carregadas de um arquivo CSV (`data/entregas.csv`) e agrupadas em **3 clusters** geograficamente próximos.  
Cada cluster representa um conjunto de entregas que pode ser atendido por um entregador.

### 3. Otimização das Rotas (TSP + A*)
Para cada cluster:
- Utilizamos o **algoritmo do vizinho mais próximo** (heurística do TSP) para definir a ordem das entregas.
- Usamos o **A*** para calcular o menor caminho entre dois pontos consecutivos no grafo.
- Resultado: cada rota percorre a menor distância total possível.

### 4. Visualização
Dois gráficos são gerados:
- **Clusters de Entregas:** mostra a distribuição das entregas agrupadas por cor.
- **Rotas Otimizadas:** mostra as rotas percorridas por cada entregador com cores diferentes.

---

## 🔧 Algoritmos Utilizados

- **A*** (A-star): algoritmo de busca heurística para menor caminho entre dois nós.
- **K-Means:** algoritmo de aprendizado não supervisionado para agrupar entregas em clusters.
- **TSP – Vizinho mais Próximo:** heurística simples para percorrer todos os pontos de um cluster na menor distância possível.

---

## 🗂 Estrutura do Repositório

```
/data
  entregas.csv              # Arquivo de entregas (ID, Nome_Cliente, Endereco)
/outputs
  resultado_otimizacao.png  # Gráfico gerado com clusters e rotas
app.py                      # Código principal
requirements.txt            # Bibliotecas necessárias
README.md                   # Este arquivo
```

---

## 📝 Diagrama do Modelo (Exemplo)

```text
Restaurante (centro) → nós (endereços) conectados por arestas com pesos
```

(O projeto gera automaticamente um grafo da cidade e pode ser exportado como imagem.)

---

## 📊 Resultados

- **Clusters formados:** 3 grupos de entregas geograficamente próximos.
- **Rotas otimizadas:** cada cluster é atendido por uma rota eficiente.
- **Distância total percorrida:** exibida no terminal após a execução.
- **Visualização:** arquivo `outputs/resultado_otimizacao.png`.

---

## 🚀 Execução do Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/usuario/rota-inteligente.git
cd ROTA_INTELIGENTE_FUNDAMENTOS_DA_IA
```

### 2. Criar Ambiente Virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Preparar Arquivo de Entregas
Coloque seu arquivo `entregas.csv` em `data/` com o seguinte formato:

| ID | Nome_Cliente | Endereco |
|----|--------------|----------|
| 1  | Cliente A    | Rua X, nº Y |
| 2  | Cliente B    | Rua Z, nº W |

### 5. Executar o Programa
```bash
python app.py
```

Os gráficos serão mostrados na tela e salvos em `outputs/`.

---

## 💡 Limitações e Possíveis Melhorias

**Limitações atuais do sistema:**

1. **Heurística simplificada do TSP:**  
   - O algoritmo do vizinho mais próximo utilizado não garante a rota globalmente ótima.  
   - Pode gerar pequenas ineficiências para grande volume de entregas.

2. **Cidade simulada em grade:**  
   - A grade 15x15 não representa ruas reais ou distâncias precisas.  
   - Não considera sentido das ruas, interseções complexas ou obstáculos urbanos.

3. **Aleatoriedade na localização das entregas:**  
   - IDs dos nós das entregas são gerados aleatoriamente.  
   - Não há restrições reais de endereços, horários ou prioridades detalhadas.

4. **Não considera tráfego ou tempo real de viagem:**  
   - Pesos das arestas são estimativas baseadas em distância, sem considerar congestionamento ou semáforos.

5. **Capacidade e limitações do entregador:**  
   - Não há limite de entregas por entregador ou tipo de veículo.  
   - Não otimiza distribuição de entregas entre múltiplos entregadores.

6. **Falta de atualização dinâmica:**  
   - Rotas são pré-calculadas, não se adaptam a novos pedidos ou cancelamentos em tempo real.

**Possíveis melhorias futuras:**

1. **Otimização avançada do TSP:**  
   - Algoritmos genéticos, simulated annealing ou branch and bound para rotas mais eficientes.

2. **Integração com mapas reais:**  
   - OpenStreetMap, Google Maps API ou outros para distâncias reais, sentido das ruas e restrições.

3. **Consideração de tráfego em tempo real:**  
   - Ajuste dinâmico das rotas com dados de trânsito e congestionamento.

4. **Priorização de entregas:**  
   - Ajuste de rotas considerando urgência, horário e tamanho dos pedidos.

5. **Múltiplos veículos e VRP:**  
   - Distribuição eficiente de entregas entre vários entregadores, usando Vehicle Routing Problem.

6. **Interface gráfica e aplicação web:**  
   - Dashboard interativo mostrando status das entregas e rotas em tempo real.

7. **Escalabilidade e performance:**  
   - Paralelização, caching e heurísticas avançadas para centenas ou milhares de entregas.

---

## 📚 Referências

- UPS – ORION: [On-Road Integrated Optimization and Navigation](https://www.ups.com)
- Medium – “Optimizing Logistics: Clustering e MILP”
- ResearchGate – AI-Powered Route Optimization
- Kardinal.ai – Case Study “Fresh Product Delivery”

---

## 🧑‍💻 Autoria

Projeto desenvolvido por **[Seu Nome]** para a disciplina *Artificial Intelligence Fundamentals*.
