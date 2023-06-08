import uuid
from typing import Dict
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories


class FakeCourseRepository(
    university.modules.education.repositories.CourseRepository,
):
    """Тестовый репозиторий курсов"""
    data: Dict[uuid.UUID, university.modules.education.domain.models.Course]


    def __init__(
        self,
        courses: List[university.modules.education.domain.models.Course],
    ) -> None:
        self.data = {course.id: course for course in courses}


    def list(
        self,
        **filters,
    ) -> List[university.modules.education.domain.models.Course]:
        """Возвращает список курсов согласно указанным фильтрам"""
        return list(self.data.values())
    

    def get(
        self,
        course_id: uuid.UUID,
    ) -> university.modules.education.domain.models.Course:
        """Возвращает экземпляр курса согласно указанному ID"""
        if course_id not in self.data:
            raise university.common.errors.EntityNotFoundError(
                f'Курс с id={course_id} не найден',
            )
        return self.data[course_id]
    

    def add(
        self,
        course: university.modules.education.domain.models.Course,
    ) -> university.modules.education.domain.models.Course:
        """Добавляет указанный курс в репозиторий"""
        self.data[course.id] = course
        return course
