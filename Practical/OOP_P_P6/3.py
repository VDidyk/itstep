# Створіть базовий клас «Домашня тварина» та похідні
# класи «Пес», «Кіт», «Папуга», «Хом’як». За допомогою
# конструктора встановіть ім’я кожної тварини та її характеристики. Реалізуйте для кожного із класів наступні
# методи:
# ■ Sound — видає звук тварини (пишемо текстом в консоль);
# ■ Show — відображає ім’я тварини;
# ■ Type — відображає підвид тварини.

from dataclasses import dataclass


@dataclass
class DomesticAnimal:
    name: str
    type: str = 'Unknown'

    def sound(self):
        raise NotImplementedError

    def show_type(self):
        print(self.type)

    def show_name(self):
        print(self.name)


class CanFly:
    def fly(self):
        print('Flying')


class CanWalk:
    def walk(self):
        print('Walking')


class CanSwim:
    def swim(self):
        print('Swimming')


@dataclass
class Dog(DomesticAnimal, CanWalk, CanSwim):
    def sound(self):
        print('Гав')


@dataclass
class Cat(DomesticAnimal, CanWalk, CanSwim):
    def sound(self):
        print('Мяу')


@dataclass
class Perrot(DomesticAnimal, CanWalk, CanFly):
    def sound(self):
        print('Кар')


@dataclass
class Hamster(DomesticAnimal, CanWalk, CanSwim):
    def sound(self):
        print('Пі')


dog = Dog('Bobik', 'Mammal')
dog.sound()
dog.swim()
dog.walk()
dog.show_name()
dog.show_type()

cat = Cat('Tom', 'Mammal')
cat.sound()
cat.swim()
cat.walk()
cat.show_name()
cat.show_type()

perrot = Perrot('Jako', 'Feathered')
perrot.sound()
perrot.walk()
perrot.fly()
perrot.show_name()
perrot.show_type()

hamster = Hamster('Jenny', 'Feathered')
hamster.sound()
hamster.walk()
hamster.show_name()
hamster.show_type()
