import uuid
from typing import Any
from typing import Dict
from typing import List

import university.common.errors
import university.modules.education.domain.models
import university.modules.education.repositories
import university.service.unit_of_work


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


class FakeUOW(university.service.unit_of_work.UnitOfWork):
    """Тестовая единица работы"""
    def __init__(self, repos: Dict[str, Any]) -> None:
        """Инициализирует тестовую единицу работы
        
        Аргументы:
            repos: Словарь репозиториев вида: 'имя_репозитория': 'репозиторий'
        """
        for repo_name, repo in repos.items():
            setattr(self, repo_name, repo)
    

    def commit(self) -> None:
        """Подтверждает внесенные изменения"""
        pass
    

    def rollback(self) -> None:
        """Откатывает внесенные изменения"""
        pass
    

    def __enter__(self) -> university.service.unit_of_work.UnitOfWork:
        """Инициализирует репозитории при входе в контекст"""
        return self
    

    def __exit__(self, *args, **kwargs) -> None:
        """Заканчивает сессию при выходе из контекста"""
        pass
