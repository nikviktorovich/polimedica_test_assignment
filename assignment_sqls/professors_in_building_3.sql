/*  Текст задания:
    Выбрать всех преподавателей, которые преподают в здании №3.
*/

SELECT professors.id, professors.full_name
FROM professors
INNER JOIN schedule ON schedule.professor_id = professors.id
INNER JOIN classrooms ON classrooms.id = schedule.classroom_id
INNER JOIN buildings ON buildings.id = classrooms.building_id
WHERE
	buildings.code = '№3';

