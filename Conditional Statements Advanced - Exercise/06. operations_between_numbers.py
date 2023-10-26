n1 = int(input())
n2 = int(input())
operator = input()

if operator == '+':
    even_or_odd = ''
    if (n1 + n2) % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{n1} + {n2} = {n1 + n2} - {even_or_odd}')

elif operator == '-':
    even_or_odd = ''
    if (n1 - n2) % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{n1} - {n2} = {n1 - n2} - {even_or_odd}')

elif operator == '*':
    even_or_odd = ''
    if (n1 * n2) % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    print(f'{n1} * {n2} = {n1 * n2} - {even_or_odd}')

elif operator == '/':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f'{n1} / {n2} = {(n1 / n2):.2f}')

elif operator == '%':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f'{n1} % {n2} = {n1 % n2}')
