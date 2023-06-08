import uuid
from typing import Dict
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories


class FakeGroupRepository(
    university.modules.education.repositories.GroupRepository,
):
    """Тестовый репозиторий групп студентов"""
    data: Dict[uuid.UUID, university.modules.education.domain.models.Group]


    def __init__(
        self,
        groups: List[university.modules.education.domain.models.Group],
    ) -> None:
        self.data = {group.id: group for group in groups}


    def list(
        self,
        **filters,
    ) -> List[university.modules.education.domain.models.Group]:
        """Возвращает список групп студентов согласно указанным фильтрам"""
        return list(self.data.values())
    

    def get(
        self,
        group_id: uuid.UUID,
    ) -> university.modules.education.domain.models.Group:
        """Возвращает экземпляр группы согласно указанному ID"""
        if group_id not in self.data:
            raise university.common.errors.EntityNotFoundError(
                f'Группа с id={group_id} не найдена',
            )
        return self.data[group_id]
    

    def add(
        self,
        group: university.modules.education.domain.models.Group,
    ) -> university.modules.education.domain.models.Group:
        """Добавляет указанную группу в репозиторий"""
        self.data[group.id] = group
        return group
