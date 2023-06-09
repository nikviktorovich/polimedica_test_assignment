import uuid
import datetime

import fastapi
import fastapi.routing
from fastapi import Depends
from fastapi import status

import university.modules.exercises.domain.services as domain_services
from university.apps.fastapi_app import deps
from university.apps.fastapi_app.routers.grades import serializers
from university.services import unit_of_work


router = fastapi.routing.APIRouter(prefix='/grades')


@router.post('/')
def add_grade(
    grade_data: serializers.GradeCreate,
    request: fastapi.Request,
    uow: unit_of_work.UnitOfWork = Depends(deps.get_uow),
):
    """Добавляет студента в репозиторий"""
    # В случае отсутствия студента или экзамена в репозитории
    # будет выброшено исключение
    student = uow.students.get(grade_data.student_id)
    exam = uow.exams.get(grade_data.exam_id)
    created_at = grade_data.created_at or datetime.datetime.now().astimezone()

    grade_service = domain_services.GradeService(uow.grades)
    grade = grade_service.add_grade(
        student=student,
        exam=exam,
        grade=grade_data.grade,
        created_at=created_at,
    )
    uow.commit()

    redirect_url = request.url_for('get_grade', grade_id=grade.id)

    return fastapi.responses.RedirectResponse(
        url=redirect_url,
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.get('/{grade_id}')
def get_grade(
    grade_id: uuid.UUID,
    uow: unit_of_work.UnitOfWork = Depends(deps.get_uow),
):
    """Возвращает информацию об оценке
    
    Аргументы:
        grade_id: Идентификатор оценки
    """
    grade = uow.grades.get(grade_id)
    return serializers.GradeRead(
        id=grade.id,
        student_id=grade.student_id,
        exam_id=grade.exam_id,
        grade=grade.grade,
        created_at=grade.created_at,
    )


@router.put('/{grade_id}')
def update_grade(
    grade_id: uuid.UUID,
    grade_data: serializers.GradeUpdate,
    request: fastapi.Request,
    uow: unit_of_work.UnitOfWork = Depends(deps.get_uow),
):
    """Обновляет информацию об указанной оценке
    
    Аргументы:
        grade_id: Идентификатор оценки
    """
    # В случае отсутствия студента или экзамена в репозитории
    # будет выброшено исключение
    student = uow.students.get(grade_data.student_id)
    exam = uow.exams.get(grade_data.exam_id)
    created_at = grade_data.created_at or datetime.datetime.now().astimezone()

    grade_service = domain_services.GradeService(uow.grades)
    grade = grade_service.update_grade(
        grade_id=grade_id,
        student=student,
        exam=exam,
        grade=grade_data.grade,
        created_at=created_at,
    )
    uow.commit()

    redirect_url = request.url_for('get_grade', grade_id=grade.id)

    return fastapi.responses.RedirectResponse(
        url=redirect_url,
        status_code=status.HTTP_303_SEE_OTHER,
    )
