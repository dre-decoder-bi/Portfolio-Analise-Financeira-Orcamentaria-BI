import pandas as pd
import random

print("--- Iniciando Geração do ORÇAMENTO (Budget) ---")

# 1. Define as 'Dimensões' do negócio
centros_custo = {
    100: 'TI',
    200: 'Vendas',
    300: 'Marketing',
    400: 'Financeiro'
}

contas_contabeis = {
    5001: 'Software e Licenças',
    5002: 'Viagens e Deslocamento',
    5003: 'Marketing Digital',
    5004: 'Salários e Encargos'
}

meses = pd.to_datetime([
    '2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01',
    '2024-05-01', '2024-06-01', '2024-07-01', '2024-08-01',
    '2024-09-01', '2024-10-01', '2024-11-01', '2024-12-01'
])

# 2. Gera os dados
dados_orcamento = []

for cc_id, cc_nome in centros_custo.items():
    for conta_id, conta_nome in contas_contabeis.items():
        for mes in meses:
            if conta_nome == 'Salários e Encargos':
                valor_orcado = random.randint(50000, 80000)
            elif conta_nome == 'Viagens e Deslocamento':
                valor_orcado = random.randint(5000, 15000)
            elif cc_nome == 'Marketing' and conta_nome == 'Marketing Digital':
                valor_orcado = random.randint(20000, 40000)
            else:
                valor_orcado = random.randint(1000, 5000)
            
            dados_orcamento.append({
                'mes': mes.strftime('%Y-%m-%d'),
                'id_centro_custo': cc_id,
                'nome_centro_custo': cc_nome,
                'id_conta_contabil': conta_id,
                'nome_conta': conta_nome,
                'valor_orcado': valor_orcado
            })

# 3. Cria o DataFrame e Salva em CSV
df_orcamento = pd.DataFrame(dados_orcamento)
df_orcamento.to_csv('orcamento.csv', index=False, sep=';', encoding='utf-8-sig')

print(f"SUCESSO: Arquivo 'orcamento.csv' gerado com {len(df_orcamento)} linhas.")

print(df_orcamento.head())
