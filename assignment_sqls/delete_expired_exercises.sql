/*  Текст задания
    Удалить задание для самостоятельной работы, которое было создано более года назад.
*/

DELETE FROM exercises
WHERE exercises.created_at < (NOW() - INTERVAL '1 year');
