/* Professors */
INSERT INTO professors (id, full_name)
VALUES ('00000000-0000-0000-0000-000000000000', 'Professor 1');

INSERT INTO professors (id, full_name)
VALUES ('00000000-0000-0000-0000-000000000001', 'Professor 2');

INSERT INTO professors (id, full_name)
VALUES ('00000000-0000-0000-0000-000000000002', 'Professor 3');

INSERT INTO professors (id, full_name)
VALUES ('00000000-0000-0000-0000-000000000003', 'Professor 4');


/* Courses */
INSERT INTO courses (id, title)
VALUES ('00000000-0000-0000-0001-000000000000', 'Course 1');

INSERT INTO courses (id, title)
VALUES ('00000000-0000-0000-0001-000000000001', 'Course 2');

INSERT INTO courses (id, title)
VALUES ('00000000-0000-0000-0001-000000000002', 'Course 3');

INSERT INTO courses (id, title)
VALUES ('00000000-0000-0000-0001-000000000003', 'Course 4');


/* Faculties */
INSERT INTO faculties (id, title)
VALUES ('00000000-0000-0000-0002-000000000000', 'Faculty 1');

INSERT INTO faculties (id, title)
VALUES ('00000000-0000-0000-0002-000000000001', 'Faculty 2');

INSERT INTO faculties (id, title)
VALUES ('00000000-0000-0000-0002-000000000002', 'Faculty 3');

INSERT INTO faculties (id, title)
VALUES ('00000000-0000-0000-0002-000000000003', 'Faculty 4');


/* Semesters */
INSERT INTO semesters (id, semester_number, begins_at, ends_at)
VALUES ('00000000-0000-0000-0003-000000000000', 1, DATE '2023-9-1', DATE '2024-2-1');

INSERT INTO semesters (id, semester_number, begins_at, ends_at)
VALUES ('00000000-0000-0000-0003-000000000001', 2, DATE '2024-2-1', DATE '2024-7-1');

INSERT INTO semesters (id, semester_number, begins_at, ends_at)
VALUES ('00000000-0000-0000-0003-000000000002', 3, DATE '2024-9-1', DATE '2025-2-1');

INSERT INTO semesters (id, semester_number, begins_at, ends_at)
VALUES ('00000000-0000-0000-0003-000000000003', 4, DATE '2025-2-1', DATE '2024-7-1');


/* Groups */
INSERT INTO groups (id, faculty_id, semester_id, code)
VALUES (
    '00000000-0000-0000-0004-000000000000', -- id
    '00000000-0000-0000-0002-000000000000', -- faculty_id
    '00000000-0000-0000-0003-000000000000', -- semester_id
    'Code 1'
);

INSERT INTO groups (id, faculty_id, semester_id, code)
VALUES (
    '00000000-0000-0000-0004-000000000001', -- id
    '00000000-0000-0000-0002-000000000001', -- faculty_id
    '00000000-0000-0000-0003-000000000001', -- semester_id
    'Code 2'
);

INSERT INTO groups (id, faculty_id, semester_id, code)
VALUES (
    '00000000-0000-0000-0004-000000000002', -- id
    '00000000-0000-0000-0002-000000000002', -- faculty_id
    '00000000-0000-0000-0003-000000000002', -- semester_id
    'Code 3'
);

INSERT INTO groups (id, faculty_id, semester_id, code)
VALUES (
    '00000000-0000-0000-0004-000000000003', -- id
    '00000000-0000-0000-0002-000000000003', -- faculty_id
    '00000000-0000-0000-0003-000000000003', -- semester_id
    'Code 4'
);


/* Students */
INSERT INTO students (id, full_name, group_id)
VALUES (
    '00000000-0000-0000-0005-000000000000', -- id
    'Student 1',
    '00000000-0000-0000-0004-000000000000'  -- group_id
);

INSERT INTO students (id, full_name, group_id)
VALUES (
    '00000000-0000-0000-0005-000000000001', -- id
    'Student 2',
    '00000000-0000-0000-0004-000000000001'  -- group_id
);

