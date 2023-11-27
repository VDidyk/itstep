# Метаклас, який вносить додаткові перевірки/логіку
# до певних методів у всіх класах.

class MyMeta(type):
    def __new__(cls, name, base, dct):
        required_methods = [
            'analytics'
        ]

        for m in required_methods:
            if m not in dct:
                raise TypeError(f"{m} method must be included!")

        return super().__new__(cls, name, base, dct)


class MyClass(metaclass=MyMeta):
    def analytics(self):
        print('Test')


m = MyClass()
