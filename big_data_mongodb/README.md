
# Aplicação Prática de Tecnologias de Banco de Dados e Big Data em uma Empresa de Comércio Eletrônico

## 1. Introdução

A E-Shop Brasil é uma das maiores plataformas de comércio eletrônico do país, atendendo milhões de clientes em todo o território nacional. Com um crescimento expressivo e um volume enorme de dados gerados diariamente, a empresa enfrenta desafios relacionados à gestão de dados, personalização da experiência do cliente e otimização logística.

Este projeto propõe uma solução prática que utiliza tecnologias de banco de dados (SQL, NoSQL) e Big Data para superar esses desafios, garantindo segurança, personalização e eficiência operacional.

## 2. Objetivos

- Garantir a segurança e privacidade dos dados dos clientes, conforme a LGPD.
- Oferecer experiências personalizadas baseadas no comportamento do usuário.
- Otimizar a logística, especialmente para regiões remotas.
- Criar uma solução escalável e sustentável a longo prazo.
- Implementar uma aplicação web interativa para gerenciar clientes usando Streamlit e MongoDB.

## 3. Configuração e Execução

### Criar ambiente virtual e instalar dependências:

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate.bat    # Windows
pip install -r requirements.txt
```

### Configurar variáveis de ambiente

Crie um arquivo `.env` com:

```env
MONGO_URI=mongodb://admin:1234@localhost:27017/admin
CRYPTO_KEY=2Mxyq_FCLOyRRysYz3X8aRKUQzJ7sbZ3iy0wK8cgE7c=
```

### Popular o banco com dados fake:

```bash
python dados_fakes.py
```

### Executar a aplicação:

```bash
streamlit run app.py
```

Acesse no navegador: `http://localhost:8501`

## 4. Funcionalidades da Aplicação

- **Login Seguro:** Autenticação simples para proteger o acesso;
- **Inserção:** Cadastro de novos clientes com validação de campos;
- **Visualização:** Listagem paginada com informações detalhadas;
- **Edição:** Alteração dos dados dos clientes com descriptografia dos e-mails;
- **Exclusão:** Remoção segura de registros;
- **Busca:** Filtros por nome, cidade e produto para facilitar consultas;
- **Logout:** Finalização da sessão atual.

## 5. Testes e Exemplos

Incluido na pasta `/exemplos` imagens:

- Tela de login;
- Inserção de cliente;
- Visualização e paginação de clientes;
- Edição e exclusão de registros;
- Busca por filtros.

## 6. Considerações Técnicas e de Segurança

- Os dados de e-mail são criptografados no banco para proteger a privacidade;
- O MongoDB exige autenticação para acessar as coleções;
- Docker isola o ambiente de banco, facilitando o deploy e a replicação do ambiente;
- Paginação e filtros garantem performance na manipulação de grandes volumes de dados.

## 7. Estrutura do Repositório

```
├── README.md
├── app.py
├── dados_fakes.py
├── docker-compose.yml
├── requirements.txt
├── .env
└── exemplos/           # Prints da aplicação
```

---

## Contexto do Projeto

### Cenário

A E-Shop Brasil possui uma ampla gama de produtos e processa mais de 100 mil pedidos por dia. Com o aumento do volume de dados e complexidade, enfrenta desafios em:

- Gestão de dados com foco em segurança e privacidade;
- Personalização da experiência do cliente;
- Otimização da logística e integração omnichannel.

### Desafios Centrais

- Garantir a segurança e privacidade dos dados (LGPD);
- Analisar dados para recomendações personalizadas;
- Otimizar a entrega e gestão de estoque, especialmente em regiões remotas;
- Integrar operações online e offline.

### Soluções Propostas

- Uso de banco de dados NoSQL para flexibilidade e escalabilidade;
- Ferramentas de Big Data para análise avançada;
- Sistema integrado para melhorar eficiência operacional;
- Aplicação em Streamlit para gerenciamento prático dos dados.

---

