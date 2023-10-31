from abc import ABC, abstractmethod
import time


class Engine(ABC):
    _name: str = None
    _volume: float = None

    def __init__(self):
        self._set_name()
        self._set_volume()

    @abstractmethod
    def _set_name(self):
        pass

    @abstractmethod
    def _set_volume(self):
        pass

    def start(self):
        time.sleep(5 / self._volume)

        return True
