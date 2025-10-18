class EventBus:
    def __init__(self):
        self._event_list = ["prompt_ready"]

    def on(self, event, callback):
        pass

    def emit(self, event, data=None):
        pass
