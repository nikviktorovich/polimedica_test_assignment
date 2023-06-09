import uuid
from typing import List

import sqlalchemy.orm

import university.common.errors
import university.modules.organizing.domain.models
from university.modules.education.domain import models as domain_models


class StudentRepository:
    """Репозиторий студентов"""
    def list(self, **filters) -> List[domain_models.Student]:
        """Возвращает список студентов согласно указанным фильтрам"""
        raise NotImplementedError()
    

    def get(self, student_id: uuid.UUID) -> domain_models.Student:
        """Возвращает экземпляр студента согласно указанному ID"""
        raise NotImplementedError()
    

    def add(self, student: domain_models.Student) -> domain_models.Student:
        """Добавляет указанного студента в репозиторий"""
        raise NotImplementedError()
    

    def list_by_course(
        self,
        course_id: uuid.UUID,
    ) -> List[domain_models.Student]:
        """Возвращает список студентов с указанным курсом в семестре"""
        raise NotImplementedError()
    

    def delete(self, student: domain_models.Student) -> None:
        """Удаляет указанного студента из репозитория"""
        raise NotImplementedError()


class SQLAlchemyStudentRepository(StudentRepository):
    """SQLAlchemy-репозиторий студентов"""
    session: sqlalchemy.orm.Session


    def __init__(self, session: sqlalchemy.orm.Session) -> None:
        """Инициализирует репозиторий с указанной сессией БД
        
        Аргументы:
            session: SQLAlchemy-сессия базы данных
        """
        self.session = session



    def list(self, **filters) -> List[domain_models.Student]:
        """Возвращает список студентов согласно указанным фильтрам"""
        q = self.session.query(domain_models.Student)

        if filters:
            q = q.filter_by(**filters)
        
        return q.all()
    

    def get(self, student_id: uuid.UUID) -> domain_models.Student:
        """Возвращает экземпляр студента согласно указанному ID
        
        Исключения:
            EntityNotFoundError: Выбрасывается, если студент
                с указанным ID не найден в репозитории
        """
        q = self.session.query(domain_models.Student).filter_by(id=student_id)
        instance = q.first()

        if instance is None:
            raise university.common.errors.EntityNotFoundError(
                f'Студент с id={student_id} не найден',
            )

        return instance
    

    def add(self, student: domain_models.Student) -> domain_models.Student:
        """Добавляет указанного студента в репозиторий"""
        self.session.add(student)
        return student
    

    def list_by_course(
        self,
        course_id: uuid.UUID,
    ) -> List[domain_models.Student]:
        """Возвращает список студентов с указанным курсом в семестре"""
        q = self.session.query(domain_models.Student)
        q = q.join(domain_models.Group)
        q = q.join(university.modules.organizing.domain.models.Syllabus)
        q = q.join(domain_models.Semester)
        q = q.join(domain_models.Course).filter_by(id=course_id)
        
        return q.all()
    

    def delete(self, student: domain_models.Student) -> None:
        """Удаляет указанного студента из репозитория"""
        self.session.delete(student)
