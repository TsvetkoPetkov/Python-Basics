age = int(input())
washing_machine = float(input())
price_doll = int(input())

dolls = 0
even_money = 0
total_even_sum = 0

for i in range(1, age+1):
    if i % 2 == 1:
        dolls += 1
    elif i % 2 == 0:
        even_money += 10
        total_even_sum += even_money
        total_even_sum = total_even_sum - 1

dolls_money = dolls * price_doll
total_money = total_even_sum + dolls_money

if washing_machine <= total_money:
    print(f"Yes! {(total_money - washing_machine):.2f}")
else:
    print(f"No! {abs(washing_machine - total_money):.2f}")
