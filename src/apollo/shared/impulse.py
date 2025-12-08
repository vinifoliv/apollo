import uuid
from datetime import datetime
from typing import Any, Final

from apollo.shared.impulse_type import ImpulseType


class Impulse:
    def __init__(self, type: ImpulseType, payload: Any = None):
        self._uuid: Final = uuid.uuid4()
        self._type: Final = type
        self._timestamp: Final = datetime.now()

    @property
    def uuid(self) -> uuid.UUID:
        return self._uuid

    @property
    def type(self) -> ImpulseType:
        return self._type

    @property
    def timestamp(self) -> datetime:
        return self._timestamp
