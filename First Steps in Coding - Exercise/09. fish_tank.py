lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

v_fish_tank = lenght * width * height
liters = v_fish_tank*0.001
percantage = percent/100

needed_liters = liters *(1-percantage)

print(needed_liters)
