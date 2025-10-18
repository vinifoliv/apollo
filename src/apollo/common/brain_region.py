from event_bus.event_bus import EventBus


class BrainRegion:
    def __init__(self, name: str, event_bus: EventBus):
        self._name = name
        self._event_bus = event_bus
