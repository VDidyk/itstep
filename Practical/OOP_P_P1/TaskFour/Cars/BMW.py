from .Car import Car
from ..Engines.B47B20 import B47B20


class BMW(Car):
    def __init__(self):
        Car.__init__(self)

    def _set_brand(self):
        self._brand = 'BMW'

    def _set_model(self):
        self._model = 'X5'

    def _set_year(self):
        self._year = 1995

    def _set_engine(self):
        self._engine = B47B20()
