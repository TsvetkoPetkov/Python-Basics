chicken_menues = int(input())
fish_menues = int(input())
veg_menues = int(input())

money_chicken = chicken_menues * 10.35
money_fish = fish_menues * 12.4
money_veg = veg_menues * 8.15

money_for_the_menues = money_veg + money_fish + money_chicken
desert_prise = 0.2 * money_for_the_menues

total_money = money_for_the_menues + desert_prise + 2.5

print(total_money)
