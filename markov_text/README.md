# Markov Chain Text Composer

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Create a script that generates new text in the style of an original author. The script reads a large text file (e.g., a public domain book), builds a Markov chain model (a dictionary where keys are words and values are a list of words that follow), and then generates new sentences by "walking" the chain.

## Possible Folder Structure
```
markov_text/
├── main.py
└── corpus.txt
```

## Inputs and Expected Outputs
- **Input:** `corpus.txt` (e.g., the text of "Alice in Wonderland")
- **Output:** A paragraph of semi-coherent, computer-generated text, e.g., "Alice said to the Caterpillar, who was sitting on the table, and the Queen..."

## Learning Objectives
- Markov chain algorithms
- Text generation techniques
- Natural language processing basics
- Statistical text modeling
