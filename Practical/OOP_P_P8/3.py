# Реалізуйте метаклас, що забороняє спадкування від
# певних класів чи змінює порядок спадкування.

class MyMeta(type):
    def __new__(cls, name, base, dct):
        forbidden_classes = [
            'MyClass'
        ]

        for class_base in base:
            if class_base.__name__ in forbidden_classes:
                raise TypeError(class_base.__name__ + ' can not be inherited!')

        base = list(base)
        if len(base) > 1:
            tmp = base[0]
            base[0] = base[1]
            base[1] = tmp

        base = tuple(base)

        return super().__new__(cls, name, base, dct)


class MyClass:
    pass


class NotMyClass:
    pass


class WhatClass:
    pass


class MyClass1(NotMyClass, WhatClass, metaclass=MyMeta):
    pass


m = MyClass1()
