year_tax = int(input())

basketball_shoes = year_tax - (year_tax*0.4)
basketball_kit = basketball_shoes - (basketball_shoes*0.2)
basket_ball = basketball_kit*0.25
accessories = basket_ball*0.2

total_money = year_tax + basketball_shoes + basketball_kit + basket_ball + accessories
print(total_money)
