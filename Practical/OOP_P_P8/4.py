# Створіть метаклас, який автоматично реєструє всі
# нові класи у певному реєстрі для подальшого
# використання.

registry = {}


class MyMeta(type):
    def __new__(cls, name, base, dct):
        new_class = super().__new__(cls, name, base, dct)

        registry[name] = new_class

        return new_class


class MyClass(metaclass=MyMeta):
    pass

print(registry)
