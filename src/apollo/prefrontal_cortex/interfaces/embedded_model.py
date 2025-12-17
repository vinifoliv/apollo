from abc import ABC, abstractmethod

from apollo.hippocampus.domain.entities.prompt import Prompt
from apollo.hippocampus.domain.entities.task import Task


class EmbeddedModel(ABC):
    @abstractmethod
    def analyze(self, prompt: Prompt) -> list[Task]:
        pass

    @abstractmethod
    def classify(self, tasks: list[Task]) -> None:
        pass
