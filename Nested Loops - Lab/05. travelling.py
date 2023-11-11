destination = input()

while destination != "End":
    budget = float(input())
    total = 0
    while budget > total:
        curr_money = float(input())
        total += curr_money

        if total >= budget:
            print(f"Going to {destination}!")

    destination = input()
