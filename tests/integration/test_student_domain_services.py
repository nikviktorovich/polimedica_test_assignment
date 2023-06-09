import datetime
import uuid

import pytest

import university.modules.education.domain.models
import university.modules.education.domain.services
from university.services import unit_of_work


@pytest.mark.usefixtures('uow', 'test_client')
def test_student_domain_service_add_student(uow: unit_of_work.UnitOfWork):
    """Тестирует добавление студента через доменный сервис"""
    group = add_group(uow)
    service = university.modules.education.domain.services.StudentService(
        repo=uow.students,
    )
    created_student = service.add_student('Some Student', group=group)
    uow.commit()

    student_from_repo = uow.students.get(created_student.id)
    assert created_student == student_from_repo
    assert student_from_repo.full_name == 'Some Student'
    assert student_from_repo.group == group


def add_group(
    uow: unit_of_work.UnitOfWork,
) -> university.modules.education.domain.models.Group:
    faculty = add_faculty(uow)
    semester = get_semester(uow)
    group_id = uuid.uuid4()
    group = university.modules.education.domain.models.Group(
        id=group_id,
        code=group_id.hex[-16:],
        faculty_id=faculty.id,
        faculty=faculty,
        semester_id=semester.id,
        semester=semester,
    )
    group = uow.groups.add(group)
    uow.commit()

    return group


def get_semester(
    uow: unit_of_work.UnitOfWork,
) -> university.modules.education.domain.models.Semester:
    semesters = uow.semesters.list()

    if semesters:
        return semesters[-1]

    semester = university.modules.education.domain.models.Semester(
        id=uuid.uuid4(),
        semester_number=1,
        begins_at=datetime.datetime.now().astimezone(),
        ends_at=datetime.datetime.now().astimezone(),
    )
    semester = uow.semesters.add(semester)
    uow.commit()

    return semester

def add_faculty(
    uow: unit_of_work.UnitOfWork,
) -> university.modules.education.domain.models.Faculty:
    faculty_id = uuid.uuid4()
    faculty = university.modules.education.domain.models.Faculty(
        id=faculty_id,
        title=f'Some faculty #{faculty_id}',
    )
    faculty = uow.faculties.add(faculty)
    uow.commit()

    return faculty


@pytest.mark.usefixtures('uow', 'test_client')
def test_student_domain_service_update_student(uow: unit_of_work.UnitOfWork):
    """Тестирует обновление данных студента через доменный сервис"""
    student = add_student(uow)
    service = university.modules.education.domain.services.StudentService(
        repo=uow.students,
    )
    new_full_name = 'New ' + student.full_name
    updated_student = service.update_student(
        instance=student,
        full_name=new_full_name,
        group = student.group,
    )
    uow.commit()

    student_from_repo = uow.students.get(updated_student.id)
    assert updated_student == student_from_repo
    assert student_from_repo.full_name == new_full_name


def add_student(
    uow: unit_of_work.UnitOfWork,
) -> university.modules.education.domain.models.Student:
    group = add_group(uow)
    student_id = uuid.uuid4()
    student = university.modules.education.domain.models.Student(
        id=student_id,
        full_name=f'Random Student #{student_id}',
        group_id=group.id,
        group=group,
    )
    student = uow.students.add(student)
    uow.commit()

    return student
