with open("find_replace/input.txt") as input_f:
    input_lines = input_f.readlines()

# word_to_replaced = input("Find : ")

# word_to_replaced_with = input("Replace : ")

word_to_replaced = "thought"

word_to_replaced_with = "think"



with open("find_replace/output.txt", "w+") as output_f:
    for line in input_lines:
        modified_line = line.replace(word_to_replaced,word_to_replaced_with)
        output_f.writelines(modified_line)



