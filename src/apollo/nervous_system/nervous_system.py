from src.apollo.common.impulse import Impulse
from src.apollo.common.impulse_type import ImpulseType
from src.apollo.common.brain_region import BrainRegion
from src.apollo.common.prompt import Prompt
from src.apollo.thalamus.thalamus import Thalamus


class NervousSystem(BrainRegion):
    def __init__(self, thalamus: Thalamus):
        self._thalamus = thalamus

    def listen(self):
        while True:
            raw_prompt = input("> ")
            prompt = Prompt.from_raw(raw_prompt)
            print("PROMPT CAPTURED:", prompt)
            impulse = Impulse(type=ImpulseType.PROMPT_READY, payload=prompt)
            self.fire_impulse(impulse)

    def fire_impulse(self, impulse):
        self._thalamus.receive_impulse(impulse)

    def catch_impulse(self):
        impulse = self._thalamus.free_impulse()

        if impulse.adressee != "nervous_system":
            self._thalamus.feed_back(impulse)
