import random

password_length = int(input("Enter password length: "))

password = []

for i in range(password_length):
    password.append(chr(random.randint(33,127)))

print(f"Your new password is: {"".join(password)}")