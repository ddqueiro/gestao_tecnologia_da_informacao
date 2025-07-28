# app.py
import streamlit as st
from pymongo import MongoClient
from bson import ObjectId
import pandas as pd
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# --- Carrega variáveis de ambiente ---
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:1234@localhost:27017/eshop_brasil?authSource=admin")
CRYPTO_KEY = os.getenv("CRYPTO_KEY") or Fernet.generate_key().decode()
fernet = Fernet(CRYPTO_KEY.encode())

# --- Inicializa sessão ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# --- Login ---
def login():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if username == "admin" and password == "1234":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

# --- Controle de autenticação ---
if not st.session_state['authenticated']:
    login()
    st.stop()

# --- Conexão MongoDB ---
client = MongoClient(MONGO_URI)
db = client["eshop_brasil"]
clientes = db["clientes"]


# --- Funções auxiliares ---
def criptografar(texto):
    return fernet.encrypt(texto.encode()).decode()

def descriptografar(texto):
    return fernet.decrypt(texto.encode()).decode()

# --- CRUD ---
def inserir_cliente(dados):
    dados["email"] = criptografar(dados["email"])
    return clientes.insert_one(dados)

def inserir_clientes(lista_dados):
    for d in lista_dados:
        d["email"] = criptografar(d["email"])
    return clientes.insert_many(lista_dados)

def listar_clientes():
    dados = list(clientes.find())
    for d in dados:
        try:
            d["email"] = descriptografar(d["email"])
        except:
            d["email"] = "[Erro de descriptografia]"
    return dados

def atualizar_cliente(id_str, novos_dados):
    try:
        _id = ObjectId(id_str)
        novos_dados["email"] = criptografar(novos_dados["email"])
    except Exception:
        st.error("ID inválido!")
        return
    return clientes.update_one({"_id": _id}, {"$set": novos_dados})

def deletar_cliente(id_str):
    try:
        _id = ObjectId(id_str)
    except Exception:
        st.error("ID inválido!")
        return
    return clientes.delete_one({"_id": _id})


# --- Interface Streamlit ---
st.title("E-Shop Brasil - Gestão de Clientes")

def logout():
    st.session_state['authenticated'] = False
    st.rerun()

if st.sidebar.button("Sair"):
    logout()

menu = st.sidebar.selectbox("Menu", ["Inserir", "Visualizar", "Editar", "Excluir", "Buscar"])



if menu == "Inserir":
    st.header("Inserir novo cliente")
    with st.form("form_inserir"):
            nome = st.text_input("Nome")
            email = st.text_input("Email")
            cidade = st.text_input("Cidade")
            produto = st.selectbox("Produto", ["Notebook", "Celular", "Tênis", "Livro", "Fone"])
            valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
            submit = st.form_submit_button("Salvar")
            if submit:
                if nome and email and cidade:
                    doc = {"nome": nome, "email": email, "cidade": cidade, "produto": produto, "valor": valor}
                    inserir_cliente(doc)
                    st.success("Cliente inserido com sucesso!")
                else:
                    st.error("Preencha todos os campos!")


