steps_sum = 0

while steps_sum < 10000:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        steps_sum += steps
        break
    else:
        steps_sum += int(steps)

if steps_sum >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps_sum - 10000} steps over the goal!")
else:
    print(f"{10000 - steps_sum} more steps to reach goal.")
