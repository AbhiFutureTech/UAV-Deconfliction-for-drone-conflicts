import numpy as np
from datetime import datetime, timedelta
from typing import List
from .models import Mission, WaypointBase

def interpolate_trajectory(mission: Mission) -> List[dict]:
    """Interpolate between waypoints to create a continuous trajectory"""
    waypoints = mission.waypoints
    if not waypoints:
        return []
    
    # Sort waypoints by timestamp if available
    if all(wp.timestamp for wp in waypoints):
        waypoints = sorted(waypoints, key=lambda wp: wp.timestamp)
    
    # Simple linear interpolation (can be enhanced)
    trajectory = []
    for i in range(len(waypoints)-1):
        wp1 = waypoints[i]
        wp2 = waypoints[i+1]
        
        steps = 10  # Number of interpolation points
        for j in range(steps):
            alpha = j / steps
            x = wp1.x + alpha * (wp2.x - wp1.x)
            y = wp1.y + alpha * (wp2.y - wp1.y)
            z = getattr(wp1, 'z', 0) + alpha * (getattr(wp2, 'z', 0) - getattr(wp1, 'z', 0))
            
            point = {'x': x, 'y': y, 'z': z if hasattr(wp1, 'z') else 0}
            if wp1.timestamp and wp2.timestamp:
                time_diff = (wp2.timestamp - wp1.timestamp).total_seconds()
                point['timestamp'] = wp1.timestamp + timedelta(seconds=alpha * time_diff)
            
            trajectory.append(point)
    
    return trajectory

def time_windows_overlap(mission1: Mission, mission2: Mission) -> bool:
    """Check if two missions have overlapping time windows"""
    return not (mission1.t_end < mission2.t_start or mission2.t_end < mission1.t_start)
