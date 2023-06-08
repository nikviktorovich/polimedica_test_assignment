import uuid
from typing import Dict
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories


class FakeStudentRepository(
    university.modules.education.repositories.StudentRepository,
):
    """Тестовый репозиторий студентов"""
    data: Dict[uuid.UUID, university.modules.education.domain.models.Student]


    def __init__(
        self,
        students: List[university.modules.education.domain.models.Student],
    ) -> None:
        self.data = {student.id: student for student in students}


    def list(
        self,
        **filters,
    ) -> List[university.modules.education.domain.models.Student]:
        """Возвращает список студентов согласно указанным фильтрам"""
        return list(self.data.values())
    

    def get(
        self,
        student_id: uuid.UUID,
    ) -> university.modules.education.domain.models.Student:
        """Возвращает экземпляр студента согласно указанному ID"""
        if student_id not in self.data:
            raise university.common.errors.EntityNotFoundError(
                f'Студент с id={student_id} не найден',
            )
        return self.data[student_id]
    

    def add(
        self,
        student: university.modules.education.domain.models.Student,
    ) -> university.modules.education.domain.models.Student:
        """Добавляет указанного студента в репозиторий"""
        self.data[student.id] = student
        return student
