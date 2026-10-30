# Habit Tracker

## Abstract

Habit Tracker is a lightweight web application designed to support daily self-improvement and behavioral consistency through a simple habit monitoring system. The project combines a minimal backend with a client-side interface to allow users to record whether daily routines were completed, review trends over time, and maintain momentum through visual progress indicators and streak tracking. The system emphasizes simplicity, immediacy, and usability, making it suitable for personal productivity and habit formation.

## 1. Introduction

Human behavior is strongly influenced by consistent routines and feedback loops. Habit formation research suggests that small, repeatable actions performed daily are more sustainable than large, infrequent efforts. Habit Tracker was developed to operationalize this principle by providing a digital environment in which users can monitor daily commitments, identify missed activities, and reinforce productive behavior through measurable progress.

This project demonstrates a practical implementation of a habit tracking application using a lightweight architecture: a Python API provides persistence, while a front-end interface delivers an intuitive user experience. The system functions as both a productivity tool and a demonstration of how small-scale web applications can integrate storage, state management, and user interaction.

## 2. Problem Statement

Many individuals struggle to maintain consistent routines because they lack a structured and low-friction method for monitoring their daily habits. Existing habit tracking solutions may be overly complex, require external accounts, or fail to reflect the user’s personal routines in a flexible manner. There is a need for a minimal but effective tool that allows users to define daily habits, evaluate completion status, and track progress without unnecessary overhead.

## 3. Objectives

The primary objectives of this project are as follows:

- Design and implement a simple habit tracking application.
- Allow users to create, edit, and remove personal habits.
- Enable daily marking of habits as completed or missed.
- Show daily and weekly progress using visual summaries.
- Persist user data in a lightweight local database.
- Maintain a responsive and accessible interface for use on desktop and mobile devices.

## 4. System Design

The application follows a client-server model with a thin backend and a static front-end.

### 4.1 Front-end

The front-end is built using HTML, CSS, and JavaScript without a larger framework, which reduces complexity and keeps the application easy to run and modify. The interface includes:

- date navigation for viewing past and present days,
- habit groups such as Morning, Daytime, and Evening,
- completion controls for done and missed states,
- progress bars and summary statistics,
- a weekly table to show activity over the last seven days.

### 4.2 Back-end

The back-end is implemented in Python using FastAPI. It exposes a minimal API for saving and retrieving application state. Data persistence is handled through SQLite, which is appropriate for a local-only, lightweight solution.

### 4.3 Data Model

The application uses a simple state storage mechanism keyed by a visitor identifier. Each user session stores habit information and daily progress in a serialized JSON structure. This design ensures simple retrieval and update operations while keeping the system lightweight.

## 5. Implementation Details

### 5.1 Architecture

The project consists of the following components:

- `api_server.py`: defines the FastAPI application and database initialization.
- `public/index.html`: contains the user interface and client-side logic.
- `data.db`: local SQLite database generated at runtime.
- `README.md`: documentation for setup and usage.

### 5.2 Core Functionalities

The implemented application supports the following features:

- Habit creation and deletion.
- Daily status updates: done or missed.
- Progress summaries for the current day.
- Streak calculation across consecutive successful completions.
- Weekly habit tracking table.
- Warning messages for missed habits to encourage recovery.
- Persistence across sessions through the backend.

### 5.3 API Endpoints

The backend exposes two primary endpoints:

- `GET /api/state` — retrieves saved user data.
- `PUT /api/state` — overwrites or updates repository state with new progress information.

The API is intentionally minimal, reflecting the project’s emphasis on simplicity and maintainability.

## 6. Technologies Used

- Python
- FastAPI
- SQLite
- HTML
- CSS
- JavaScript

## 7. Setup and Usage

### Prerequisites

- Python 3.x installed
- `pip` for installing dependencies

### Installation

```bash
pip install fastapi uvicorn
```

### Running the Application

Start the API server:

```bash
python3 api_server.py
```

The server listens on:

```text
http://localhost:8000
```

Open `public/index.html` in a browser and set the backend URL placeholder to `http://localhost:8000` before use.

## 8. Evaluation and Findings

The Habit Tracker project demonstrates that a small-scale personal productivity application can be built effectively using minimal tools. The design prioritizes accessibility, speed, and low setup overhead, which are important for habit-oriented tools. The use of a local database eliminates dependency on external services while preserving functional persistence.

The application also illustrates that an interface can remain visually polished and usable without relying on larger frontend frameworks. This makes the project suitable for rapid prototyping and educational purposes.

## 9. Limitations

Although the project is functional, it has several limitations:

- it stores data locally rather than in a multi-user backend,
- it does not include authentication or user accounts,
- it lacks advanced analytics or data export features,
- it does not provide cross-device synchronization.

## 10. Future Work

Future enhancements could include:

- user authentication and cloud-based storage,
- visual charts for habit trends over longer periods,
- reminder notifications,
- customizable habit categories and priorities,
- integration with mobile-friendly interfaces and APIs.

## 11. Conclusion

Habit Tracker is a compact and practical application that embodies the principles of habit formation and productivity through regular self-monitoring. By combining a simple front-end with a lightweight backend, the project successfully demonstrates how personal software can be both useful and easy to implement. It serves as a strong foundation for future development in behavioral tracking, productivity applications, and self-improvement technologies.

## 12. License

This project is intended for educational and personal use.
