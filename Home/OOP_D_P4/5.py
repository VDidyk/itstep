# Створіть клас Character, який має атрибути name, health
# та damage. Реалізуйте метод класу attack, який виводить
# повідомлення про атаку гравця.

class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        print(f"{self.name} attacks {target.name} with the damage {self.damage}.")
        target.health -= self.damage


character = Character('Vitaliy', 100, 20)
character1 = Character('Stepan', 100, 10)

character.attack(character1)
