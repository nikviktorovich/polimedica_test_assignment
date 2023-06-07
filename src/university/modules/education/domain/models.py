import dataclasses
import datetime
import uuid


@dataclasses.dataclass
class Professor:
    """Доменная модель преподавателя

    Атрибуты:
        id: Идентификатор преподавателя
        full_name: ФИО преподавателя
    """
    id: uuid.UUID
    full_name: str


@dataclasses.dataclass
class Semester:
    """Доменная модель семестра

    Атрибуты:
        id: Идентификатор семестра
        semester_number: Порядковый номер семестра
        begins_at: Дата начала семестра
        ends_at: Дата окончания семестра
    """
    id: uuid.UUID
    semester_number: int
    begins_at: datetime.datetime
    ends_at: datetime.datetime


@dataclasses.dataclass
class Faculty:
    """Доменная модель факультета

    Атрибуты:
        id: Идентификатор факультета
        title: Наименование факультета
    """
    id: uuid.UUID
    title: str


@dataclasses.dataclass
class Group:
    """Доменная модель группы студентов
    
    Атрибуты:
        id: Идентификатор группы
        faculty_id: Идентификатор факультета
        semester_id: Идентификатор семестра
        code: Кодовый симольный идентификатор группы
        faculty: Экземпляр объекта факультета
        semester: Экземпляр объекта семестра
    """
    id: uuid.UUID
    faculty_id: uuid.UUID
    semester_id: uuid.UUID
    code: str
    faculty: Faculty
    semester: Semester


@dataclasses.dataclass
class Student:
    """Доменная модель студента
    
    Атрибуты:
        id: Идентификатор студента
        full_name: ФИО студента
        group_id: Идентификатор группы
        group: Экземпляр объекта группы
    """
    id: uuid.UUID
    full_name: str
    group_id: uuid.UUID
    group: Group


@dataclasses.dataclass
class Course:
    """Доменная модель курса
    
    Атрибуты:
        id: Идентификатор курса
        title: Название курса
    """
    id: uuid.UUID
    title: str
