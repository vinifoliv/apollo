from apollo.hippocampus import hippocampus
from apollo.peripheral_nervous_system.peripheral_nervous_system import (
    PeripheralNervousSystem,
)
from apollo.prefrontal_cortex.llama_classifier import LlamaClassifier
from apollo.prefrontal_cortex.prefrontal_cortex import PrefrontalCortex
from apollo.thalamus.thalamus import Thalamus


hippocampus = hippocampus.Hippocampus()
thalamus = Thalamus()
peripheral_nervous_system = PeripheralNervousSystem(hippocampus, thalamus)

classifier = LlamaClassifier()
prefrontal_cortex = PrefrontalCortex(classifier, hippocampus, thalamus)


if __name__ == "__main__":
    peripheral_nervous_system.listen()
