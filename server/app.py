from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
import uvicorn

app = FastAPI(title="Amit OpenEnv Server")

class ActionModel(BaseModel):
    action: Any = None

@app.get("/")
def read_root():
    return {"status": "Amit's OpenEnv is Running Successfully!"}

@app.post("/reset")
def reset_env():
    return {"observation": {"status": "environment_reset"}, "info": {}}

@app.post("/step")
def step_env(req: ActionModel = None):
    return {"observation": {"status": "step_executed"}, "reward": 0.5, "done": False, "info": {}}

@app.get("/state")
def get_state():
    return {"current_state": "ready"}

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
