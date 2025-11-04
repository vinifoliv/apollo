from collections import deque

from src.apollo.common.impulse import Impulse


class Thalamus:
    def __init__(self):
        self._impulse_queue: deque[Impulse] = []

    def receive_impulse(self, impulse: Impulse):
        self._impulse_queue.append(impulse)

    def free_impulse(self) -> Impulse:
        return self._impulse_queue.popleft()

    def feed_back(self, impulse: Impulse):
        self._impulse_queue.appendleft(impulse)
