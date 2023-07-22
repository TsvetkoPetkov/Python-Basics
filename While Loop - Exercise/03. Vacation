needed_money = float(input())
owned_money = float(input())

spend_counter = 0
days_counter = 0

while True:
    action = input()
    current_money = float(input())

    if action == "spend":
        spend_counter += 1
        owned_money -= current_money
        days_counter += 1
        if owned_money - current_money < 0:
            owned_money = 0
    elif action == "save":
        spend_counter = 0
        days_counter += 1
        owned_money += current_money

    if spend_counter == 5:
        print("You can't save the money.")
        print(days_counter)
        break

    if owned_money >= needed_money:
        print(f"You saved the money for {days_counter} days.")
        break
