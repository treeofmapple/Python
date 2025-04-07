import sqlite3
import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

api_url = 'https://jsonplaceholder.typicode.com/posts'  # API de exemplo
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()  # Transformar resposta em formato JSON
    print(f'Dados extraídos com sucesso, {len(data)} registros.')
else:
    print("Erro ao obter dados da API.")

df = pd.DataFrame(data)

df_transformed = df[['userId', 'id', 'title', 'body']]
print(df_transformed.head())  # Exibir os primeiros registros após transformação

conn = sqlite3.connect('data_pipeline.db')

df_transformed.to_sql('posts', conn, if_exists='replace', index=False)

loaded_df = pd.read_sql('SELECT * FROM posts LIMIT 5', conn)
print(loaded_df)

conn.close()

engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

df_transformed.to_sql('posts', engine, if_exists='replace', index=False)

loaded_df = pd.read_sql('SELECT * FROM posts LIMIT 5', engine)
print(loaded_df)
