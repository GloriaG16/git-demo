import os

while True:
    command = input("$ ")

    parts = command.split()

    if not parts:
            continue
    
    if parts[0] == "echo":
        print(" ".join(parts[1:]))

    elif parts[0] == "exit":
        break

    elif parts[0] == "pwd":
        print(os.getcwd())
    
    else:
        print("你输入了：", command)
    