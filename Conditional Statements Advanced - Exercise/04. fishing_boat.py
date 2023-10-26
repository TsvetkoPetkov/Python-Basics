budget = int(input())
season = input()
fishermans = int(input())

price = 0

if season == "Spring":
    price = 3000
    if fishermans <= 6:
        price -= price*0.1
    elif 11 >= fishermans > 6:
        price -= price*0.15
    elif fishermans >= 12:
        price -= price * 0.25

    if fishermans % 2 == 0:
        price -= price * 0.05
elif season == "Summer":
    price = 4200
    if fishermans <= 6:
        price -= price * 0.1
    elif 11 >= fishermans > 6:
        price -= price * 0.15
    elif fishermans >= 12:
        price -= price * 0.25

    if fishermans % 2 == 0:
        price -= price * 0.05

elif season == "Autumn":
    price = 4200
    if fishermans <= 6:
        price -= price * 0.1
    elif 11 >= fishermans > 6:
        price -= price * 0.15
    elif fishermans >= 12:
        price -= price * 0.25

elif season == "Winter":
    price = 2600
    if fishermans <= 6:
        price -= price * 0.1
    elif 11 >= fishermans > 6:
        price -= price * 0.15
    elif fishermans >= 12:
        price -= price * 0.25
    if fishermans % 2 == 0:
        price -= price * 0.05

if budget >= price:
    print(f"Yes! You have {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(price - budget):.2f} leva.")
