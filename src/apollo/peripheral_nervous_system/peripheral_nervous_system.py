from typing import Final
from apollo.hippocampus.hippocampus import Hippocampus
from apollo.shared.impulse import Impulse
from apollo.shared.impulse_type import ImpulseType
from apollo.shared.prompt import Prompt
from apollo.thalamus.thalamus import Thalamus


class PeripheralNervousSystem:
    def __init__(self, hippocampus: Hippocampus, thalamus: Thalamus) -> None:
        self._hippocampus: Final = hippocampus
        self._thalamus: Final = thalamus

    def listen(self):
        while True:
            raw_input = input("> ")
            prompt = Prompt(raw_input)

            self._hippocampus.store(prompt)

            impulse = Impulse(
                type=ImpulseType.PROMPT_IS_READY, artifact_uuid=prompt.uuid
            )
            self._thalamus.publish(impulse)
