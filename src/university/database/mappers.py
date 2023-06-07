import sqlalchemy.orm
from sqlalchemy.orm import relationship

import university.modules.classrooms.database.models
import university.modules.classrooms.domain.models
import university.modules.education.database.models
import university.modules.education.domain.models
import university.modules.exercises.database.models
import university.modules.exercises.domain.models
import university.modules.organizing.database.models
import university.modules.organizing.domain.models


def start_mappers() -> None:
    """Связывает ORM- и доменные модели
    
    Связывает ORM- и доменные модели, делая их взаимозаменяемыми
    """
    registry = sqlalchemy.orm.registry()

    start_classrooms_mappers(registry)
    start_education_mappers(registry)
    start_exercises_mappers(registry)
    start_organizing_mappers(registry)


def start_classrooms_mappers(registry: sqlalchemy.orm.registry) -> None:
    """Связывает ORM- и доменные модели модуля classrooms"""
    registry.map_imperatively(
        university.modules.classrooms.domain.models.Building,
        university.modules.classrooms.database.models.Building,
    )

    registry.map_imperatively(
        university.modules.classrooms.domain.models.Classroom,
        university.modules.classrooms.database.models.Classroom,
        properties={
            'building': relationship(
                university.modules.classrooms.domain.models.Building,
            ),
        },
    )


def start_education_mappers(registry: sqlalchemy.orm.registry) -> None:
    """Связывает ORM- и доменные модели модуля education"""
    registry.map_imperatively(
        university.modules.education.domain.models.Professor,
        university.modules.education.database.models.Professor,
    )

    registry.map_imperatively(
        university.modules.education.domain.models.Semester,
        university.modules.education.database.models.Semester,
    )

    registry.map_imperatively(
        university.modules.education.domain.models.Faculty,
        university.modules.education.database.models.Faculty,
    )
    
    registry.map_imperatively(
        university.modules.education.domain.models.Group,
        university.modules.education.database.models.Group,
        properties={
            'faculty': relationship(
                university.modules.education.domain.models.Faculty,
            ),
            'semester': relationship(
                university.modules.education.domain.models.Semester,
            ),
        },
    )

    registry.map_imperatively(
        university.modules.education.domain.models.Student,
        university.modules.education.database.models.Student,
        properties={
            'group': relationship(
                university.modules.education.domain.models.Group,
            ),
        },
    )

    registry.map_imperatively(
        university.modules.education.domain.models.Course,
        university.modules.education.database.models.Course,
    )


def start_exercises_mappers(registry: sqlalchemy.orm.registry) -> None:
    """Связывает ORM- и доменные модели модуля exercises"""
    registry.map_imperatively(
        university.modules.exercises.domain.models.Exam,
        university.modules.exercises.database.models.Exam,
        properties={
            'course': relationship(
                university.modules.education.domain.models.Course,
            ),
            'professor': relationship(
                university.modules.education.domain.models.Professor,
            ),
            'group': relationship(
                university.modules.education.domain.models.Group,
            ),
            'classroom': relationship(
                university.modules.classrooms.domain.models.Classroom,
            ),
        },
    )

    registry.map_imperatively(
        university.modules.exercises.domain.models.Grade,
        university.modules.exercises.database.models.Grade,
        properties={
            'student': relationship(
                university.modules.education.domain.models.Student,
            ),
            'exam': relationship(
                university.modules.exercises.domain.models.Exam,
            ),
        },
    )

    registry.map_imperatively(
        university.modules.exercises.domain.models.Exercise,
        university.modules.exercises.database.models.Exercise,
        properties={
            'course': relationship(
                university.modules.education.domain.models.Course,
            ),
        },
    )

    registry.map_imperatively(
        university.modules.exercises.domain.models.EducationalProgram,
        university.modules.exercises.database.models.EducationalProgram,
        properties={
            'course': relationship(
                university.modules.education.domain.models.Course,
            ),
            'exercise': relationship(
                university.modules.exercises.domain.models.Exercise,
            ),
        },
    )


def start_organizing_mappers(registry: sqlalchemy.orm.registry) -> None:
    """Связывает ORM- и доменные модели модуля organizing"""
    registry.map_imperatively(
        university.modules.organizing.domain.models.Schedule,
        university.modules.organizing.database.models.Schedule,
        properties={
            'professor': relationship(
                university.modules.education.domain.models.Professor,
            ),
            'course': relationship(
                university.modules.education.domain.models.Course,
            ),
            'classroom': relationship(
                university.modules.classrooms.domain.models.Classroom,
            ),
        },
    )

    registry.map_imperatively(
        university.modules.organizing.domain.models.Department,
        university.modules.organizing.database.models.Department,
        properties={
            'head_professor': relationship(
                university.modules.education.domain.models.Professor,
            ),
        },
    )

    registry.map_imperatively(
        university.modules.organizing.domain.models.Syllabus,
        university.modules.organizing.database.models.Syllabus,
        properties={
            'group': relationship(
                university.modules.education.domain.models.Group,
            ),
            'semester': relationship(
                university.modules.education.domain.models.Semester,
            ),
            'course': relationship(
                university.modules.education.domain.models.Course,
            ),
        },
    )
