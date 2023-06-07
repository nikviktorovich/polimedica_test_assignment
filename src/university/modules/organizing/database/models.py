import uuid

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP

import university.database.orm
import university.modules.classrooms.database.models
import university.modules.education.database.models


class Schedule(university.database.orm.Base):
    """Таблица расписаний занятий по курсам

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
    __tablename__ = 'schedule'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    professor_id = Column(ForeignKey('professors.id'))
    course_id = Column(ForeignKey('courses.id'))
    classroom_id = Column(ForeignKey('classrooms.id'))
    begins_at = Column(type_=TIMESTAMP(timezone=True))
    ends_at = Column(type_=TIMESTAMP(timezone=True))
    professor = relationship(university.modules.education.database.models.Professor)
    course = relationship(university.modules.education.database.models.Course)
    classroom = relationship(university.modules.classrooms.database.models.Classroom)


class Department(university.database.orm.Base):
    """Таблица отделений (кафедр) ВУЗа

    Атрибуты:
        id: Идентификатор кафедры
        title: Название кафедры
        head_professor_id: Идентификатор преподавателя, заведующего кафедрой
        head_professor: Экземпляр объекта преподавателя, заведующего кафедрой
    """
    __tablename__ = 'departments'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255))
    head_professor_id = Column(ForeignKey('professors.id'))
    head_professor = relationship(
        university.modules.education.database.models.Professor,
    )


class Syllabus(university.database.orm.Base):
    """Таблица учебного плана

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
    __tablename__ = 'syllabus'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String(50))
    group_id = Column(ForeignKey('groups.id'))
    semester_id = Column(ForeignKey('semesters.id'))
    course_id = Column(ForeignKey('courses.id'))
    reserved_hours = Column(Integer)
    note = Column(Text)
    group = relationship(university.modules.education.database.models.Group)
    semester = relationship(university.modules.education.database.models.Semester)
    course = relationship(university.modules.education.database.models.Course)
