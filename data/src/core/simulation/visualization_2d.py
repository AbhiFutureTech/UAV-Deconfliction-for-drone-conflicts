import matplotlib.pyplot as plt
import matplotlib.animation as animation
from core.models import Mission, ConflictReport

def plot_2d_trajectories(
    primary_mission: Mission,
    other_missions: List[Mission],
    conflict_report: ConflictReport
):
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot primary mission
    xs = [wp.x for wp in primary_mission.waypoints]
    ys = [wp.y for wp in primary_mission.waypoints]
    ax.plot(xs, ys, 'b-', label='Primary Mission', linewidth=2)
    ax.scatter(xs, ys, c='blue', s=100)
    
    # Plot other missions
    for mission in other_missions:
        xs = [wp.x for wp in mission.waypoints]
        ys = [wp.y for wp in mission.waypoints]
        ax.plot(xs, ys, 'r--', alpha=0.5, label=f'Other Drone {mission.drone_id}')
        ax.scatter(xs, ys, c='red', s=50)
    
    # Highlight conflicts
    for conflict in conflict_report.conflicts:
        ax.scatter(
            conflict['location'][0], 
            conflict['location'][1], 
            c='yellow', 
            edgecolors='black',
            s=200,
            marker='*',
            label='Conflict Point'
        )
    
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('2D Trajectory Conflict Visualization')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    return fig
