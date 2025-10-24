from src.apollo.pns.pns import PNS
from src.apollo.prefrontal_cortex.prefrontal_cortex import PrefrontalCortex
from src.apollo.thalamus.thalamus import Thalamus


thalamus = Thalamus()
pns = PNS(thalamus)
prefrontal_cortex = PrefrontalCortex(thalamus)

if __name__ == "__main__":
    pns.listen()
