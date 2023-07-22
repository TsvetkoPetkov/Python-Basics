n_juri = int(input())

pres_name = input()
total_sum = 0
count_pres = 0

while pres_name != "Finish":
    t_sum = 0
    average_sum = 0
    for i in range(n_juri):
        grade = float(input())
        t_sum += grade
        average_sum = t_sum / n_juri
        total_sum += grade

    print(f"{pres_name} - {average_sum:.2f}.")
    count_pres += 1
    pres_name = input()
    if pres_name == "Finish":
        print(f"Student's final assessment is {(total_sum/(count_pres*n_juri)):.2f}.")
