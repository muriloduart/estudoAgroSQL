import sqlite3
import pandas as pd

import os
DB = os.path.join(os.path.dirname(__file__), '..', 'banco.db')
conn = sqlite3.connect(DB)

print("=" * 50)
print("NÍVEL 2 — JOIN (unindo tabelas)")
print("=" * 50)

# ── EXEMPLO 1: JOIN simples ───────────────────────────
print("\n[ Talhões com nome da fazenda ]")
df = pd.read_sql("""
    SELECT fazenda.nome AS fazenda,
           talhao.nome  AS talhao,
           talhao.area
      FROM talhao
      INNER JOIN fazenda ON talhao.id_fazenda = fazenda.id
""", conn)
print(df)

# ── EXEMPLO 2: JOIN com filtro ────────────────────────
print("\n[ Talhões da Fazenda Boa Vista ]")
df = pd.read_sql("""
    SELECT fazenda.nome AS fazenda,
           talhao.nome  AS talhao,
           talhao.area
      FROM talhao
      INNER JOIN fazenda ON talhao.id_fazenda = fazenda.id
     WHERE fazenda.nome = 'Fazenda Boa Vista'
""", conn)
print(df)

# ── EXEMPLO 3: JOIN com 3 tabelas ─────────────────────
print("\n[ Plantios com nome do talhão e da cultura ]")
df = pd.read_sql("""
    SELECT fazenda.nome   AS fazenda,
           talhao.nome    AS talhao,
           cultura.nome   AS cultura,
           plantio.ano,
           plantio.produtividade
      FROM plantio
      INNER JOIN talhao  ON plantio.id_talhao  = talhao.id
      INNER JOIN cultura ON plantio.id_cultura = cultura.id
      INNER JOIN fazenda ON talhao.id_fazenda  = fazenda.id
     ORDER BY fazenda.nome, plantio.ano
""", conn)
print(df)

conn.close()