# O exemplo abaixo é a carga no SQL dos dados de 2024 extraídos do site da Camara dos Deputados

import pandas as pd
import psycopg2
from psycopg2 import sql
import psycopg2.extras

# Configurações do banco de dados
db_config = {
    'dbname': 'Dados_RFB',
    'user': 'postgres',
    'password': '****',
    'host': 'localhost',
    'port': '5432'
}

# Conecta ao banco de dados
conn = psycopg2.connect(**db_config)
cur = conn.cursor()

# URL do arquivo Excel
file_url = 'http://www.camara.leg.br/cotas/Ano-2024.xlsx'

# Lê o arquivo Excel diretamente do URL
df = pd.read_excel(file_url)

# Converte o DataFrame para uma lista de tuplas
data_tuples = [tuple(x) for x in df.to_numpy()]

# Cria a tabela se não existir
create_table_query = """
DROP TABLE IF EXISTS cotas_ano_2024;
CREATE TABLE IF NOT EXISTS cotas_ano_2024 (
    coluna1 text COLLATE pg_catalog."default",
    coluna2 text COLLATE pg_catalog."default",
    coluna3 text COLLATE pg_catalog."default",
    coluna4 text COLLATE pg_catalog."default",
    coluna5 text COLLATE pg_catalog."default",
    coluna6 text COLLATE pg_catalog."default",
    coluna7 text COLLATE pg_catalog."default",
    coluna8 text COLLATE pg_catalog."default",
    coluna9 text COLLATE pg_catalog."default",
    coluna10 text COLLATE pg_catalog."default",
    coluna11 text COLLATE pg_catalog."default",
    coluna12 text COLLATE pg_catalog."default",
    coluna13 text COLLATE pg_catalog."default",
    CNPJ_CPF text COLLATE pg_catalog."default",
    coluna15 text COLLATE pg_catalog."default",
    coluna16 text COLLATE pg_catalog."default",
    coluna17 text COLLATE pg_catalog."default",
    coluna18 text COLLATE pg_catalog."default",
    coluna19 text COLLATE pg_catalog."default",
    coluna20 text COLLATE pg_catalog."default",
    coluna21 text COLLATE pg_catalog."default",
    coluna22 text COLLATE pg_catalog."default",
    coluna23 text COLLATE pg_catalog."default",
    coluna24 text COLLATE pg_catalog."default",
    coluna25 text COLLATE pg_catalog."default",
    coluna26 text COLLATE pg_catalog."default",
    coluna27 text COLLATE pg_catalog."default",
    coluna28 text COLLATE pg_catalog."default",
    coluna29 text COLLATE pg_catalog."default",
    coluna30 text COLLATE pg_catalog."default",
    coluna31 text COLLATE pg_catalog."default",
    coluna32 text COLLATE pg_catalog."default"
    -- adicione mais colunas conforme necessário
);
"""
cur.execute(create_table_query)
conn.commit()

# Insere os dados na tabela
insert_query = sql.SQL("""
INSERT INTO cotas_ano_2024 (coluna1, coluna2, coluna3, coluna4, coluna5, coluna6, coluna7, coluna8, coluna9, coluna10, coluna11, coluna12, coluna13, CNPJ_CPF, coluna15, coluna16, coluna17, coluna18, coluna19, coluna20, coluna21, coluna22, coluna23, coluna24, coluna25, coluna26, coluna27, coluna28, coluna29, coluna30, coluna31, coluna32)
VALUES %s
""")
psycopg2.extras.execute_values(cur, insert_query, data_tuples)
conn.commit()

# Fecha a conexão
cur.close()
conn.close()
