# Habit Tracker

A simple daily habit tracker inspired by the idea of building small systems that compound over time. The app helps you mark habits as done or missed, track your streaks, review the last 7 days, and keep momentum with a calm, lightweight interface.

## Features

- Daily habit checklist with grouped categories
- Mark each habit as done or missed
- View the current day, previous day, and next day
- Track streaks for each habit
- See progress across the last 7 days
- Reset the current day or edit habits
- Persistent data saved through a lightweight backend
- Responsive single-page frontend for desktop and mobile

## Tech Stack

- Python + FastAPI for the API layer
- SQLite for local persistence
- Vanilla HTML, CSS, and JavaScript for the frontend

## Project Structure

```text
habit-tracker/
├── api_server.py        # FastAPI server and SQLite storage
├── public/
│   └── index.html       # Frontend UI for tracking habits
├── .gitignore
├── README.md
└── data.db              # SQLite database created at runtime
```

## How it works

The app stores each user's habit progress in a SQLite database keyed by a visitor ID. The frontend loads and saves state through the FastAPI endpoints:

- `GET /api/state` — load saved progress
- `PUT /api/state` — save updated progress

This allows the dashboard to persist your daily habit data between sessions.

## Getting Started

### 1. Install dependencies

```bash
pip install fastapi uvicorn
```

### 2. Start the API server

```bash
python3 api_server.py
```

The API runs on:

```text
http://localhost:8000
```

### 3. Open the app

Open `public/index.html` in a browser and replace the placeholder value `__PORT_8000__` in the file with:

```text
http://localhost:8000
```

Then refresh the page.

## Run locally

```bash
python3 api_server.py
```

Then open the page in your browser and start tracking your habits.

## Notes

This project is intentionally lightweight and beginner-friendly. It is a good example of combining a small backend with a static frontend to create a simple personal productivity tool.

## License

This project is available for personal use and learning purposes.
