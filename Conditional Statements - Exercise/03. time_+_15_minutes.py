hours = int(input())
minutes = int(input())

real_hours = hours * 60
time = real_hours + minutes + 15

hours_plus_fifteen = time // 60
minutes_plus_fifteen = time % 60

if hours_plus_fifteen > 23:
    hours_plus_fifteen = 0

if minutes_plus_fifteen < 10:
    print(f"{hours_plus_fifteen}:0{minutes_plus_fifteen}")
else:
    print(f"{hours_plus_fifteen}:{minutes_plus_fifteen}")
