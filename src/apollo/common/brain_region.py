from src.apollo.common.impulse import Impulse
from src.apollo.thalamus.thalamus import Thalamus


class BrainRegion:
    def __init__(self, thalamus: Thalamus):
        self._thalamus = thalamus

    def fire_impulse(self, impulse: Impulse):
        self._thalamus.receive_impulse(impulse)
