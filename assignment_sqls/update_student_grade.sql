/*	Текст задания:
	Обновить оценку студента по курсу.

	Комментарий:
	Так как не указаны параметры нужного студента, выбирается
	первый попавшийся студент
*/

UPDATE grades
SET grade = 4
WHERE
	student_id IN (
		SELECT students.id
		FROM students
		LIMIT 1
	)
	AND exam_id IN (
		SELECT exams.id
		FROM exams
		INNER JOIN courses ON exams.course_id = courses.id
		WHERE courses.title = 'Математика'
	);
