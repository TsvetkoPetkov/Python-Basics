city = input()
sales = float(input())
result = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        result = 0.05 * sales
        print(f"{result:.2f}")
    elif 500 < sales <= 1000:
        result = 0.07 * sales
        print(f"{result:.2f}")
    elif 1000 < sales <= 10000:
        result = 0.08 * sales
        print(f"{result:.2f}")
    elif sales > 10000:
        result = 0.12 * sales
        print(f"{result:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        result = 0.045 * sales
        print(f"{result:.2f}")
    elif 500 < sales <= 1000:
        result = 0.075 * sales
        print(f"{result:.2f}")
    elif 1000 < sales <= 10000:
        result = 0.1 * sales
        print(f"{result:.2f}")
    elif sales > 10000:
        result = 0.13 * sales
        print(f"{result:.2f}")
    else:
        print("error")

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        result = 0.055 * sales
        print(f"{result:.2f}")
    elif 500 < sales <= 1000:
        result = 0.08 * sales
        print(f"{result:.2f}")
    elif 1000 < sales <= 10000:
        result = 0.12 * sales
        print(f"{result:.2f}")
    elif sales > 10000:
        result = 0.145 * sales
        print(f"{result:.2f}")
    else:
        print("error")
else:
    print("error")
