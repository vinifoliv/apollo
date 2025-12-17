from apollo.hippocampus.domain.entities.hippocampus import Hippocampus
from apollo.infrastructure.logger.loguru_logger import LoguruLogger
from apollo.infrastructure.prefrontal_cortex.llama_embedded_model import (
    LlamaEmbeddedModel,
)
from apollo.peripheral_nervous_system.domain.peripheral_nervous_system import (
    PeripheralNervousSystem,
)
from apollo.prefrontal_cortex.domain.prefrontal_cortex import PrefrontalCortex
from apollo.thalamus.domain.thalamus import Thalamus


logger = LoguruLogger()

hippocampus = Hippocampus()
thalamus = Thalamus()
peripheral_nervous_system = PeripheralNervousSystem(hippocampus, thalamus)

embedded_model = LlamaEmbeddedModel()
prefrontal_cortex = PrefrontalCortex(embedded_model, hippocampus, thalamus, logger)


if __name__ == "__main__":
    peripheral_nervous_system.listen()
