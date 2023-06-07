import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.classrooms.domain import models as domain_models


class BuildingRepository:
    def list(self, **filters) -> List[domain_models.Building]:
        """Возвращает список зданий согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, building_id: uuid.UUID) -> domain_models.Building:
        """Возвращает здание согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, building: domain_models.Building) -> domain_models.Building:
        """Добавляет указанное здание в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyBuildingRepository(BuildingRepository):
    """SQLAlchemy-репозиторий зданий"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Building]:
        """Возвращает список зданий согласно указанным фильтрам"""
        q = self.session.query(domain_models.Building)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, building_id: uuid.UUID) -> domain_models.Building:
        """Возвращает здание согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если здание с указанным ID
                не найдено в репозитории
        """
        q = self.session.query(domain_models.Building).filter_by(id=building_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Здание с id={building_id} не найдено',
            )

        return instance
    

    def add(self, building: domain_models.Building) -> domain_models.Building:
        """Добавляет указанное здание в репозиторий"""
        self.session.add(building)
        return building
