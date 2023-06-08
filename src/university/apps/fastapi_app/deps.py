from collections.abc import Iterator

import sqlalchemy.engine
from fastapi import Depends

import university.config
from university.service import unit_of_work


def get_db_engine() -> sqlalchemy.engine.Engine:
    connection_url = university.config.get_database_connection_url()
    engine = sqlalchemy.engine.create_engine(connection_url)
    return engine


def get_uow(
    engine: sqlalchemy.engine.Engine =  Depends(get_db_engine),
) -> Iterator[unit_of_work.UnitOfWork]:
    with unit_of_work.SQLAlchemyUnitOfWork(engine=engine) as uow:
        yield uow
