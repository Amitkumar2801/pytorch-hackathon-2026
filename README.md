# Advanced Cognitive Agent Environment (OpenEnv)
**Meta PyTorch Hackathon (Scaler School of Technology) - Round 1 Submission**

## 📌 Overview
This repository hosts a robust, containerized environment designed to evaluate autonomous LLM reasoning capabilities. Built using the OpenEnv specification, it simulates a dynamic real-world sequential task execution environment suitable for AI agent interaction and training.

## 🚀 Key Features
* **Standardized Logging:** Implements professional `logging` modules utilizing `[START]`, `[STEP]`, and `[END]` markers for precise automated scoring.
* **API Readiness:** Built with FastAPI, exposing a `/health` endpoint for orchestration and readiness probes.
* **Configurable Dynamics:** Fully integrated with `API_BASE_URL` and `MODEL_NAME` via environment variables.
* **Dockerized:** Packaged for seamless deployment on Hugging Face Spaces.

## 📁 Repository Structure
* `inference.py`: Core execution script managing the agent's evaluation sequence and state logging.
* `openenv.yaml`: Metadata configuration defining the environment's capabilities and sequential task definitions.
* `main.py`: FastAPI server script.
* `Dockerfile` & `requirements.txt`: Environment dependencies and container configuration.

## 🛠️ Usage
To run the environment locally:
```bash
pip install -r requirements.txt
python inference.py
