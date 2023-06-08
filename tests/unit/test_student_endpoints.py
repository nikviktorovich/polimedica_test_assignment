import uuid

import fastapi
import pytest
from fastapi import status
from fastapi.testclient import TestClient

import university.modules.education.domain.models as domain_models
from university.apps.fastapi_app import deps

from .. import common


@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_student_endpoint_get_student(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует успешное получение данных о студенте"""
    group = domain_models.Group(
        id=uuid.uuid4(),
        faculty_id=uuid.uuid4(),
        semester_id=uuid.uuid4(),
        code='somecode',
        faculty=None,   # type: ignore
        semester=None,  # type: ignore
    )
    group_repo = common.FakeGroupRepository([group])

    student = domain_models.Student(
        id=uuid.uuid4(),
        full_name='Some Student',
        group_id=group.id,
        group=group,
    )
    student_repo = common.FakeStudentRepository([student])

    uow = common.FakeUOW(students=student_repo, groups=group_repo)
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.get(f'/students/{student.id}')
    assert resp.status_code == status.HTTP_200_OK
    assert uuid.UUID(resp.json()['id']) == student.id


@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_student_endpoint_add_student_successfully(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует успешное добавление студента"""
    group = domain_models.Group(
        id=uuid.uuid4(),
        faculty_id=uuid.uuid4(),
        semester_id=uuid.uuid4(),
        code='somecode',
        faculty=None,   # type: ignore
        semester=None,  # type: ignore
    )
    group_repo = common.FakeGroupRepository([group])
    student_repo = common.FakeStudentRepository([])
    uow = common.FakeUOW(students=student_repo, groups=group_repo)
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.post('/students', json={
        'full_name': 'Some Name',
        'group_id': str(group.id),
    })
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['full_name'] == 'Some Name'


@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_student_endpoint_add_student_with_wrong_group_id(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует успешное добавление студента"""
    group_repo = common.FakeGroupRepository([])
    student_repo = common.FakeStudentRepository([])
    uow = common.FakeUOW(students=student_repo, groups=group_repo)
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.post('/students', json={
        'full_name': 'Some Name',
        'group_id': str(uuid.uuid4()),
    })
    assert resp.status_code == status.HTTP_404_NOT_FOUND



@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_student_endpoint_update_student(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует обновление данных студента"""
    group = domain_models.Group(
        id=uuid.uuid4(),
        faculty_id=uuid.uuid4(),
        semester_id=uuid.uuid4(),
        code='somecode',
        faculty=None,   # type: ignore
        semester=None,  # type: ignore
    )
    group_repo = common.FakeGroupRepository([group])

    student = domain_models.Student(
        id=uuid.uuid4(),
        full_name='Some Student',
        group_id=group.id,
        group=group,
    )
    student_repo = common.FakeStudentRepository([student])

    uow = common.FakeUOW(students=student_repo, groups=group_repo)
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.put(f'/students/{student.id}', json={
        'full_name': 'Some New Student',
        'group_id': str(group.id),
    })
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['full_name'] == 'Some New Student'
