# Scalable FastAPI Application

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
This project is purely about professional API architecture. Refactor a simple API into the scalable "Bigger Applications" structure recommended by the official FastAPI documentation. This involves using `APIRouter` to split your path operations into multiple files (e.g., `users.py`, `items.py`) and including them in the main app object.

## Possible Folder Structure
```
scalable_fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py         # (Main FastAPI app, includes routers)
│   ├── dependencies.py # (Shared dependencies)
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── items.py    # (APIRouter for /items)
│   │   └── users.py    # (APIRouter for /users)
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** `GET http://127.0.0.1:8000/users/`
- **Output:** JSON from the `users.py` router

## Learning Objectives
- Scalable API architecture
- FastAPI router system
- Code organization patterns
- Professional development practices
- Modular application design
