from datetime import datetime
from typing import override
from uuid import uuid4, UUID

from apollo.shared.artifact import Artifact


class Prompt(Artifact):
    def __init__(self, value: str) -> None:
        self._uuid: UUID = uuid4()
        self._timestamp: datetime = datetime.now()
        self._value: str = value

    @property
    @override
    def uuid(self) -> UUID:
        return self._uuid

    @property
    @override
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def value(self) -> str:
        return self._value
