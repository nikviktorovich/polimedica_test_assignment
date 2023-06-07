import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.education.domain import models as domain_models


class FacultyRepository:
    """Репозиторий факультетов"""
    def list(self, **filters) -> List[domain_models.Faculty]:
        """Возвращает список факультетов согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, faculty_id: uuid.UUID) -> domain_models.Faculty:
        """Возвращает экземпляр факультета согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, faculty: domain_models.Faculty) -> domain_models.Faculty:
        """Добавляет указанный факультет в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyFacultyRepository(FacultyRepository):
    """SQLAlchemy-репозиторий факультетов"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Faculty]:
        """Возвращает список факультетов согласно указанным фильтрам"""
        q = self.session.query(domain_models.Faculty)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, faculty_id: uuid.UUID) -> domain_models.Faculty:
        """Возвращает экземпляр факультета согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если факультет
                с указанным ID не найден в репозитории
        """
        q = self.session.query(domain_models.Faculty).filter_by(id=faculty_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Факультет с id={faculty_id} не найден',
            )

        return instance
    

    def add(self, faculty: domain_models.Faculty) -> domain_models.Faculty:
        """Добавляет указанный факультет в репозиторий"""
        self.session.add(faculty)
        return faculty
