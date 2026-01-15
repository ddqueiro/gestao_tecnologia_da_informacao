"""
Rota Inteligente: Otimização de Entregas com Algoritmos de IA
Sistema simplificado sem classes - apenas funções
"""

import math
import random
import heapq
import csv
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional, Set
import pandas as pd


# =============================================================================
# ESTRUTURAS BÁSICAS
# =============================================================================

def distancia_euclidiana(x1, y1, x2, y2):
    """Calcula distância euclidiana entre dois pontos"""
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# =============================================================================
# GRAFO 
# =============================================================================

def gerar_cidade(largura=15, altura=15):
    """Gera cidade em grid e retorna dados do grafo"""
    nos = {}
    arestas = {}
    vizinhos = {}
    
    # Cria nós
    id_no = 0
    for y in range(altura):
        for x in range(largura):
            eh_restaurante = (x == largura//2 and y == altura//2)
            nos[id_no] = {
                'id': id_no,
                'x': float(x),
                'y': float(y),
                'eh_restaurante': eh_restaurante
            }
            vizinhos[id_no] = []
            id_no += 1
    
    # Conecta nós adjacentes
    for y in range(altura):
        for x in range(largura):
            id_atual = y * largura + x
            
            if x < largura - 1:
                id_direita = y * largura + (x + 1)
                peso = 1.0 + random.uniform(0.1, 0.5)
                arestas[(id_atual, id_direita)] = peso
                arestas[(id_direita, id_atual)] = peso
                vizinhos[id_atual].append(id_direita)
                vizinhos[id_direita].append(id_atual)
                
            if y < altura - 1:
                id_baixo = (y + 1) * largura + x
                peso = 1.0 + random.uniform(0.1, 0.5)
                arestas[(id_atual, id_baixo)] = peso
                arestas[(id_baixo, id_atual)] = peso
                vizinhos[id_atual].append(id_baixo)
                vizinhos[id_baixo].append(id_atual)
    
    return nos, arestas, vizinhos


def obter_restaurante(nos):
    """Encontra o nó do restaurante"""
    for no in nos.values():
        if no['eh_restaurante']:
            return no
    return None


def obter_peso(arestas, id_origem, id_destino):
    """Retorna peso de uma aresta"""
    return arestas.get((id_origem, id_destino), float('inf'))


# =============================================================================
# ALGORITMO A* 
# =============================================================================

def astar(nos, arestas, vizinhos, inicio, objetivo):
    """Algoritmo A* para encontrar menor caminho"""
    if inicio == objetivo:
        return [inicio], 0.0
        
    aberto = []
    fechado = set()
    veio_de = {}
    custo_g = {inicio: 0.0}
    
    # Heurística: distância euclidiana
    no_inicio = nos[inicio]
    no_objetivo = nos[objetivo]
    h_inicio = distancia_euclidiana(no_inicio['x'], no_inicio['y'], 
                                   no_objetivo['x'], no_objetivo['y'])
    f_inicio = custo_g[inicio] + h_inicio
    
    heapq.heappush(aberto, (f_inicio, inicio, 0.0, h_inicio))
    
    while aberto:
        f_atual, id_atual, g_atual, h_atual = heapq.heappop(aberto)
        
        if id_atual == objetivo:
            caminho = reconstruir_caminho(veio_de, id_atual)
            return caminho, custo_g[id_atual]
            
        fechado.add(id_atual)
        
        for vizinho in vizinhos[id_atual]:
            if vizinho in fechado:
                continue
                
            peso = obter_peso(arestas, id_atual, vizinho)
            g_tentativo = custo_g.get(id_atual, float('inf')) + peso
            
            if g_tentativo < custo_g.get(vizinho, float('inf')):
                veio_de[vizinho] = id_atual
                custo_g[vizinho] = g_tentativo
                
                no_vizinho = nos[vizinho]
                no_objetivo = nos[objetivo]
                h = distancia_euclidiana(no_vizinho['x'], no_vizinho['y'],
                                       no_objetivo['x'], no_objetivo['y'])
                f = g_tentativo + h
                
                heapq.heappush(aberto, (f, vizinho, g_tentativo, h))
                
    return [], float('inf')


def reconstruir_caminho(veio_de, atual):
    """Reconstrói o caminho a partir do mapeamento pai-filho"""
    caminho = [atual]
    while atual in veio_de:
        atual = veio_de[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho


# =============================================================================
# K-MEANS 
# =============================================================================

def kmeans(entregas, nos, k=3):
    """Algoritmo K-Means para agrupamento"""
    if not entregas:
        return []
        
    # Converte entregas em pontos
    pontos = []
    for entrega in entregas:
        no = nos[entrega['id_no']]
        pontos.append((no['x'], no['y']))
        
    if not pontos:
        return []
        
    # Inicializa centros aleatoriamente
    centros = random.sample(pontos, min(k, len(pontos)))
    
    # Executa K-Means
    for _ in range(50):
        # Atribui pontos aos centros
        atribuicoes = []
        for entrega in entregas:
            no = nos[entrega['id_no']]
            distancias = [distancia_euclidiana(no['x'], no['y'], c[0], c[1]) 
                         for c in centros]
            melhor_centro = distancias.index(min(distancias))
            atribuicoes.append(melhor_centro)
            
        # Atualiza centros
        novos_centros = []
        for i in range(len(centros)):
            pontos_cluster = [pontos[j] for j, a in enumerate(atribuicoes) if a == i]
            if pontos_cluster:
                media_x = sum(p[0] for p in pontos_cluster) / len(pontos_cluster)
                media_y = sum(p[1] for p in pontos_cluster) / len(pontos_cluster)
                novos_centros.append((media_x, media_y))
            else:
                novos_centros.append(centros[i])
                
        centros = novos_centros
        
    return atribuicoes


# =============================================================================
# TSP SIMPLES
# =============================================================================

def tsp(nos, arestas, vizinhos, inicio, nos_entrega):
    """Algoritmo TSP Nearest Neighbor"""
    if not nos_entrega:
        return [inicio], 0.0
        
    rota = [inicio]
    nao_visitados = set(nos_entrega)
    atual = inicio
    distancia_total = 0.0
    
    while nao_visitados:
        mais_proximo = None
        menor_distancia = float('inf')
        
        for no in nao_visitados:
            _, distancia = astar(nos, arestas, vizinhos, atual, no)
            if distancia < menor_distancia:
                menor_distancia = distancia
                mais_proximo = no
                
        if mais_proximo is not None:
            rota.append(mais_proximo)
            nao_visitados.remove(mais_proximo)
            distancia_total += menor_distancia
            atual = mais_proximo
        else:
            break
            
    return rota, distancia_total


# =============================================================================
# CARREGAMENTO DE DADOS
# =============================================================================

def carregar_entregas():
    """Carrega entregas do arquivo CSV"""
    try:
        df = pd.read_csv('data/entregas.csv')
        entregas = []
        for _, row in df.iterrows():
            entrega = {
                'id': int(row['ID']),
                'nome_cliente': row['Nome_Cliente'],
                'endereco': row['Endereco'],
                'id_no': random.randint(0, 199),  # Gera ID do nó aleatoriamente
                'prioridade': random.randint(1, 3)  # Gera prioridade aleatória (1-3)
            }
            entregas.append(entrega)
        return entregas
    except Exception as e:
        print(f"Erro ao carregar entregas: {e}")
        return None


# =============================================================================
# VISUALIZAÇÃO
# =============================================================================

def visualizar_resultados(nos, rotas, grupos, entregas):
    """Visualiza os resultados"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico 1: Clusters
    ax1.set_title("Clusters de Entregas")
    for no in nos.values():
        cor = 'red' if no['eh_restaurante'] else 'lightblue'
        tamanho = 100 if no['eh_restaurante'] else 20
        ax1.scatter(no['x'], no['y'], c=cor, s=tamanho, alpha=0.7)
        
    cores = ['green', 'orange', 'purple']
    for i, grupo in enumerate(grupos):
        cor = cores[i % len(cores)]
        for idx in grupo:
            entrega = entregas[idx]
            no = nos[entrega['id_no']]
            ax1.scatter(no['x'], no['y'], c=cor, s=50, alpha=0.8, marker='s')
            
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.grid(True, alpha=0.3)
    
    # Gráfico 2: Rotas
    ax2.set_title("Rotas Otimizadas")
    for no in nos.values():
        cor = 'red' if no['eh_restaurante'] else 'lightblue'
        tamanho = 100 if no['eh_restaurante'] else 20
        ax2.scatter(no['x'], no['y'], c=cor, s=tamanho, alpha=0.7)
        
    for i, (rota, distancia) in enumerate(rotas):
        cor = cores[i % len(cores)]
        x_rota = []
        y_rota = []
        for id_no in rota:
            no = nos[id_no]
            x_rota.append(no['x'])
            y_rota.append(no['y'])
        ax2.plot(x_rota, y_rota, color=cor, linewidth=2, alpha=0.8,
                label=f'Rota {i+1}: {distancia:.1f}km')
                
    ax2.legend()
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/resultado_otimizacao.png', dpi=300, bbox_inches='tight')
    plt.show()


# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def main():
    """Função principal do sistema"""
    print("ROTA INTELIGENTE - SABOR EXPRESS")
    print("="*50)
    
    # 1. Gera cidade
    print("Gerando cidade...")
    nos, arestas, vizinhos = gerar_cidade()
    print(f"Cidade criada com {len(nos)} pontos")
    
    # 2. Carrega entregas
    print("Carregando entregas...")
    entregas = carregar_entregas()
    if not entregas:
        print("Erro: Arquivo 'entregas.csv' não encontrado!")
        return
    print(f"{len(entregas)} entregas carregadas")
    
    # 3. Agrupa entregas
    print("Agrupando entregas...")
    clusters = kmeans(entregas, nos, 3)
    
    # Converte para listas de índices
    grupos = [[] for _ in range(3)]
    for i, cluster in enumerate(clusters):
        grupos[cluster].append(i)
        
    for i, grupo in enumerate(grupos):
        print(f"   Cluster {i+1}: {len(grupo)} entregas")
        
    # 4. Otimiza rotas
    print("Otimizando rotas...")
    restaurante = obter_restaurante(nos)
    
    if not restaurante:
        print("Restaurante não encontrado!")
        return
        
    rotas = []
    for i, grupo in enumerate(grupos):
        if grupo:
            nos_entrega = [entregas[idx]['id_no'] for idx in grupo]
            rota, distancia = tsp(nos, arestas, vizinhos, restaurante['id'], nos_entrega)
            rotas.append((rota, distancia))
            print(f"   Rota {i+1}: {len(nos_entrega)} entregas, {distancia:.2f}km")
            
    # 5. Visualiza resultados
    print("Gerando visualização...")
    visualizar_resultados(nos, rotas, grupos, entregas)
    
    # 6. Resumo
    distancia_total = sum(rota[1] for rota in rotas)
    print(f"\nRESUMO:")
    print(f"   Distância total: {distancia_total:.2f} km")
    print(f"   Número de rotas: {len(rotas)}")
    print(f"   Entregas processadas: {len(entregas)}")



# =============================================================================
# EXECUÇÃO
# =============================================================================

if __name__ == "__main__":
    import os
    os.makedirs('outputs', exist_ok=True)
    
    main()