# Simple Banking System

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Create a command-line banking system using OOP principles. You will create a `Client` class (with attributes like name, account number, balance, and methods like `deposit()`, `withdraw()`, `check_balance()`) and a `Bank` class that manages a dictionary of Client objects. The `main.py` file will run the CLI menu to interact with the bank.

## Possible Folder Structure
```
banking_system/
├── main.py     # (Runs the CLI menu, instantiates Bank)
├── bank.py     # (Contains the Bank class)
└── client.py   # (Contains the Client class)
```

## Inputs and Expected Outputs
- **Input:** CLI commands: `create_account John`, `deposit John 100`, `balance John`
- **Output:** `Account created.`, `Deposited $100.`, `Current Balance: $100`

## Learning Objectives
- Object-Oriented Programming (OOP)
- Class design and implementation
- Banking system logic
- Multi-file project structure
