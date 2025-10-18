from apollo.common.brain_region import BrainRegion
from event_bus.event_bus import EventBus


class PNS(BrainRegion):
    def __init__(self, event_bus: EventBus):
        super(name="pns", event_bus=event_bus)

    def listen(self):
        while True:
            pass
