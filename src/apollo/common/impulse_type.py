from enum import Enum


class ImpulseType(Enum):
    PROMPT_READY = "prompt_ready"
    PROMPT_INTERPRETED = "prompt_interpreted"
    PROMPT_RESPONSE_READY = "prompt_response_ready"
