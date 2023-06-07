import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.classrooms.domain import models as domain_models


class ClassroomRepository:
    """Репозиторий аудиторий"""
    def list(self, **filters) -> List[domain_models.Classroom]:
        """Возвращает список аудиторий согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, classroom_id: uuid.UUID) -> domain_models.Classroom:
        """Возвращает аудиторию согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, classroom: domain_models.Classroom) -> domain_models.Classroom:
        """Добавляет указанную аудиторию в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyClassroomRepository(ClassroomRepository):
    """SQLAlchemy-репозиторий аудиторий"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Classroom]:
        """Возвращает список аудиторий согласно указанным фильтрам"""
        q = self.session.query(domain_models.Classroom)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, classroom_id: uuid.UUID) -> domain_models.Classroom:
        """Возвращает аудиторию согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если аудитория с указанным ID
                не найдена в репозитории
        """
        q = self.session.query(domain_models.Classroom).filter_by(id=classroom_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Аудитория с id={classroom_id} не найдена',
            )

        return instance
    

    def add(self, classroom: domain_models.Classroom) -> domain_models.Classroom:
        """Добавляет указанную аудиторию в репозиторий"""
        self.session.add(classroom)
        return classroom
