# Створіть метаклас, що перевіряє наявність певних
# атрибутів у всіх класах, які використовують цей
# метаклас

class MyMeta(type):
    def __new__(cls, name, base, dct):
        required_attrs = [
            'x', 'y'
        ]

        for a in required_attrs:
            if a not in dct:
                raise AttributeError(f"{a} attribute is required!")

        return super().__new__(cls, name, base, dct)


class MyClass(metaclass=MyMeta):
    x = 1
    y = 1
    pass


m = MyClass()
