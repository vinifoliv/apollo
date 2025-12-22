from typing import Any, override
from loguru import logger

from apollo.logger.interfaces.logger import Logger


class LoguruLogger(Logger):
    @override
    def info(self, msg: str, **kwargs: Any) -> None:
        logger.info(msg, **kwargs)

    @override
    def error(self, msg: str, **kwargs: Any) -> None:
        logger.error(msg, **kwargs)

    @override
    def debug(self, msg: str, **kwargs) -> None:
        logger.debug(msg, **kwargs)
