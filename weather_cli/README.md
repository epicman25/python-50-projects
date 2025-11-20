# CLI Weather App

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Create a command-line tool that fetches and displays the weather for a user-specified city. This requires using the `requests` library to call a free weather API (like OpenWeatherMap), parsing the JSON response, and printing a formatted, human-readable forecast. This project teaches API keys (using `.env` files), JSON parsing, and HTTP error handling.

## Possible Folder Structure
```
weather_cli/
├── main.py
├── requirements.txt
└── .env
```

## Inputs and Expected Outputs
- **Input:** `python main.py "London"`
- **Output:** `London, UK: 15°C, Light Rain`

## Learning Objectives
- API integration
- HTTP requests
- JSON parsing
- Environment variables
- Error handling
