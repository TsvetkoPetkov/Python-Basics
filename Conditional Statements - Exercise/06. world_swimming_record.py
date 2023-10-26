from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_a_meter = float(input())

time = distance_in_meters * time_in_seconds_for_a_meter
t = distance_in_meters/15
t = floor(t)
plus_time = t * 12.5
total_time = time + plus_time

more_seconds_needed = total_time - record_in_seconds

if record_in_seconds > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {more_seconds_needed:.2f} seconds slower.")
