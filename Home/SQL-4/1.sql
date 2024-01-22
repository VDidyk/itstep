--1. Виведіть усі можливі пари рядків викладачів і груп.
SELECT Teachers.Name, Groups.Name
FROM Teachers
CROSS JOIN Groups;

--2. Виведіть назви факультетів, фонд фінансування кафедр яких перевищує фонд фінансування факультету.
SELECT Faculties.Name, Departments.Name, Faculties.Financing, Departments.Financing
FROM Faculties
INNER JOIN Departments ON Faculties.Id = Departments.FacultyId
WHERE Departments.Financing > Faculties.Financing;

--3. Виведіть прізвища кураторів груп і назви груп, які вони курирують
SELECT Curators.Surname, Groups.Name AS GroupName
FROM Curators
INNER JOIN GroupsCurators ON Curators.Id = GroupsCurators.CuratorId
INNER JOIN Groups ON GroupsCurators.GroupId = Groups.Id;

--4. Виведіть імена та прізвища викладачів, які читають лекції у групі «P107».

SELECT Teachers.Name, Teachers.Surname
FROM Teachers
JOIN Lectures ON Lectures.TeacherId = Teachers.Id
JOIN GroupsLectures ON GroupsLectures.LectureId = Lectures.Id
JOIN Groups ON Groups.Id = GroupsLectures.GroupId
WHERE Groups.Name = 'P107';

--5. Виведіть прізвища викладачів і назви факультетів, на яких вони читають лекції.

SELECT Teachers.Surname, Faculties.Name
FROM Teachers
JOIN TeacherDepartment ON TeacherDepartment.TeacherId = Teachers.Id
JOIN Faculties ON Faculties.Id = TeacherDepartment.FacultyId;


--6. Виведіть назви кафедр і назви груп, які до них належать.
SELECT Departments.Name, Groups.Name
FROM Departments
JOIN Groups ON Groups.DepartmentId = Departments.Id;

--7. Виведіть назви предметів, які викладає викладач «Samantha Adams».
SELECT Subjects.Name
FROM Subjects
JOIN Lectures ON Lectures.SubjectId = Subjects.Id
JOIN Teachers ON Teachers.Id = Lectures.TeacherId
WHERE Teachers.Name = 'Samantha' AND Teachers.Surname = 'Adams';

--8.Виведіть назви кафедр, на яких викладається дисципліна «Database Theory».

SELECT DISTINCT Departments.Name
FROM Subjects
JOIN SubjectsDepartments ON Subjects.Id = SubjectsDepartments.SubjectId
JOIN Departments ON Departments.Id = SubjectsDepartments.DepartmentId
WHERE Subjects.Name = 'Database Theory';


--9. Виведіть назви груп, що належать до факультету «Computer Science»:

SELECT Groups.Name
FROM Groups
JOIN Departments ON Departments.Id = Groups.DepartmentId
JOIN Faculties ON Faculties.Id = Departments.FacultyId
WHERE Faculties.Name = 'Computer Science';

--Виведіть назви груп 5-го курсу, а також назви факультетів, до яких вони належать:
SELECT Groups.Name, Faculties.Name
FROM Groups
JOIN Departments ON Departments.Id = Groups.DepartmentId
JOIN Faculties ON Faculties.Id = Departments.FacultyId
WHERE Groups.Year = 5;


--Виведіть повні імена викладачів і лекції, які вони читають (назви предметів та груп). Зробіть відбір по тим лекціям, які проходять в аудиторії «B103»:
SELECT Teachers.Name || ' ' || Teachers.Surname AS "Teacher Name",
       Subjects.Name AS "Subject",
       Groups.Name AS "Group"
FROM Lectures
JOIN Teachers ON Teachers.Id = Lectures.TeacherId
JOIN Subjects ON Subjects.Id = Lectures.SubjectId
JOIN GroupsLectures ON GroupsLectures.LectureId = Lectures.Id
JOIN Groups ON Groups.Id = GroupsLectures.GroupId
WHERE Lectures.LectureRoom = 'B103';

