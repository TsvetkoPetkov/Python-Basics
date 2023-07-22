name = input()

cl = 1

counter = 0
grade_sum = 0

while cl <= 12:
    grade = float(input())
    if grade < 4.00:
        counter += 1
    elif grade >= 4.00:
        grade_sum += grade
        cl += 1
    if counter == 2:
        break


if counter == 2:
    print(f"{name} has been excluded at {cl} grade")
else:
    print(f"{name} graduated. Average grade: {(grade_sum/12):.2f}")
