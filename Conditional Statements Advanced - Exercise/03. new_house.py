flower = input()
n_flowers = int(input())
budget = int(input())

total_sum = 0

if flower == "Roses":
    total_sum = n_flowers * 5
    if n_flowers > 80:
        total_sum -= total_sum * 0.1
elif flower == "Dahlias":
    total_sum = n_flowers * 3.8
    if n_flowers > 90:
        total_sum -= total_sum * 0.15
elif flower == "Tulips":
    total_sum = n_flowers * 2.8
    if n_flowers > 80:
        total_sum -= total_sum * 0.15
elif flower == "Narcissus":
    total_sum = n_flowers * 3
    if n_flowers < 120:
        total_sum += total_sum * 0.15
elif flower == "Gladiolus":
    total_sum = n_flowers * 2.5
    if n_flowers < 80:
        total_sum += total_sum * 0.2

if budget >= total_sum:
    print(f"Hey, you have a great garden with {n_flowers} {flower} "
          f"and {(budget - total_sum):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(total_sum - budget):.2f} leva more.")
