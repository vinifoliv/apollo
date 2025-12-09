from typing import Final
from apollo.hippocampus.hippocampus import Hippocampus
from apollo.prefrontal_cortex.embedded_model.embedded_model import EmbeddedModel
from apollo.shared.impulse import Impulse
from apollo.shared.impulse_type import ImpulseType
from apollo.shared.task import Task
from apollo.thalamus.thalamus import Thalamus


class PrefrontalCortex:
    def __init__(
        self,
        embedded_model: EmbeddedModel,
        hippocampus: Hippocampus,
        thalamus: Thalamus,
    ) -> None:
        self._embedded_model: Final = embedded_model
        self._hippocampus: Final = hippocampus
        self._thalamus: Final = thalamus

        self._thalamus.subscribe(
            type=ImpulseType.PROMPT_IS_READY, listener=self.interpret
        )

    def interpret(self, impulse: Impulse):
        print("Impulse received:", impulse.uuid, impulse.type, impulse.timestamp)
        prompt = (
            self._hippocampus.recall(uuid=impulse.artifact_uuid)
            if impulse.artifact_uuid
            else None
        )
        if prompt is None:
            return print("No prompt")

        tasks: list[Task] = self._embedded_model.analyze(prompt)
        print("interpretation", tasks)
