number_of_lines = int(input("Enter number of lines in the text file : "))

with open(f'text_generator/{number_of_lines}_lines.txt','w') as output_file:
    for i in range(1, number_of_lines+1):
        output_file.write(f'This is line {i} \n')