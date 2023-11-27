# Метаклас, що додає перевірку та обробку аргументів
# __init__ у всіх класах.

class MyMeta(type):
    def __new__(cls, name, base, dct):
        orig_init = dct.get('__init__')

        def new_init(self, *args, **kwargs):
            if not args:
                raise ValueError("No arguments provided")

            if orig_init:
                orig_init(self, *args, **kwargs)

        dct['__init__'] = new_init

        return super().__new__(cls, name, base, dct)


class MyClass(metaclass=MyMeta):
    def __init__(self, x):
        self.x = x


m = MyClass(1)
