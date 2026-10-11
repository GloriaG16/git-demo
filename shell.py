import os
import subprocess

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

    elif parts[0] == "cd":

        if len(parts) < 2:
            continue
        
        os.chdir(parts[1])

    else:
        try:
            subprocess.run(parts)
        except FileNotFoundError:
            print("command not found")