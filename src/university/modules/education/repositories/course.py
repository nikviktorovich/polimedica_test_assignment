import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.education.domain import models as domain_models


class CourseRepository:
    """Репозиторий курсов"""
    def list(self, **filters) -> List[domain_models.Course]:
        """Возвращает список курсов согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, course_id: uuid.UUID) -> domain_models.Course:
        """Возвращает экземпляр курса согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, course: domain_models.Course) -> domain_models.Course:
        """Добавляет указанный курс в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyCourseRepository(CourseRepository):
    """SQLAlchemy-репозиторий курсов"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Course]:
        """Возвращает список курсов согласно указанным фильтрам"""
        q = self.session.query(domain_models.Course)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, course_id: uuid.UUID) -> domain_models.Course:
        """Возвращает экземпляр курса согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если курс
                с указанным ID не найден в репозитории
        """
        q = self.session.query(domain_models.Course).filter_by(id=course_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Курс с id={course_id} не найден',
            )

        return instance
    

    def add(self, course: domain_models.Course) -> domain_models.Course:
        """Добавляет указанный курс в репозиторий"""
        self.session.add(course)
        return course
