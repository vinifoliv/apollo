# Apollo

## Introduction
Apollo is an AI model orchestration system, created for providing an open source solution for stacking multimodal models into a single system.

## How to run
1. Get the Ollama container up and running

Run the container
```sh
docker compose up -d
```

Pull and run Llama3.2:3B model
```sh
docker exec -it ollama ollama run llama3.2:3b
```

2. Set up Python environment

Create a virtual environment
```sh
python -m venv venv
```

Install the dependencies
```sh
pip install -f requirements.txt
```

3. Run the project

Move to the `src/` directory and run the project
```sh
python -m apollo.app
```