INSERT INTO students (id, full_name, group_id)
VALUES (
    '00000000-0000-0000-0005-000000000002', -- id
    'Student 3',
    '00000000-0000-0000-0004-000000000002'  -- group_id
);

INSERT INTO students (id, full_name, group_id)
VALUES (
    '00000000-0000-0000-0005-000000000003', -- id
    'Student 4',
    '00000000-0000-0000-0004-000000000003'  -- group_id
);


/* Departments */
INSERT INTO departments (id, title, head_professor_id)
VALUES (
    '00000000-0000-0000-0006-000000000000', -- id
    'Department 1',
    '00000000-0000-0000-0000-000000000000'  -- head_professor_id
);

INSERT INTO departments (id, title, head_professor_id)
VALUES (
    '00000000-0000-0000-0006-000000000001', -- id
    'Department 2',
    '00000000-0000-0000-0000-000000000001'  -- head_professor_id
);

INSERT INTO departments (id, title, head_professor_id)
VALUES (
    '00000000-0000-0000-0006-000000000002', -- id
    'Department 3',
    '00000000-0000-0000-0000-000000000002'  -- head_professor_id
);

INSERT INTO departments (id, title, head_professor_id)
VALUES (
    '00000000-0000-0000-0006-000000000003', -- id
    'Department 4',
    '00000000-0000-0000-0000-000000000003'  -- head_professor_id
);


/* Buildings */
INSERT INTO  buildings (id, code)
VALUES ('00000000-0000-0000-0007-000000000000', 'Building 1');

INSERT INTO  buildings (id, code)
VALUES ('00000000-0000-0000-0007-000000000001', 'Building 2');

INSERT INTO  buildings (id, code)
VALUES ('00000000-0000-0000-0007-000000000002', 'Building 3');

INSERT INTO  buildings (id, code)
VALUES ('00000000-0000-0000-0007-000000000003', 'Building 4');


/* Classrooms */
INSERT INTO classrooms (id, code, building_id)
VALUES (
    '00000000-0000-0000-0008-000000000000', -- id
    'Classroom 1',
    '00000000-0000-0000-0007-000000000000'  -- building_id
);

INSERT INTO classrooms (id, code, building_id)
VALUES (
    '00000000-0000-0000-0008-000000000001', -- id
    'Classroom 2',
    '00000000-0000-0000-0007-000000000001'  -- building_id
);

INSERT INTO classrooms (id, code, building_id)
VALUES (
    '00000000-0000-0000-0008-000000000002', -- id
    'Classroom 3',
    '00000000-0000-0000-0007-000000000002'  -- building_id
);

INSERT INTO classrooms (id, code, building_id)
VALUES (
    '00000000-0000-0000-0008-000000000003', -- id
    'Classroom 4',
    '00000000-0000-0000-0007-000000000003'  -- building_id
);


/* Exams */
INSERT INTO exams (id, course_id, professor_id, group_id, classroom_id, begins_at)
VALUES (
    '00000000-0000-0000-0009-000000000000', -- id
    '00000000-0000-0000-0001-000000000000', -- course_id
    '00000000-0000-0000-0000-000000000000', -- professor_id
    '00000000-0000-0000-0004-000000000000', -- group_id
    '00000000-0000-0000-0008-000000000000', -- classroom_id
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);

INSERT INTO exams (id, course_id, professor_id, group_id, classroom_id, begins_at)
VALUES (
    '00000000-0000-0000-0009-000000000001', -- id
    '00000000-0000-0000-0001-000000000001', -- course_id
    '00000000-0000-0000-0000-000000000001', -- professor_id
    '00000000-0000-0000-0004-000000000001', -- group_id
    '00000000-0000-0000-0008-000000000001', -- classroom_id
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);

INSERT INTO exams (id, course_id, professor_id, group_id, classroom_id, begins_at)
VALUES (
    '00000000-0000-0000-0009-000000000002', -- id
    '00000000-0000-0000-0001-000000000002', -- course_id
    '00000000-0000-0000-0000-000000000002', -- professor_id
    '00000000-0000-0000-0004-000000000002', -- group_id
    '00000000-0000-0000-0008-000000000002', -- classroom_id
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);

