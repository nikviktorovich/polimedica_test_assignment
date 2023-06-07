import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.education.domain import models as domain_models


class SemesterRepository:
    """Репозиторий семестров"""
    def list(self, **filters) -> List[domain_models.Semester]:
        """Возвращает список семестров согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, semester_id: uuid.UUID) -> domain_models.Semester:
        """Возвращает экземпляр семестра согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, semester: domain_models.Semester) -> domain_models.Semester:
        """Добавляет указанный семестр в репозиторий"""
        raise NotImplementedError()


class SQLAlchemySemesterRepository(SemesterRepository):
    """SQLAlchemy-репозиторий семестров"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Semester]:
        """Возвращает список семестров согласно указанным фильтрам"""
        q = self.session.query(domain_models.Semester)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, semester_id: uuid.UUID) -> domain_models.Semester:
        """Возвращает экземпляр семестра согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если семестр
                с указанным ID не найден в репозитории
        """
        q = self.session.query(domain_models.Semester).filter_by(id=semester_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Семестр с id={semester_id} не найден',
            )

        return instance
    

    def add(self, semester: domain_models.Semester) -> domain_models.Semester:
        """Добавляет указанный семестр в репозиторий"""
        self.session.add(semester)
        return semester
