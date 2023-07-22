floors = int(input())
rooms = int(input())

for curr_floors in range(floors, 0, -1):
    for curr_rooms in range(0, rooms):
        if curr_floors == floors:
            print(f"L{curr_floors}{curr_rooms}", end=" ")
        elif curr_floors % 2 == 0:
            print(f"O{curr_floors}{curr_rooms}", end=" ")
        elif curr_floors % 2 == 1:
            print(f"A{curr_floors}{curr_rooms}", end=" ")

    print()
