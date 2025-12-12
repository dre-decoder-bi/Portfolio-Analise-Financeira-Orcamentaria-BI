import pandas as pd
import random
from faker import Faker

print("--- Iniciando Geração do REALIZADO (Actual) ---")

# Inicia o Faker
fake = Faker('pt_BR')

# 1. Usa as mesmas dimensões do script anterior
centros_custo_ids = [100, 200, 300, 400]
contas_contabeis_ids = [5001, 5002, 5003, 5004]

# 2. Gera os dados transacionais
QTD_TRANSACOES = 20000
dados_realizado = []

for i in range(1, QTD_TRANSACOES + 1):
    # Escolhe aleatoriamente uma conta e cc
    conta_id = random.choice(contas_contabeis_ids)
    cc_id = random.choice(centros_custo_ids)
    
    # Gera um valor de transação
    if conta_id == 5004:
        valor_gasto = random.uniform(1500, 8000)
    elif conta_id == 5002:
        valor_gasto = random.uniform(50, 1200)
    else:
        valor_gasto = random.uniform(20, 500)
        
    dados_realizado.append({
        'id_transacao': 10000 + i,
        'data_transacao': fake.date_between(start_date='-1y', end_date='today'), # Transações do último ano
        'id_centro_custo': cc_id,
        'id_conta_contabil': conta_id,
        'fornecedor': fake.company(),
        'valor_gasto': round(valor_gasto, 2)
    })

# 3. Cria o DataFrame e Salva em CSV
df_realizado = pd.DataFrame(dados_realizado)
df_realizado.to_csv('realizado.csv', index=False, sep=';', encoding='utf-8-sig')

print(f"SUCESSO: Arquivo 'realizado.csv' gerado com {len(df_realizado)} linhas.")

print(df_realizado.head())
