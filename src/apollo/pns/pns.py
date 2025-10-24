from src.apollo.common.impulse import Impulse
from src.apollo.common.impulse_type import ImpulseType
from src.apollo.common.brain_region import BrainRegion
from src.apollo.common.prompt import Prompt
from src.apollo.thalamus.thalamus import Thalamus


class PNS(BrainRegion):
    def __init__(self, thalamus: Thalamus):
        super().__init__(thalamus)

    def listen(self):
        while True:
            raw_prompt = input("> ")
            prompt = Prompt.from_raw(raw_prompt)
            self.fire_prompt_is_ready(prompt)

    def fire_prompt_is_ready(self, prompt: Prompt):
        impulse = Impulse(type=ImpulseType.PROMPT_READY, payload=prompt)
        self.fire_impulse(impulse)
