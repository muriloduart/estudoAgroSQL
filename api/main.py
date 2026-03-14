from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.routers import fazendas, culturas

app = FastAPI(title="AgroSQL API")

app.include_router(fazendas.router)
app.include_router(culturas.router)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>AgroSQL API</h2>
    <table border="1" cellpadding="6">
        <tr><th>Rota</th><th>Descrição</th></tr>
        <tr><td><a href="/fazendas">GET /fazendas</a></td><td>Lista todas as fazendas (com filtro por nome)</td></tr>
        <tr><td><a href="/fazendas/1">GET /fazendas/{id}</a></td><td>Retorna uma fazenda pelo ID</td></tr>
        <tr><td><a href="/fazendas/1/plantios">GET /fazendas/{id}/plantios</a></td><td>Retorna todos os plantios de uma fazenda</td></tr>
        <tr><td><a href="/culturas">GET /culturas</a></td><td>Lista todas as culturas</td></tr>
    </table>
    """
