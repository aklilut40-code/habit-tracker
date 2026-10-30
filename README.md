# Daily Habits Tracker

A simple daily habit tracker inspired by *Atomic Habits*. Mark each habit ✓ (done) or ✗ (missed), track streaks, and see the last 7 days.

## Run locally

```bash
pip install fastapi uvicorn
python3 api_server.py        # starts the API on port 8000
```

Then open `public/index.html`, replacing `__PORT_8000__` in the file with `http://localhost:8000`.
