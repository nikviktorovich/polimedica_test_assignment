/*	Текст задания:
	Выбрать всех студентов, обучающихся на курсе "Математика".

	Комментарий:
	Данный запрос выбирает всех студентов, у которых в текущем семестре
	присутствует курс "Математика"
*/

SELECT students.id, students.group_id, students.full_name
FROM students
INNER JOIN groups ON students.group_id = groups.id
INNER JOIN syllabus ON syllabus.group_id = groups.id
INNER JOIN semesters ON syllabus.semester_id = semesters.id
INNER JOIN courses ON syllabus.course_id = courses.id
WHERE
	syllabus.semester_id = groups.semester_id
	AND courses.title = 'Математика';
