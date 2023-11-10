number_one = int(input())
number_two = int(input())


for i in range(number_one, number_two+1):
    str_num = str(i)
    even_sum = 0
    odd_sum = 0
    
    for j in range(len(str_num)):
        if j % 2 == 0:
            even_sum += int(str_num[j])
        else:
            odd_sum += int(str_num[j])

    if even_sum == odd_sum:
        print(int(str_num), end=" ")
