from src.apollo.common.brain_region import BrainRegion
from src.apollo.thalamus.thalamus import Thalamus


class PrefrontalCortex(BrainRegion):
    def __init__(self, thalamus: Thalamus):
        super().__init__(thalamus)
