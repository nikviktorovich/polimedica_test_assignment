import sqlalchemy.engine
import sqlalchemy.orm

import university.modules.classrooms.repositories
import university.modules.education.repositories
import university.modules.exercises.repositories
import university.modules.organizing.repositories


class UnitOfWork:
    """Менеджер для атомарной работы с сессией базы данных"""
    buildings: university.modules.classrooms.repositories.BuildingRepository
    classrooms: university.modules.classrooms.repositories.ClassroomRepository

    courses: university.modules.education.repositories.CourseRepository
    faculties: university.modules.education.repositories.FacultyRepository
    groups: university.modules.education.repositories.GroupRepository
    professors: university.modules.education.repositories.ProfessorRepository
    semesters: university.modules.education.repositories.SemesterRepository
    students: university.modules.education.repositories.StudentRepository

    exams: university.modules.exercises.repositories.ExamRepository
    exercises: university.modules.exercises.repositories.ExerciseRepository
    grades: university.modules.exercises.repositories.GradeRepository
    programs: university.modules.exercises.repositories.ProgramRepository

    departments: university.modules.organizing.repositories.DepartmentRepository
    schedules: university.modules.organizing.repositories.ScheduleRepository
    syllabus: university.modules.organizing.repositories.SyllabusRepository


    def commit(self) -> None:
        """Подтверждает внесенные изменения"""
        raise NotImplementedError()
    

    def rollback(self) -> None:
        """Откатывает внесенные изменения"""
        raise NotImplementedError()
    

    def __enter__(self) -> 'UnitOfWork':
        """Инициализирует репозитории при входе в контекст"""
        raise NotImplementedError()
    

    def __exit__(self, *args, **kwargs) -> None:
        """Заканчивает сессию при выходе из контекста"""
        raise NotImplementedError()


class SQLAlchemyUnitOfWork(UnitOfWork):
    """Менеджер для атомарной работы с сессией базы данных"""
    session: sqlalchemy.orm.Session
    session_factory: sqlalchemy.orm.sessionmaker


    def __init__(self, engine: sqlalchemy.engine.Engine) -> None:
        """Инициализирует менеджер
        
        Аргументы:
            engine: SQLAlchemy движок, связанный с нужной базой данных
        """
        self.session_factory = sqlalchemy.orm.sessionmaker(bind=engine)


    def commit(self) -> None:
        """Подтверждает внесенные изменения"""
        self.session.commit()
    

    def rollback(self) -> None:
        """Откатывает внесенные изменения"""
        self.session.rollback()
    

    def __enter__(self) -> UnitOfWork:
        """Инициализирует репозитории при входе в контекст"""
        self.session = self.session_factory()

        self.buildings = university.modules.classrooms.repositories.\
            SQLAlchemyBuildingRepository(self.session)
        self.classrooms = university.modules.classrooms.repositories.\
            SQLAlchemyClassroomRepository(self.session)
        
        self.courses = university.modules.education.repositories.\
            SQLAlchemyCourseRepository(self.session)
        self.faculties = university.modules.education.repositories.\
            SQLAlchemyFacultyRepository(self.session)
        self.groups = university.modules.education.repositories.\
            SQLAlchemyGroupRepository(self.session)
        self.professors = university.modules.education.repositories.\
            SQLAlchemyProfessorRepository(self.session)
        self.semesters = university.modules.education.repositories.\
            SQLAlchemySemesterRepository(self.session)
        self.students = university.modules.education.repositories.\
            SQLAlchemyStudentRepository(self.session)
        
        self.exams = university.modules.exercises.repositories.\
            SQLAlchemyExamRepository(self.session)
        self.exercises = university.modules.exercises.repositories.\
            SQLAlchemyExerciseRepository(self.session)
        self.grades = university.modules.exercises.repositories.\
            SQLAlchemyGradeRepository(self.session)
        self.programs = university.modules.exercises.repositories.\
            SQLAlchemyProgramRepository(self.session)
        
        self.departments = university.modules.organizing.repositories.\
            SQLAlchemyDepartmentRepository(self.session)
        self.schedules = university.modules.organizing.repositories.\
            SQLAlchemyScheduleRepository(self.session)
        self.syllabus = university.modules.organizing.repositories.\
            SQLAlchemySyllabusRepository(self.session)

        return self
    

    def __exit__(self, *args, **kwargs) -> None:
        """Заканчивает сессию при выходе из контекста"""
        self.session.close()
