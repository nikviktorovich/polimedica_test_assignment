import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.exercises.domain import models as domain_models


class ExamRepository:
    """Репозиторий экзаменов"""
    def list(self, **filters) -> List[domain_models.Exam]:
        """Возвращает список экзаменов согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, exam_id: uuid.UUID) -> domain_models.Exam:
        """Возвращает экземпляр экзамена согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, exam: domain_models.Exam) -> domain_models.Exam:
        """Добавляет указанный экзамен в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyExamRepository(ExamRepository):
    """SQLAlchemy-репозиторий экзаменов"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Exam]:
        """Возвращает список экзаменов согласно указанным фильтрам"""
        q = self.session.query(domain_models.Exam)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, exam_id: uuid.UUID) -> domain_models.Exam:
        """Возвращает экземпляр экзамена согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если экзамен
                с указанным ID не найден в репозитории
        """
        q = self.session.query(domain_models.Exam).filter_by(id=exam_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Экзамен с id={exam_id} не найден',
            )

        return instance
    

    def add(self, exam: domain_models.Exam) -> domain_models.Exam:
        """Добавляет указанный экзамен в репозиторий"""
        self.session.add(exam)
        return exam
