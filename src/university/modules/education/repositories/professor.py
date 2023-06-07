import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.education.domain import models as domain_models


class ProfessorRepository:
    """Репозиторий преподавателей"""
    def list(self, **filters) -> List[domain_models.Professor]:
        """Возвращает список преподавателей согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, professor_id: uuid.UUID) -> domain_models.Professor:
        """Возвращает экземпляр преподавателя согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, professor: domain_models.Professor) -> domain_models.Professor:
        """Добавляет указанного преподавателя в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyProfessorRepository(ProfessorRepository):
    """SQLAlchemy-репозиторий преподавателей"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Professor]:
        """Возвращает список преподавателей согласно указанным фильтрам"""
        q = self.session.query(domain_models.Professor)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, professor_id: uuid.UUID) -> domain_models.Professor:
        """Возвращает экземпляр преподавателя согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если преподаватель
                с указанным ID не найден в репозитории
        """
        q = self.session.query(domain_models.Professor).filter_by(id=professor_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Преподаватель с id={professor_id} не найден',
            )

        return instance
    

    def add(self, professor: domain_models.Professor) -> domain_models.Professor:
        """Добавляет указанного преподавателя в репозиторий"""
        self.session.add(professor)
        return professor
