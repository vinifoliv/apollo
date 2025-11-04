from src.apollo.common.impulse_type import ImpulseType
from src.apollo.common.prompt import Prompt
from src.apollo.common.brain_region import BrainRegion
from src.apollo.thalamus.thalamus import Thalamus


class Cortex(BrainRegion):
    def __init__(self, thalamus: Thalamus):
        self._thalamus = thalamus

    def interpret(self, prompt: Prompt):
        self.fire_impulse()
        print(f"Prompt '{prompt}' interpreted.")

    def catch_impulse(self):
        impulse = self._thalamus.free_impulse()

        match impulse.type:
            case ImpulseType.PROMP_READY:
                prompt = impulse.payload
                self._interpret(prompt)
            case _:
                self._thalamus.feed_back(impulse)

    def fire_impulse(self, impulse):
        return super().fire_impulse(impulse)
