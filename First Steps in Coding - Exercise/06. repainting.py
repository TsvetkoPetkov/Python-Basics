nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())


nylon_sum = (nylon + 2)*1.5
paint_sum = (paint + paint*10/100) * 14.5
thinner_sum = thinner * 5

sum_for_materials = nylon_sum + paint_sum + thinner_sum + 0.4
money_for_workers = (sum_for_materials * 30/100) * hours
total_sum = sum_for_materials + money_for_workers

print(total_sum)
