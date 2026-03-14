import sqlite3
import pandas as pd
import os

DB = os.path.join(os.path.dirname(__file__), '..', 'banco.db')
conn = sqlite3.connect(DB)

print("=" * 50)
print("NÍVEL 3 — VIEWS")
print("=" * 50)

# ── O QUE É UMA VIEW? ─────────────────────────────────
#
# Uma VIEW é uma query salva no banco com um nome.
# Em vez de repetir um JOIN complexo toda vez,
# você cria a view uma vez e consulta como tabela normal.
#
# Sem view → repete o JOIN em todo lugar
# Com view → SELECT * FROM vw_plantios

# ── CRIANDO A VIEW ────────────────────────────────────
#
# Colunas disponíveis para filtro (WHERE) e agrupamento (GROUP BY):
#   fazenda      → nome da fazenda        ex: 'Fazenda Boa Vista'
#   talhao       → nome do talhão         ex: 'Talhão A'
#   cultura      → nome da cultura        ex: 'Soja', 'Milho', 'Algodão'
#   ano          → ano do plantio         ex: 2023, 2024
#   produtividade→ sacas por hectare      ex: 62.0
#
conn.execute("DROP VIEW IF EXISTS vw_plantios")
conn.execute("""
    CREATE VIEW vw_plantios AS
    SELECT f.nome AS fazenda,
           t.nome AS talhao,
           c.nome AS cultura,
           p.ano,
           p.produtividade
      FROM plantio p
      JOIN talhao  t ON p.id_talhao  = t.id
      JOIN fazenda f ON t.id_fazenda  = f.id
      JOIN cultura c ON p.id_cultura  = c.id
""")
print("\nView 'vw_plantios' criada com sucesso.")

# ── EXEMPLO 1: consulta simples na view ───────────────
# A view se comporta como uma tabela — SELECT * funciona
print("\n[ Todos os plantios via view ]")
df = pd.read_sql("SELECT * FROM vw_plantios ORDER BY fazenda, ano", conn)
print(df)

# ── EXEMPLO 2: filtro por cultura ─────────────────────
# Como é uma tabela normal, WHERE funciona normalmente
print("\n[ Apenas plantios de Soja ]")
df = pd.read_sql("SELECT * FROM vw_plantios WHERE cultura = 'Soja'", conn)
print(df)

# ── EXEMPLO 3: agregação sobre a view ─────────────────
# GROUP BY também funciona — como em qualquer tabela
print("\n[ Produtividade média por fazenda ]")
df = pd.read_sql("""
    SELECT fazenda,
           ROUND(AVG(produtividade), 1) AS media_produtividade
      FROM vw_plantios
     GROUP BY fazenda
     ORDER BY media_produtividade DESC
""", conn)
print(df)

# ── REMOVENDO A VIEW ──────────────────────────────────
# DROP VIEW para não conflitar se rodar o script de novo
conn.execute("DROP VIEW IF EXISTS vw_plantios")
conn.close()
print("\nView removida. Banco no estado original.")
