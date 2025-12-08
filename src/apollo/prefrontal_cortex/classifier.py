from abc import ABC, abstractmethod
from apollo.shared.prompt import Prompt


class Classifier(ABC):
    @abstractmethod
    def classify(self, prompt: Prompt) -> str:
        pass
