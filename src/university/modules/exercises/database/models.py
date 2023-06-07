import uuid

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP

import university.database.orm
import university.modules.classrooms.database.models
import university.modules.education.database.models
import university.modules.organizing.database.models


class Exam(university.database.orm.Base):
    """Таблица экзаменов

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
    __tablename__ = 'exams'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(ForeignKey('courses.id'))
    professor_id = Column(ForeignKey('professors.id'))
    group_id = Column(ForeignKey('groups.id'))
    classroom_id = Column(ForeignKey('classrooms.id'))
    begins_at = Column(type_=TIMESTAMP(timezone=True))
    course = relationship(university.modules.education.database.models.Course)
    professor = relationship(university.modules.education.database.models.Professor)
    group = relationship(university.modules.education.database.models.Group)
    classroom = relationship(university.modules.classrooms.database.models.Classroom)


class Grade(university.database.orm.Base):
    """Таблица оценок

    Атрибуты:
        id: Идентификатор оценки
        student_id: Идентификатор студента
        exam_id: Идентификатор экзамена
        grade: Оценка студента за экзамен
        created_at: Дата выставления оценки
        student: Экземпляр объекта студента
        exam: Экземпляр объекта экзамена
    """
    __tablename__ = 'grades'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(ForeignKey('students.id'))
    exam_id = Column(ForeignKey('exams.id'))
    grade = Column(Integer)
    created_at = Column(type_=TIMESTAMP(timezone=True))
    student = relationship(university.modules.education.database.models.Student)
    exam = relationship(Exam)


class Exercise(university.database.orm.Base):
    """Таблица самостоятельных работ

    Атрибуты:
        id: Идентификатор самостоятельного задания
        course_id: Идентификатор курса, к которому подготовлено задание
        content: Содержание самостоятельной работы
        created_at: Дата и время создания задания
        course: Экземпляр объекта курса
    """
    __tablename__ = 'exercises'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(ForeignKey('courses.id'))
    content = Column(Text)
    created_at = Column(type_=TIMESTAMP(timezone=True))
    course = relationship(university.modules.education.database.models.Course)


class EducationalProgram(university.database.orm.Base):
    """Таблица программы курса (учебного года)

    Атрибуты:
        id: Идентификатор записи
        course_id: Идентификатор курса
        topic: Наименование темы
        content: Описание содержания учебного материала по теме
        exercise_id: Опциональный идентификатор самостоятельной работы для темы
        course: Экземпляр объекта курса
        exercise: Экземпляр объекта самостоятельной работы
    """
    __tablename__ = 'educational_programs'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(ForeignKey('courses.id'))
    topic = Column(String(255))
    content = Column(Text)
    exercise_id = Column(ForeignKey('exercises.id'))
    course = relationship(university.modules.education.database.models.Course)
    exercise = relationship(Exercise)
