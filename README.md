# 📄 UAV Strategic Deconfliction System – Code Documentation

## 📦 Data Structures

### `Waypoint`
Represents a single point in 3D space and time.

### `DroneMission`
Represents a drone's full flight path.

## 🔍 Conflict Detection Logic

- `euclidean_distance(p1, p2)`
- `check_conflict(primary, others)`

## 📊 Visualization

- `plot_missions()`: 3D static plot
- `animate_4d()`: Time-evolving animation

## 🧪 Sample Input

A JSON-like list of waypoints with coordinates and timestamps.
