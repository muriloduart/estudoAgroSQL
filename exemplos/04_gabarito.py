import sqlite3
import pandas as pd

import os
DB = os.path.join(os.path.dirname(__file__), '..', 'banco.db')
conn = sqlite3.connect(DB)

print("=" * 50)
print("GABARITO — NÍVEL 4")
print("=" * 50)

# ── EXERCÍCIO 1 ───────────────────────────────────────
# Liste todos os talhões com área maior que 300,
# mostrando o nome do talhão e o nome da fazenda.
print("\n[ Ex 1: Talhões com área > 300 e nome da fazenda ]")
df = pd.read_sql("""
    SELECT t.nome AS talhao, f.nome AS fazenda, t.area
    FROM talhao t
    INNER JOIN fazenda f ON f.id = t.id_fazenda
    WHERE t.area > 300
    ORDER BY t.area DESC
""", conn)
print(df)

# ── EXERCÍCIO 2 ───────────────────────────────────────
# Quantos talhões cada fazenda tem?
# Mostre o nome da fazenda e a contagem, ordenado do maior para o menor.
print("\n[ Ex 2: Quantidade de talhões por fazenda ]")
df = pd.read_sql("""
    SELECT f.nome AS fazenda, COUNT(t.id) AS qtd_talhoes
    FROM fazenda f
    LEFT JOIN talhao t ON t.id_fazenda = f.id
    GROUP BY f.id, f.nome
    ORDER BY qtd_talhoes DESC
""", conn)
print(df)

# ── EXERCÍCIO 3 ───────────────────────────────────────
# Mostre os plantios realizados em 2024,
# com o nome do talhão, da cultura e a produtividade.
print("\n[ Ex 3: Plantios de 2024 ]")
df = pd.read_sql("""
    SELECT t.nome AS talhao, c.nome AS cultura, p.produtividade
    FROM plantio p
    INNER JOIN talhao t  ON t.id  = p.id_talhao
    INNER JOIN cultura c ON c.id  = p.id_cultura
    WHERE p.ano = 2024
    ORDER BY p.produtividade DESC
""", conn)
print(df)

# ── EXERCÍCIO 4 ───────────────────────────────────────
# Qual a produtividade média por cultura?
# Mostre apenas as culturas com média acima de 60.
print("\n[ Ex 4: Culturas com produtividade média > 60 ]")
df = pd.read_sql("""
    SELECT c.nome AS cultura, ROUND(AVG(p.produtividade), 2) AS media_prod
    FROM plantio p
    INNER JOIN cultura c ON c.id = p.id_cultura
    GROUP BY c.id, c.nome
    HAVING AVG(p.produtividade) > 60
    ORDER BY media_prod DESC
""", conn)
print(df)

# ── EXERCÍCIO 5 ───────────────────────────────────────
# Liste as fazendas que NÃO possuem nenhum talhão cadastrado.
print("\n[ Ex 5: Fazendas sem talhão ]")
df = pd.read_sql("""
    SELECT f.nome AS fazenda, f.estado
    FROM fazenda f
    LEFT JOIN talhao t ON t.id_fazenda = f.id
    WHERE t.id IS NULL
""", conn)
print(df)

conn.close()
