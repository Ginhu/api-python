from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.libs import dh

app = FastAPI()


@app.get('/')
def read_root():
    return JSONResponse({'status': 'online'})


@app.get('/agora')
def agora():
    return JSONResponse({'agora': dh.hoje_zero_hora_iso()})
