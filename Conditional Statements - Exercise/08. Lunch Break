from math import ceil
film_name = input()
film_continuation = int(input())
rest_continuation = int(input())

lunch_time = (1/8) * rest_continuation
relax_time = (1/4) * rest_continuation

remaining_time = rest_continuation - lunch_time - relax_time

needed_time = film_continuation - remaining_time
time_left = remaining_time - film_continuation

if film_continuation > remaining_time:
    print(f"You don't have enough time to watch {film_name}, "
          f"you need {ceil(needed_time)} more minutes.")
else:
    print(f"You have enough time to watch {film_name} and left "
          f"with {ceil(time_left)} minutes free time.")
