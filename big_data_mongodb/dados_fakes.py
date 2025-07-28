from pymongo import MongoClient
from faker import Faker

def popular_mongodb(uri, db_name="eshop_brasil", colecao="clientes", total_docs=1_000_000, batch_size=100_000):
    fake = Faker()
    client = MongoClient(uri)
    db = client[db_name]
    clientes = db[colecao]

    produtos = ["Notebook", "Celular", "Tênis", "Livro", "Fone"]

    print(f"Iniciando inserção de {total_docs} documentos na coleção '{colecao}' do banco '{db_name}'")

    for i in range(0, total_docs, batch_size):
        batch = []
        for _ in range(batch_size):
            batch.append({
                "nome": fake.name(),
                "email": fake.email(),
                "cidade": fake.city(),
                "produto": fake.random.choice(produtos),
                "valor": round(fake.random.uniform(50, 2000), 2)
            })
        clientes.insert_many(batch)
        print(f"Batch {i // batch_size + 1} inserido ({i + batch_size} de {total_docs})")

    print("Inserção concluída!")

if __name__ == "__main__":
    MONGO_URI = "mongodb://localhost:27017"  # ajuste da uri

    popular_mongodb(MONGO_URI)
