import math

tournaments = int(input())
beggining_points = int(input())

average = 0
wins = 0

for i in range(1, tournaments+1):
    level = input()

    if level == "W":
        beggining_points += 2000
        average += 2000
        wins += 1
    elif level == "F":
        beggining_points += 1200
        average += 1200
    elif level == "SF":
        beggining_points += 720
        average += 720

pr_average = average / tournaments
percent_wins = wins / tournaments * 100

print(f"Final points: {beggining_points}")
print(f"Average points: {math.floor(pr_average)}")
print(f"{percent_wins:.2f}%")
