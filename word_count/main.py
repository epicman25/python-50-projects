

with open("word_count/input.txt") as f:
    input_lines = f.readlines()

word_counter = {}

for line in input_lines:
    line = line.replace('\n',"")
    line = line.replace(".","")
    line = line.replace(",","")
    for word in line.split(" "):
        try:
            word_counter[word] +=1
        except:
            word_counter[word] = 1

for  values in word_counter:
    print(f"{values} : {word_counter[values]}")

print(f"Total word count is  : {sum(word_counter.values())}")
