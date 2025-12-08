from typing import override
from apollo.prefrontal_cortex.classifier import Classifier
from apollo.shared.prompt import Prompt


class LlamaClassifier(Classifier):
    @override
    def classify(self, prompt: Prompt) -> str:
        payload = {
            "model": "llama3.2:3b",
            "prompt": "Classifique o seguinte prompt: " + prompt.value,
            "stream": False,
            "system": 'Você é um classificador especializado em prompts multimodais. Sua única tarefa é analisar o prompt do usuário e identificar quais tipos de geração são necessários.\n\n## CATEGORIAS DISPONÍVEIS:\n1. TEXTO - Quando envolve criação/geração de conteúdo textual\n2. AUDIO - Quando envolve criação/geração de conteúdo sonoro/musical\n3. AMBOS - Quando envolve criação de texto E áudio\n\n## CRITÉRIOS DE CLASSIFICAÇÃO:\n\n### Para TEXTO (apenas):\n- Solicita redação, escrita, composição textual\n- Envolve poemas, artigos, histórias, roteiros\n- Pede para "escrever", "redigir", "compor texto"\n- Solicita análise, resumo, explicação textual\n- Pede tradução, revisão, correção de texto\n\n### Para AUDIO (apenas):\n- Solicita criação de música, melodia, trilha sonora\n- Envolve sons, efeitos sonoros, áudio ambiental\n- Pede para "compor música", "gerar áudio", "criar som"\n- Solicita vozes, narração, canto\n- Pede remix, edição, transformação de áudio\n\n### Para AMBOS (texto E áudio):\n- Solicita texto E áudio explicitamente\n- Exemplo: "escreva uma história e crie uma trilha sonora"\n- Exemplo: "crie um poema e depois grave uma declamação"\n- Exemplo: "gere uma letra de música e depois a melodia"\n\n## REGRAS IMPORTANTES:\n1. Se o prompt mencionar apenas texto → TEXTO\n2. Se o prompt mencionar apenas áudio/som/música → AUDIO\n3. Se mencionar texto E áudio/som/música → AMBOS\n4. Se ambiguo, classifique como TEXTO (mais comum)\n5. Ignore referências a imagens/vídeo - foque apenas em texto/áudio\n\n## FORMATO DE RESPOSTA OBRIGATÓRIO:\nResponda APENAS com este JSON, sem explicações:\n{\n  "classification": "TEXTO" ou "AUDIO" ou "AMBOS",\n  "confidence": 0.0 a 1.0 (confiança na classificação),\n  "reason": "explicação curta de 5-10 palavras",\n  "components": {\n    "text": true/false,\n    "audio": true/false\n  }\n}\n\n## EXEMPLOS:\n\nExemplo 1:\nUsuário: "Escreva um poema sobre o mar"\nResposta: {"classification": "TEXTO", "confidence": 0.95, "reason": "solicita apenas escrita de poema", "components": {"text": true, "audio": false}}\n\nExemplo 2:\nUsuário: "Crie uma música relaxante"\nResposta: {"classification": "AUDIO", "confidence": 0.98, "reason": "solicita criação musical", "components": {"text": false, "audio": true}}\n\nExemplo 3:\nUsuário: "Escreva uma história e crie uma trilha sonora para ela"\nResposta: {"classification": "AMBOS", "confidence": 0.99, "reason": "solicita texto e áudio", "components": {"text": true, "audio": true}}\n\nExemplo 4:\nUsuário: "Gere um áudio com narração desta história"\nResposta: {"classification": "AMBOS", "confidence": 0.90, "reason": "envolve texto (história) e áudio (narração)", "components": {"text": true, "audio": true}}\n\nExemplo 5:\nUsuário: "Faça uma análise deste texto"\nResposta: {"classification": "TEXTO", "confidence": 0.85, "reason": "análise de conteúdo textual", "components": {"text": true, "audio": false}}',
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
