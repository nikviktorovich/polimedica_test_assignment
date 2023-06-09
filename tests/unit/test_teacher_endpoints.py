import uuid

import fastapi
import pytest
from fastapi import status
from fastapi.testclient import TestClient

import university.modules.education.domain.models as domain_models
from university.apps.fastapi_app import deps

from .. import common


@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_teacher_endpoint_list_teachers(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует успешное получение списка преподавателей"""
    professor_repo = common.FakeProfessorRepository([
        domain_models.Professor(id=uuid.uuid4(), full_name='Professor 1'),
        domain_models.Professor(id=uuid.uuid4(), full_name='Professor 2'),
    ])

    uow = common.FakeUOW(professors=professor_repo)
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.get('/teachers')
    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == len(professor_repo.list())
