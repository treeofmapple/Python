import sqlite3
import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Passo 1: Extração de dados
# Exemplo de uma API, você pode substituir pela URL da sua API
api_url = 'https://jsonplaceholder.typicode.com/posts'  # API de exemplo
response = requests.get(api_url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Transformar resposta em formato JSON
    print(f'Dados extraídos com sucesso, {len(data)} registros.')
else:
    print("Erro ao obter dados da API.")

# Passo 2: Transformação dos dados
# Criando um DataFrame do Pandas para manipulação
df = pd.DataFrame(data)

# Exemplo de transformação: Vamos simplificar os dados e pegar apenas alguns campos
df_transformed = df[['userId', 'id', 'title', 'body']]
print(df_transformed.head())  # Exibir os primeiros registros após transformação

# Passo 3: Carregar os dados no banco SQLite
# Conectar ao banco SQLite (ou criar o banco se não existir)
conn = sqlite3.connect('data_pipeline.db')

# Criar tabela no banco de dados, se não existir
df_transformed.to_sql('posts', conn, if_exists='replace', index=False)

# Verificar se os dados foram carregados corretamente
loaded_df = pd.read_sql('SELECT * FROM posts LIMIT 5', conn)
print(loaded_df)

# Fechar a conexão
conn.close()

# Passo 3: Carregar os dados no PostgreSQL
engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

# Carregar os dados na tabela 'posts'
df_transformed.to_sql('posts', engine, if_exists='replace', index=False)

# Verificar se os dados foram carregados
loaded_df = pd.read_sql('SELECT * FROM posts LIMIT 5', engine)
print(loaded_df)
