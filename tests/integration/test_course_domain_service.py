import pytest

import university.modules.education.domain.services
from university.services import unit_of_work


@pytest.mark.usefixtures('uow', 'test_client')
def test_course_domain_service_add_course(uow: unit_of_work.UnitOfWork):
    """Тестирует добавление курса через доменный сервис"""
    service = university.modules.education.domain.services.CourseService(
        repo=uow.courses,
    )
    created_course = service.add_course('Some title')
    uow.commit()

    course_from_repo = uow.courses.get(created_course.id)
    assert created_course == course_from_repo
    assert course_from_repo.title == 'Some title'