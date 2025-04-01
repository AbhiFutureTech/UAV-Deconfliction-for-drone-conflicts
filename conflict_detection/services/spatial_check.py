def detect_spatial_conflict(primary_mission, simulated_flights):
    conflicts = []
    for flight in simulated_flights:
        for waypoint in flight["waypoints"]:
            for primary_waypoint in primary_mission["waypoints"]:
                if (abs(primary_waypoint["x"] - waypoint["x"]) < 10 and 
                    abs(primary_waypoint["y"] - waypoint["y"]) < 10):  # 10m buffer
                    conflicts.append({"location": waypoint, "conflict_with": flight["id"]})
    return conflicts
