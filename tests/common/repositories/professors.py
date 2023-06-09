import uuid
from typing import Dict
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories


class FakeProfessorRepository(
    university.modules.education.repositories.ProfessorRepository,
):
    """Тестовый репозиторий преподавателей"""
    data: Dict[uuid.UUID, university.modules.education.domain.models.Professor]


    def __init__(
        self,
        professors: List[university.modules.education.domain.models.Professor],
    ) -> None:
        self.data = {professor.id: professor for professor in professors}


    def list(
        self,
        **filters,
    ) -> List[university.modules.education.domain.models.Professor]:
        """Возвращает список преподавателей согласно указанным фильтрам"""
        return list(self.data.values())
