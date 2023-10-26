month = input()
nights = int(input())

studio_sum = 0
apartment_sum = 0

if month == "May" or month == "October":
    studio_sum = nights * 50
    apartment_sum = nights * 65
    if 14 > nights > 7:
        studio_sum -= studio_sum * 0.05
    elif nights > 14:
        studio_sum -= studio_sum * 0.3
elif month == "June" or month == "September":
    studio_sum = nights * 75.2
    apartment_sum = nights * 68.7
    if nights > 14:
        studio_sum -= studio_sum * 0.2
elif month == "July" or month == "August":
    studio_sum = nights * 76
    apartment_sum = nights * 77

if nights > 14:
    apartment_sum -= apartment_sum * 0.1

print(f"Apartment: {apartment_sum:.2f} lv.")
print(f"Studio: {studio_sum:.2f} lv.")
