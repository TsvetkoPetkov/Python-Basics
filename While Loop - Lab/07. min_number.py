import sys

command = input()

min_n = sys.maxsize
while command != "Stop":
    if command != "Stop":
        int_command = int(command)
        if int_command < min_n:
            min_n = int_command

    command = input()
print(min_n)
