import uuid

import university.modules.education.domain.models as domain_models
from university.modules.education import repositories


class StudentService:
    """Доменный сервис студента"""
    repo: repositories.StudentRepository


    def __init__(self, repo: repositories.StudentRepository) -> None:
        """Инициализирует доменный сервис студента
        
        Аргументы:
            repo: Репозиторий студентов
        """
        self.repo = repo
    

    def add_student(
        self,
        full_name: str,
        group: domain_models.Group,
    ) -> domain_models.Student:
        """Добавляет студента в репозиторий
        
        Аргументы:
            full_name: ФИО студента
            group: Экземпляр группы студента
        """
        student_id = uuid.uuid4()
        instance = domain_models.Student(
            id=student_id,
            full_name=full_name,
            group_id=group.id,
            group=group,
        )
        instance = self.repo.add(instance)
        return instance
