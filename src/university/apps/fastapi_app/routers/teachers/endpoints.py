from typing import List

import fastapi
import fastapi.routing
from fastapi import Depends

from university.apps.fastapi_app import deps
from university.apps.fastapi_app.routers.teachers import serializers
from university.services import unit_of_work


router = fastapi.routing.APIRouter(prefix='/teachers')


@router.get('/')
def list_teachers(uow: unit_of_work.UnitOfWork = Depends(deps.get_uow)):
    """Возвращает список данных преподавателей"""
    professors = uow.professors.list()
    professor_serializers: List[serializers.TeacherRead] = []
    for professor in professors:
        professor_serializer = serializers.TeacherRead(
            id=professor.id,
            full_name=professor.full_name,
        )
        professor_serializers.append(professor_serializer)
    return professor_serializers