INSERT INTO exams (id, course_id, professor_id, group_id, classroom_id, begins_at)
VALUES (
    '00000000-0000-0000-0009-000000000003', -- id
    '00000000-0000-0000-0001-000000000003', -- course_id
    '00000000-0000-0000-0000-000000000003', -- professor_id
    '00000000-0000-0000-0004-000000000003', -- group_id
    '00000000-0000-0000-0008-000000000003', -- classroom_id
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);


/* Grades */
INSERT INTO grades (id, student_id, exam_id, grade, created_at)
VALUES (
    '00000000-0000-0000-0010-000000000000', -- id
    '00000000-0000-0000-0005-000000000000', -- student_id
    '00000000-0000-0000-0009-000000000000', -- exam_id
    4,
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);

INSERT INTO grades (id, student_id, exam_id, grade, created_at)
VALUES (
    '00000000-0000-0000-0010-000000000001', -- id
    '00000000-0000-0000-0005-000000000001', -- student_id
    '00000000-0000-0000-0009-000000000001', -- exam_id
    4,
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);

INSERT INTO grades (id, student_id, exam_id, grade, created_at)
VALUES (
    '00000000-0000-0000-0010-000000000002', -- id
    '00000000-0000-0000-0005-000000000002', -- student_id
    '00000000-0000-0000-0009-000000000002', -- exam_id
    4,
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);

INSERT INTO grades (id, student_id, exam_id, grade, created_at)
VALUES (
    '00000000-0000-0000-0010-000000000003', -- id
    '00000000-0000-0000-0005-000000000003', -- student_id
    '00000000-0000-0000-0009-000000000003', -- exam_id
    4,
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);


/* Schedule */
INSERT INTO schedule (id, professor_id, course_id, classroom_id, begins_at, ends_at)
VALUES (
    '00000000-0000-0000-0011-000000000000', -- id
    '00000000-0000-0000-0000-000000000000', -- professor_id
    '00000000-0000-0000-0001-000000000000', -- course_id
    '00000000-0000-0000-0008-000000000000', -- classroom_id
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00',
    TIMESTAMP WITH TIME ZONE '2023-09-01 10:00:00 +00:00'
);

INSERT INTO schedule (id, professor_id, course_id, classroom_id, begins_at, ends_at)
VALUES (
    '00000000-0000-0000-0011-000000000001', -- id
    '00000000-0000-0000-0000-000000000001', -- professor_id
    '00000000-0000-0000-0001-000000000001', -- course_id
    '00000000-0000-0000-0008-000000000001', -- classroom_id
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00',
    TIMESTAMP WITH TIME ZONE '2023-09-01 10:00:00 +00:00'
);

INSERT INTO schedule (id, professor_id, course_id, classroom_id, begins_at, ends_at)
VALUES (
    '00000000-0000-0000-0011-000000000002', -- id
    '00000000-0000-0000-0000-000000000002', -- professor_id
    '00000000-0000-0000-0001-000000000002', -- course_id
    '00000000-0000-0000-0008-000000000002', -- classroom_id
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00',
    TIMESTAMP WITH TIME ZONE '2023-09-01 10:00:00 +00:00'
);

INSERT INTO schedule (id, professor_id, course_id, classroom_id, begins_at, ends_at)
VALUES (
    '00000000-0000-0000-0011-000000000003', -- id
    '00000000-0000-0000-0000-000000000003', -- professor_id
    '00000000-0000-0000-0001-000000000003', -- course_id
    '00000000-0000-0000-0008-000000000003', -- classroom_id
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00',
    TIMESTAMP WITH TIME ZONE '2023-09-01 10:00:00 +00:00'
);


/* Exercises */
INSERT INTO exercises (id, course_id, content, created_at)
VALUES(
    '00000000-0000-0000-0012-000000000000', -- id
    '00000000-0000-0000-0001-000000000000', -- course_id
    'Exercise 1 content',
    TIMESTAMP WITH TIME ZONE '2022-03-01 08:00:00 +00:00'
);

