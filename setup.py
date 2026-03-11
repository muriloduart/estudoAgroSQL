import sqlite3
import subprocess
import sys

# Instala dependências necessárias
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "-q"])

# Cria (ou reconecta) o banco de dados local
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# ── TABELAS ──────────────────────────────────────────────

cursor.executescript("""
    DROP TABLE IF EXISTS plantio;
    DROP TABLE IF EXISTS talhao;
    DROP TABLE IF EXISTS fazenda;
    DROP TABLE IF EXISTS cultura;

    CREATE TABLE fazenda (
        id          INTEGER PRIMARY KEY,
        nome        TEXT,
        estado      TEXT,
        area_total  REAL
    );

    CREATE TABLE talhao (
        id          INTEGER PRIMARY KEY,
        id_fazenda  INTEGER,
        nome        TEXT,
        area        REAL,
        FOREIGN KEY (id_fazenda) REFERENCES fazenda(id)
    );

    CREATE TABLE cultura (
        id   INTEGER PRIMARY KEY,
        nome TEXT
    );

    CREATE TABLE plantio (
        id            INTEGER PRIMARY KEY,
        id_talhao     INTEGER,
        id_cultura    INTEGER,
        ano           INTEGER,
        produtividade REAL,   -- sacas/hectare
        FOREIGN KEY (id_talhao)  REFERENCES talhao(id),
        FOREIGN KEY (id_cultura) REFERENCES cultura(id)
    );
""")

# ── DADOS ────────────────────────────────────────────────

cursor.executemany("INSERT INTO fazenda VALUES (?, ?, ?, ?)", [
    (1, 'Fazenda Boa Vista',   'MT', 1500.0),
    (2, 'Fazenda São João',    'GO', 800.0),
    (3, 'Fazenda Santa Maria', 'MS', 2200.0),
    (4, 'Fazenda Esperança',   'PR', 400.0),
    (5, 'Fazenda Nova',        'BA', 600.0),
])

cursor.executemany("INSERT INTO talhao VALUES (?, ?, ?, ?)", [
    (1, 1, 'Talhão A', 300.0),
    (2, 1, 'Talhão B', 250.0),
    (3, 1, 'Talhão C', 180.0),
    (4, 2, 'Talhão A', 400.0),
    (5, 2, 'Talhão B', 150.0),
    (6, 3, 'Talhão A', 600.0),
    (7, 3, 'Talhão B', 500.0),
    (8, 4, 'Talhão A', 200.0),
])

cursor.executemany("INSERT INTO cultura VALUES (?, ?)", [
    (1, 'Soja'),
    (2, 'Milho'),
    (3, 'Algodão'),
])

cursor.executemany("INSERT INTO plantio VALUES (?, ?, ?, ?, ?)", [
    (1,  1, 1, 2023, 58.0),
    (2,  1, 1, 2024, 62.0),
    (3,  2, 2, 2023, 110.0),
    (4,  2, 2, 2024, 95.0),
    (5,  3, 1, 2024, 55.0),
    (6,  4, 1, 2023, 60.0),
    (7,  4, 3, 2024, 80.0),
    (8,  5, 2, 2024, 100.0),
    (9,  6, 1, 2023, 70.0),
    (10, 6, 1, 2024, 72.0),
    (11, 7, 3, 2024, 85.0),
    (12, 8, 2, 2023, 90.0),
    (13, 8, 2, 2024, 105.0),
])

conn.commit()
conn.close()

print("Banco criado com sucesso!")
print("Tabelas: fazenda, talhao, cultura, plantio")
