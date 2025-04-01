from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Waypoint2D(BaseModel):
    x: float
    y: float
    timestamp: Optional[datetime] = None

class Waypoint3D(Waypoint2D):
    z: float

class Mission(BaseModel):
    waypoints: List[Waypoint2D]  # or Waypoint3D for 3D/4D
    t_start: datetime
    t_end: datetime
    drone_id: str

class ConflictReport(BaseModel):
    is_conflict: bool
    conflicts: List[dict]
    conflicting_drones: List[str]
