from fastapi import APIRouter
from fastapi.responses import JSONResponse

router_webhook = APIRouter(prefix='/webhook')


@router_webhook.get('/health')
def health_check():
    return JSONResponse(content={'status': 'ok'}, status_code=200)


@router_webhook.post('/webhook_example')
def webhook_example():
    ...
