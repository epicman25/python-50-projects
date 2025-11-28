first_number = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
second_number = int(input("Enter second number: "))

def add(num_1,num_2):
    return num_1+num_2


def subtract(num_1,num_2):
    return num_1-num_2

def multiply(num_1,num_2):
    return num_1 * num_2

def divide(num_1,num_2):
    return num_1 / num_2

if operator == "+":
    print(f"The result is : {add(first_number,second_number)}")
elif operator == "-":
    print(f"The result is : {subtract(first_number,second_number)}")
elif operator == "*":
    print(f"The result is : {multiply(first_number,second_number)}")
elif operator == "/":
    print(f"The result is : {divide(first_number,second_number)}")
else:
    print("Invalid operator")
