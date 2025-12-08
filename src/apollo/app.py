from apollo.peripheral_nervous_system import peripheral_nervous_system
from apollo.prefrontal_cortex.prefrontal_cortex import PrefrontalCortex
from apollo.thalamus.thalamus import Thalamus


thalamus = Thalamus()
peripheral_nervous_system = peripheral_nervous_system.PeripheralNervousSystem(thalamus)
prefrontal_cortex = PrefrontalCortex(thalamus)


if __name__ == "__main__":
    peripheral_nervous_system.listen()
