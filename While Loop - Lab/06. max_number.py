import sys

command = input()

max_n = -sys.maxsize
while command != "Stop":
    if command != "Stop":
        int_command = int(command)
        if int_command > max_n:
            max_n = int_command

    command = input()
print(max_n)
