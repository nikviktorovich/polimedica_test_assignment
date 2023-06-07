import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.exercises.domain import models as domain_models


class GradeRepository:
    """Репозиторий оценок"""
    def list(self, **filters) -> List[domain_models.Grade]:
        """Возвращает список оценок согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, grade_id: uuid.UUID) -> domain_models.Grade:
        """Возвращает экземпляр оценки согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, grade: domain_models.Grade) -> domain_models.Grade:
        """Добавляет указанную оценку в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyGradeRepository(GradeRepository):
    """SQLAlchemy-репозиторий оценок"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Grade]:
        """Возвращает список оценок согласно указанным фильтрам"""
        q = self.session.query(domain_models.Grade)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, grade_id: uuid.UUID) -> domain_models.Grade:
        """Возвращает экземпляр оценки согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если оценка
                с указанным ID не найдена в репозитории
        """
        q = self.session.query(domain_models.Grade).filter_by(id=grade_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Оценка с id={grade_id} не найдена',
            )

        return instance
    

    def add(self, grade: domain_models.Grade) -> domain_models.Grade:
        """Добавляет указанную оценку в репозиторий"""
        self.session.add(grade)
        return grade
