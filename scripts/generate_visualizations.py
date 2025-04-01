import json
import matplotlib.pyplot as plt
from src.core.models import Mission
from src.simulation.visualization_2d import plot_2d_trajectories
from src.core.conflict_detection_2d import check_2d_conflict

# Load sample data
with open('src/data/sample_missions.json') as f:
    data = json.load(f)

primary_mission = Mission(**data['primary_mission'])
other_missions = [Mission(**m) for m in data['other_missions']]

# Check for conflicts
conflict_report = check_2d_conflict(primary_mission, other_missions)

# Generate visualization
fig = plot_2d_trajectories(primary_mission, other_missions, conflict_report)
plt.savefig('docs/2d_conflict_visualization.png')
plt.close()

print("Conflict visualization generated at docs/2d_conflict_visualization.png")
