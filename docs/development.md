# Development

Use a virtual environment and synthetic data. Keep model caches, `face_embedding.txt`, simulated logs, camera captures, and Redis credentials untracked.

## Checks

```bash
python -m compileall Home.py auth.py face_rec.py upload_logs.py pages
```

Then exercise registration, recognition, report refresh, authentication failure, missing Redis, and no-face camera frames. Add focused tests for numerical similarity and report aggregation before changing thresholds or log formats.
