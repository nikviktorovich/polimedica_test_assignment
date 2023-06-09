import datetime
import uuid
from typing import Optional

import pydantic


class GradeBase(pydantic.BaseModel):
    """Родительский класс сериализаторов оценки"""
    student_id: uuid.UUID
    exam_id: uuid.UUID
    grade: int


class GradeCreate(GradeBase):
    """Сериализатор создания оценки"""
    created_at: Optional[datetime.datetime] = None


class GradeRead(GradeBase):
    """Сериализатор вывода оценки"""
    id: uuid.UUID
    created_at: datetime.datetime


class GradeUpdate(GradeCreate):
    """Сериализатор обновления информации оценки"""
    pass
