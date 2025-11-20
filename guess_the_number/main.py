from random import randint

generated_number = randint(0, 10)
guessed_number = int(input("Please guess the number : "))
hasGuessed = False

while hasGuessed == False:
    if guessed_number > generated_number:
        guessed_number = int(input("Too high! Guess again : "))
    elif guessed_number < generated_number:
        guessed_number = int(input("Too low! Guess again : "))
    else:
        hasGuessed = True
        print(f"Yayyyyy.... The number is correct. It is {generated_number}")
