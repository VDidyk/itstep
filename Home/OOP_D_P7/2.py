# Створіть клас температурного датчика, де обмежується
# температура в межах прийнятних для датчика значень, за
# допомогою property()

class TemperatureSensor:
    def __init__(self):
        self.__t = 0

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, t):
        if t < -30 or t > 50:
            raise ValueError

        self.__t = t


s = TemperatureSensor()
s.t = 25
print(s.t)
