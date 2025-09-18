# 🚀 Rota Inteligente: Otimização de Entregas com Algoritmos de IA  

## 📌 Descrição do Problema  
A empresa fictícia **Sabor Express** atua com delivery de alimentos na região central da cidade. Durante horários de pico (almoço e jantar), enfrenta atrasos nas entregas, rotas ineficientes, aumento de custos de combustível e insatisfação dos clientes.  

Atualmente, os percursos são definidos de forma manual, baseados apenas na experiência dos entregadores. Para se manter competitiva, a empresa precisa de uma solução tecnológica para otimizar as rotas de entrega.  

---

## 🎯 Objetivo  
Desenvolver uma **solução inteligente**, baseada em algoritmos de Inteligência Artificial, capaz de sugerir as melhores rotas para os entregadores, agrupando entregas próximas e reduzindo tempo e custo operacional.  

---

## 🛠️ Abordagem Utilizada  

- **Representação em Grafo**:  
  Os pontos de entrega são modelados como vértices e as ruas como arestas, com pesos baseados na distância/tempo estimado.

- **Algoritmos de Busca (A*, BFS, DFS)**:  
  Utilizados para encontrar caminhos mais curtos entre pontos de entrega.

- **Clustering com K-Means**:  
  Agrupamento de entregas próximas em clusters para otimizar o trabalho dos entregadores.

- **API OpenRouteService**:  
  Utilizada para geocodificação dos endereços e cálculo das rotas otimizadas.

---

## 🗂️ Estrutura do Repositório  

```
📦 rota_inteligente_fundamentos_da_IA
 ┣ 📂 data
 ┃ ┗ 📄 entregas.csv           # Endereços das entregas
 ┣ 📂 src
 ┃ ┗ 📄 rota_inteligente.py    # Código principal
 ┣ 📄 .env                     # Chave da API OpenRouteService
 ┣ 📄 requirements.txt         # Bibliotecas necessárias
 ┣ 📄 rotas_otimizadas.html    # Saída com rotas otimizadas no mapa
 ┗ 📄 README.md                # Este arquivo
```

---

## ⚙️ Execução  

### 1️⃣ Instalar Dependências  
```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar Variáveis de Ambiente  
Crie um arquivo `.env` na raiz do projeto com a seguinte linha:  
```
ORS_API_KEY=sua_chave_da_api_aqui
```

### 3️⃣ Executar o Projeto  
```bash
python src/rota_inteligente.py
```

O sistema gerará um arquivo **rotas_otimizadas.html** com as rotas otimizadas no mapa interativo.

---

## 📊 Resultados Obtidos  

- Endereços geocodificados e visualizados em mapa interativo.  
- Agrupamento das entregas por proximidade utilizando K-Means.  
- Rotas otimizadas calculadas via API, reduzindo tempo e custo.  

---

## 📈 Métricas Avaliadas  

- Tempo total estimado das rotas.  
- Redução de distância percorrida após aplicação do algoritmo.  
- Quantidade de clusters versus tempo médio por rota.  

---

## 📚 Fontes de Pesquisa  

1. **Estudo de caso da UPS – ORION**  
   Sistema de otimização de rotas utilizado pela UPS, combinando heurísticas e dados de tráfego para economia de milhões de dólares/ano.  

2. **Medium – “Optimizing Logistics: Clustering e MILP”**  
   Aplicação prática de K-Means e programação linear inteira mista para agrupar entregas e minimizar distância.  

3. **ResearchGate – AI-Powered Route Optimization**  
   Explora integração de IA, sensores IoT e algoritmos heurísticos para roteamento dinâmico.  

4. **Kardinal.ai – Fresh Product Delivery**  
   Caso real de uso de algoritmos para otimização contínua de rotas e planejamento dinâmico.  

---

## 💡 Possíveis Melhorias  

## Roteamento dinâmico com técnicas avançadas

Explorar algoritmos genéticos, otimização por colônia de formigas ou aprendizado por reforço para gerar rotas que se adaptem automaticamente a mudanças no cenário, como novas entregas, bloqueios de ruas ou alterações no tempo de deslocamento.

## Integração com dados de tráfego em tempo real

Conectar a solução a APIs públicas ou privadas (ex.: Google Maps Traffic, Waze, MapBox) para considerar condições reais de trânsito e estimar tempos de chegada mais precisos. Isso permite que o sistema ajuste a rota antes e durante o percurso.

## Painel web de acompanhamento operacional

Desenvolver um painel online (por exemplo, com Streamlit, Dash ou React + Flask) para que gestores acompanhem, em tempo real, a localização dos entregadores, status de cada entrega, alertas de atrasos e métricas de performance. Isso traz mais visibilidade e permite intervenções rápidas quando necessário.  

---

## 👩‍💻 Autor  

Projeto desenvolvido por **Dannyelly Dayane Queiroz** como parte da disciplina **Artificial Intelligence Fundamentals**.
