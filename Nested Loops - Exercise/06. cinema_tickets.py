command = input()

student_counter = 0
standard_counter = 0
kid_counter = 0
total_counter = 0

while command != "Finish":
    film_name = command
    empty_places = int(input())

    t_ticket = input()
    places_per_film = 0

    while t_ticket != "End":
        ticket_type = t_ticket
        places_per_film += 1

        if ticket_type == "student":
            student_counter += 1
            total_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
            total_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1
            total_counter += 1

        if places_per_film == empty_places:
            break

        t_ticket = input()

    command = input()
    print(f"{film_name} - {((places_per_film / empty_places) * 100):.2f}% full.")

print(f"Total tickets: {total_counter}")
print(f"{(student_counter / total_counter)*100:.2f}% student tickets.")
print(f"{(standard_counter / total_counter)*100:.2f}% standard tickets.")
print(f"{(kid_counter / total_counter)*100:.2f}% kids tickets.")
