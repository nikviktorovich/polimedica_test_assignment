import uuid
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories
from . import base


class FakeStudentRepository(
    base.BaseFakeRepository[university.modules.education.domain.models.Student],
    university.modules.education.repositories.StudentRepository,
):
    """Тестовый репозиторий студентов"""
    def __init__(
        self,
        students: List[university.modules.education.domain.models.Student],
    ) -> None:
        super().__init__(students)
    

    def get(
        self,
        student_id: uuid.UUID,
    ) -> university.modules.education.domain.models.Student:
        return super().get(student_id)
    

    def add(
        self,
        student: university.modules.education.domain.models.Student,
    ) -> university.modules.education.domain.models.Student:
        return super().add(student)
    

    def delete(
        self,
        student: university.modules.education.domain.models.Student,
    ) -> None:
        """Удаляет указанного студента из репозитория"""
        del self.data[student.id]
