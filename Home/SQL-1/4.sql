--Створіть однотабличну базу даних «Овочі та фрукти»,
--яка зберігатиме таку інформацію:
--■ Назва;
--■ Тип (овоч або фрукт);
--■ Колір;
--■ Калорійність;
--■ Короткий опис

CREATE DATABASE fruits_and_vegetables;


CREATE TABLE FruitsAndVegetables (
    Name VARCHAR(255),
    Type VARCHAR(50),
    Color VARCHAR(50),
    Calories INT,
    Description TEXT
);
