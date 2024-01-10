--Створіть наступні запити для таблиці з інформацією про
--овочі та фрукти із попереднього завдання:
--■ Відображення всієї інформації з таблиці овочів та фруктів;
--■ Відображення усіх овочів;
--■ Відображення усіх фруктів;
--■ Відображення усіх назв овочів та фруктів;
--■ Відображення усіх кольорів. Кольори мають бути унікальними;
--■ Відображення фруктів певного кольору;
--■ Відображення овочів певного кольору

SELECT * FROM fruits_and_vegetables;
SELECT * FROM fruits_and_vegetables WHERE Type = 'Vegetable';
SELECT * FROM fruits_and_vegetables WHERE Type = 'Fruit';
SELECT Name FROM fruits_and_vegetables;
SELECT DISTINCT Color FROM fruits_and_vegetables;
SELECT * FROM fruits_and_vegetables WHERE Type = 'Fruit' AND Color = 'Red';
SELECT * FROM fruits_and_vegetables WHERE Type = 'Vegetable' AND Color = 'Green';
