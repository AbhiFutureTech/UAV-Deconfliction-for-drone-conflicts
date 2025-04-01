import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from core.models import Mission, ConflictReport

def plot_3d_trajectories(
    primary_mission: Mission,
    other_missions: List[Mission],
    conflict_report: ConflictReport
):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot primary mission
    xs = [wp.x for wp in primary_mission.waypoints]
    ys = [wp.y for wp in primary_mission.waypoints]
    zs = [wp.z for wp in primary_mission.waypoints]
    ax.plot(xs, ys, zs, 'b-', label='Primary Mission', linewidth=2)
    ax.scatter(xs, ys, zs, c='blue', s=100)
    
    # Plot other missions
    for mission in other_missions:
        xs = [wp.x for wp in mission.waypoints]
        ys = [wp.y for wp in mission.waypoints]
        zs = [wp.z for wp in mission.waypoints]
        ax.plot(xs, ys, zs, 'r--', alpha=0.5, label=f'Other Drone {mission.drone_id}')
        ax.scatter(xs, ys, zs, c='red', s=50)
    
    # Highlight conflicts
    for conflict in conflict_report.conflicts:
        ax.scatter(
            conflict['location'][0], 
            conflict['location'][1], 
            conflict['location'][2],
            c='yellow', 
            edgecolors='black',
            s=200,
            marker='*',
            label='Conflict Point'
        )
    
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Altitude (Z)')
    ax.set_title('3D Trajectory Conflict Visualization')
    ax.legend()
    plt.tight_layout()
    return fig
