# Detecting Fake News

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
Implement the "Detecting Fake News" project, a text classification task. The project must use `TfidfVectorizer` (for feature extraction from text) and `PassiveAggressiveClassifier` (a specific online learning algorithm), as specified in the source repository. This forces you to learn these specific scikit-learn components.

## Possible Folder Structure
```
detecting_fake_news/
├── data/
│   ├── raw/         # (Original news.csv)
│   ├── processed/   # (Cleaned data)
├── notebooks/
│   └── fake_news_detection.ipynb
├── reports/
│   └── figures/     # (Classification report, confusion matrix)
├── src/
│   ├── __init__.py
│   ├── data.py      # (Data processing)
│   └── model.py     # (Model training)
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** `data/raw/news.csv` (with "text" and "label" columns)
- **Output:** A classification report (precision, recall, F1-score) and a confusion matrix saved in `reports/figures/`

## Learning Objectives
- Text classification techniques
- TF-IDF vectorization
- PassiveAggressiveClassifier usage
- Natural language processing
- Fake news detection algorithms
