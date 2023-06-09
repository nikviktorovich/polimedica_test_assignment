import uuid
from typing import List

import university.common.errors
import university.modules.exercises.domain.models
import university.modules.exercises.repositories
from . import base


class FakeGradeRepository(
    base.BaseFakeRepository[university.modules.exercises.domain.models.Grade],
    university.modules.exercises.repositories.GradeRepository,
):
    """Тестовый репозиторий оценок"""
    def __init__(
        self,
        grades: List[university.modules.exercises.domain.models.Grade],
    ) -> None:
        super().__init__(grades)
    

    def get(
        self,
        grade_id: uuid.UUID,
    ) -> university.modules.exercises.domain.models.Grade:
        return super().get(grade_id)
    

    def add(
        self,
        grade: university.modules.exercises.domain.models.Grade
    ) -> university.modules.exercises.domain.models.Grade:
        return super().add(grade)

