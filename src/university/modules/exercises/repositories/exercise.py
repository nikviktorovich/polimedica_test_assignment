import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.exercises.domain import models as domain_models


class ExerciseRepository:
    """Репозиторий самостоятельных работ"""
    def list(self, **filters) -> List[domain_models.Exercise]:
        """Возвращает список самостоятельных работ по указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, exercise_id: uuid.UUID) -> domain_models.Exercise:
        """Возвращает экземпляр самостоятельной работы
        согласно указанному ID
        """
        raise NotImplementedError()
    

    def add(self, exercise: domain_models.Exercise) -> domain_models.Exercise:
        """Добавляет указанную самостоятельную работу в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyExerciseRepository(ExerciseRepository):
    """SQLAlchemy-репозиторий самостоятельных работ"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Exercise]:
        """Возвращает список самостоятельных работ по указанным фильтрам"""
        q = self.session.query(domain_models.Exercise)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, exercise_id: uuid.UUID) -> domain_models.Exercise:
        """Возвращает экземпляр самостоятельной работы согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если оценка
                с указанным ID не найдена в репозитории
        """
        q = self.session.query(domain_models.Exercise).filter_by(id=exercise_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Самостоятельная работа с id={exercise_id} не найдена',
            )

        return instance
    

    def add(self, exercise: domain_models.Exercise) -> domain_models.Exercise:
        """Добавляет указанную самостоятельную работу в репозиторий"""
        self.session.add(exercise)
        return exercise
