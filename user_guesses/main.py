from random import randint

start_range = int(input("Enter the starting range for the number : "))
end_range = int(input("Enter the ending range for the number : "))


num_list = [i for i in range(start_range,end_range+1)]

low_pointer = 0
high_pointer = len(num_list)-1


mid_pointer = (low_pointer + high_pointer)//2
guessed_number = num_list[mid_pointer]

userinput = 'w'

while userinput != 'c':
    userinput = input(f"Is your number {guessed_number}? (h|l|c) : ")
    if userinput == 'l': 
        high_pointer = mid_pointer-1
        mid_pointer = (low_pointer + high_pointer)//2
        guessed_number = num_list[mid_pointer]
    elif userinput == 'h':
        low_pointer = mid_pointer+1
        mid_pointer = (low_pointer + high_pointer)//2
        guessed_number = num_list[mid_pointer]
    
print(f"Yayyyyyyy the number you thought of is : {guessed_number}")
    
