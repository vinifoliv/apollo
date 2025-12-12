from collections import defaultdict
from uuid import UUID
from apollo.shared.entities.artifact import Artifact


class Hippocampus:
    def __init__(self) -> None:
        self._storage: dict[UUID, Artifact] = defaultdict(Artifact)

    def store(self, artifact: Artifact) -> None:
        self._storage[artifact.uuid] = artifact

    def recall(self, uuid: UUID) -> Artifact | None:
        for artifact in self._storage.values():
            if artifact.uuid == uuid:
                return artifact

        return None
