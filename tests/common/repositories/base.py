import uuid
from typing import Dict
from typing import List
from typing import Generic
from typing import TypeVar

import university.common.errors


T = TypeVar('T')


class BaseFakeRepository(Generic[T]):
    data: Dict[uuid.UUID, T]


    def __init__(self, entities: List[T]) -> None:
        self.data = {entity.id: entity for entity in entities} # type: ignore


    def list(self, **filters) -> List[T]:
        return list(self.data.values())
    

    def get(self, entity_id: uuid.UUID) -> T:
        if entity_id not in self.data:
            raise university.common.errors.EntityNotFoundError(
                f'Запись с id={entity_id} не найдена',
            )
        return self.data[entity_id]
    

    def add(self, entity: T) -> T:
        self.data[entity.id] = entity # type: ignore
        return entity
