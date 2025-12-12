from apollo.hippocampus import hippocampus
from apollo.peripheral_nervous_system.peripheral_nervous_system import (
    PeripheralNervousSystem,
)
from apollo.prefrontal_cortex.entities.prefrontal_cortex import PrefrontalCortex
from apollo.prefrontal_cortex.adapters.llama_embedded_model import LlamaEmbeddedModel
from apollo.shared.adapters.loguru_logger import LoguruLogger
from apollo.thalamus.thalamus import Thalamus

logger = LoguruLogger()

hippocampus = hippocampus.Hippocampus()
thalamus = Thalamus()
peripheral_nervous_system = PeripheralNervousSystem(hippocampus, thalamus)

embedded_model = LlamaEmbeddedModel()
prefrontal_cortex = PrefrontalCortex(embedded_model, hippocampus, thalamus, logger)


if __name__ == "__main__":
    peripheral_nervous_system.listen()
