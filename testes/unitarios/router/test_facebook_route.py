import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from src.app import app
from src.services.webhook_facebook_service import WebhookFacebook


@pytest.fixture
def api():
    client = TestClient(app)
    return client


def test_health(api):
    ret = api.get(url='webhook_facebook/health')
    assert ret.status_code == 200
    assert ret.json() == {'status': 'ok'}


def test_verification_route_success(api):
    params = "?hub.mode=subscribe&hub.challenge=123&hub.verify_token=test"
    ret = api.get(url=f"webhook_facebook/facebook{params}")
    assert ret.status_code == 200
    assert ret.json() == 123


def test_verification_route_fail(api):
    params = "?hub.mode=subscribe&hub.challenge=123&hub.verify_token=WRONG"
    ret = api.get(url=f"webhook_facebook/facebook{params}")
    assert ret.status_code == 400


def test_webhook_route_success(api, mocker: MockerFixture):
    data = {"test_id": "teste"}
    mock = mocker.patch.object(WebhookFacebook, 'save_data_db')

    ret = api.post("webhook_facebook/facebook", json=data)

    assert ret.status_code == 200
    assert ret.json() == {'content': 'ok', 'status_code': 200}
    assert mock.called


def test_webhook_route_fail_check_data(api, mocker: MockerFixture):
    data = {"wrong_id": "teste"}
    mock = mocker.patch.object(WebhookFacebook, 'save_data_db')

    ret = api.post("webhook_facebook/facebook", json=data)

    assert ret.status_code == 400
    assert ret.json() == {'content': 'Fail', 'status_code': 400}
    assert mock.called
