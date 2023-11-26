# Створіть метаклас, що перевіряє наявність певних
# атрибутів у всіх класах, які використовують цей
# метаклас

class MyMeta(type):
    def __new__(cls, name, base, dct):
        required_attrs = [
            'x', 'y'
        ]

        if not all(attr in dct for attr in required_attrs):
            raise AttributeError

        return super().__new__(cls, name, base, dct)


class MyClass(metaclass=MyMeta):
    x = 1
    y = 1


m = MyClass()
