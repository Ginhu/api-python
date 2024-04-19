from fastapi import FastAPI
from fastapi.responses import JSONResponse
from rotas.router_teste import router_teste

from src.libs import dh

app = FastAPI()

app.include_router(router_teste)


@app.get('/')
def read_root():
    return JSONResponse({'status': 'online'})


@app.get('/agora')
def agora():
    return JSONResponse({'agora': dh.hoje_zero_hora_iso()})
