budget = float(input())
N = int(input())
M = int(input())
P = int(input())

n_sum = N * 250
m_sum = (n_sum * 0.35) * M
p_sum = (n_sum * 0.1) * P

total_sum = n_sum + m_sum + p_sum

if N > M:
   total_sum -= total_sum * 0.15

needed_money = total_sum - budget
money_left = budget - total_sum

if budget >= total_sum:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
