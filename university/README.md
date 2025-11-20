# University Management System (Inheritance)

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Build a system to model a university, focusing on OOP inheritance. Create a base `Person` class. Then, create `Student` and `Professor` classes that inherit from Person. Student could have attributes like `student_id` and `courses` (a list). Professor could have `employee_id` and `department`.

## Possible Folder Structure
```
university/
├── main.py       # (Creates and prints student/professor objects)
└── models.py     # (Contains Person, Student, Professor classes)
```

## Inputs and Expected Outputs
- **Input:** (In main.py) `s1 = Student("Alice", 123)`, `p1 = Professor("Dr. Bob", 789, "Physics")`
- **Output:** `print(s1.name)` -> Alice, `print(p1.department)` -> Physics

## Learning Objectives
- Inheritance concepts
- Class hierarchies
- Polymorphism
- University system modeling
