/*  Таблица преподавателей

    Поля:
        id: Идентификатор преподавателя
        full_name: ФИО преподавателя
*/
CREATE TABLE IF NOT EXISTS professors (
    id UUID PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL
);


/*  Таблица курсов

    Поля:
        id: Идентификатор курса
        title: Название курса
*/
CREATE TABLE IF NOT EXISTS courses (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);


/*  Таблица факультетов

    Поля:
        id: Идентификатор факультета
        title: Наименование факультета
*/
CREATE TABLE IF NOT EXISTS faculties (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);


/*  Таблица семетров

    Поля:
        id: Идентификатор семестра
        semester_number: Порядковый номер семестра
        begins_at: Дата и время начала семестра
        ends_at: Дата и время окончания семестра
*/
CREATE TABLE IF NOT EXISTS semesters (
    id UUID PRIMARY KEY,
    semester_number INTEGER UNIQUE NOT NULL,
    begins_at TIMESTAMP WITH TIME ZONE NOT NULL,
    ends_at TIMESTAMP WITH TIME ZONE NOT NULL
);


/*  Таблица групп

    Поля:
        id: Идентификатор группы в базе данных
        faculty_id: Идентификатор факультета
        semester_id: Идентификатор семестра
        code: Символьный код группы
*/
CREATE TABLE IF NOT EXISTS groups (
    id UUID PRIMARY KEY,
    faculty_id UUID NOT NULL,
    semester_id UUID NOT NULL,
    code VARCHAR(16) UNIQUE NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES faculties(id) ON DELETE CASCADE,
    FOREIGN KEY (semester_id) REFERENCES semesters(id) ON DELETE CASCADE
);


/*  Таблица студентов

    Поля:
        id: Идентификатор студента
        full_name: ФИО студента
*/
CREATE TABLE IF NOT EXISTS students (
    id UUID PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    group_id UUID NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
);


/*  Таблица отделений (кафедр) ВУЗа

    Поля:
        id: Идентификатор кафедры
        title: Название кафедры
        head_professor_id: Идентификатор преподавателя, заведующего кафедрой
*/
CREATE TABLE IF NOT EXISTS departments (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    head_professor_id UUID NOT NULL,
    FOREIGN KEY (head_professor_id) REFERENCES professors(id) ON DELETE CASCADE
);


/*  Таблица зданий (корпусов)

    Поля:
        id: Идентификатор здания
        code: Кодовое название здания
*/
CREATE TABLE IF NOT EXISTS buildings (
    id UUID PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL
);


/*  Таблица аудиторий

    Поля:
        id: Идентификатор аудитории
        code: Кодовое название аудитории
*/
CREATE TABLE IF NOT EXISTS classrooms (
    id UUID PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    building_id UUID NOT NULL,
    FOREIGN KEY (building_id) REFERENCES buildings(id)
);


/*  Таблица экзаменов

    Поля:
        id: Идентификатор экзамена
        course_id: Идентификатор курса, по которому идет экзамен
        professor_id: Идентификатор преподавателя, принимающего экзамен
        group_id: Идентификатор экзаменуемой группы
        classroom_id: Идентификатор аудитории
        begins_at: Дата начала экзамена
*/
CREATE TABLE IF NOT EXISTS exams (
    id UUID PRIMARY KEY,
    course_id UUID NOT NULL,
    professor_id UUID NOT NULL,
    group_id UUID NOT NULL,
    classroom_id UUID NOT NULL,
    begins_at TIMESTAMP WITH TIME ZONE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    FOREIGN KEY (professor_id) REFERENCES professors(id) ON DELETE CASCADE,
    FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE
);


/*  Таблица оценок

    Поля:
        id: Идентификатор оценки
        student_id: Идентификатор студента
        exam_id: Идентификатор экзамена
        created_at: Дата выставления оценки
*/
CREATE TABLE IF NOT EXISTS grades (
    id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    exam_id UUID NOT NULL,
    grade INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (exam_id) REFERENCES exams(id) ON DELETE CASCADE
);


/*  Таблица расписаний занятий по курсам

    Поля:
        id: Идентификатор записи
        professor_id: Идентификатор преподавателя
        course_id: Идентификатор курса
        begins_at: Дата и время начала занятия
        ends_at: Дата и время окончания занятия

*/
CREATE TABLE IF NOT EXISTS schedule (
    id UUID PRIMARY KEY,
    professor_id UUID NOT NULL,
    course_id UUID NOT NULL,
    classroom_id UUID NOT NULL,
    begins_at TIMESTAMP WITH TIME ZONE NOT NULL,
    ends_at TIMESTAMP WITH TIME ZONE NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professors(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE
);


/*  Таблица заданий для самостоятельной работы

    Поля:
        id: Идентификатор задания
        course_id: Идентификатор курса
        content: Содержание самостоятельной работы
        created_at: Дата и время создания задания
*/
CREATE TABLE IF NOT EXISTS exercises (
    id UUID PRIMARY KEY,
    course_id UUID NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);


/*  Таблица программы курса (учебного года)

    Поля:
        id: Идентификатор записи
        course_id: Идентификатор курса
        topic: Наименование темы
        content: Описание содержания учебного материала по теме
        exercise_id: Опциональный идентификатор самостоятельной работы для темы
*/
CREATE TABLE IF NOT EXISTS educational_programs (
    id UUID PRIMARY KEY,
    course_id UUID NOT NULL,
    topic VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    exercise_id UUID NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    FOREIGN KEY (exercise_id) REFERENCES exercises(id) ON DELETE CASCADE
);


/*  Таблица учебного плана

    Поля:
        id: Идентификатор записи
        code: Код учебного плана
        group_id: Идентификатор группы, которой назначен план
        semester_id: Идентификатор семестра
        course_id: Идентификатор курса
        reserved_hours: Кол-во часов
        note: Дополнительная информация
*/
CREATE TABLE IF NOT EXISTS syllabus (
    id UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    group_id UUID NOT NULL,
    semester_id UUID NOT NULL,
    course_id UUID NOT NULL,
    reserved_hours INTEGER NOT NULL,
    note TEXT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE,
    FOREIGN KEY (semester_id) REFERENCES semesters(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);
