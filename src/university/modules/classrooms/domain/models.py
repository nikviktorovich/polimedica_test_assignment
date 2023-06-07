import datetime
import dataclasses
import uuid


@dataclasses.dataclass
class Building:
    """Доменная модель здания
    
    Атрибуты:
        id: Идентификатор здания
        code: Кодовое символьное наименование здания
    """
    id: uuid.UUID
    code: str


@dataclasses.dataclass
class Classroom:
    """Доменная модель аудитории
    
    Атрибуты:
        id: Идентификатор аудитории
        code: Кодовое символьное название аудитории
        building_id: Идентификатор здания, в котором расположена аудитория
        building: Экземпляр объекта здания
    """
    id: uuid.UUID
    code: str
    building_id: uuid.UUID
    building: Building
