from http import HTTPStatus

from fastapi.testclient import TestClient

from backend_lego_personal_inventory.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_if_conjunto_is_black_panther():
    client = TestClient(app)

    response = client.get('/conjunto')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'conjunto': 'pantera-negra'}


def test_exercicio_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
