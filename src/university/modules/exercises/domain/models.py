import dataclasses
import datetime
import uuid

import university.modules.classrooms.domain.models
import university.modules.education.domain.models


@dataclasses.dataclass
class Exam:
    """Доменная модель экзамена

    Атрибуты:
        id: Идентификатор экзамена
        course_id: Идентификатор курса, по которому идет экзамен
        professor_id: Идентификатор преподавателя, принимающего экзамен
        group_id: Идентификатор экзаменуемой группы
        classroom_id: Идентификатор аудитории
        begins_at: Дата начала экзамена
        course: Экземпляр объекта курса
        professor: Экземпляр объекта преподавателя
        group: Экземпляр объекта группы студентов
        classroom: Экземпляр объекта аудитории
    """
    id: uuid.UUID
    course_id: uuid.UUID
    professor_id: uuid.UUID
    group_id: uuid.UUID
    classroom_id: uuid.UUID
    begins_at: datetime.datetime
    course: university.modules.education.domain.models.Course
    professor: university.modules.education.domain.models.Professor
    group: university.modules.education.domain.models.Group
    classroom: university.modules.classrooms.domain.models.Classroom


@dataclasses.dataclass
class Grade:
    """Доменная модель оценки
    
    Атрибуты:
        id: Идентификатор оценки
        student_id: Идентификатор студента
        exam_id: Идентификатор экзамена
        grade: Оценка студента за экзамен
        created_at: Дата выставления оценки
        student: Экземпляр объекта студента
        exam: Экземпляр объекта экзамена
    """
    id: uuid.UUID
    student_id: uuid.UUID
    exam_id: uuid.UUID
    grade: int
    created_at: datetime.datetime
    student: university.modules.education.domain.models.Student
    exam: Exam


@dataclasses.dataclass
class Exercise:
    """Доменная модель самостоятельной работы
    
    Атрибуты:
        id: Идентификатор самостоятельного задания
        course_id: Идентификатор курса, к которому подготовлено задание
        content: Содержание самостоятельной работы
        created_at: Дата и время создания задания
        course: Экземпляр объекта курса
    """
    id: uuid.UUID
    course_id: uuid.UUID
    content: str
    created_at: datetime.datetime
    course: university.modules.education.domain.models.Course


@dataclasses.dataclass
class EducationalProgram:
    """Доменная модель программы курса (учебного года)
    
    Атрибуты:
        id: Идентификатор записи
        course_id: Идентификатор курса
        topic: Наименование темы
        content: Описание содержания учебного материала по теме
        exercise_id: Опциональный идентификатор самостоятельной работы для темы
        course: Экземпляр объекта курса
        exercise: Экземпляр объекта самостоятельной работы
    """
    id: uuid.UUID
    course_id: uuid.UUID
    topic: str
    content: str
    exercise_id: uuid.UUID
    course: university.modules.education.domain.models.Course
    exercise: Exercise
