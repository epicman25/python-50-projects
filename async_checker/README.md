# Asynchronous URL Checker

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
Master asynchronous programming, a key topic in advanced Python. Write a script to check the HTTP status of 100 URLs from a text file. First, write it sequentially using `requests`. Second, rewrite it concurrently using `asyncio` and `httpx`. The goal is to compare the total execution time and understand the power of async.

## Possible Folder Structure
```
async_checker/
├── main.py
├── urls.txt
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** `urls.txt` (containing 100 URLs)
- **Output:** A printout: `Checked 100 URLs (Sequential) in 15.2s.`, `Checked 100 URLs (Async) in 1.1s.`

## Learning Objectives
- Asynchronous programming concepts
- asyncio and httpx libraries
- Performance optimization
- Concurrent programming
- Advanced Python concepts
