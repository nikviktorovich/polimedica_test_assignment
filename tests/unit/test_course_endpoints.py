import uuid

import fastapi
import pytest
from fastapi import status
from fastapi.testclient import TestClient

import university.modules.education.domain.models as domain_models
from university.apps.fastapi_app import deps

from .. import common


@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_course_endpoint_get_course(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует маршрут получения экземпляра курса по ID"""
    course = domain_models.Course(id=uuid.uuid4(), title='Some title')
    course_repo = common.FakeCourseRepository([course])
    uow = common.FakeUOW(courses=course_repo)
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.get(f'/courses/{course.id.hex}')
    assert resp.status_code == status.HTTP_200_OK
    assert uuid.UUID(resp.json()['id']) == course.id


@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_course_endpoint_add_course(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует маршрут создания экземпляра курса"""
    course_repo = common.FakeCourseRepository([])
    uow = common.FakeUOW(courses=course_repo)
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.post('/courses', json={'title': 'Some title'})
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['title'] == 'Some title'
