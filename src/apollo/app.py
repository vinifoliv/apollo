from event_bus.event_bus import EventBus
from pns.pns import PNS
from prefrontal_cortex.prefrontal_cortex import PrefrontalCortex
from thalamus.thalamus import Thalamus

event_bus = EventBus()

pns = PNS(event_bus)
prefrontal_cortex = PrefrontalCortex(event_bus)
thalamus = Thalamus(event_bus)

pns.listen()
