import datetime
import uuid

import pytest

import university.modules.education.domain.models
import university.modules.education.domain.services
import university.modules.exercises.domain.models
import university.modules.exercises.domain.services
import university.modules.classrooms.domain.models
from university.services import unit_of_work


@pytest.mark.usefixtures('uow', 'test_client')
def test_grade_domain_service_add_grade(uow: unit_of_work.UnitOfWork):
    """Тестирует добавление оценки через доменный сервис"""
    service = university.modules.exercises.domain.services.GradeService(
        repo=uow.grades,
    )

    student = add_student(uow)
    exam = add_exam(uow, student.group)
    created_grade = service.add_grade(
        student=student,
        exam=exam,
        grade=4,
        created_at=datetime.datetime.now().astimezone(),
    )
    uow.commit()

    grade_from_repo = uow.grades.get(created_grade.id)
    assert created_grade == grade_from_repo
    assert grade_from_repo.student == student
    assert grade_from_repo.exam == exam
    assert grade_from_repo.grade == 4


@pytest.mark.usefixtures('uow', 'test_client')
def test_grade_domain_service_update_grade(uow: unit_of_work.UnitOfWork):
    """Тестирует обновление данных оценки через доменный сервис"""
    service = university.modules.exercises.domain.services.GradeService(
        repo=uow.grades,
    )

    student = add_student(uow)
    exam = add_exam(uow, student.group)
    created_grade = service.add_grade(
        student=student,
        exam=exam,
        grade=4,
        created_at=datetime.datetime.now().astimezone(),
    )
    uow.commit()
    assert created_grade.grade == 4

    updated_grade = service.update_grade(
        created_grade,
        student=student,
        exam=exam,
        grade=5,
        created_at=created_grade.created_at,
    )
    uow.commit()

    assert updated_grade == created_grade
    assert updated_grade.grade == 5


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


def add_exam(
    uow: unit_of_work.UnitOfWork,
    group: university.modules.education.domain.models.Group,
) -> university.modules.exercises.domain.models.Exam:
    course = add_course(uow)
    professor = add_professor(uow)
    classroom = add_classroom(uow)
    exam = university.modules.exercises.domain.models.Exam(
        id=uuid.uuid4(),
        course_id=course.id,
        course=course,
        group_id=group.id,
        group=group,
        professor_id=professor.id,
        professor=professor,
        classroom_id=classroom.id,
        classroom=classroom,
        begins_at=datetime.datetime.now().astimezone(),
    )
    uow.exams.add(exam)
    uow.commit()

    return exam


def add_course(
    uow: unit_of_work.UnitOfWork,
) -> university.modules.education.domain.models.Course:
    course = university.modules.education.domain.models.Course(
        id=uuid.uuid4(),
        title='Some course',
    )
    uow.courses.add(course)
    uow.commit()

    return course


def add_professor(
    uow: unit_of_work.UnitOfWork,
) -> university.modules.education.domain.models.Professor:
    professor = university.modules.education.domain.models.Professor(
        id=uuid.uuid4(),
        full_name='Some Professor',
    )
    uow.professors.add(professor)
    uow.commit()

    return professor


def add_classroom(
    uow: unit_of_work.UnitOfWork,
) -> university.modules.classrooms.domain.models.Classroom:
    building_id = uuid.uuid4()
    building = university.modules.classrooms.domain.models.Building(
        id=uuid.uuid4(),
        code=building_id.hex,
    )
    uow.buildings.add(building)
    uow.commit()

    classroom_id = uuid.uuid4()
    classroom = university.modules.classrooms.domain.models.Classroom(
        id=classroom_id,
        code=classroom_id.hex,
        building_id=building.id,
        building=building,
    )
    uow.classrooms.add(classroom)
    uow.commit()

    return classroom
