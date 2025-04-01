def detect_temporal_conflict(primary_mission, simulated_flights):
    conflicts = []
    for flight in simulated_flights:
        for primary_waypoint in primary_mission["waypoints"]:
            for waypoint in flight["waypoints"]:
                if (primary_waypoint["time"] == waypoint["time"]):  # Exact time match
                    conflicts.append({"location": waypoint, "time": waypoint["time"], "conflict_with": flight["id"]})
    return conflicts
