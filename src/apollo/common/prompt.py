import datetime


class Prompt:
    def __init__(self, value: str):
        self.timestamp = datetime.now()
        self.value = value
