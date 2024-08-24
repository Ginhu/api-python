from fastapi import APIRouter, Body, Query, Response
from fastapi.responses import JSONResponse

from src import conf
from src.services.webhook_facebook_service import WebhookFacebook

router_facebook = APIRouter(prefix='/webhook_facebook')


@router_facebook.get('/health')
def health_check():
    return JSONResponse(content={'status': 'ok'}, status_code=200)


# Verification route
@router_facebook.get('/facebook')
def webhook_facebook_validacao(
        hub_mode: str = Query(alias="hub.mode"),
        hub_challenge: str = Query(alias="hub.challenge"),
        hub_verify_token: str = Query(alias="hub.verify_token")):
    if hub_mode == 'subscribe' and hub_verify_token == conf.verification_token:
        return Response(hub_challenge)
    return Response(status_code=400)


# webhook route
@router_facebook.post('/facebook')
def webhook_facebook(data: dict = Body(...)):
    service = WebhookFacebook(data=data)
    service.save_data_db()
    ret = service.check_data()
    return JSONResponse(content=ret, status_code=ret['status_code'])
