from math import pi
figure_type = input()


if figure_type == "square":
    side = float(input())
    S = side * side
elif figure_type == "rectangle":
    side_A = float(input())
    side_B = float(input())
    S = side_A * side_B
elif figure_type == "circle":
    radius = float(input())
    S = pi*radius*radius
elif figure_type == "triangle":
    tr_side = float(input())
    height = float(input())
    S = (tr_side * height) / 2

print(f"{S:.3f}")
