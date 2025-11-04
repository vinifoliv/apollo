from src.apollo.cortex.cortex import Cortex
from src.apollo.nervous_system.nervous_system import NervousSystem
from src.apollo.thalamus.thalamus import Thalamus


thalamus = Thalamus()
nervous_system = NervousSystem(thalamus)
cortex = Cortex(thalamus)

if __name__ == "__main__":
    nervous_system.listen()
