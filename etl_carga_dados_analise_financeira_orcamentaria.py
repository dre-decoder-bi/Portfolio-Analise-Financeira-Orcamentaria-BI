import pandas as pd
from sqlalchemy import create_engine
import os

print("--- Iniciando Carga (LOAD) para o Banco de Dados POSTGRESQL ---")

ARQUIVO_ORCADO = 'orcamento.csv'
ARQUIVO_REALIZADO = 'realizado.csv'

DATABASE_URL = "postgresql://postgres:[SUA_SENHA_AQUI]@[SEU_HOST_AQUI]/postgres"

if not os.path.exists(ARQUIVO_ORCADO) or not os.path.exists(ARQUIVO_REALIZADO):
    print(f"ERRO: Arquivo '{ARQUIVO_ORCADO}' ou '{ARQUIVO_REALIZADO}' não encontrado.")
    print("Execute os scripts 'gerar_orcamento.py' e 'gerar_realizado.py' primeiro.")
elif DATABASE_URL == "COLE_A_STRING_DE_CONEXÃO_AQUI":
    print("ERRO: Você não editou o script!")
    print("Por favor, cole sua string de conexão na variável 'DATABASE_URL'.")
else:
    try:
        print(f"Lendo {ARQUIVO_ORCADO}...")
        df_orcamento = pd.read_csv(ARQUIVO_ORCADO, sep=';')
        
        print(f"Lendo {ARQUIVO_REALIZADO}...")
        df_realizado = pd.read_csv(ARQUIVO_REALIZADO, sep=';')
        print("Arquivos CSV lidos com sucesso.")

        print(f"Conectando ao banco de dados PostgreSQL na nuvem (Supabase)...")
        engine = create_engine(DATABASE_URL)
        
        with engine.connect() as conn:
            print("Conexão estabelecida com sucesso.")

        print("Carregando tabela 'orcamento'...")
        df_orcamento.to_sql('orcamento', engine, if_exists='replace', index=False, schema='public')
        
        print("Carregando tabela 'realizado'...")
        df_realizado.to_sql('realizado', engine, if_exists='replace', index=False, schema='public')

        print("\n--- SUCESSO ---")
        print("Dados dos arquivos CSV foram carregados com sucesso no banco PostgreSQL (Supabase).")

    except Exception as e:
        print(f"\n--- ERRO DURANTE A EXECUÇÃO ---")
        print(f"Ocorreu um problema: {e}")
        print("\nVerifique se:")
        print("1. A sua string de conexão está correta.")
        print("2. Você substituiu o '[YOUR-PASSWORD]' pela sua senha real.")
        print("3. Você tem conexão com a internet.")