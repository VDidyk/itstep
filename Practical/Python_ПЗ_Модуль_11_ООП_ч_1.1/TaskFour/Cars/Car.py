from abc import ABC, abstractmethod
from ..Engines.Engine import Engine


class Car():
    _model: str = None
    _year: int = None
    _brand: str = None
    _engine: Engine = None

    # _engine: Engine = None

    def __init__(self):
        self._set_brand()
        self._set_model()
        self._set_year()
        self._set_engine()

    @abstractmethod
    def _set_brand(self):
        pass

    @abstractmethod
    def _set_model(self):
        pass

    @abstractmethod
    def _set_year(self):
        pass

    @abstractmethod
    def _set_engine(self):
        pass

    def start_engine(self):
        print(f"{self._brand} {self._model} ({self._year}) is starting...")
        self._engine.start()
        print("Started!")
