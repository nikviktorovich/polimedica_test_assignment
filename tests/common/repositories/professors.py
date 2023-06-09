import uuid
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories
from . import base


class FakeProfessorRepository(
    base.BaseFakeRepository[university.modules.education.domain.models.Professor],
    university.modules.education.repositories.ProfessorRepository,
):
    """Тестовый репозиторий преподавателей"""
    def __init__(
        self,
        professors: List[university.modules.education.domain.models.Professor],
    ) -> None:
        super().__init__(professors)


    def get(
        self,
        professor_id: uuid.UUID,
    ) -> university.modules.education.domain.models.Professor:
        return super().get(professor_id)
    

    def add(
        self,
        professor: university.modules.education.domain.models.Professor,
    ) -> university.modules.education.domain.models.Professor:
        return super().add(professor)
