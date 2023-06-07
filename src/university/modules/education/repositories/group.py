import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.education.domain import models as domain_models


class GroupRepository:
    """Репозиторий групп"""
    def list(self, **filters) -> List[domain_models.Group]:
        """Возвращает список групп согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, group_id: uuid.UUID) -> domain_models.Group:
        """Возвращает экземпляр группы согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, group: domain_models.Group) -> domain_models.Group:
        """Добавляет указанную группу в репозиторий"""
        raise NotImplementedError()


class SQLAlchemyGroupRepository(GroupRepository):
    """SQLAlchemy-репозиторий групп"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Group]:
        """Возвращает список групп согласно указанным фильтрам"""
        q = self.session.query(domain_models.Group)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, group_id: uuid.UUID) -> domain_models.Group:
        """Возвращает экземпляр группы согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если группа
                с указанным ID не найден в репозитории
        """
        q = self.session.query(domain_models.Group).filter_by(id=group_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Группа с id={group_id} не найдена',
            )

        return instance
    

    def add(self, group: domain_models.Group) -> domain_models.Group:
        """Добавляет указанную группу в репозиторий"""
        self.session.add(group)
        return group
