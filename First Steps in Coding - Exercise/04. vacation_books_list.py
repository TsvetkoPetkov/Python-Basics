number_of_pages = int(input())
pages_per_hour = int(input())
needed_days = int(input())

total_time_for_reading = number_of_pages//pages_per_hour

time_per_day = total_time_for_reading//needed_days

print(time_per_day)
