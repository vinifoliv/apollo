from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID


class Artifact(ABC):
    @property
    @abstractmethod
    def uuid(self) -> UUID:
        pass

    @property
    @abstractmethod
    def timestamp(self) -> datetime:
        pass
