import uuid
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories
from . import base


class FakeGroupRepository(
    base.BaseFakeRepository[university.modules.education.domain.models.Group],
    university.modules.education.repositories.GroupRepository,
):
    """Тестовый репозиторий групп студентов"""
    def __init__(
        self,
        groups: List[university.modules.education.domain.models.Group],
    ) -> None:
        super().__init__(groups)
    

    def get(
        self,
        group_id: uuid.UUID,
    ) -> university.modules.education.domain.models.Group:
        return super().get(group_id)
    

    def add(
        self,
        group: university.modules.education.domain.models.Group,
    ) -> university.modules.education.domain.models.Group:
        return super().add(group)
