--Створіть наступні запити для бази даних з оцінками
--студентів із попереднього практичного завдання:
--■ Показати ПІБ усіх студентів з мінімальною оцінкою
--у вказаному діапазоні.
--■ Показати інформацію про студентів, яким виповнилося 20 років.
--■ Показати інформацію про студентів з віком, у вказаному діапазоні.
--■ Показати інформацію про студентів із конкретним
--ім’ям. Наприклад, показати студентів з ім’ям Борис.
--■ Показати інформацію про студентів, в номері яких
--є три сімки.
--■ Показати електронні адреси студентів, що починаються з конкретної літери

SELECT FullName
FROM student_grades
WHERE AverageGrade BETWEEN 2 AND 10;

SELECT *
FROM student_grades
WHERE YEAR(CURRENT_DATE) - YEAR(BirthDate) = 20;

SELECT *
FROM student_grades
WHERE YEAR(CURRENT_DATE) - YEAR(BirthDate) BETWEEN 18 AND 25;

SELECT *
FROM student_grades
WHERE FullName LIKE 'Boris%';

SELECT *
FROM student_grades
WHERE Phone LIKE '%777%';

SELECT Email
FROM student_grades
WHERE Email LIKE 'A%';
