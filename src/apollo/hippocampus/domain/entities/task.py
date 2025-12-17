from datetime import datetime
from typing import override
from uuid import UUID, uuid4

from apollo.hippocampus.domain.entities.artifact import Artifact
from apollo.hippocampus.domain.entities.prompt import Prompt
from apollo.hippocampus.domain.entities.task_type import TaskType


class Task:
    def __init__(
        self,
        description: str,
        task_dependencies: list[UUID],
        original_prompt: Prompt,
        type: TaskType = TaskType.UNCLASSIFIED,
        artifact: Artifact | None = None,
    ) -> None:
        self._uuid: UUID = uuid4()
        self._timestamp: datetime = datetime.now()
        self._type: TaskType = type
        self._description: str = description
        self._task_dependencies: list[UUID] = []
        self._artifact: Artifact | None = artifact
        self._original_prompt: Prompt = original_prompt

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def type(self) -> TaskType:
        return self._type

    @property
    def description(self) -> str:
        return self._description

    @property
    def task_dependencies(self) -> list[UUID]:
        return self._task_dependencies

    @property
    def artifact(self) -> Artifact | None:
        return self._artifact

    @property
    def original_prompt(self) -> Prompt:
        return self._original_prompt

    def classify_as(self, type: TaskType) -> None:
        self._type = type

    def is_classified(self) -> bool:
        return self._type != TaskType.UNCLASSIFIED

    @override
    def __repr__(self) -> str:
        return (
            f"Task("
            f"uuid={self._uuid!r}, "
            f"description={self._description!r}, "
            f"type={self._type!r}, "
            f"prompt={self._original_prompt!r}, "
            f"dependencies_count={len(self._task_dependencies)}, "
            f"artifact={self._artifact}"
            f")"
        )

    @override
    def __str__(self) -> str:
        formatted_timestamp = self._timestamp.strftime("%Y-%m-%d %H:%M")
        shortened_description = self._description[:47] + "..."

        return (
            f"Task ("
            f"uuid={self._uuid}, "
            f"timestamp={formatted_timestamp}, "
            f"type={self._type}, "
            f"description={shortened_description}"
            f")"
        )
