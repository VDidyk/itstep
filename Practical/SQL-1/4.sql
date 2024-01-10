--Створіть базу даних для зберігання оцінок студентів.
--У базі даних створіть таблицю «Оцінки студентів», яка
--зберігатиме таку інформацію:
--■ ПІБ студента;
--■ місто;
--■ країна;
--■ дата народження;
--■ електронна адреса;
--■ контактний телефон;
--■ назва групи;
--■ середня оцінка за рік з усіх предметів;
--■ назва предмета з мінімальною, середньою оцінкою;
--■ назва предмета з максимальною, середньою
--оцінкою.
--Наповніть цю базу даних трьома студентами

CREATE TABLE student_grades (
    FullName VARCHAR(255),
    City VARCHAR(100),
    Country VARCHAR(100),
    BirthDate DATE,
    Email VARCHAR(255),
    Phone VARCHAR(50),
    GroupName VARCHAR(50),
    AverageGrade DECIMAL(3, 2),
    SubjectWithMinAvgGrade VARCHAR(255),
    SubjectWithMaxAvgGrade VARCHAR(255)
);

INSERT INTO student_grades (FullName, City, Country, BirthDate, Email, Phone, GroupName, AverageGrade, SubjectWithMinAvgGrade, SubjectWithMaxAvgGrade)
VALUES
('Студент 1', 'Місто1', 'Країна1', '2000-01-01', 'student1@example.com', '1234567890', 'Група1', 4.5, 'Предмет1', 'Предмет2'),
('Студент 2', 'Місто2', 'Країна2', '2000-02-02', 'student2@example.com', '0987654321', 'Група2', 3.8, 'Предмет3', 'Предмет4'),
('Студент 3', 'Місто3', 'Країна3', '2000-03-03', 'student3@example.com', '1230984567', 'Група3', 4.2, 'Предмет5', 'Предмет6');
