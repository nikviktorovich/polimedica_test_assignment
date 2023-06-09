from collections.abc import Iterator

import fastapi
import fastapi.testclient
import pytest

import university.apps.fastapi_app.main


@pytest.fixture(scope='session')
def fastapi_app() -> Iterator[fastapi.FastAPI]:
    yield university.apps.fastapi_app.main.app
    university.apps.fastapi_app.main.app.dependency_overrides.clear()


@pytest.fixture(scope='session')
def test_client(fastapi_app) -> Iterator[fastapi.testclient.TestClient]:
    client = fastapi.testclient.TestClient(app=fastapi_app)
    with client:
        yield client
