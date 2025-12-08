from typing import Final
from apollo.hippocampus.hippocampus import Hippocampus
from apollo.shared.impulse import Impulse
from apollo.shared.impulse_type import ImpulseType
from apollo.thalamus.thalamus import Thalamus
from apollo.prefrontal_cortex.classifier import Classifier


class PrefrontalCortex:
    def __init__(
        self, classifier: Classifier, hippocampus: Hippocampus, thalamus: Thalamus
    ) -> None:
        self._classifier: Final = classifier
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

        interpretation = self._classifier.classify(prompt)
        print("interpretation", interpretation)
