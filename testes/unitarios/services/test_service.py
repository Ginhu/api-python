# from pytest_mock import MockerFixture
from pytest_mock import MockerFixture
from src.services.webhook_facebook_service import WebhookFacebook


def test_check_data_succes():
    data = {'test_id': ''}
    inst = WebhookFacebook(data=data)
    ret = inst.check_data()
    assert ret == {'content': 'ok', 'status_code': 200}


def test_check_data_fail():
    data = {'wrong_id': ''}
    inst = WebhookFacebook(data=data)
    ret = inst.check_data()
    assert ret == {'content': 'Fail', 'status_code': 400}


def test_process_data():
    ...


def test_sava_data_db(mocker: MockerFixture):
    data = {'test_data': 'test'}
    inst = WebhookFacebook(data=data)
    mock = mocker.patch.object(WebhookFacebook, 'save_data_db')
    inst.save_data_db()

    assert mock.called
