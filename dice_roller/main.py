import random

number_of_dice = int(input("How many dice? "))

number_of_sides = int(input("How many sides? "))

rolls = []

for die in range(number_of_dice):
    rolls.append(random.randint(1,number_of_sides))

for i in range(len(rolls)):
    print(f"Roll {i+1} : {rolls[i]}")

print(f"Total : {sum(rolls)}")