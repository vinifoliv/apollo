from typing import Final, cast

from apollo.hippocampus.hippocampus import Hippocampus
from apollo.prefrontal_cortex.interfaces.embedded_model import EmbeddedModel
from apollo.shared.entities.impulse import Impulse
from apollo.shared.entities.impulse_type import ImpulseType
from apollo.shared.entities.prompt import Prompt
from apollo.shared.interfaces.logger import Logger
from apollo.thalamus.thalamus import Thalamus


class PrefrontalCortex:
    def __init__(
        self,
        embedded_model: EmbeddedModel,
        hippocampus: Hippocampus,
        thalamus: Thalamus,
        logger: Logger,
    ) -> None:
        self._embedded_model: Final = embedded_model
        self._hippocampus: Final = hippocampus
        self._thalamus: Final = thalamus
        self._logger: Final = logger

        self._thalamus.subscribe(
            type=ImpulseType.PROMPT_IS_READY, listener=self.interpret
        )

    def interpret(self, impulse: Impulse) -> None:
        self._logger.info("[TRACE] [PrefrontalCortex] interpreting")

        prompt = (
            self._hippocampus.recall(uuid=impulse.artifact_uuid)
            if impulse.artifact_uuid
            else None
        )

        if prompt is None:
            self._logger.info("[TRACE] [PrefrontalCortex] prompt not found")
            return print("No prompt")

        self._logger.info("[TRACE] [PrefrontalCortex] prompt recalled")

        self._logger.info("[TRACE] [PrefrontalCortex] analyzing prompt")
        tasks = self._embedded_model.analyze(prompt=cast(Prompt, prompt))
        for task in tasks:
            self._logger.info(f"[PrefrontalCortex] {task}")

        self._logger.info("[TRACE] [PrefrontalCortex] classifying tasks")
        self._embedded_model.classify(tasks)
        for task in tasks:
            self._logger.info(f"[PrefrontalCortex] {task}")

        self._logger.info("[TRACE] [PrefrontalCortex] intrepreting complete")
