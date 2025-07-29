import streamlit as st
from pymongo import MongoClient
from bson import ObjectId
import pandas as pd
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# --- Carrega variáveis de ambiente ---
load_dotenv('sensivel.env')
MONGO_URI = os.getenv("MONGO_URI")
CRYPTO_KEY = os.getenv("CRYPTO_KEY")

if not MONGO_URI:
    raise ValueError("MONGO_URI não definida no ambiente")
if not CRYPTO_KEY:
    raise ValueError("CRYPTO_KEY não definida no ambiente")

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

# --- Logout ---
def logout():
    st.session_state['authenticated'] = False
    st.rerun()

# --- Conexão MongoDB ---
client = MongoClient(MONGO_URI)
db = client["eshop_brasil"]

# --- Criptografia ---
def criptografar(texto):
    return fernet.encrypt(texto.encode()).decode()

def descriptografar(texto):
    try:
        return fernet.decrypt(texto.encode()).decode()
    except Exception:
        return "[Erro de descriptografia]"

# --- CRUD CLIENTES ---
clientes = db["clientes"]

def inserir_cliente(dados):
    dados["email"] = criptografar(dados["email"])
    return clientes.insert_one(dados)

def listar_clientes(filtros=None, page=1, page_size=20):
    query = filtros or {}
    skip = (page - 1) * page_size
    cursor = clientes.find(query).skip(skip).limit(page_size)
    docs = list(cursor)
    for d in docs:
        d["email"] = descriptografar(d.get("email", "")) if d.get("email") else ""
        d["_id"] = str(d["_id"])
    total = clientes.count_documents(query)
    return docs, total

# --- CRUD PRODUTOS ---
produtos = db["produtos"]

def inserir_produto(dados):
    return produtos.insert_one(dados)

def listar_produtos(filtros=None, page=1, page_size=20):
    query = filtros or {}
    skip = (page - 1) * page_size
    cursor = produtos.find(query).skip(skip).limit(page_size)
    docs = list(cursor)
    for d in docs:
        d["_id"] = str(d["_id"])
    total = produtos.count_documents(query)
    return docs, total

def atualizar_estoque_produto(produto_id, nova_quantidade):
    try:
        produtos.update_one({"_id": ObjectId(produto_id)}, {"$set": {"estoque": nova_quantidade}})
        return True
    except Exception as e:
        st.error(f"Erro ao atualizar estoque: {str(e)}")
        return False

# --- Telas ---
def dashboard_tela():
    st.title("Dashboard")
    st.write("Bem-vindo ao ERP da E-Shop Brasil!")

    total_clientes = clientes.count_documents({})
    total_produtos = produtos.count_documents({})

    produtos_list = list(produtos.find({}))

    estoque_total = 0
    valor_faturado = 0.0

    for prod in produtos_list:
        estoque = prod.get("estoque", 0)
        preco = prod.get("preco", 0.0)
        estoque_total += estoque
        valor_faturado += estoque * preco

    col1, col2 = st.columns(2)
    col1.metric("Total de Clientes", total_clientes)
    col2.metric("Total de Produtos", total_produtos)

    col3, col4 = st.columns(2)
    col3.metric("Estoque Total", estoque_total)
    col4.metric("Valor Faturado (R$)", f"{valor_faturado:.2f}")

def clientes_tela():
    st.title("Clientes")
    menu = st.radio("Ações", ["Inserir", "Visualizar / Editar / Deletar"], horizontal=True)

    if menu == "Inserir":
        with st.form("form_inserir_cliente"):
            nome = st.text_input("Nome Completo")
            email = st.text_input("Email")
            cidade = st.text_input("Cidade")
            submit = st.form_submit_button("Salvar")
            if submit:
                if nome and email and cidade:
                    doc = {"nome": nome, "email": email, "cidade": cidade}
                    inserir_cliente(doc)
                    st.success("Cliente inserido com sucesso!")
                else:
                    st.error("Preencha todos os campos.")

    elif menu == "Visualizar / Editar / Deletar":
        st.subheader("Buscar clientes")
        termo_busca = st.text_input("Buscar por nome, email ou cidade")

        # Monta o filtro
        filtros = {}
        if termo_busca:
            filtros = {
                "$or": [
                    {"nome": {"$regex": termo_busca, "$options": "i"}},
                    {"email": {"$regex": termo_busca, "$options": "i"}},
                    {"cidade": {"$regex": termo_busca, "$options": "i"}},
                ]
            }

        page = st.number_input("Página", min_value=1, value=1)
        clientes_list, total = listar_clientes(filtros=filtros, page=page)
        st.write(f"Total de clientes encontrados: {total}")

        if clientes_list:
            for cliente in clientes_list:
                with st.expander(f"{cliente['nome']} - {cliente['cidade']}"):
                    with st.form(f"form_editar_{cliente['_id']}"):
                        nome_edit = st.text_input("Nome", value=cliente["nome"])
                        email_edit = st.text_input("Email", value=cliente["email"])
                        cidade_edit = st.text_input("Cidade", value=cliente["cidade"])
                        col1, col2 = st.columns(2)
                        salvar = col1.form_submit_button("Salvar alterações")
                        deletar = col2.form_submit_button("Deletar")

                        if salvar:
                            novos_dados = {
                                "nome": nome_edit,
                                "email": email_edit,
                                "cidade": cidade_edit
                            }
                            atualizar_cliente(cliente["_id"], novos_dados)
                            st.success("Cliente atualizado com sucesso!")
                            st.experimental_rerun()

                        if deletar:
                            deletar_cliente(cliente["_id"])
                            st.warning("Cliente deletado.")
                            st.experimental_rerun()
        else:
            st.info("Nenhum cliente encontrado.")



    elif menu == "Visualizar":
        page = st.number_input("Página", min_value=1, value=1)
        clientes_list, total = listar_clientes(page=page)
        st.write(f"Total de clientes: {total}")
        if clientes_list:
            df = pd.DataFrame(clientes_list)
            st.dataframe(df)
        else:
            st.info("Nenhum cliente encontrado.")

