from fastapi import APIRouter, Body, Query, Response
from fastapi.responses import JSONResponse

from src.webhook_facebook.services.webhook_facebook_service import WebhookFacebook

router_facebook = APIRouter(prefix='/webhook_facebook')


@router_facebook.get('/health')
def health_check():
    return JSONResponse(content={'status': 'ok'}, status_code=200)


@router_facebook.get('/facebook')
def webhook_facebook_validacao(
        hub_mode: str = Query(alias="hub.mode"),
        hub_challenge: str = Query(alias="hub.challenge"),
        hub_verify_token: str = Query(alias="hub.verify_token")):
    if hub_mode == 'subscribe' and hub_verify_token == 'test_token_facebook':
        return Response(hub_challenge)
    return Response(status_code=400)


@router_facebook.post('/facebook')
def webhook_facebook(data: dict = Body(...)):
    service = WebhookFacebook(data=data)
    ret = service.check_data()
    return JSONResponse(content=ret, status_code=ret['status_code'])
