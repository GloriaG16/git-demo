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
            print("cd: 请提供目录名称")
            continue

        try:
            os.chdir(parts[1])
        except OSError:
            print("cd: 无法进入这个目录")

    else:
        try:
            subprocess.run(parts)
        except FileNotFoundError:
            print("command not found")