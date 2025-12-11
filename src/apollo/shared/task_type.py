from enum import Enum


class TaskType(Enum):
    UNCLASSIFIED = "unclassified"
    TEXT = "text"
    AUDIO = "audio"
    VIDEO = "video"
