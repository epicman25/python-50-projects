# Hangman (Simple)

**Difficulty Level:** Beginner (Est. 1 Hour)

## Project Description
A simplified version of Hangman. The script has a single, hard-coded secret word. The user guesses letters. The script shows the "hanged man" (using ASCII art for each wrong guess) and the word with correctly guessed letters filled in (`_ _ T _ _`). The game ends on a win or loss.

## Possible Folder Structure
```
hangman/
└── main.py
```

## Inputs and Expected Outputs
- **Input:** `Secret word is: _ _ _ _ _`, `Guess a letter: e`
- **Output:** `_ e _ _ e`, `You have 5 lives left`

## Learning Objectives
- Game logic implementation
- ASCII art display
- Letter tracking
- Win/loss conditions
