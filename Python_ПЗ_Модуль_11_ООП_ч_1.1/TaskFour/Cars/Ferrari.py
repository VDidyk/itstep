from .Car import Car
from ..Engines.F140FE import F140FE


class Ferrari(Car):
    def __init__(self):
        Car.__init__(self)

    def _set_brand(self):
        self._brand = 'Ferrari'

    def _set_model(self):
        self._model = 'G15'

    def _set_year(self):
        self._year = 2015

    def _set_engine(self):
        self._engine = F140FE()
