from abc import ABC, abstractmethod
from typing import Any


class Logger(ABC):
    @abstractmethod
    def info(self, msg: str, **kwargs: Any) -> None: ...

    @abstractmethod
    def error(self, msg: str, **kwargs: Any) -> None: ...

    @abstractmethod
    def debug(self, msg: str, **kwargs: Any) -> None: ...
