from fastapi import FastAPI
from app.routes import check_conflict, upload_data

app = FastAPI(title="UAV Conflict Detection API")

# Include Routes
app.include_router(check_conflict.router, prefix="/conflict")
app.include_router(upload_data.router, prefix="/upload")

@app.get("/")
def home():
    return {"message": "Welcome to UAV Conflict Detection API"}
