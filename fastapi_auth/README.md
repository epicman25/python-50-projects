# FastAPI with User Authentication

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
Extend the CRUD API from project 41 to include user authentication. Implement `/token` endpoint using OAuth2 with password flow. Secure the CRUD endpoints so that (for example) only authenticated users can create items. This involves password hashing (`passlib`), JWT token creation, and FastAPI's `Depends` system for protected routes.

## Possible Folder Structure
```
fastapi_auth/
├── main.py
├── auth.py         # (Token/OAuth2 logic, user helpers)
├── crud.py
├── database.py
├── models.py
├── schemas.py
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** `POST /token` with form data `username=...` & `password=...`
- **Output:** JSON `{"access_token": "...", "token_type": "bearer"}`
- **Input:** `POST /books/` without a valid Authorization header
- **Output:** `401 Unauthorized`

## Learning Objectives
- OAuth2 authentication
- JWT token management
- Password hashing and security
- Protected route implementation
- Authentication middleware
