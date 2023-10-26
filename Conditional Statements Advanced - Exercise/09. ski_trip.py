days = int(input())
place = input()
grade = input()

total_sum = 0

if place == "room for one person":
    total_sum = (days-1) * 18
elif place == "apartment":
    total_sum = (days-1) * 25
    if days < 10:
        total_sum -= total_sum * 0.3
    elif 10 <= days <= 15:
        total_sum -= total_sum * 0.35
    elif days > 15:
        total_sum -= total_sum * 0.5
elif place == "president apartment":
    total_sum = (days-1) * 35
    if days < 10:
        total_sum -= total_sum * 0.1
    elif 10 <= days <= 15:
        total_sum -= total_sum * 0.15
    elif days > 15:
        total_sum -= total_sum * 0.2

if grade == "positive":
    total_sum += total_sum * 0.25
elif grade == "negative":
    total_sum -= total_sum * 0.1

print(f"{total_sum:.2f}")
