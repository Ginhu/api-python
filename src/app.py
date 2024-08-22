from fastapi import FastAPI
from fastapi.responses import JSONResponse
from rotas.router_teste import router_teste
from webhook_facebook.routes.webhook_facebook_route import router_facebook

app = FastAPI()

app.include_router(router_teste)
app.include_router(router_facebook)


@app.get('/')
def read_root():
    return JSONResponse({'status': 'online'})


@app.get('/agora')
def agora():
    return JSONResponse({'status': "ok"})
