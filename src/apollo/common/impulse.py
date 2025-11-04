from datetime import datetime

from src.apollo.common.impulse_status import ImpulseStatus
from src.apollo.common.impulse_type import ImpulseType


class Impulse:
    def __init__(self, type: ImpulseType, payload=None):
        self.timestamp = datetime.now()
        self.type = type
        self.payload = payload
        self.status = ImpulseStatus.PENDING

    def __str__(self):
        return f"[{self.timestamp}] {self.type} {self.payload}"
