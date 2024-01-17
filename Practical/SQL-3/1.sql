CREATE DATABASE Hospital;

CREATE TABLE Departments (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Building INT NOT NULL,
    Financing DECIMAL(10,2) NOT NULL DEFAULT 0,
    Name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Diseases (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE,
    Severity INT NOT NULL DEFAULT 1
);

CREATE TABLE Doctors (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Phone CHAR(10),
    Salary DECIMAL(10,2) NOT NULL CHECK(Salary >= 0),
    Surname VARCHAR(255) NOT NULL
);

CREATE TABLE Examinations (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    DayOfWeek INT NOT NULL CHECK(DayOfWeek BETWEEN 1 AND 7),
    EndTime TIME NOT NULL,
    Name VARCHAR(100) NOT NULL UNIQUE,
    StartTime TIME NOT NULL CHECK(StartTime BETWEEN '08:00:00' AND '18:00:00')
);

CREATE TABLE Wards (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Building INT NOT NULL,
    Floor INT NOT NULL CHECK(Floor >= 1),
    Name VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO Departments (Building, Financing, Name)
VALUES
    (1, 50000, 'Cardiology'),
    (2, 60000, 'Neurology'),
    (3, 45000, 'Pediatrics');

INSERT INTO Diseases (Name, Severity)
VALUES
    ('Hypertension', 2),
    ('Diabetes', 3),
    ('Asthma', 1);

INSERT INTO Doctors (Name, Phone, Salary, Surname)
VALUES
    ('John Smith', '123-456-7890', 80000, 'Doe'),
    ('Mary Johnson', '987-654-3210', 75000, 'Smith'),
    ('David Brown', '555-123-4567', 90000, 'Johnson');

INSERT INTO Examinations (DayOfWeek, EndTime, Name, StartTime)
VALUES
    (1, '10:00 AM', 'Blood Test', '8:00 AM'),
    (3, '2:00 PM', 'MRI Scan', '11:00 AM'),
    (5, '4:30 PM', 'X-ray', '2:00 PM');

INSERT INTO Wards (Building, Floor, Name)
VALUES
    (1, 2, 'ICU Ward'),
    (2, 3, 'Pediatric Ward'),
    (3, 1, 'Surgery Ward');


SELECT * FROM Wards;
SELECT Surname, Phone FROM Doctors;
SELECT DISTINCT Floor FROM Wards;
SELECT Name AS "Name of Disease", Severity AS "Severity of Disease" FROM Diseases;
SELECT Name FROM Departments WHERE Building = 5 AND Financing < 30000;
SELECT Name FROM Departments WHERE Building = 3 AND Financing BETWEEN 12000 AND 15000;
SELECT Name FROM Wards WHERE (Building = 4 OR Building = 5) AND Floor = 1;
SELECT Name, Building, Financing FROM Departments WHERE (Building = 3 OR Building = 6) AND (Financing < 11000 OR Financing > 25000);
SELECT Surname FROM Doctors WHERE (Salary + 120) > 1500;
SELECT Surname FROM Doctors WHERE Salary > (3 * 500);
SELECT DISTINCT Name FROM Examinations WHERE DayOfWeek BETWEEN 1 AND 3 AND StartTime >= '12:00' AND EndTime <= '15:00';
SELECT Name, Building FROM Departments WHERE Building IN (1, 3, 8, 10);
SELECT Name FROM Diseases WHERE Severity NOT IN (1, 2);
SELECT Name FROM Departments WHERE Building NOT IN (1, 3);
SELECT Name FROM Departments WHERE Building IN (1, 3);
SELECT Surname FROM Doctors WHERE Name LIKE 'N%';
