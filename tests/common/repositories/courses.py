import uuid
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories
from . import base


class FakeCourseRepository(
    base.BaseFakeRepository[university.modules.education.domain.models.Course],
    university.modules.education.repositories.CourseRepository,
):
    """Тестовый репозиторий курсов"""
    def __init__(
        self,
        courses: List[university.modules.education.domain.models.Course],
    ) -> None:
        super().__init__(courses)
    

    def get(
        self,
        course_id: uuid.UUID,
    ) -> university.modules.education.domain.models.Course:
        return super().get(course_id)
    

    def add(
        self,
        course: university.modules.education.domain.models.Course,
    ) -> university.modules.education.domain.models.Course:
        return super().add(course)
