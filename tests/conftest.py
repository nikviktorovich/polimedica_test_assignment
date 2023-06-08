from collections.abc import Iterator

import fastapi
import fastapi.testclient
import pytest

import university.apps.fastapi_app.main


@pytest.fixture(scope='function')
def fastapi_app() -> Iterator[fastapi.FastAPI]:
    yield university.apps.fastapi_app.main.app
    university.apps.fastapi_app.main.app.dependency_overrides.clear()


@pytest.fixture(scope='function')
def test_client(fastapi_app) -> fastapi.testclient.TestClient:
    client = fastapi.testclient.TestClient(app=fastapi_app)
    return client
