# 📊 Sales & Profit Intelligence System

## 📝 Sobre o Projeto
Este projeto foi desenvolvido para simular um cenário real de **Business Intelligence (BI)** em um E-commerce. O objetivo principal é extrair dados brutos de um banco de dados relacional e transformá-los em insights financeiros estratégicos, como faturamento e lucro real por categoria de produto.

O diferencial deste projeto é a implementação de **boas práticas de segurança**, utilizando variáveis de ambiente para proteger credenciais sensíveis.

## 🛠️ Tecnologias e Ferramentas
- **SQL (MySQL):** Modelagem de dados, criação de tabelas e consultas complexas (Joins).
- **Python:** Linguagem base para o motor de análise.
- **Pandas:** Manipulação e transformação de dados (ETL).
- **SQLAlchemy:** Integração entre a camada de aplicação e o banco de dados.
- **Matplotlib:** Geração de visualizações gráficas para suporte à decisão.
- **Python-dotenv:** Gerenciamento de variáveis de ambiente e segurança.

## 📈 Insights Gerados
A análise automatizada permite identificar:
1. **Performance por Categoria:** Visão clara de quais categorias trazem maior margem de lucro.
2. **Saúde Financeira:** Comparativo automático entre preço de custo, preço de venda e volume.
3. **Dashboard Executivo:** Gráfico de barras simplificado para apresentações gerenciais.

[Dashboard de Vendas][dashboard.png]

## 🔐 Segurança e Boas Práticas
O projeto utiliza um arquivo `.env` para armazenar as credenciais do banco de dados (Host, User, Password). Este arquivo está listado no `.gitignore` para garantir que senhas nunca sejam expostas em repositórios públicos, seguindo padrões de conformidade técnica.

## 🚀 Como executar o projeto

1. **Configurar o Banco de Dados:**
   - Execute o script `setup_banco.sql` no seu MySQL Workbench para criar a base e os dados iniciais.

2. **Configurar o Ambiente Python:**
   - Instale as dependências necessárias:
     ```bash
     pip install pandas sqlalchemy mysql-connector-python matplotlib python-dotenv
     ```

3. **Configurar as Credenciais:**
   - Crie um arquivo `.env` na raiz do projeto com as seguintes chaves:
     ```text
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_HOST=localhost
     DB_NAME=analise_vendas
     ```

4. **Rodar a Análise:**
   - Execute o comando:
     ```bash
     python analise_vendas.py
     ```

---
**Desenvolvido por Wendel - Analista de Dados Trainee**


[dashboard.png]: dashboard.png