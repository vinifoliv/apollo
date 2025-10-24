from datetime import datetime

from src.apollo.common.impulse_type import ImpulseType


class Impulse:
    def __init__(self, type: ImpulseType, payload=None):
        self.timestamp = datetime.now()
        self.type = type;
        self.payload = payload

    def __str__(self) -> str:
        return f"Event {self.type} at [{self.timestamp}]"
