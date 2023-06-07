import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.organizing.domain import models as domain_models


class ScheduleRepository:
    """Репозиторий расписаний"""
    def list(self, **filters) -> List[domain_models.Schedule]:
        """Возвращает список записей расписаний согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, schedule_record_id: uuid.UUID) -> domain_models.Schedule:
        """Возвращает экземпляр записи расписания согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, schedule: domain_models.Schedule) -> domain_models.Schedule:
        """Добавляет указанную запись в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyScheduleRepository(ScheduleRepository):
    """SQLAlchemy-репозиторий расписаний"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Schedule]:
        """Возвращает список записей расписаний согласно указанным фильтрам"""
        q = self.session.query(domain_models.Schedule)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, schedule_record_id: uuid.UUID) -> domain_models.Schedule:
        """Возвращает экземпляр записи расписания согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если запись
                с указанным ID не найдена в репозитории
        """
        q = self.session.query(domain_models.Schedule)
        q = q.filter_by(id=schedule_record_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Запись в расписании с id={schedule_record_id} не найдена',
            )

        return instance
    

    def add(self, schedule: domain_models.Schedule) -> domain_models.Schedule:
        """Добавляет указанную запись в репозиторий"""
        self.session.add(schedule)
        return schedule
