# AgroSQL Study — SQLite + Pandas aplicados ao Agronegócio

Estudo prático de SQL com um banco de dados temático do agronegócio brasileiro, explorando consultas do básico ao avançado com **SQLite**, **Pandas** e **FastAPI**.

## Sobre o projeto

O banco simula um cenário de gestão agrícola com fazendas, talhões, culturas e registros de plantio — estrutura comum em sistemas de agricultura de precisão. **Todos os dados são fictícios**, criados exclusivamente para fins de estudo.

**Modelo de dados:**

```
fazenda ──< talhao ──< plantio >── cultura
```

| Tabela    | Descrição                                      |
|-----------|------------------------------------------------|
| `fazenda` | Propriedades rurais (nome, estado, área total) |
| `talhao`  | Subdivisões de cada fazenda                    |
| `cultura` | Culturas plantadas (Soja, Milho, Algodão)      |
| `plantio` | Registros de produtividade por talhão e ano    |

## Exemplos SQL

| Arquivo                         | Nível         | Tópicos                              |
|---------------------------------|---------------|--------------------------------------|
| `exemplos/01_select_simples.py` | Básico        | SELECT, WHERE, ORDER BY              |
| `exemplos/02_join.py`           | Intermediário | INNER JOIN, LEFT JOIN                |
| `exemplos/03_subquery.py`       | Avançado      | Subqueries, agregações aninhadas     |
| `exemplos/04_exercicios.py`     | Prático       | Exercícios para praticar             |
| `exemplos/04_gabarito.py`       | Prático       | Gabarito dos exercícios              |
| `exemplos/05_views.py`          | DBA           | CREATE VIEW, consultas sobre views   |
| `exemplos/06_indices.py`        | DBA           | CREATE INDEX, EXPLAIN QUERY PLAN     |

## API REST

Os dados do banco são expostos via API construída com **FastAPI**. As rotas retornam tabelas HTML navegáveis pelo browser.

| Rota                        | Descrição                                        |
|-----------------------------|--------------------------------------------------|
| `GET /`                     | Página inicial com listagem das rotas            |
| `GET /fazendas`             | Lista todas as fazendas (filtro por nome)        |
| `GET /fazendas/{id}`        | Retorna uma fazenda pelo ID                      |
| `GET /fazendas/{id}/plantios` | Retorna todos os plantios de uma fazenda       |
| `GET /culturas`             | Lista todas as culturas                          |

**Estrutura da API:**

```
api/
├── main.py         — inicializa o app e registra os routers
├── database.py     — conexão com o banco
├── utils.py        — funções auxiliares compartilhadas
└── routers/
    ├── fazendas.py — rotas de fazenda e plantios
    └── culturas.py — rotas de cultura
```

## Tecnologias

- Python 3
- SQLite3 (built-in)
- Pandas (`pd.read_sql`)
- FastAPI + Uvicorn

## Como rodar

```bash
# 1. Criar o banco e instalar dependências
python3 setup.py
pip install fastapi uvicorn

# 2. Rodar os exemplos SQL
python3 exemplos/01_select_simples.py
python3 exemplos/02_join.py
python3 exemplos/03_subquery.py
python3 exemplos/04_exercicios.py
python3 exemplos/05_views.py
python3 exemplos/06_indices.py

# 3. Subir a API
uvicorn api.main:app --reload
# Acesse: http://localhost:8000
```

## Visualizando o banco no VS Code

Instale a extensão **[Database Client](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-database-client2)** (by Weijan Chen) para abrir e navegar pelo `banco.db` diretamente no editor.

---

> Estudo pessoal para praticar SQL e desenvolvimento de APIs em um contexto real de agronegócio.
