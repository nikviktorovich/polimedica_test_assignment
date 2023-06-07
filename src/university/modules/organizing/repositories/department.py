import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.organizing.domain import models as domain_models


class DepartmentRepository:
    """Репозиторий кафедр"""
    def list(self, **filters) -> List[domain_models.Department]:
        """Возвращает список кафедр согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, department_id: uuid.UUID) -> domain_models.Department:
        """Возвращает экземпляр кафедры согласно указанному ID"""
        raise NotImplementedError()
    

    def add(
        self,
        department: domain_models.Department,
    ) -> domain_models.Department:
        """Добавляет указанную кафедру в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyDepartmentRepository(DepartmentRepository):
    """SQLAlchemy-репозиторий кафедр"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Department]:
        """Возвращает список кафедр согласно указанным фильтрам"""
        q = self.session.query(domain_models.Department)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, department_id: uuid.UUID) -> domain_models.Department:
        """Возвращает экземпляр кафедры согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если кафедра
                с указанным ID не найдена в репозитории
        """
        q = self.session.query(domain_models.Department)
        q = q.filter_by(id=department_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Кафедра с id={department_id} не найдена',
            )

        return instance
    

    def add(
        self,
        department: domain_models.Department,
    ) -> domain_models.Department:
        """Добавляет указанную кафедру в репозиторий"""
        self.session.add(department)
        return department
