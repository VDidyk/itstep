# Метаклас, що може змінювати ім'я класу залежно
# від певних умов або параметрів.

class MyMeta(type):
    def __new__(cls, name, base, dct):
        is_good_mood = False

        if not is_good_mood:
            name = "BadClass"

        return super().__new__(cls, name, base, dct)


class MyClass(metaclass=MyMeta):
    pass


m = MyClass()
print(m.__class__.__name__)
