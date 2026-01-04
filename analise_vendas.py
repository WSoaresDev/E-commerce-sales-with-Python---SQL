import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import sys

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
DATABASE = os.getenv('DB_NAME')

try:
        # Criando a conexão usando as variáveis de ambiente
        engine = create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}')
        
        # 2. Query de Analista (A mesma que você já tinha)
        query = """
        SELECT 
            p.nome_produto, p.categoria, v.quantidade, v.data_venda,
            (p.preco_venda * v.quantidade) as faturamento,
            ((p.preco_venda - p.preco_custo) * v.quantidade) as lucro_total
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id_produto;
        """

        # 3. Carregando dados no Pandas
        df = pd.read_sql(query, engine)

        # 4. Análise e Prints (Isso é o que está faltando para aparecer no terminal!)
        if not df.empty:
            analise_categoria = df.groupby('categoria')['lucro_total'].sum().reset_index()
            
            print("\n--- RELATÓRIO DE PERFORMANCE ---")
            print(f"Faturamento Total: R$ {df['faturamento'].sum():.2f}")
            print(f"Lucro Total: R$ {df['lucro_total'].sum():.2f}")
            print("\nLucro por Categoria:")
            print(analise_categoria)

            # 5. Gerar o gráfico
            plt.figure(figsize=(10,6))
            plt.bar(analise_categoria['categoria'], analise_categoria['lucro_total'], color='skyblue')
            plt.title('Lucro Total por Categoria de Produto')
            plt.ylabel('Lucro (R$)')
            plt.show()
        else:
            print("⚠️ O banco de dados retornou uma tabela vazia.")

except Exception as e:
        print(f"❌ ERRO: Verifique seu arquivo .env ou se o MySQL está ligado.")
        print(f"Detalhes: {e}")
        sys.exit()
