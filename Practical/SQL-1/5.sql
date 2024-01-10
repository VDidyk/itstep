--Створіть наступні запити для таблиці з оцінками
--студентів із попереднього завдання:
--■ Відображати всієї інформації з таблиці зі студентами
--та оцінками.
--■ Відображати ПІБ усіх студентів.
--■ Відображати усіх середніх оцінок.
--■ Показати ПІБ усіх студентів з мінімальною оцінкою,
--більшою, ніж зазначена.
--■ Показати країни студентів. Назви країн мають бути
--унікальними.
--■ Показати міста студентів. Назви міст мають бути
--унікальними.
--■ Показати назви груп. Назви груп мають бути унікальними.
--■ Показати назви усіх предметів із мінімальними середніми оцінками. Назви предметів мають бути унікальними

SELECT * FROM student_grades;
SELECT FullName FROM student_grades;
SELECT AverageGrade FROM student_grades;
SELECT FullName FROM student_grades WHERE AverageGrade > 3;
SELECT DISTINCT Country FROM student_grades;
SELECT DISTINCT City FROM student_grades;
SELECT DISTINCT GroupName FROM student_grades;
SELECT DISTINCT SubjectWithMinAvgGrade FROM student_grades;
