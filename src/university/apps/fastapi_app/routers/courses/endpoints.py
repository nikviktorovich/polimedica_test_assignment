import uuid

import fastapi
import fastapi.responses
import fastapi.routing
from fastapi import Depends
from fastapi import status

import university.modules.education.domain.services as domain_services
from university.apps.fastapi_app import deps
from university.apps.fastapi_app.routers.courses import serializers
from university.services import unit_of_work


router = fastapi.routing.APIRouter(prefix='/courses')


@router.post('/')
def add_course(
    course_data: serializers.CourseCreate,
    request: fastapi.Request,
    uow: unit_of_work.UnitOfWork = Depends(deps.get_uow),
):
    """Маршрут добавления нового курса в репозиторий"""
    course_service = domain_services.CourseService(uow.courses)
    course = course_service.add_course(title=course_data.title)
    uow.commit()

    redirect_url = request.url_for('get_course', course_id=course.id)

    return fastapi.responses.RedirectResponse(
        url=redirect_url,
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.get('/{course_id}', response_model=serializers.CourseRead)
def get_course(
    course_id: uuid.UUID,
    uow: unit_of_work.UnitOfWork = Depends(deps.get_uow),
):
    """Маршрут получения экземпляра курса по его ID"""
    course = uow.courses.get(course_id=course_id)

    return serializers.CourseRead(
        id=course.id,
        title=course.title,
    )
