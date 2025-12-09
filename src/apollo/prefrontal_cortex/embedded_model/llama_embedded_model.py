from typing import override

from apollo.prefrontal_cortex.embedded_model.embedded_model import EmbeddedModel
from apollo.prefrontal_cortex.embedded_model.system_prompts.analyze_system_prompt import (
    analyze_system_prompt,
)
from apollo.prefrontal_cortex.embedded_model.system_prompts.classify_system_prompt import (
    classify_system_prompt,
)
from apollo.shared.prompt import Prompt
from apollo.shared.task import Task


class LlamaEmbeddedModel(EmbeddedModel):
    @override
    def analyze(self, prompt: Prompt) -> list[Task]:
        payload = {
            "model": "llama3.2:3b",
            "prompt": f"Analyze:\n{prompt.value}",
            "stream": False,
            "system": analyze_system_prompt,
            "options": {
                "temperature": 0.1,
                "num_predict": 50,
                "top_p": 0.9,
                "repeat_penalty": 1.1,
            },
        }

    @override
    def classify(self, tasks: list[Task]) -> None:
        payload = {
            "model": "llama3.2:3b",
            "prompt": "Classifique o seguinte prompt: " + prompt.value,
            "stream": False,
            "system": classify_system_prompt,
            "options": {
                "temperature": 0.1,
                "num_predict": 50,
                "top_p": 0.9,
                "repeat_penalty": 1.1,
            },
        }

        try:
            import requests

            response = requests.post(
                url="http://localhost:11434/api/generate", json=payload, timeout=5000000
            )

            if response.status_code == 200:
                return response.json()["response"]
            else:
                return f"Erro: {response.json()}"

        except Exception as e:
            return f"Erro de conexão: {e.args[0]}"
