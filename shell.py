import os
import subprocess
import shlex

def run_external_command(parts):
    try:
        subprocess.run(parts)
    except FileNotFoundError:
        print("command not found:", parts[0])

while True:
    command = input("$ ")

    try:
        parts = shlex.split(command)
    except ValueError:
        print("命令格式有误，请检查引号")
        continue

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
        run_external_command(parts)