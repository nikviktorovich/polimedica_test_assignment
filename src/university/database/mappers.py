import sqlalchemy.orm
from sqlalchemy.orm import relationship


def start_mappers() -> None:
    registry = sqlalchemy.orm.registry()

    ...
