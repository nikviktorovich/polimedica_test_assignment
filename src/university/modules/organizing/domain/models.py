import datetime
import dataclasses
import uuid

import university.modules.classrooms.domain.models
import university.modules.education.domain.models


@dataclasses.dataclass
class Schedule:
    """Доменная модель расписания занятий по курсам

    Атрибуты:
        id: Идентификатор записи
        professor_id: Идентификатор преподавателя
        course_id: Идентификатор курса
        classroom_id: Идентификатор аудитории
        begins_at: Дата и время начала занятия
        ends_at: Дата и время окончания занятия
        professor: Экземпляр объекта преподавателя
        course: Экземпляр объекта курса
        classroom: Экземпляр объекта аудитории
    """
    id: uuid.UUID
    professor_id: uuid.UUID
    course_id: uuid.UUID
    classroom_id: uuid.UUID
    begins_at: datetime.datetime
    ends_at: datetime.datetime
    professor: university.modules.education.domain.models.Professor
    course: university.modules.education.domain.models.Course
    classroom: university.modules.classrooms.domain.models.Classroom


@dataclasses.dataclass
class Department:
    """Доменная модель отделения (кафедры) ВУЗа
    
    Атрибуты:
        id: Идентификатор кафедры
        title: Название кафедры
        head_professor_id: Идентификатор преподавателя, заведующего кафедрой
        head_professor: Экземпляр объекта преподавателя, заведующего кафедрой
    """
    id: uuid.UUID
    title: str
    head_professor_id: uuid.UUID
    head_professor: university.modules.education.domain.models.Professor


@dataclasses.dataclass
class Syllabus:
    """Доменная модель учебного плана
    
    Атрибуты:
        id: Идентификатор записи
        code: Код учебного плана
        group_id: Идентификатор группы, которой назначен план
        semester_id: Идентификатор семестра
        course_id: Идентификатор курса
        reserved_hours: Кол-во часов
        note: Дополнительная информация
        group: Экземпляр объекта группы
        semester: Экземпляр объекта семестра
        course: Экземпляр объекта курса
    """
    id: uuid.UUID
    code: str
    group_id: uuid.UUID
    semester_id: uuid.UUID
    course_id: uuid.UUID
    reserved_hours: int
    note: str
    group: university.modules.education.domain.models.Group
    semester: university.modules.education.domain.models.Semester
    course: university.modules.education.domain.models.Course