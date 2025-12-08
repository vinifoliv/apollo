from uuid import UUID, uuid4
from datetime import datetime
from typing import Final

from apollo.shared.impulse_type import ImpulseType


class Impulse:
    def __init__(self, type: ImpulseType, artifact_uuid: UUID | None = None) -> None:
        self._uuid: Final = uuid4()
        self._type: Final = type
        self._timestamp: Final = datetime.now()
        self._artifact_uuid: Final = artifact_uuid

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @property
    def type(self) -> ImpulseType:
        return self._type

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def artifact_uuid(self) -> UUID | None:
        return self._artifact_uuid
