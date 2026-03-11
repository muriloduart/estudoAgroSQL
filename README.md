# AgroSQL Study — SQLite + Pandas aplicados ao Agronegócio

Estudo prático de SQL com um banco de dados temático do agronegócio brasileiro, explorando consultas do básico ao avançado com **SQLite** e **Pandas**.

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

## Conteúdo

| Arquivo                        | Nível     | Tópicos                                  |
|-------------------------------|-----------|------------------------------------------|
| `setup.py`                    | —         | Criação do banco e inserção de dados     |
| `exemplos/01_select_simples.py` | Básico    | SELECT, WHERE, ORDER BY                  |
| `exemplos/02_join.py`          | Intermediário | INNER JOIN, LEFT JOIN               |
| `exemplos/03_subquery.py`      | Avançado  | Subqueries, agregações aninhadas         |
| `exemplos/04_exercicios.py`    | Prático   | Exercícios para praticar                 |
| `exemplos/04_gabarito.py`      | Prático   | Gabarito dos exercícios                  |

## Tecnologias

- Python 3
- SQLite3 (built-in)
- Pandas (`pd.read_sql`)

## Visualizando o banco no VS Code

Instale a extensão **[Database Client](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-database-client2)** (by Weijan Chen) para abrir e navegar pelo `banco.db` diretamente no editor.

## Como rodar

```bash
# 1. Criar o banco e instalar dependências
python setup.py

# 2. Rodar os exemplos
python exemplos/01_select_simples.py
python exemplos/02_join.py
python exemplos/03_subquery.py
python exemplos/04_exercicios.py

# Após tentar, confira o gabarito
python exemplos/04_gabarito.py
```

---

> Estudo pessoal para praticar SQL em um contexto real de agronegócio.
