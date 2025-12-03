import base64
import random

word_list = [
    "YXBwbGU=",
    "Y2hhaXI=",
    "bGlnaHQ=",
    "c3Rvcm0=",
    "cGxhbnQ=",
    "YnJpY2s=",
    "dHJlbmQ=",
    "ZmxhbWU=",
    "b2NlYW4=",
    "c291bmQ="
]

guess_word = random.choices(word_list)
secret_word = base64.b64decode(guess_word[0]).decode('utf-8')
print(secret_word)

HANGMANPICS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]


guessed_letters = []

number_of_lives = len(HANGMANPICS)-1

suspese_word = ["_"] * len(secret_word)
print(" ".join(suspese_word))

while number_of_lives >= 0 or "_" in suspese_word:
    print(HANGMANPICS[len(HANGMANPICS)-1-number_of_lives])
    guess_letter = input("Guess the letter : ").lower()

    if guess_letter in guessed_letters:
        print("Already guessed")
        continue

    guessed_letters.append(guess_letter)

    if guess_letter in secret_word:
        for i,letter in enumerate(secret_word):
            if letter == guess_letter:
                suspese_word[i] = guess_letter
        print(" ".join(suspese_word))
    else:
        number_of_lives-=1
        print("Wrong!!!")

    if "_" not in suspese_word:
        print(f"You Win! The word was: {secret_word}")
        break

if "_" in suspese_word:
        print(f"You Lost! The word was: {secret_word}")


