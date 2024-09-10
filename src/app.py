from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.router.router_teste import router_teste
from src.router.webhook_facebook_route import router_facebook
from src.router.webhook_route import router_webhook

app = FastAPI()

app.include_router(router_teste)
app.include_router(router_facebook)
app.include_router(router_webhook)


@app.get('/')
def read_root():
    return JSONResponse({'status': 'online'})


@app.get('/agora')
def agora():
    return JSONResponse({'status': "ok"})
