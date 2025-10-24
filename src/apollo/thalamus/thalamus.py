from typing import List
from ..common.impulse import Impulse


class Thalamus:
    def __init__(self):
        self.impulses: List[Impulse] = []

    def receive_impulse(self, impulse: Impulse):
        self.impulses.append(impulse)
