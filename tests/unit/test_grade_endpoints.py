import datetime
import uuid

import fastapi
import pytest
from fastapi import status
from fastapi.testclient import TestClient

import university.modules.education.domain.models
import university.modules.exercises.domain.models
from university.apps.fastapi_app import deps

from .. import common


@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_grade_endpoint_add_grade(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует успешное добавление оценки"""
    student = university.modules.education.domain.models.Student(
        id=uuid.uuid4(),
        full_name='Some Student',
        group_id=None, # type: ignore
        group=None, # type: ignore
    )
    student_repo = common.FakeStudentRepository([student])

    exam = university.modules.exercises.domain.models.Exam(
        id=uuid.uuid4(),
        professor_id=None, # type: ignore
        professor=None, # type: ignore
        group_id=None, # type: ignore
        group=None, # type: ignore
        classroom_id=None, # type: ignore
        classroom=None, # type: ignore
        course_id=None, # type: ignore
        course=None, # type: ignore
        begins_at=datetime.datetime.now(),
    )
    exam_repo = common.FakeExamRepository([exam])

    grade_repo = common.FakeGradeRepository([])
    uow = common.FakeUOW(
        students=student_repo,
        exams=exam_repo,
        grades=grade_repo,
    )
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.post(f'/grades', json={
        'student_id': str(student.id),
        'exam_id': str(exam.id),
        'grade': 4,
    })
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['grade'] == 4


@pytest.mark.usefixtures('fastapi_app', 'test_client')
def test_grade_endpoint_update_grade(
    fastapi_app: fastapi.FastAPI,
    test_client: TestClient,
):
    """Тестирует успешное добавление оценки"""
    student = university.modules.education.domain.models.Student(
        id=uuid.uuid4(),
        full_name='Some Student',
        group_id=None, # type: ignore
        group=None, # type: ignore
    )
    student_repo = common.FakeStudentRepository([student])

    exam = university.modules.exercises.domain.models.Exam(
        id=uuid.uuid4(),
        professor_id=None, # type: ignore
        professor=None, # type: ignore
        group_id=None, # type: ignore
        group=None, # type: ignore
        classroom_id=None, # type: ignore
        classroom=None, # type: ignore
        course_id=None, # type: ignore
        course=None, # type: ignore
        begins_at=datetime.datetime.now(),
    )
    exam_repo = common.FakeExamRepository([exam])

    grade = university.modules.exercises.domain.models.Grade(
        id=uuid.uuid4(),
        student_id=student.id,
        student=student,
        exam_id=exam.id,
        exam=exam,
        grade=4,
        created_at=datetime.datetime.now().astimezone(),
    )
    grade_repo = common.FakeGradeRepository([grade])

    uow = common.FakeUOW(
        students=student_repo,
        exams=exam_repo,
        grades=grade_repo,
    )
    fastapi_app.dependency_overrides[deps.get_uow] = lambda: uow

    resp = test_client.put(f'/grades/{grade.id}', json={
        'student_id': str(student.id),
        'exam_id': str(exam.id),
        'grade': 5,
    })
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['grade'] == 5
    assert grade.grade == 5
