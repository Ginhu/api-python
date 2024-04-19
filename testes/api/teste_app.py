from datetime import datetime
from fastapi.testclient import TestClient
import pytest

from src.app import app


@pytest.fixture
def api():
    app.dependency_overrides = {}
    cliente = TestClient(app)
    return cliente


def testa_decodifica_token(api: TestClient):
    url = '/'
    ret = api.get(url)
    assert ret.status_code == 200
    assert ret.json() == {'status': 'online'}


def testa_libs_acessivel(api: TestClient):
    url = '/agora'
    ret = api.get(url)
    assert ret.status_code == 200
    ret_json = ret.json()
    agora = datetime.now()
    assert agora.date().isoformat() in ret_json['agora']
