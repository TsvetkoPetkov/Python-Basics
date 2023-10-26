exam_hour = int(input())
exam_minutes = int(input())
arriving_hour = int(input())
arriving_minutes = int(input())

total_exam_time = (exam_hour * 60) + exam_minutes
total_arriving_time = (arriving_hour * 60) + arriving_minutes

difference = abs(total_exam_time - total_arriving_time)

if total_arriving_time > total_exam_time:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hour = difference // 60
        minutes = difference % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")

elif total_arriving_time == total_exam_time:
    print("On time")
elif total_arriving_time >= (total_exam_time - 30):
    print("On time")
    print(f"{difference} minutes before the start")

elif abs(total_arriving_time - total_exam_time) > 30:
    print("Early")
    if difference < 60:
        print(f"{difference} minutes before the start")
    else:
        hour = difference // 60
        minutes = difference % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")
