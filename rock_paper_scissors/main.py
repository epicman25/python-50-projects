import random

RPS = ["rock","paper","scissors"]

user_guess = input("Enter your choice (rock, paper, scissors):")

if user_guess in RPS:
    system_guess = random.choices(RPS,weights=[0.3,0.3,0.7],k=1)[0]
    print(f"System guess is .......... : {str(system_guess)}")
    if system_guess == user_guess:
        print("Draw ----- Try Again")
    elif system_guess == "rock" and user_guess == "scissors" :
        print("Yayyyyy....... System wins")
    elif system_guess == "scissors" and user_guess == "paper" :
        print("Yayyyyy....... System wins")
    elif system_guess == "paper" and user_guess == "rock" :
        print("Yayyyyy....... System wins")
    elif user_guess == "rock" and system_guess == "scissors" :
        print("HeHeHe ...... This time you WIN")
    elif user_guess == "scissors" and system_guess == "paper" :
        print("HeHeHe ...... This time you WIN")
    elif user_guess == "paper" and system_guess == "rock" :
        print("HeHeHe ...... This time you WIN")


