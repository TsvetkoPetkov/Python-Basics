film_budget = float(input())
number_of_statists = int(input())
clothes_for_one_statist = float(input())

decor = 0.1 * film_budget
price_for_clothes = number_of_statists * clothes_for_one_statist

if number_of_statists > 150:
    price_for_clothes -= price_for_clothes * 0.1

total_price = decor + price_for_clothes

money_left = film_budget - total_price
needed_money = total_price - film_budget

if film_budget < total_price:
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
