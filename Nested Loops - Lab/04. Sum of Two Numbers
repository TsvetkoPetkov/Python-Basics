beginning = int(input())
end = int(input())
magical_number = int(input())

combinations = 0
is_found = False

for i in range(beginning, end+1):
    for j in range(beginning, end+1):
        combinations += 1
        if i + j == magical_number:
            is_found = True
            print(f"Combination N:{combinations} ({i} + {j} = {magical_number})")
            break
    if is_found:
        break

if not is_found:
    print(f"{combinations} combinations - neither equals {magical_number}")
