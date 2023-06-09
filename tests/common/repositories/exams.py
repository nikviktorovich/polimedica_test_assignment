import uuid
from typing import List

import university.common.errors
import university.modules.exercises.domain.models
import university.modules.exercises.repositories
from . import base


class FakeExamRepository(
    base.BaseFakeRepository[university.modules.exercises.domain.models.Exam],
    university.modules.exercises.repositories.ExamRepository,
):
    """Тестовый репозиторий оценок"""
    def __init__(
        self,
        exams: List[university.modules.exercises.domain.models.Exam],
    ) -> None:
        super().__init__(exams)
    

    def get(
        self,
        exam_id: uuid.UUID,
    ) -> university.modules.exercises.domain.models.Exam:
        return super().get(exam_id)
    

    def add(
        self,
        exam: university.modules.exercises.domain.models.Exam
    ) -> university.modules.exercises.domain.models.Exam:
        return super().add(exam)

