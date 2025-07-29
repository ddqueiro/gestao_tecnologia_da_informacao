
# Aplicação Prática de Tecnologias de Banco de Dados e Big Data em uma Empresa de Comércio Eletrônico — E-Shop Brasil

---

## Estrutura do Repositório

```
├── README.md                 # Você está aqui
├── docker-compose.yml        # Configuração dos containers MongoDB e Spark
├── Dockerfile.spark          # Dockerfile para container Spark 
├── app.py                    # Aplicação Streamlit principal
├── popular_dados.py          # Script para popular o banco com dados fake
├── requirements.txt          # Dependências Python
├── sensivel.env              # Variáveis de ambiente 
└── exemplos/                 # Prints demonstrativos do streamlit
```


## 1. Introdução

A E-Shop Brasil é uma das maiores plataformas de comércio eletrônico do país, atendendo milhões de clientes e processando milhares de pedidos diariamente. Com o crescimento da empresa, surgem desafios relacionados à gestão eficiente dos dados, personalização da experiência do cliente e otimização logística.

Este projeto apresenta uma solução prática baseada em tecnologias modernas de banco de dados e Big Data, utilizando MongoDB, Docker, Streamlit e criptografia para atender às necessidades da E-Shop Brasil.

---

## 2. Apresentação do Problema e Contexto

A empresa enfrenta os seguintes desafios principais:

- **Gestão de Dados:** garantir a segurança e privacidade dos dados dos clientes, conforme a LGPD, e melhorar a análise para recomendações personalizadas.
- **Otimização da Logística:** aprimorar o controle de estoques, otimizar entregas e integrar canais online e offline para uma experiência omnichannel eficiente.
- **Escalabilidade:** manter um ambiente tecnológico que suporte o crescimento da base de clientes e pedidos.

---

## 3. Objetivos do Projeto

- Criar um ambiente isolado e padronizado para desenvolvimento e operação utilizando Docker.
- Implementar um banco de dados NoSQL MongoDB para armazenamento flexível dos dados.
- Desenvolver uma aplicação web interativa em Streamlit para operações CRUD de clientes, produtos e estoque.
- Garantir a segurança dos dados sensíveis com criptografia.
- Fornecer um mecanismo para popular o banco com dados fake para testes e demonstrações.
- Facilitar a execução e manutenção da solução por meio de documentação clara e organização do código.

---

## 4. Descrição do Projeto

### 4.1 Uso do Docker

O Docker é utilizado para criar um ambiente isolado e padronizado, eliminando problemas de configuração local e facilitando o deploy. A infraestrutura é orquestrada pelo `docker-compose.yml`, que configura:

- Um container com MongoDB, configurado com usuário e senha, persistência de dados e rede dedicada.
- Um container opcional para Spark (processamento Big Data), com Dockerfile próprio e dependência do MongoDB.

### 4.2 Container MongoDB

- Baseado na imagem oficial `mongo:latest`.
- Configurado para rodar na porta 27017.
- Volume persistente para garantir a integridade dos dados.
- Usuário administrador `admin` com senha `1234` (que pode ser alterado conforme a necessidade).

### 4.3 Aplicação Streamlit (`app.py`)

- Conecta-se ao MongoDB via URI configurada em variáveis de ambiente.
- Implementa login básico para controle de acesso.
- Permite inserir, editar, excluir e listar dados de clientes e produtos.
- Manipula o estoque com controle de entrada e saída.
- Criptografa o campo email dos clientes usando `cryptography.Fernet` para proteger dados sensíveis.
- Exibe métricas importantes no dashboard.
- Suporta paginação e filtros para facilitar a navegação pelos registros.

### 4.4 Script de Dados Fake (`popular_dados.py`)

- Gera e insere dados falsos para clientes e produtos usando a biblioteca Faker.
- Criptografa emails dos clientes para manter a consistência com a aplicação.
- Permite popular rapidamente o banco para testes e demonstrações.

---

## 5. Passos para Implementação

### 5.1 Configurar variáveis de ambiente

Crie um arquivo `sensivel.env` na raiz do projeto com o seguinte conteúdo:

```env
MONGO_URI=mongodb://admin:1234@localhost:27017/eshop_brasil?authSource=admin
CRYPTO_KEY=R3jehhSUPlzUFGAfm5Oha_iGlL-k_Nm8fXwye6gM7-A=
```

> **Importante:** A chave `CRYPTO_KEY` deve ser uma chave Fernet válida. Para gerar uma nova chave, execute:

```python
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
```

### 5.2 Instalar dependências Python

No ambiente Python que rodará a aplicação, instale as dependências:

```bash
pip install -r requirements.txt
```

### 5.3 Subir a infraestrutura Docker

Execute na raiz do projeto:

```bash
docker-compose up -d
```

Esse comando iniciará o MongoDB e o container Spark (se presente).

### 5.4 Popular o banco com dados fake (opcional)

Para popular a base de dados com dados fictícios para testes, execute:

```bash
python popular_dados.py
```

Isso vai gerar e inserir 100.000 clientes e 1.000 produtos fake, criptografando os emails.

### 5.5 Executar a aplicação Streamlit

Para iniciar a aplicação web:

```bash
streamlit run app.py
```

Acesse o sistema pelo navegador no endereço [http://localhost:8501](http://localhost:8501).

---

## 6. Funcionalidades da Aplicação

- **Login:** Acesso protegido com usuário e senha.
- **Dashboard:** Exibe métricas como total de clientes, total de produtos, estoque total e valor faturado.
- **Clientes:** Inserção, edição, exclusão, busca e paginação de clientes. Os emails são criptografados no banco.
- **Produtos:** Inserção, listagem, visualização de detalhes e controle de estoque.
- **Estoque:** Visualização do estoque agregado por produto, registro de movimentações de entrada e saída com validação.
- **Segurança:** Criptografia e descriptografia dos emails com Fernet.

---

## 7. Testes e Exemplos

A pasta exemplos/ contém imagens que demonstram as principais funcionalidades da aplicação:

- **login.JPG:** Tela de login e autenticação do usuário.
- **dashboard.JPG:** Visão geral do dashboard com métricas de clientes, produtos, estoque e faturamento.
- **clientes inserir.JPG:** Formulário para inserir novos clientes.
- **cliente buscar.JPG:** Interface para busca e listagem de clientes com filtros.
- **editar e deletar.JPG:** Tela para editar ou excluir registros de clientes.
- **produtos inserir e visualizar.JPG:** Inserção e visualização de produtos cadastrados.
- **estoque.JPG:** Controle e movimentação do estoque de produtos.

Esses exemplos auxiliam na compreensão das funcionalidades implementadas e no uso prático da aplicação.

---

```

