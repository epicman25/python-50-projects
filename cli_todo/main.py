tasks = []

print("Simple TODO list")
print("==================")
print("Available commands : add <task>, view, remove <number>, quit")
while True:
    command = input("> ").strip()
    if command == "quit":
        print("Good Byeeeeeee")
        break

    elif command.lower() == "view":
        if len(tasks) == 0:
            print("No tasks found")
        else:
            for i,task in enumerate(tasks, start=1):
                print(f"{i} : {task}")

    elif command.split(" ")[0] == "add":
        task = command[4:].strip()
        tasks.append(task)
        print(f"Added {task}")
    
    elif command.split()[0] == "remove":
        task_index = command[7:].strip()
        if task_index.isdigit() == True:
            index = int(task_index)-1
            if 0 <= index < len(tasks):
                removed_task = tasks[index]
                tasks.pop(index)
                print(f"Removed : {removed_task}")
            else:
                print("The task number out of range")
        else:
            print("Please provide a valid task number")


    else:
        print("Unknown command : Try: add <task>, view, remove <number>, quit")
        

