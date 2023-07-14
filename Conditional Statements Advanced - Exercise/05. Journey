budget = float(input())
season = input()

destination = ''
place = ''

if season == "summer":
    if budget <= 100:
        destination = "Bulgaria"
        budget = budget * 0.3
        place = "Camp"
    elif 100 < budget <= 1000:
        destination = "Balkans"
        budget = budget * 0.4
        place = "Camp"
    elif budget > 1000:
        destination = "Europe"
        budget = budget * 0.9
        place = "Hotel"

elif season == "winter":
    place = "Hotel"
    if budget <= 100:
        destination = "Bulgaria"
        budget = budget * 0.7
    elif 100 < budget <= 1000:
        destination = "Balkans"
        budget = budget * 0.8
    elif budget > 1000:
        destination = "Europe"
        budget = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")
