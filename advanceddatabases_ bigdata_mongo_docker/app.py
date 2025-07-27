import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Conexão com o MongoDB
client = MongoClient("mongodb+srv://<USUÁRIO>:<SENHA>@<SEU_CLUSTER>.mongodb.net/?retryWrites=true&w=majority")
db = client["eshop_db"]
colecao_clientes = db["clientes"]

# Título do sistema
st.title("E-Shop | Aplicação Prática de Tecnologias de Banco de Dados e Big Data")

# Menu
menu = st.sidebar.radio("Navegar", [
    "Cadastrar Cliente",
    "Visualizar Clientes",
    "Editar ou Excluir Cliente",
    "Buscar por Filtros"
])

# Cadastrar cliente
if menu == "Cadastrar Cliente":
    st.subheader("Cadastro de Cliente")
    with st.form("form_cliente"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        cidade = st.text_input("Cidade")
        estado = st.text_input("Estado")
        produto = st.selectbox("Produto", ["Notebook", "Smartphone", "Fone de Ouvido", "Smartwatch", "Livro"])
        preco = st.number_input("Valor da Compra (R$)", min_value=0.0, step=0.01)
        enviado = st.form_submit_button("Salvar")

        if enviado:
            colecao_clientes.insert_one({
                "nome": nome,
                "email": email,
                "cidade": cidade,
                "estado": estado,
                "produto": produto,
                "preco": preco
            })
            st.success("Cliente cadastrado com sucesso!")

# Visualizar dados
elif menu == "Visualizar Clientes":
    st.subheader("Lista de Clientes")
    dados = list(colecao_clientes.find({}, {"_id": 0}))
    if dados:
        df = pd.DataFrame(dados)
        st.dataframe(df)
    else:
        st.info("Nenhum cliente encontrado.")

# Editar ou excluir
elif menu == "Editar ou Excluir Cliente":
    st.subheader("Editar ou Excluir Cliente")
    clientes = list(colecao_clientes.find())
    if clientes:
        nomes = [f"{c['nome']} ({str(c['_id'])})" for c in clientes]
        selecionado = st.selectbox("Selecione um cliente:", nomes)
        cliente = clientes[nomes.index(selecionado)]
        novo_nome = st.text_input("Nome", value=cliente["nome"])
        novo_email = st.text_input("Email", value=cliente["email"])
        nova_cidade = st.text_input("Cidade", value=cliente["cidade"])
        novo_estado = st.text_input("Estado", value=cliente["estado"])
        novo_produto = st.selectbox("Produto", ["Notebook", "Smartphone", "Fone de Ouvido", "Smartwatch", "Livro"], index=["Notebook", "Smartphone", "Fone de Ouvido", "Smartwatch", "Livro"].index(cliente["produto"]))
        novo_preco = st.number_input("Valor da Compra (R$)", value=float(cliente["preco"]))

        col1, col2 = st.columns(2)
        if col1.button("Atualizar"):
            colecao_clientes.update_one(
                {"_id": cliente["_id"]},
                {"$set": {
                    "nome": novo_nome,
                    "email": novo_email,
                    "cidade": nova_cidade,
                    "estado": novo_estado,
                    "produto": novo_produto,
                    "preco": novo_preco
                }}
            )
            st.success("Dados atualizados.")
        if col2.button("Excluir"):
            colecao_clientes.delete_one({"_id": cliente["_id"]})
            st.warning("Cliente excluído com sucesso.")
    else:
        st.info("Não há clientes cadastrados.")

# Filtros
elif menu == "Buscar por Filtros":
    st.subheader("Filtrar Clientes")
    cidade_filtro = st.text_input("Cidade")
    produto_filtro = st.selectbox("Produto", ["", "Notebook", "Smartphone", "Fone de Ouvido", "Smartwatch", "Livro"])

    query = {}
    if cidade_filtro:
        query["cidade"] = cidade_filtro
    if produto_filtro:
        query["produto"] = produto_filtro

    resultados = list(colecao_clientes.find(query, {"_id": 0}))
    if resultados:
        st.dataframe(pd.DataFrame(resultados))
    else:
        st.info("Nenhum cliente encontrado com esse filtro.")
