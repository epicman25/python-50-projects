# Laptop Price Predictor

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
Build an end-to-end regression model to predict laptop prices. Use the `cookiecutter-data-science` structure. This involves loading the data, extensive feature engineering (e.g., one-hot encoding for "Company," extracting numbers from "Ram"), training a model (RandomForestRegressor or XGBoost), and evaluating it using Root Mean Squared Error (RMSE).

## Possible Folder Structure
```
laptop_price_predictor/
├── data/
│   ├── raw/         # (Original laptops.csv)
│   ├── processed/   # (Cleaned data.csv)
├── notebooks/
│   └── model.ipynb  # (Model training notebook)
├── models/
│   └── laptop_price_regressor.joblib
├── src/
│   ├── __init__.py
│   ├── data.py      # (Data processing)
│   └── features.py  # (Feature engineering)
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** `data/raw/laptops.csv`
- **Output:** A `models/laptop_price_regressor.joblib` file and a `notebooks/` file reporting the final Test RMSE

## Learning Objectives
- End-to-end ML pipeline
- Feature engineering techniques
- Regression model training
- Model evaluation metrics
- Professional ML project structure
