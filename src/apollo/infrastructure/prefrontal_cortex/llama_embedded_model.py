from typing import cast, override
import requests
import json

from apollo.hippocampus.domain.entities.prompt import Prompt
from apollo.hippocampus.domain.entities.task import Task
from apollo.hippocampus.domain.entities.task_type import TaskType
from apollo.prefrontal_cortex.domain.utils.analyze_system_prompt import (
    analyze_system_prompt,
)
from apollo.prefrontal_cortex.domain.utils.classify_system_prompt import (
    classify_system_prompt,
)
from apollo.prefrontal_cortex.interfaces.embedded_model import EmbeddedModel


class LlamaEmbeddedModel(EmbeddedModel):
    @override
    def analyze(self, prompt: Prompt) -> list[Task]:
        response = requests.post(
            url="http://localhost:11434/api/generate",
            timeout=500000,
            json={
                "model": "llama3.2:3b",
                "prompt": f"Analyze: {prompt.value}",
                "stream": False,
                "system": analyze_system_prompt,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 50,
                    "top_p": 0.9,
                    "repeat_penalty": 1.1,
                },
            },
        )

        if response.status_code != 200:
            error = cast(str, response.json())
            raise Exception(f"Failed to analyze user's prompt: {error}")

        llama_tasks = cast(
            list[dict[str, str]], json.loads(cast(str, response.json()["response"]))
        )

        tasks = [
            Task(
                description=task["description"],
                task_dependencies=[],
                original_prompt=prompt,
            )
            for task in llama_tasks
        ]

        return tasks

    @override
    def classify(self, tasks: list[Task]) -> None:
        classifying_tasks = "\n".join(
            f"UUID: {task.uuid} DESCRIPTION: {task.description}" for task in tasks
        )

        response = requests.post(
            url="http://localhost:11434/api/generate",
            timeout=5000000,
            json={
                "model": "llama3.2:3b",
                "prompt": f"Classify the tasks:\n{classifying_tasks}",
                "stream": False,
                "system": classify_system_prompt,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 50,
                    "top_p": 0.9,
                    "repeat_penalty": 1.1,
                },
            },
        )

        if response.status_code != 200:
            error = cast(str, response.json())
            raise Exception(f"Failed to classify tasks: {error}")

        llama_tasks = cast(
            list[dict[str, str]], json.loads(cast(str, response.json()["response"]))
        )

        for task in tasks:
            llama_task = next(
                (
                    llama_task
                    for llama_task in llama_tasks
                    if llama_task["uuid"] == str(task.uuid)
                ),
                None,
            )

            if llama_task is None:
                return

            classification = TaskType(llama_task["classification"])

            task.classify_as(classification)
