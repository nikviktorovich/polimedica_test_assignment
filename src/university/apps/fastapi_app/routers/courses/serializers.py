import uuid

import pydantic
from pydantic import Field


class CourseBase(pydantic.BaseModel):
    """Родительский класс сериализаторов курса"""
    title: str = Field(max_length=255)


class CourseRead(CourseBase):
    """Сериализатор запроса на получение курса"""
    id: uuid.UUID


class CourseCreate(CourseBase):
    """Сериализатор запроса на создание курса"""
    pass
