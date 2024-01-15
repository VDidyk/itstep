--Створіть наступні запити для бази даних з оцінками
--студентів із попереднього практичного завдання:
--■ Показати мінімальну середню оцінку по всіх студентах.
--■ Показати максимальну середню оцінку по всіх студентах.
--■ Показати статистику міст. Має відображатися назва
--міста та кількість студентів з цього міста.
--■ Показати статистику студентів. Має відображатися
--назва країни та кількість студентів з цієї країни.
--■ Показати кількість студентів з мінімальною середньою
--оцінкою з математики.
--■ Показати кількість студентів з максимальною середньою оцінкою з математики.
--■ Показати кількість студентів у кожній групі.
--■ Показати середню оцінку групи.

SELECT MIN(AverageGrade) AS MinAverageGrade
FROM student_grades;

SELECT MAX(AverageGrade) AS MaxAverageGrade
FROM student_grades;

SELECT City, COUNT(*) AS NumberOfStudents
FROM student_grades
GROUP BY City;

SELECT Country, COUNT(*) AS NumberOfStudents
FROM student_grades
GROUP BY Country;

SELECT COUNT(*) AS StudentsWithMinMathGrade
FROM student_grades
WHERE SubjectWithMinAvgGrade = 'Mathematics';

SELECT COUNT(*) AS StudentsWithMaxMathGrade
FROM student_grades
WHERE SubjectWithMaxAvgGrade = 'Mathematics';

SELECT GroupName, COUNT(*) AS NumberOfStudents
FROM student_grades
GROUP BY GroupName;

SELECT GroupName, AVG(AverageGrade) AS AverageGroupGrade
FROM student_grades
GROUP BY GroupName;
