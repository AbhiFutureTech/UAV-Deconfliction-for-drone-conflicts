from fastapi import APIRouter, HTTPException
from core.models import Mission, ConflictReport
from core.conflict_detection_2d import check_2d_conflict
from core.conflict_detection_3d import check_3d_conflict
from core.conflict_detection_4d import check_4d_conflict
from typing import List

router = APIRouter()

@router.post("/check-conflict/2d", response_model=ConflictReport)
async def check_2d_conflict_api(
    primary_mission: Mission,
    other_missions: List[Mission],
    safety_buffer: float = 5.0
):
    return check_2d_conflict(primary_mission, other_missions, safety_buffer)

@router.post("/check-conflict/3d", response_model=ConflictReport)
async def check_3d_conflict_api(
    primary_mission: Mission,
    other_missions: List[Mission],
    safety_buffer: float = 5.0,
    altitude_buffer: float = 3.0
):
    return check_3d_conflict(
        primary_mission, 
        other_missions, 
        safety_buffer, 
        altitude_buffer
    )

@router.post("/check-conflict/4d", response_model=ConflictReport)
async def check_4d_conflict_api(
    primary_mission: Mission,
    other_missions: List[Mission],
    safety_buffer: float = 5.0,
    altitude_buffer: float = 3.0
):
    return check_4d_conflict(
        primary_mission, 
        other_missions, 
        safety_buffer, 
        altitude_buffer
    )
