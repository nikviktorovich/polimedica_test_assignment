import uuid

import pydantic
from pydantic import Field


class StudentBase(pydantic.BaseModel):
    """Родительский класс сериализаторов студента"""
    group_id: uuid.UUID
    full_name: str = Field(max_length=255)


class StudentCreate(StudentBase):
    """Сериализатор создания нового экземпляра студента"""
    pass


class StudentRead(StudentBase):
    """Сериализатор получения данных о студенте"""
    id: uuid.UUID
