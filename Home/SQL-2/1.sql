--Створіть наступні запити для бази даних з інформацією
--про овочі та фрукти з попереднього домашнього завдання:
--■ Відображення усіх овочів з калорійністю, менше вказаної.
--■ Відображення усіх фруктів з калорійністю у вказаному
--діапазоні.
--■ Відображення усіх овочів, у назві яких є вказане слово.
--Наприклад, слово: капуста.
--■ Відображення усіх овочів та фруктів, у короткому описі
--яких є вказане слово. Наприклад, слово: гемоглобін.
--■ Показати усі овочі та фрукти жовтого або червоного
--кольору.

SELECT *
FROM FruitsAndVegetables
WHERE Type = 'овоч' AND Calories < 50;

SELECT *
FROM FruitsAndVegetables
WHERE Type = 'фрукт' AND Calories BETWEEN 50 AND 100;

SELECT *
FROM FruitsAndVegetables
WHERE Type = 'овоч' AND Name LIKE '%капуста%';

SELECT *
FROM FruitsAndVegetables
WHERE Description LIKE '%гемоглобін%';

SELECT *
FROM FruitsAndVegetables
WHERE Color IN ('жовтий', 'червоний');