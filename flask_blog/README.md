# Basic Flask Web App

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Build a simple "microblog" with Flask. Create a `main.py` that runs the app. It should have at least two routes: `/` (the main page, which shows posts) and `/add` (a page with a form to add a new post). For this intermediate project, the posts can be stored in a simple global list.

## Possible Folder Structure
```
flask_blog/
├── main.py
├── templates/
│   ├── index.html
│   └── add_post.html
├── static/
│   └── style.css
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** User navigates to `http://127.0.0.1:5000/add` and submits a form
- **Output:** The user is redirected to `/`, which now displays the new post

## Learning Objectives
- Web development with Flask
- Template rendering
- Form handling
- Routing concepts
