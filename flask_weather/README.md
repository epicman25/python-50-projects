# Flask Weather App

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Combine the skills from projects 25 and 33. Create a Flask web app where a user can type a city name into a form. When the form is submitted, the app's backend calls the weather API (using your `WeatherAPIClient` class), gets the forecast, and then renders an HTML template displaying that forecast.

## Possible Folder Structure
```
flask_weather/
├── main.py
├── client.py        # (The WeatherAPIClient from project 26)
├── templates/
│   ├── index.html
│   └── forecast.html
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** User enters "Tokyo" in an HTML form and clicks "Submit"
- **Output:** A new page `forecast.html` is rendered, showing "Tokyo, JP: 22°C..."

## Learning Objectives
- Integrating APIs with web apps
- Form processing
- Template data passing
- Weather application development
