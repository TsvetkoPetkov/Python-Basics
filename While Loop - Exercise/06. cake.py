length = int(input())
width = int(input())

total_pieces = length * width
is_stop = False

while total_pieces > 0:
    curr_pieces = input()

    if curr_pieces == "STOP":
        is_stop = True
        print(f"{total_pieces} pieces are left.")
        break
    else:
        total_pieces -= int(curr_pieces)


if not is_stop:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
