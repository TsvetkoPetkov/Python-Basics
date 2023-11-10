n = int(input())

for i in range(1111, 10000):
    str_i = str(i)
    counter = 0

    for j in str_i:
        number_j = int(j)
        if number_j != 0:
            if n % number_j == 0:
                counter += 1

    if counter == 4 or counter == 5:
        print(str_i, end=" ")