elif menu == "Visualizar":
    st.header("Lista de clientes")
    
    if 'page_visualizar' not in st.session_state:
        st.session_state.page_visualizar = 1

    page_size = 50
    total_docs = clientes.count_documents({})
    total_pages = (total_docs // page_size) + (1 if total_docs % page_size > 0 else 0)

    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.button("Anterior") and st.session_state.page_visualizar > 1:
            st.session_state.page_visualizar -= 1
    with col3:
        if st.button("Próximo") and st.session_state.page_visualizar < total_pages:
            st.session_state.page_visualizar += 1

    st.write(f"Página {st.session_state.page_visualizar} de {total_pages} — Total clientes: {total_docs}")

    skip_count = (st.session_state.page_visualizar - 1) * page_size
    clientes_cursor = clientes.find().skip(skip_count).limit(page_size)
    clientes_list = list(clientes_cursor)

    for d in clientes_list:
        try:
            d["email"] = descriptografar(d["email"])
        except:
            d["email"] = "[Erro de descriptografia]"

    if clientes_list:
        df = pd.DataFrame(clientes_list)
        df['_id'] = df['_id'].astype(str)
        st.dataframe(df)
    else:
        st.info("Nenhum cliente encontrado.")


elif menu == "Editar":
    st.header("Editar cliente")
    clientes_list = listar_clientes()
    if clientes_list:
        opcoes = {f"{c['nome']} - {c['_id']}": str(c['_id']) for c in clientes_list}
        selecionado = st.selectbox("Escolha o cliente para editar", list(opcoes.keys()))
        id_cliente = opcoes[selecionado]
        cliente = clientes.find_one({"_id": ObjectId(id_cliente)})

        with st.form("form_editar"):
            nome = st.text_input("Nome", value=cliente.get("nome", ""))
            email = st.text_input("Email", value=descriptografar(cliente.get("email", "")))
            cidade = st.text_input("Cidade", value=cliente.get("cidade", ""))
            produtos = ["Notebook", "Celular", "Tênis", "Livro", "Fone"]
            produto_index = produtos.index(cliente.get("produto", "Notebook")) if cliente.get("produto") in produtos else 0
            produto = st.selectbox("Produto", produtos, index=produto_index)
            valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f", value=cliente.get("valor", 0.0))
            submit = st.form_submit_button("Atualizar")

            if submit:
                if nome and email and cidade:
                    novos_dados = {"nome": nome, "email": email, "cidade": cidade, "produto": produto, "valor": valor}
                    atualizar_cliente(id_cliente, novos_dados)
                    st.success("Cliente atualizado com sucesso!")
                else:
                    st.error("Por favor, preencha todos os campos obrigatórios!")
    else:
        st.info("Nenhum cliente para editar.")

elif menu == "Excluir":
    st.header("Excluir cliente")
    clientes_list = listar_clientes()
    if clientes_list:
        opcoes = {f"{c['nome']} - {c['_id']}": str(c['_id']) for c in clientes_list}
        selecionado = st.selectbox("Escolha o cliente para excluir", list(opcoes.keys()))
        id_cliente = opcoes[selecionado]

        if st.button("Excluir"):
            deletar_cliente(id_cliente)
            st.warning("Cliente excluído com sucesso!")
    else:
        st.info("Nenhum cliente para excluir.")

elif menu == "Buscar":
    st.header("Buscar clientes")
    nome_filtro = st.text_input("Filtrar por nome")
    cidade_filtro = st.text_input("Filtrar por cidade")
    produto_filtro = st.selectbox("Filtrar por produto", ["", "Notebook", "Celular", "Tênis", "Livro", "Fone"])

    query = {}
    if nome_filtro:
        query["nome"] = {"$regex": nome_filtro, "$options": "i"}
    if cidade_filtro:
        query["cidade"] = {"$regex": cidade_filtro, "$options": "i"}
    if produto_filtro:
        query["produto"] = produto_filtro

    if 'page_buscar' not in st.session_state:
        st.session_state.page_buscar = 1

    page_size = 50
    total_docs = clientes.count_documents(query)
    total_pages = (total_docs // page_size) + (1 if total_docs % page_size > 0 else 0)

    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.button("Anterior") and st.session_state.page_buscar > 1:
            st.session_state.page_buscar -= 1
    with col3:
        if st.button("Próximo") and st.session_state.page_buscar < total_pages:
            st.session_state.page_buscar += 1

    st.write(f"Página {st.session_state.page_buscar} de {total_pages} — Total clientes: {total_docs}")

    skip_count = (st.session_state.page_buscar - 1) * page_size
    resultados_cursor = clientes.find(query).skip(skip_count).limit(page_size)
    resultados = list(resultados_cursor)

    for r in resultados:
        try:
            r["email"] = descriptografar(r["email"])
        except:
            r["email"] = "[Erro de descriptografia]"

    if resultados:
        df = pd.DataFrame(resultados)
        df['_id'] = df['_id'].astype(str)
        st.dataframe(df)
    else:
        st.info("Nenhum cliente encontrado com esses filtros.")
