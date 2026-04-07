from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI(
    title="OpenEnv Evaluation Server", 
    description="Containerized node for Meta PyTorch Hackathon",
    version="1.0.0"
)

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Health check endpoint for container orchestration systems."""
    return JSONResponse(content={"status": "operational", "message": "Environment system checks passed."})

@app.get("/")
def root():
    """Root endpoint for basic verification."""
    return {"system": "OpenEnv Node", "status": "Active", "owner": "Amit Kumar"}
