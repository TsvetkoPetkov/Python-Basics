n = int(input())

p1 = 0
p1_numbers = 0
p2 = 0
p2_numbers = 0
p3 = 0
p3_numbers = 0
p4 = 0
p4_numbers = 0
p5 = 0
p5_numbers = 0

for i in range(1, n+1):
    number = int(input())
    if number < 200:
        p1_numbers += 1
        p1 = p1_numbers / n * 100
    elif 200 <= number <= 399:
        p2_numbers += 1
        p2 = p2_numbers / n * 100
    elif 400 <= number <= 599:
        p3_numbers += 1
        p3 = p3_numbers / n * 100
    elif 600 <= number <= 799:
        p4_numbers += 1
        p4 = p4_numbers / n * 100
    elif number >= 800:
        p5_numbers += 1
        p5 = p5_numbers / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
