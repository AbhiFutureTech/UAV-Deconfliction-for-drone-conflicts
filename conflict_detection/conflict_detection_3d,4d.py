# Similar structure to 2D but with altitude (z) dimension
def check_3d_conflict(
    primary_mission: Mission,
    other_missions: List[Mission],
    safety_buffer: float = 5.0,
    altitude_buffer: float = 3.0
) -> ConflictReport:
    conflicts = []
    conflicting_drones = set()
    
    primary_traj = interpolate_trajectory(primary_mission)
    
    for other_mission in other_missions:
        if not time_windows_overlap(primary_mission, other_mission):
            continue
            
        other_traj = interpolate_trajectory(other_mission)
        
        for t in get_overlapping_times(primary_traj, other_traj):
            primary_pos = get_position_at_time(primary_traj, t)
            other_pos = get_position_at_time(other_traj, t)
            
            horizontal_dist = np.linalg.norm(
                np.array(primary_pos[:2]) - np.array(other_pos[:2])
            )
            vertical_dist = abs(primary_pos[2] - other_pos[2])
            
            if (horizontal_dist < safety_buffer and 
                vertical_dist < altitude_buffer):
                conflict = {
                    "time": t,
                    "location": primary_pos,
                    "horizontal_distance": horizontal_dist,
                    "vertical_distance": vertical_dist,
                    "conflicting_drone": other_mission.drone_id
                }
                conflicts.append(conflict)
                conflicting_drones.add(other_mission.drone_id)
    
    return ConflictReport(
        is_conflict=len(conflicts) > 0,
        conflicts=conflicts,
        conflicting_drones=list(conflicting_drones)
    )
