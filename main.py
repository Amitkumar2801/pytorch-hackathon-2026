from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI(title="Amit OpenEnv Server")

class ActionModel(BaseModel):
    action: Any = None

@app.get("/")
def read_root():
    return {"status": "Amit's OpenEnv is Running Successfully!"}

# Yeh endpoints system check karega:
@app.post("/reset")
def reset_env():
    return {"observation": {"status": "environment_reset"}, "info": {}}

@app.post("/step")
def step_env(req: ActionModel = None):
    return {"observation": {"status": "step_executed"}, "reward": 0.5, "done": False, "info": {}}

@app.get("/state")
def get_state():
    return {"current_state": "ready"}
