from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
from api.database import get_conn
from api.utils import pagina

router = APIRouter(prefix="/fazendas", tags=["Fazendas"])


# GET /fazendas — lista todas as fazendas com seletor por nome
@router.get("", response_class=HTMLResponse)
def listar_fazendas(nome: str = None):
    conn = get_conn()
    todas = pd.read_sql("SELECT nome FROM fazenda ORDER BY nome", conn)

    if nome:
        df = pd.read_sql("SELECT * FROM fazenda WHERE nome = ?", conn, params=[nome])
    else:
        df = pd.read_sql("SELECT * FROM fazenda", conn)
    conn.close()

    opcoes = "".join(
        f'<option value="{n}" {"selected" if n == nome else ""}>{n}</option>'
        for n in todas["nome"]
    )

    seletor = f"""
        <form method="get">
            <label>Fazenda:</label>
            <select name="nome" onchange="this.form.submit()">
                <option value="">-- Todas --</option>
                {opcoes}
            </select>
        </form>
    """

    return pagina(seletor + df.to_html(index=False, border=1))


# GET /fazendas/{id} — retorna uma fazenda pelo ID
@router.get("/{id}", response_class=HTMLResponse)
def buscar_fazenda(id: int):
    conn = get_conn()
    df = pd.read_sql("SELECT * FROM fazenda WHERE id = ?", conn, params=[id])
    conn.close()
    if df.empty:
        raise HTTPException(status_code=404, detail="Fazenda não encontrada")
    return pagina(df.to_html(index=False, border=1))


# GET /fazendas/{id}/plantios — retorna todos os plantios de uma fazenda
@router.get("/{id}/plantios", response_class=HTMLResponse)
def plantios_por_fazenda(id: int):
    conn = get_conn()
    df = pd.read_sql("""
        SELECT f.nome AS fazenda,
               t.nome AS talhao,
               c.nome AS cultura,
               p.ano,
               p.produtividade
          FROM plantio p
          JOIN talhao  t ON p.id_talhao  = t.id
          JOIN fazenda f ON t.id_fazenda  = f.id
          JOIN cultura c ON p.id_cultura  = c.id
         WHERE f.id = ?
         ORDER BY p.ano
    """, conn, params=[id])
    conn.close()
    if df.empty:
        raise HTTPException(status_code=404, detail="Fazenda não encontrada ou sem plantios")
    return pagina(df.to_html(index=False, border=1))
