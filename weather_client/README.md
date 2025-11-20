# API Client Wrapper (OOP + API)

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Build on the previous project by creating an OOP wrapper for the API. Create a `WeatherAPIClient` class. The class should be initialized with an API key. It should have methods like `get_forecast(city)` that handle the requests call and JSON parsing internally. This abstracts the API logic, making it reusable.

## Possible Folder Structure
```
weather_client/
├── main.py         # (Imports and uses the client)
├── client.py       # (Contains WeatherAPIClient class)
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** (In main.py) `client = WeatherAPIClient(api_key)`, `forecast = client.get_forecast("Tokyo")`
- **Output:** `print(forecast)` -> `Tokyo, JP: 22°C, Clear Sky`

## Learning Objectives
- API wrapper design
- Class-based API clients
- Code abstraction
- Reusable components
