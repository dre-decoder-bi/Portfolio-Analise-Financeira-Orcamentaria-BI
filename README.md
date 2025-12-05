# Análise de Variância Orçamentária (Orçado vs. Realizado)

Projeto de Business Intelligence que simula uma análise financeira completa, desde a criação dos dados até o dashboard.

## 🎯 Objetivo

Comparar os valores orçados com os gastos reais de uma empresa fictícia, identificando os principais desvios (variâncias) por Centro de Custo e Conta Contábil.

## 🛠️ Arquitetura do Projeto (ELT)

1.  **Extração (Python):** Os scripts (`gerar_orcamento.py`, `gerar_realizado.py`) usam Pandas e Faker para criar um dataset sintético de 20.000 transações realistas.
2.  **Carga (Python):** O script (`etl_carga_dados_analise_financeira_orcamentaria.py`) usa SQLAlchemy e Psycopg2 para carregar os CSVs em um banco de dados **PostgreSQL** hospedado na nuvem (Supabase).
3.  **Transformação (SQL):** Uma `VIEW` (`v_analise_financeira_orcamentaria`) é criada no banco de dados para agregar os dados transacionais e calcular as variâncias (Absoluta e Percentual) em nível de servidor.
4.  **Visualização (Power BI):** O dashboard final se conecta a um **Fluxo de Dados (Dataflow)** do Power BI, que por sua vez consome a `VIEW` do PostgreSQL, garantindo performance e escalabilidade.

## 📊 Dashboard Interativo

## 📜 Print da tela do Dashboard
([Capa Dashboard Financeiro](analise_financeira_orcamentaria_capa.png))

## 🔗 Link do Dashboard Interativo
([Demo Dashboard Financeiro](https://youtu.be/M5WMPgp4BPY))

## 🔧 Ferramentas Utilizadas

* **Linguagens:** Python (Pandas, Faker, SQLAlchemy, Psycopg2) e SQL (PostgreSQL)
* **Banco de Dados:** PostgreSQL na Nuvem (Supabase)
* **BI:** Power BI Desktop & Power BI Service (Dataflows)

---
*Desenvolvido por Andressa*
