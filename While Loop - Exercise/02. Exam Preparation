bad_grades = int(input())

task = input()

counter = 0

total_grades_counter = 0
total_sum = 0
is_not_good = False
last_task = ''

while task != 'Enough':
    grade = int(input())

    if grade <= 4:
        counter += 1

    if counter >= bad_grades:
        is_not_good = True
        print(f"You need a break, {counter} poor grades.")
        break

    total_grades_counter += 1
    total_sum += grade
    last_task = task
    task = input()


if not is_not_good:
    print(f"Average score: {(total_sum/total_grades_counter):.2f}")
    print(f"Number of problems: {total_grades_counter}")
    print(f"Last problem: {last_task}")
