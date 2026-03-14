from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import pandas as pd
from api.database import get_conn
from api.utils import pagina

router = APIRouter(prefix="/culturas", tags=["Culturas"])


@router.get("", response_class=HTMLResponse)
def listar_culturas():
    conn = get_conn()
    df = pd.read_sql("SELECT * FROM cultura", conn)
    conn.close()
    return pagina(df.to_html(index=False, border=1))
