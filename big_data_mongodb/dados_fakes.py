from pymongo import MongoClient
from faker import Faker
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
import random


from dotenv import load_dotenv
load_dotenv("sensivel.env")
print("CRYPTO_KEY:", os.getenv("CRYPTO_KEY"))
print("MONGO_URI:", os.getenv("MONGO_URI"))


def popular_mongodb(uri, db_name="eshop_brasil", total_clientes=100_000, total_produtos=1000):
    fake = Faker()
    client = MongoClient(uri)
    db = client[db_name]
    clientes = db["clientes"]
    produtos = db["produtos"]

    CRYPTO_KEY = os.getenv("CRYPTO_KEY")
    if not CRYPTO_KEY:
        raise ValueError("CRYPTO_KEY não definida no ambiente")
    fernet = Fernet(CRYPTO_KEY.encode())

    produtos_nomes = ["Notebook", "Celular", "Tênis", "Livro", "Fone", "Monitor", "Teclado", "Mouse", "Cadeira", "Mesa"]

    print(f"Iniciando inserção de {total_clientes} clientes...")
    batch_size = 10_000
    for i in range(0, total_clientes, batch_size):
        batch = []
        for _ in range(min(batch_size, total_clientes - i)):
            email_plain = fake.email()
            email_crypt = fernet.encrypt(email_plain.encode()).decode()
            batch.append({
                "nome": fake.name(),
                "email": email_crypt,
                "cidade": fake.city(),
            })
        clientes.insert_many(batch)
        print(f"Clientes: Inseridos {i + len(batch)} de {total_clientes}")

    print(f"Iniciando inserção de {total_produtos} produtos...")
    batch_size = 500
    for i in range(0, total_produtos, batch_size):
        batch = []
        for _ in range(min(batch_size, total_produtos - i)):
            nome = random.choice(produtos_nomes)
            descricao = fake.text(max_nb_chars=100)
            preco = round(random.uniform(50, 2000), 2)
            estoque = random.randint(0, 1000)
            batch.append({
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                "estoque": estoque
            })
        produtos.insert_many(batch)
        print(f"Produtos: Inseridos {i + len(batch)} de {total_produtos}")

    print("Inserção concluída!")

if __name__ == "__main__":
    MONGO_URI = "mongodb://admin:1234@localhost:27017/eshop_brasil?authSource=admin"   
    popular_mongodb(MONGO_URI)
