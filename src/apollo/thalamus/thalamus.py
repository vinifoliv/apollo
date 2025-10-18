from apollo.common.brain_region import BrainRegion
from event_bus.event_bus import EventBus


class Thalamus(BrainRegion):
    def __init__(self, event_bus: EventBus):
        super(name="thalamus", event_bus=event_bus)
