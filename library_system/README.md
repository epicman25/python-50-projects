# Library Management System

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Implement a library management system using OOP. Create a `Book` class (attributes: title, author, "is_borrowed") and a `Library` class (attributes: a list of Book objects; methods: `add_book()`, `borrow_book()`, `return_book()`, `view_books()`). The `main.py` provides the user menu.

## Possible Folder Structure
```
library_system/
├── main.py     # (CLI menu)
├── library.py  # (Contains Library class)
└── book.py     # (Contains Book class)
```

## Inputs and Expected Outputs
- **Input:** User selects "1" (Add Book), then enters "1984" and "George Orwell"
- **Output:** `Book '1984' added successfully`
- **Input:** User selects "3" (Borrow Book), enters "1984"
- **Output:** `You have borrowed '1984'`

## Learning Objectives
- OOP design patterns
- Class relationships
- Library management logic
- Menu-driven applications
