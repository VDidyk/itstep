# Створіть метаклас, який автоматично додає певні
# атрибути до всіх класів, що використовують його.

class MyMeta(type):
    def __new__(cls, name, base, dct):
        dct['x'] = 1
        dct['y'] = 2

        return super().__new__(cls, name, base, dct)


class MyClass(metaclass=MyMeta):
    pass


m = MyClass()
print(m.x)
print(m.y)
