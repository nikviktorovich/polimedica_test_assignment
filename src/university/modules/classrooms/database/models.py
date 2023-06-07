import uuid

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

import university.database.orm


class Building(university.database.orm.Base):
    """Таблица зданий

    Атрибуты:
        id: Идентификатор здания
        code: Кодовое символьное наименование здания
    """
    __tablename__ = 'buildings'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String(50), unique=True)


class Classroom(university.database.orm.Base):
    """Таблица аудиторий

    Атрибуты:
        id: Идентификатор аудитории
        code: Кодовое символьное название аудитории
        building_id: Идентификатор здания, в котором расположена аудитория
        building: Экземпляр объекта здания
    """
    __tablename__ = 'classrooms'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String(50))
    building_id = Column(ForeignKey('buildings.id'))
    building = relationship(Building)
