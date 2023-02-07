import pytest


@pytest.mark.asyncio()
async def it_returns_a_response_to_a_health_check(client):
    response = await client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
