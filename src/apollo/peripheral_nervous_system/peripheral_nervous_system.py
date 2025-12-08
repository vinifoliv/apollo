from apollo.shared.impulse import Impulse
from apollo.shared.impulse_type import ImpulseType
from apollo.shared.prompt import Prompt
from apollo.thalamus.thalamus import Thalamus


class PeripheralNervousSystem:
    def __init__(self, thalamus: Thalamus):
        self._thalamus: Thalamus = thalamus

    def listen(self):
        while True:
            raw_input = input("> ")
            prompt = Prompt(raw_input)
            impulse = Impulse(type=ImpulseType.PROMPT_IS_READY, payload=prompt)
            self._thalamus.publish(impulse)
