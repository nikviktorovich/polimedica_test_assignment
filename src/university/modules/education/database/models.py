import uuid

from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

import university.database.orm


class Professor(university.database.orm.Base):
    """Таблица преподавателей
    
    Атрибуты:
        id: Идентификатор преподавателя
        full_name: ФИО преподавателя
    """
    __tablename__ = 'professors'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(255))


class Semester(university.database.orm.Base):
    """Таблица семестров

    Атрибуты:
        id: Идентификатор семестра
        semester_number: Порядковый номер семестра
        begins_at: Дата начала семестра
        ends_at: Дата окончания семестра
    """
    __tablename__ = 'semesters'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    semester_number = Column(Integer, unique=True)
    begins_at = Column(Date)
    ends_at = Column(Date)


class Faculty(university.database.orm.Base):
    """Таблица факультетов

    Атрибуты:
        id: Идентификатор факультета
        title: Наименование факультета
    """
    __tablename__ = 'faculties'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255))


class Group(university.database.orm.Base):
    """Таблица групп студентов
    
    Атрибуты:
        id: Идентификатор группы
        faculty_id: Идентификатор факультета
        semester_id: Идентификатор семестра
        code: Кодовый симольный идентификатор группы
        faculty: Экземпляр объекта факультета
        semester: Экземпляр объекта семестра
    """
    __tablename__ = 'groups'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    faculty_id = Column(ForeignKey('faculties.id'))
    semester_id = Column(ForeignKey('semesters.id'))
    code = Column(String(16))
    faculty = relationship(Faculty)
    semester = relationship(Semester)


class Student(university.database.orm.Base):
    """Таблица студентов
    
    Атрибуты:
        id: Идентификатор студента
        full_name: ФИО студента
        group_id: Идентификатор группы
        group: Экземпляр объекта группы
    """
    __tablename__ = 'students'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(255))
    group_id = Column(ForeignKey('groups.id'))
    group = relationship(Group)


class Course(university.database.orm.Base):
    """Таблица курсов
    
    Атрибуты:
        id: Идентификатор курса
        title: Название курса
    """
    __tablename__ = 'courses'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255))
