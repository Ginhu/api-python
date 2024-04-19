from fastapi import APIRouter
from fastapi.responses import JSONResponse

router_teste = APIRouter(prefix='/teste')


@router_teste.get('/teste')
def teste():
    return JSONResponse({'teste': 'ok'})
