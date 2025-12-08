from apollo.shared.impulse import Impulse
from apollo.shared.impulse_type import ImpulseType
from apollo.thalamus.thalamus import Thalamus


class PrefrontalCortex:
    def __init__(self, thalamus: Thalamus):
        self._thalamus: Thalamus = thalamus

        self._thalamus.subscribe(
            type=ImpulseType.PROMPT_IS_READY, listener=self.interpret
        )

    def interpret(self, impulse: Impulse):
        print("Impulse received:", impulse)
