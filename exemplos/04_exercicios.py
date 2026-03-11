import sqlite3
import pandas as pd

import os
DB = os.path.join(os.path.dirname(__file__), '..', 'banco.db')
conn = sqlite3.connect(DB)

print("=" * 50)
print("NÍVEL 4 — EXERCÍCIOS (escreva as queries!)")
print("=" * 50)

# ── EXERCÍCIO 1 ───────────────────────────────────────
# Liste todos os talhões com área maior que 300,
# mostrando o nome do talhão e o nome da fazenda.
print("\n[ Ex 1: Talhões com área > 300 e nome da fazenda ]")
df = pd.read_sql("""
    -- escreva sua query aqui
""", conn)
print(df)

# ── EXERCÍCIO 2 ───────────────────────────────────────
# Quantos talhões cada fazenda tem?
# Mostre o nome da fazenda e a contagem, ordenado do maior para o menor.
print("\n[ Ex 2: Quantidade de talhões por fazenda ]")
df = pd.read_sql("""
    -- escreva sua query aqui
""", conn)
print(df)

# ── EXERCÍCIO 3 ───────────────────────────────────────
# Mostre os plantios realizados em 2024,
# com o nome do talhão, da cultura e a produtividade.
print("\n[ Ex 3: Plantios de 2024 ]")
df = pd.read_sql("""
    -- escreva sua query aqui
""", conn)
print(df)

# ── EXERCÍCIO 4 ───────────────────────────────────────
# Qual a produtividade média por cultura?
# Mostre apenas as culturas com média acima de 60.
print("\n[ Ex 4: Culturas com produtividade média > 60 ]")
df = pd.read_sql("""
    -- escreva sua query aqui
""", conn)
print(df)

# ── EXERCÍCIO 5 ───────────────────────────────────────
# Liste as fazendas que NÃO possuem nenhum talhão cadastrado.
print("\n[ Ex 5: Fazendas sem talhão ]")
df = pd.read_sql("""
    -- escreva sua query aqui
""", conn)
print(df)

conn.close()