def produtos_tela():
    st.title("Produtos")
    menu = st.radio("Ações", ["Inserir", "Visualizar"], horizontal=True)

    if menu == "Inserir":
        with st.form("form_inserir_produto"):
            nome = st.text_input("Nome do Produto")
            descricao = st.text_area("Descrição")
            preco = st.number_input("Preço (R$)", min_value=0.0, format="%.2f")
            estoque_inicial = st.number_input("Estoque inicial", min_value=0, step=1)
            submit = st.form_submit_button("Salvar")
            if submit:
                if nome and descricao:
                    doc = {
                        "nome": nome,
                        "descricao": descricao,
                        "preco": preco,
                        "estoque": estoque_inicial
                    }
                    inserir_produto(doc)
                    st.success("Produto inserido com sucesso!")
                else:
                    st.error("Preencha os campos obrigatórios.")

    elif menu == "Visualizar":
        page = st.number_input("Página", min_value=1, value=1)
        produtos_list, total = listar_produtos(page=page)
        st.write(f"Total de produtos: {total}")
        if produtos_list:
            df = pd.DataFrame(produtos_list)
            st.dataframe(df)
        else:
            st.info("Nenhum produto encontrado.")

def estoque_tela():
    st.title("Estoque")

    produtos_list, _ = listar_produtos(page=1, page_size=1000)
    if not produtos_list:
        st.info("Nenhum produto cadastrado.")
        return

    # Agrupa os produtos por nome somando os estoques
    df = pd.DataFrame(produtos_list)
    df_agrupado = df.groupby("nome", as_index=False).agg({
        "estoque": "sum",
        "descricao": "first",
        "preco": "mean"
    }).rename(columns={"nome": "Produto", "estoque": "Estoque", "descricao": "Descrição", "preco": "Preço Médio (R$)"})

    st.subheader("Estoque Agrupado por Produto")
    st.dataframe(df_agrupado)

    st.write("---")
    st.subheader("Registrar movimentação de estoque")

    # Para movimentação vamos usar os produtos originais (não agrupados) para escolher por nome e ID
    options = {f"{p['nome']} (Estoque atual: {p.get('estoque', 0)})": p['_id'] for p in produtos_list}
    selecionado = st.selectbox("Produto", list(options.keys()))
    produto_id = options[selecionado]

    tipo = st.selectbox("Tipo de movimentação", ["Entrada", "Saída"])
    quantidade = st.number_input("Quantidade", min_value=1, step=1)

    if st.button("Registrar movimentação"):
        produto = produtos.find_one({"_id": ObjectId(produto_id)})
        if not produto:
            st.error("Produto não encontrado.")
            return

        estoque_atual = produto.get("estoque", 0)
        if tipo == "Entrada":
            novo_estoque = estoque_atual + quantidade
        else:
            novo_estoque = estoque_atual - quantidade
            if novo_estoque < 0:
                st.error("Quantidade insuficiente em estoque para saída.")
                return

        sucesso = atualizar_estoque_produto(produto_id, novo_estoque)
        if sucesso:
            st.success(f"Movimentação registrada! Estoque atualizado: {novo_estoque}")
        else:
            st.error("Falha ao atualizar estoque.")

# --- Controle principal ---
if not st.session_state['authenticated']:
    login()
    st.stop()

st.sidebar.title("Menu")
menu = st.sidebar.selectbox("Seção", ["Dashboard", "Clientes", "Produtos", "Estoque", "Sair"])

if menu == "Sair":
    logout()
elif menu == "Dashboard":
    dashboard_tela()
elif menu == "Clientes":
    clientes_tela()
elif menu == "Produtos":
    produtos_tela()
elif menu == "Estoque":
    estoque_tela()
