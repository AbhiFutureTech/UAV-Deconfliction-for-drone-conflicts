from fastapi import APIRouter, HTTPException
from app.services.spatial_check import detect_spatial_conflict
from app.services.temporal_check import detect_temporal_conflict

router = APIRouter()

@router.post("/")
def check_conflict(primary_mission: dict, simulated_flights: list):
    spatial_conflict = detect_spatial_conflict(primary_mission, simulated_flights)
    temporal_conflict = detect_temporal_conflict(primary_mission, simulated_flights)

    if spatial_conflict or temporal_conflict:
        return {"status": "Conflict detected", "details": spatial_conflict + temporal_conflict}
    return {"status": "Clear"}
