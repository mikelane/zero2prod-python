import pytest
from starlite import (
    AsyncTestClient,
    Starlite,
)

from api.app import app as _app


@pytest.fixture()
def app() -> Starlite:
    return _app


@pytest.fixture()
def client(app) -> AsyncTestClient:
    return AsyncTestClient(app)
