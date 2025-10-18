from apollo.common.brain_region import BrainRegion
from event_bus.event_bus import EventBus


class PrefrontalCortex(BrainRegion):
    def __init__(self, event_bus: EventBus):
        super(name="prefronal_cortex", event_bus=event_bus)
