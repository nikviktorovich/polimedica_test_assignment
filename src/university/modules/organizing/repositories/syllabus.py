import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.organizing.domain import models as domain_models


class SyllabusRepository:
    """Репозиторий учебного плана"""
    def list(self, **filters) -> List[domain_models.Syllabus]:
        """Возвращает список записей учебного плана
        согласно указанным фильтрам
        """
        raise NotImplementedError()
    

    def get(self, syllabus_id: uuid.UUID) -> domain_models.Syllabus:
        """Возвращает экземпляр записи учебного плана согласно указанному ID"""
        raise NotImplementedError()
    

    def add(
        self,
        syllabus: domain_models.Syllabus,
    ) -> domain_models.Syllabus:
        """Добавляет указанную запись учебного плана в репозиторий"""
        raise NotImplementedError()


class SQLAlchemySyllabusRepository(SyllabusRepository):
    """SQLAlchemy-репозиторий учебного плана"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Syllabus]:
        """Возвращает список записей учебного плана
        согласно указанным фильтрам
        """
        q = self.session.query(domain_models.Syllabus)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, syllabus_id: uuid.UUID) -> domain_models.Syllabus:
        """Возвращает экземпляр записи учебного плана согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если запись учебного плана
                с указанным ID не найдена в репозитории
        """
        q = self.session.query(domain_models.Syllabus)
        q = q.filter_by(id=syllabus_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Запись учебного плана с id={syllabus_id} не найдена',
            )

        return instance
    

    def add(
        self,
        syllabus: domain_models.Syllabus,
    ) -> domain_models.Syllabus:
        """Добавляет указанную запись учебного плана в репозиторий"""
        self.session.add(syllabus)
        return syllabus
