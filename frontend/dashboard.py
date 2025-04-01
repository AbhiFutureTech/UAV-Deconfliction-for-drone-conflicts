curl -X POST "http://localhost:8000/api/v1/check-conflict/3d" \
  -H "Content-Type: application/json" \
  -d '{"primary_mission": {...}, "other_missions": [...]}'
