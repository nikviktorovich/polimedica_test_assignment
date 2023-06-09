import datetime
import uuid

import university.modules.education.domain.models
import university.modules.exercises.domain.models as domain_models
from university.modules.exercises import repositories


class GradeService:
    """Доменный сервис оценки"""
    repo: repositories.GradeRepository


    def __init__(self, repo: repositories.GradeRepository) -> None:
        """Инициализирует доменный сервис оценки
        
        Аргументы:
            repo: Репозиторий оценок
        """
        self.repo = repo
    

    def add_grade(
        self,
        student: university.modules.education.domain.models.Student,
        exam: domain_models.Exam,
        grade: int,
        created_at: datetime.datetime,
    ) -> domain_models.Grade:
        """Добавляет новую оценку в репозиторий
        
        Аргументы:
            student: Экземпляр объекта студента
            exam: Экземпляр объекта экзамена
            grade: Оценка студента за экзамен
            created_at: Дата выставления оценки
        """
        grade_id = uuid.uuid4()
        instance = domain_models.Grade(
            id=grade_id,
            student=student,
            student_id=student.id,
            exam=exam,
            exam_id=exam.id,
            grade=grade,
            created_at=created_at,
        )
        instance = self.repo.add(instance)
        return instance
    

    def update_grade(
        self,
        instance: domain_models.Grade,
        student: university.modules.education.domain.models.Student,
        exam: domain_models.Exam,
        grade: int,
        created_at: datetime.datetime,
    ) -> domain_models.Grade:
        """Обновляет информацию о существующей оценке
        
        Аргументы:
            instance: Экземпляр объекта оценки
            student: Экземпляр объекта студента
            exam: Экземпляр объекта экзамена
            grade: Оценка студента за экзамен
            created_at: Дата выставления оценки
        """
        instance.student = student
        instance.student_id = student.id
        instance.exam = exam
        instance.exam_id = exam.id
        instance.grade = grade
        instance.created_at = created_at

        return instance
