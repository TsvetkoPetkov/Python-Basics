width = int(input())
length = int(input())
height = int(input())

total_space = height * width * length

is_done = False

while total_space > 0:
    box = input()

    if box == "Done":
        is_done = True
        print(f"{total_space} Cubic meters left.")
        break
    else:
        total_space -= int(box)

if not is_done:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
