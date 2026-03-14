import sqlite3
import pandas as pd
import os

DB = os.path.join(os.path.dirname(__file__), '..', 'banco.db')
conn = sqlite3.connect(DB)

print("=" * 50)
print("NÍVEL 4 — ÍNDICES")
print("=" * 50)

# ── O QUE É UM ÍNDICE? ────────────────────────────────
#
# Um índice é uma estrutura auxiliar que o banco cria
# para encontrar registros sem precisar ler a tabela inteira.
#
# Analogia: índice de um livro — você vai direto na página
# certa em vez de ler o livro inteiro.
#
# Quando criar índice:
#   - Colunas usadas em WHERE com frequência
#   - Colunas usadas em JOIN (foreign keys)
#   - Colunas usadas em ORDER BY
#
# Custo do índice:
#   - Ocupa espaço em disco
#   - INSERT/UPDATE ficam um pouco mais lentos
#   - Por isso não se cria índice em tudo — só onde há ganho real

# ── EXPLAIN QUERY PLAN ────────────────────────────────
#
# Mostra como o banco vai executar a query.
# SCAN   → leu a tabela inteira linha por linha (lento em tabelas grandes)
# SEARCH → usou índice, foi direto aos registros (rápido)

print("\n[ Plano SEM índice — SCAN (lê tudo) ]")
plano = conn.execute("""
    EXPLAIN QUERY PLAN
    SELECT * FROM plantio WHERE id_talhao = 3
""").fetchall()
for linha in plano:
    print(" ", linha[3])

# ── CRIANDO OS ÍNDICES NAS FOREIGN KEYS ───────────────
#
# A tabela 'plantio' é a que mais cresce em um sistema real
# (um registro por talhão por safra). Os JOINs sempre passam
# pelas FKs, então são os melhores candidatos a índice.
#
# Convenção de nome: idx_<tabela>_<coluna>

conn.execute("DROP INDEX IF EXISTS idx_plantio_talhao")
conn.execute("DROP INDEX IF EXISTS idx_plantio_cultura")
conn.execute("DROP INDEX IF EXISTS idx_talhao_fazenda")

conn.execute("CREATE INDEX idx_plantio_talhao  ON plantio (id_talhao)")
conn.execute("CREATE INDEX idx_plantio_cultura ON plantio (id_cultura)")
conn.execute("CREATE INDEX idx_talhao_fazenda  ON talhao  (id_fazenda)")

print("\nÍndices criados.")

# ── EXPLAIN APÓS CRIAR O ÍNDICE ───────────────────────

print("\n[ Plano COM índice — SEARCH (vai direto) ]")
plano = conn.execute("""
    EXPLAIN QUERY PLAN
    SELECT * FROM plantio WHERE id_talhao = 3
""").fetchall()
for linha in plano:
    print(" ", linha[3])

# ── ÍNDICE COMPOSTO ───────────────────────────────────
#
# Quando o WHERE filtra por duas colunas juntas com frequência,
# um índice composto é mais eficiente que dois índices separados.
# Exemplo: buscar plantios de um talhão em um ano específico.

conn.execute("DROP INDEX IF EXISTS idx_plantio_talhao_ano")
conn.execute("CREATE INDEX idx_plantio_talhao_ano ON plantio (id_talhao, ano)")

print("\n[ Plano com índice composto (talhao + ano) ]")
plano = conn.execute("""
    EXPLAIN QUERY PLAN
    SELECT * FROM plantio WHERE id_talhao = 1 AND ano = 2024
""").fetchall()
for linha in plano:
    print(" ", linha[3])

# ── LISTANDO OS ÍNDICES DO BANCO ──────────────────────
#
# sqlite_master guarda a definição de todos os objetos do banco
# (tabelas, views, índices). Útil para auditoria.

print("\n[ Índices existentes no banco ]")
df = pd.read_sql("""
    SELECT name, tbl_name AS tabela, sql
      FROM sqlite_master
     WHERE type = 'index'
       AND name LIKE 'idx_%'
     ORDER BY tbl_name
""", conn)
print(df)

# ── REMOVENDO OS ÍNDICES ──────────────────────────────
conn.execute("DROP INDEX IF EXISTS idx_plantio_talhao")
conn.execute("DROP INDEX IF EXISTS idx_plantio_cultura")
conn.execute("DROP INDEX IF EXISTS idx_talhao_fazenda")
conn.execute("DROP INDEX IF EXISTS idx_plantio_talhao_ano")
conn.close()

print("\nÍndices removidos. Banco no estado original.")
