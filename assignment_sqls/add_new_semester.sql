/*  Текст задания
    Добавить новый семестр в учебный год.

    Комментарий:
    Так как в задании на построение базы данных не предусмотрена
    таблица учебного года, задание сводится к добавлению записи
    в таблицу семестров.
*/

INSERT INTO semesters (id, semester_number, begins_at, ends_at)
SELECT * FROM (
	SELECT gen_random_uuid() AS id, semester_number, begins_at, ends_at
	FROM (
		(
			SELECT
				s1.semester_number + 1 AS semester_number,
				s1.ends_at AS begins_at,
				s1.ends_at + INTERVAL '6 month' AS ends_at
			FROM semesters AS s1
		) UNION (
			SELECT
				1 AS semester_number,
				MAKE_DATE(EXTRACT(YEAR FROM NOW())::int, 9, 1) AS begins_at,
				MAKE_DATE(EXTRACT(YEAR FROM NOW())::int + 1, 2, 1) AS ends_at
		)
	) AS s2
	ORDER BY s2.semester_number DESC
	LIMIT 1
) AS sub_s

