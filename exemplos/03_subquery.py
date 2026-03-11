import sqlite3
import pandas as pd

import os
DB = os.path.join(os.path.dirname(__file__), '..', 'banco.db')
conn = sqlite3.connect(DB)

print("=" * 50)
print("NÍVEL 3 — SUBQUERY (query dentro de query)")
print("=" * 50)

# ── EXEMPLO 1: subquery no WHERE com IN ───────────────
print("\n[ Fazendas que têm talhão com área > 400 ]")
df = pd.read_sql("""
    SELECT nome, estado
      FROM fazenda
     WHERE id IN (
         SELECT id_fazenda
           FROM talhao
          WHERE area > 400
     )
""", conn)
print(df)

# ── EXEMPLO 2: subquery com valor único ───────────────
print("\n[ Talhões com área acima da média ]")
df = pd.read_sql("""
    SELECT nome, area
      FROM talhao
     WHERE area > (
         SELECT AVG(area) FROM talhao
     )
     ORDER BY area DESC
""", conn)
print(df)

# ── EXEMPLO 3: subquery no FROM ───────────────────────
print("\n[ Média de produtividade por cultura (via subquery no FROM) ]")
df = pd.read_sql("""
    SELECT cultura_nome, AVG(produtividade) AS media
      FROM (
          SELECT cultura.nome AS cultura_nome,
                 plantio.produtividade
            FROM plantio
            INNER JOIN cultura ON plantio.id_cultura = cultura.id
      ) dados
     GROUP BY cultura_nome
""", conn)
print(df)

conn.close()