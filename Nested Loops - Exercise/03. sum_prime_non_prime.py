prime = 0
non_prime = 0

while True:
    str_number = input()

    if str_number == "stop":
        break
    else:
        number = int(str_number)

        if number < 0:
            print("Number is negative.")
            
        counter = 0
        
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
                
    if number > 0:
        if counter <= 2:
            prime += number
        else:
            non_prime += number

print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
