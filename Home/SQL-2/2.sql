--Створіть наступні запити для бази даних з інформацією
--про овочі та фрукти з попереднього домашнього завдання:
--■ Показати кількість овочів.
--■ Показати кількість фруктів.
--■ Показати кількість овочів та фруктів заданого кольору.
--■ Показати кількість овочів та фруктів кожного кольору.
--■ Показати колір мінімальної кількості овочів та фруктів.
--■ Показати колір максимальної кількості овочів та фруктів.
--■ Показати мінімальну калорійність овочів та фруктів.
--■ Показати максимальну калорійність овочів та фруктів.
--■ Показати середню калорійність овочів та фруктів.
--■ Показати фрукт з мінімальною калорійністю.
--■ Показати фрукт з максимальною калорійністю.

SELECT COUNT(*) AS NumberOfVegetables
FROM FruitsAndVegetables
WHERE Type = 'овоч';

SELECT COUNT(*) AS NumberOfFruits
FROM FruitsAndVegetables
WHERE Type = 'фрукт';

SELECT COUNT(*) AS NumberOfItems
FROM FruitsAndVegetables
WHERE Color = 'червоний';

SELECT Color, COUNT(*) AS NumberOfItems
FROM FruitsAndVegetables
GROUP BY Color;

SELECT Color, COUNT(*) AS NumberOfItems
FROM FruitsAndVegetables
GROUP BY Color
ORDER BY NumberOfItems ASC
LIMIT 1;

SELECT Color, COUNT(*) AS NumberOfItems
FROM FruitsAndVegetables
GROUP BY Color
ORDER BY NumberOfItems DESC
LIMIT 1;

SELECT MIN(Calories) AS MinCalories
FROM FruitsAndVegetables;

SELECT MAX(Calories) AS MaxCalories
FROM FruitsAndVegetables;

SELECT AVG(Calories) AS AverageCalories
FROM FruitsAndVegetables;

SELECT Name, Calories
FROM FruitsAndVegetables
WHERE Type = 'фрукт'
ORDER BY Calories ASC
LIMIT 1;

SELECT Name, Calories
FROM FruitsAndVegetables
WHERE Type = 'фрукт'
ORDER BY Calories DESC
LIMIT 1;
