from datetime import datetime


class Prompt:
    def __init__(self, value: str):
        self.timestamp = datetime.now()
        self.value = value

    @staticmethod
    def from_raw(prompt: str):
        return Prompt(value=prompt)

    def __str__(self) -> str:
        return f"[{self.timestamp.isoformat()}] {self.value}"
