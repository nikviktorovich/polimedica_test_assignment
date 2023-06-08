import uuid

import university.modules.education.domain.models as domain_models
from university.modules.education import repositories


class CourseService:
    """Доменный сервис курса"""
    repo: repositories.CourseRepository


    def __init__(self, repo: repositories.CourseRepository) -> None:
        self.repo = repo
    

    def add_course(self, title: str) -> domain_models.Course:
        instance_id = uuid.uuid4()
        instance = domain_models.Course(id=instance_id, title=title)
        instance = self.repo.add(instance)
        return instance
    

    def get_course(self, course_id: uuid.UUID) -> domain_models.Course:
        instance = self.repo.get(course_id=course_id)
        return instance
