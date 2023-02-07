import pytest
from starlite import (
    AsyncTestClient,
    Starlite,
)

import api.app


@pytest.fixture()
def app() -> Starlite:
    return api.app.app


@pytest.fixture()
def client(app) -> AsyncTestClient:
    return AsyncTestClient(app)


@pytest.mark.asyncio()
async def it_returns_a_response_to_a_health_check(client):
    response = await client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
