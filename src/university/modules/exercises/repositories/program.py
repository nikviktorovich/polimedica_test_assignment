import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
from university.modules.exercises.domain import models as domain_models


class ProgramRepository:
    """Репозиторий программ курса"""
    def list(self, **filters) -> List[domain_models.EducationalProgram]:
        """Возвращает список записей программ согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, program_id: uuid.UUID) -> domain_models.EducationalProgram:
        """Возвращает экземпляр записи программ согласно указанному ID"""
        raise NotImplementedError()
    

    def add(
        self,
        program: domain_models.EducationalProgram,
    ) -> domain_models.EducationalProgram:
        """Добавляет указанную запись в репозиторий программ"""
        raise NotImplementedError()


class SQLAlchemyProgramRepository(ProgramRepository):
    """SQLAlchemy-репозиторий программ курса"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.EducationalProgram]:
        """Возвращает список записей программ согласно указанным фильтрам"""
        q = self.session.query(domain_models.EducationalProgram)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, program_id: uuid.UUID) -> domain_models.EducationalProgram:
        """Возвращает экземпляр записи программ согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если запись
                с указанным ID не найдена в репозитории
        """
        q = self.session.query(domain_models.EducationalProgram)
        q = q.filter_by(id=program_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Запись программы курса с id={program_id} не найдена',
            )

        return instance
    

    def add(
        self,
        program: domain_models.EducationalProgram,
    ) -> domain_models.EducationalProgram:
        """Добавляет указанную запись в репозиторий программ"""
        self.session.add(program)
        return program
