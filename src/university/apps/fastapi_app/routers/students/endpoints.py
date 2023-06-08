import uuid

import fastapi
import fastapi.routing
from fastapi import Depends
from fastapi import status

import university.modules.education.domain.services as domain_services
from university.apps.fastapi_app import deps
from university.apps.fastapi_app.routers.students import serializers
from university.service import unit_of_work


router = fastapi.routing.APIRouter(prefix='/students')


@router.post('/')
def add_student(
    student_data: serializers.StudentCreate,
    request: fastapi.Request,
    uow: unit_of_work.UnitOfWork = Depends(deps.get_uow),
):
    """Добавляет студента в репозиторий"""
    # В случае отсутствия группы в репозитории будет выброшено исключение
    group = uow.groups.get(group_id=student_data.group_id)

    student_service = domain_services.StudentService(uow.students)
    student = student_service.add_student(
        full_name=student_data.full_name,
        group=group,
    )
    uow.commit()

    redirect_url = request.url_for('get_student', student_id=student.id)

    return fastapi.responses.RedirectResponse(
        url=redirect_url,
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.get('/{student_id}')
def get_student(
    student_id: uuid.UUID,
    uow: unit_of_work.UnitOfWork = Depends(deps.get_uow),
):
    """Возвращает ответ с данными студента
    
    Аргументы:
        student_id: Идентификатор студента
    """
    # В случае отсутствия студента в репозитории будет выброшено исключение
    student = uow.students.get(student_id=student_id)

    return serializers.StudentRead(
        id=student.id,
        full_name=student.full_name,
        group_id=student.group_id,
    )
