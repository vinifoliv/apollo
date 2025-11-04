from abc import ABC, abstractmethod
from src.apollo.common.impulse import Impulse
from src.apollo.thalamus.thalamus import Thalamus


class BrainRegion(ABC):
    @abstractmethod
    def __init__(self, thalamus: Thalamus):
        pass

    @abstractmethod
    def fire_impulse(self, impulse: Impulse):
        self._thalamus.receive_impulse(impulse)

    @abstractmethod
    def catch_impulse(self):
        impulse = self._thalamus.free_impulse()
