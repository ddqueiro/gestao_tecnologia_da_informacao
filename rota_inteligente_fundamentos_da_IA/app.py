import os
import pandas as pd
import folium
import openrouteservice
from sklearn.cluster import KMeans
import time
from dotenv import load_dotenv

# ===== CONFIGURAÇÃO =====
load_dotenv()
ORS_API_KEY = os.getenv("ORS_API_KEY")
if not ORS_API_KEY:
    raise ValueError("Favor definir ORS_API_KEY no arquivo .env")

N_CLUSTERS = 2  # Número de clusters/entregadores
CSV_PATH = "data/entregas.csv"

# ===== 1. CARREGAR CSV =====
df = pd.read_csv(CSV_PATH)

# ===== 2. GEOCODIFICAR ENDEREÇOS =====
client = openrouteservice.Client(key=ORS_API_KEY)

latitudes = []
longitudes = []

for endereco in df["endereco"]:
    try:
        resp = client.pelias_search(text=endereco)
        coord = resp['features'][0]['geometry']['coordinates']  # [lon, lat]
        longitudes.append(coord[0])
        latitudes.append(coord[1])
    except Exception as e:
        print("Erro geocodificando:", endereco, e)
        longitudes.append(None)
        latitudes.append(None)
    time.sleep(1)  # respeitar limite free ORS

df["longitude"] = longitudes
df["latitude"] = latitudes
df = df.dropna()

# ===== 3. AGRUPAMENTO K-MEANS =====
coords = df[["longitude", "latitude"]].values
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42)
df["cluster"] = kmeans.fit_predict(coords)

# ===== 4. CRIAR MAPA =====
mapa = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=14)
colors = ["red", "blue", "green", "purple", "orange"]

# ===== 5. CALCULAR ROTAS OTIMIZADAS POR CLUSTER =====
for cluster_id in df["cluster"].unique():
    pontos_cluster = df[df["cluster"] == cluster_id][["longitude", "latitude"]].values.tolist()
    
    if len(pontos_cluster) > 1:
        # Pedir a rota otimizada ao ORS (mais curta possível)
        rota = client.directions(
            coordinates=pontos_cluster,
            profile="driving-car",
            format="geojson",
            optimize_waypoints=True  # otimiza ordem dos pontos
        )
        folium.GeoJson(
            rota,
            name=f"Rota Cluster {cluster_id}",
            style_function=lambda x, cid=cluster_id: {
                "color": colors[cid % len(colors)],
                "weight": 5,
                "opacity": 0.7
            }
        ).add_to(mapa)
    
    # Marcadores
    for _, row in df[df["cluster"] == cluster_id].iterrows():
        folium.Marker(
            [row["latitude"], row["longitude"]],
            popup=f"Entrega {row['id']} (Cluster {cluster_id})\n{row['endereco']}",
            icon=folium.Icon(color=colors[cluster_id % len(colors)])
        ).add_to(mapa)

# ===== 6. SALVAR MAPA =====
mapa.save("rotas_otimizadas.html")
print("Mapa gerado: rotas_otimizadas.html")
print("Processo concluído!")
