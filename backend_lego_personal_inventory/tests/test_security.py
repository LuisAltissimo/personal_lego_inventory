from http import HTTPStatus

import pytest
from jwt import decode

from backend_lego_personal_inventory.security import (
    create_access_token,
    settings,
)


@pytest.mark.asyncio
async def test_jwt():
    data = {'test': 'test'}
    token = await create_access_token(data)

    decoded = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert decoded['test'] == data['test']
    assert 'exp' in decoded


@pytest.mark.asyncio
async def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