INSERT INTO exercises (id, course_id, content, created_at)
VALUES(
    '00000000-0000-0000-0012-000000000001', -- id
    '00000000-0000-0000-0001-000000000001', -- course_id
    'Exercise 2 content',
    TIMESTAMP WITH TIME ZONE '2022-09-01 08:00:00 +00:00'
);

INSERT INTO exercises (id, course_id, content, created_at)
VALUES(
    '00000000-0000-0000-0012-000000000002', -- id
    '00000000-0000-0000-0001-000000000002', -- course_id
    'Exercise 3 content',
    TIMESTAMP WITH TIME ZONE '2023-03-01 08:00:00 +00:00'
);

INSERT INTO exercises (id, course_id, content, created_at)
VALUES(
    '00000000-0000-0000-0012-000000000003', -- id
    '00000000-0000-0000-0001-000000000003', -- course_id
    'Exercise 4 content',
    TIMESTAMP WITH TIME ZONE '2023-09-01 08:00:00 +00:00'
);


/* Educational programs */
INSERT INTO educational_programs (id, course_id, topic, content, exercise_id)
VALUES (
    '00000000-0000-0000-0013-000000000000', -- id
    '00000000-0000-0000-0001-000000000000', -- course_id
    'Program 1 topic',
    'Program 1 content',
    '00000000-0000-0000-0012-000000000000'  -- exercise_id
);

INSERT INTO educational_programs (id, course_id, topic, content, exercise_id)
VALUES (
    '00000000-0000-0000-0013-000000000001', -- id
    '00000000-0000-0000-0001-000000000001', -- course_id
    'Program 2 topic',
    'Program 2 content',
    '00000000-0000-0000-0012-000000000001'  -- exercise_id
);

INSERT INTO educational_programs (id, course_id, topic, content, exercise_id)
VALUES (
    '00000000-0000-0000-0013-000000000002', -- id
    '00000000-0000-0000-0001-000000000002', -- course_id
    'Program 3 topic',
    'Program 3 content',
    '00000000-0000-0000-0012-000000000002'  -- exercise_id
);

INSERT INTO educational_programs (id, course_id, topic, content, exercise_id)
VALUES (
    '00000000-0000-0000-0013-000000000003', -- id
    '00000000-0000-0000-0001-000000000003', -- course_id
    'Program 4 topic',
    'Program 4 content',
    '00000000-0000-0000-0012-000000000003'  -- exercise_id
);


/* Syllabus */
INSERT INTO syllabus (id, code, group_id, semester_id, course_id, reserved_hours, note)
VALUES (
    '00000000-0000-0000-0014-000000000000', -- id
    'SYLLABUS1CODE',
    '00000000-0000-0000-0004-000000000000', -- group_id
    '00000000-0000-0000-0003-000000000000', -- semester_id
    '00000000-0000-0000-0001-000000000000', -- course_id
    100,
    'Syllabus 1 note'
);

INSERT INTO syllabus (id, code, group_id, semester_id, course_id, reserved_hours, note)
VALUES (
    '00000000-0000-0000-0014-000000000001', -- id
    'SYLLABUS2CODE',
    '00000000-0000-0000-0004-000000000001', -- group_id
    '00000000-0000-0000-0003-000000000001', -- semester_id
    '00000000-0000-0000-0001-000000000001', -- course_id
    100,
    'Syllabus 2 note'
);

INSERT INTO syllabus (id, code, group_id, semester_id, course_id, reserved_hours, note)
VALUES (
    '00000000-0000-0000-0014-000000000002', -- id
    'SYLLABUS3CODE',
    '00000000-0000-0000-0004-000000000002', -- group_id
    '00000000-0000-0000-0003-000000000002', -- semester_id
    '00000000-0000-0000-0001-000000000002', -- course_id
    100,
    'Syllabus 3 note'
);

INSERT INTO syllabus (id, code, group_id, semester_id, course_id, reserved_hours, note)
VALUES (
    '00000000-0000-0000-0014-000000000003', -- id
    'SYLLABUS4CODE',
    '00000000-0000-0000-0004-000000000003', -- group_id
    '00000000-0000-0000-0003-000000000003', -- semester_id
    '00000000-0000-0000-0001-000000000003', -- course_id
    100,
    'Syllabus 4 note'
);
