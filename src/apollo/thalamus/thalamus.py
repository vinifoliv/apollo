from collections import defaultdict
from typing import Callable, TypeAlias

from apollo.shared.impulse import Impulse
from apollo.shared.impulse_type import ImpulseType


Listener: TypeAlias = Callable[[Impulse], None]


class Thalamus:
    def __init__(self):
        self._listeners: dict[ImpulseType, list[Listener]] = defaultdict(list)
        self._log: list[Impulse] = []

    def subscribe(self, type: ImpulseType, listener: Listener):
        self._listeners[type].append(listener)

    def publish(self, impulse: Impulse):
        for listener in self._listeners[impulse.type]:
            listener(impulse)
