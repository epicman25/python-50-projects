# FastAPI CRUD API with Database

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
Build a full CRUD (Create, Read, Update, Delete) API for a resource (e.g., "Books" or "Users"). This project must use **FastAPI** for the API logic, **Pydantic** models for data validation and serialization (`schemas.py`), and **SQLAlchemy** with a SQLite database for persistence (`models.py`). Create separate files for different concerns.

## Possible Folder Structure
```
fastapi_crud_db/
├── main.py         # (Imports router, runs app)
├── crud.py         # (Functions to interact with DB, e.g., get_user)
├── database.py     # (Engine, SessionLocal, Base)
├── models.py       # (SQLAlchemy models)
├── schemas.py      # (Pydantic models)
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** `POST /books/` with JSON `{"title": "1984", "author": "George Orwell"}`
- **Output:** A 200 OK response with the created object's JSON
- **Input:** `GET /books/1`
- **Output:** `{"id": 1, "title": "1984", "author": "George Orwell"}`

## Learning Objectives
- FastAPI framework mastery
- Database integration with SQLAlchemy
- API design patterns
- Data validation with Pydantic
- Professional API architecture
