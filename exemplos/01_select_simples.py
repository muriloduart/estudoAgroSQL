import sqlite3
import pandas as pd

# Antes de rodar esse arquivo, rode o setup.py uma vez para criar o banco!
import os
DB = os.path.join(os.path.dirname(__file__), '..', 'banco.db')
conn = sqlite3.connect(DB)

print("=" * 50)
print("NÍVEL 1 — SELECT simples")
print("=" * 50)

# ── EXEMPLO 1: buscar tudo de uma tabela ──────────────
print("\n[ Todas as fazendas ]")
df = pd.read_sql("SELECT * FROM fazenda", conn)
print(df)

# ── EXEMPLO 2: filtrar com WHERE ──────────────────────
print("\n[ Fazendas do MT ]")
df = pd.read_sql("SELECT nome, area_total FROM fazenda WHERE estado = 'MT'", conn)
print(df)

# ── EXEMPLO 3: ordenar com ORDER BY ───────────────────
print("\n[ Fazendas ordenadas por area_total (maior primeiro) ]")
df = pd.read_sql("SELECT nome, area_total FROM fazenda ORDER BY area_total DESC", conn)
print(df)

conn.close()