from collections.abc import Iterator

import fastapi
import fastapi.testclient
import pytest
import sqlalchemy.engine

import university.apps.fastapi_app.main
import university.config
from university.services import unit_of_work


@pytest.fixture(scope='session')
def fastapi_app() -> Iterator[fastapi.FastAPI]:
    yield university.apps.fastapi_app.main.app
    university.apps.fastapi_app.main.app.dependency_overrides.clear()


@pytest.fixture(scope='session')
def test_client(fastapi_app) -> Iterator[fastapi.testclient.TestClient]:
    client = fastapi.testclient.TestClient(app=fastapi_app)
    with client:
        yield client


def get_db_engine() -> sqlalchemy.engine.Engine:
    connection_url = university.config.get_database_connection_url()
    engine = sqlalchemy.engine.create_engine(connection_url)
    return engine


@pytest.fixture(scope='function')
def uow() -> Iterator[unit_of_work.UnitOfWork]:
    """Возвращает единицу работы с активным соединением с БД"""
    engine = get_db_engine()
    with unit_of_work.SQLAlchemyUnitOfWork(engine=engine) as uow:
        yield uow
