n_groups = int(input())

people_sum = 0

musala_people = 0
monblan_people = 0
kilimandjaro_people = 0
k2_people = 0
everest_people = 0

for i in range(1, n_groups+1):
    group = int(input())
    
    if group <= 5:
        musala_people += group
        people_sum += group
    elif 6 <= group <= 12:
        monblan_people += group
        people_sum += group
    elif 13 <= group <= 25:
        kilimandjaro_people += group
        people_sum += group
    elif 26 <= group <= 40:
        k2_people += group
        people_sum += group
    elif group >= 41:
        everest_people += group
        people_sum += group

musala_percent = musala_people / people_sum * 100
monblan_percent = monblan_people / people_sum * 100
kilimandjaro_percent = kilimandjaro_people / people_sum * 100
k2_percent = k2_people / people_sum * 100
everest_percent = everest_people / people_sum * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
