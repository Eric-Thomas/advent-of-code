import os

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day9-data.txt"
file_path = os.path.join(parent_dir, inputs)
red_points = []
with open(file_path, "r") as fp:
    for line in fp.readlines():
        red_points.append(tuple(list(map(int, line.strip().split(",")))))

areas_and_points = []
for i in range(len(red_points)):
    x1, y1 = red_points[i]
    for j in range(i + 1, len(red_points)):
        x2, y2 = red_points[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        areas_and_points.append((area, (x1, y1), (x2, y2)))

areas_and_points.sort(reverse=True)

green_lines = []
for i in range(len(red_points)):
    x1, y1 = red_points[i]
    next_point = i + 1
    if next_point >= len(red_points):
        # Last point connects to first point
        next_point = 0
    x2, y2 = red_points[next_point]

    green_lines.append(((x1, y1), (x2, y2)))

for area, red_p1, red_p2 in areas_and_points:
    red_x1, red_y1 = red_p1
    red_x2, red_y2 = red_p2
    green_line_inside = False
    for green_p1, green_p2 in green_lines:
        green_x1, green_y1 = green_p1
        green_x2, green_y2 = green_p2
        # Vertical line
        if green_x1 == green_x2:
            if min(red_x1, red_x2) < green_x1 < max(red_x1, red_x2) and (
                min(red_y1, red_y2) <= green_y1 <= max(red_y1, red_y2)
                or min(red_y1, red_y2) <= green_y2 <= max(red_y1, red_y2)
            ):
                green_line_inside = True
                break

        # Horizontal line
        elif green_y1 == green_y2:
            if min(red_y1, red_y2) < green_y1 < max(red_y1, red_y2) and (
                min(red_x1, red_x2) <= green_x1 <= max(red_x1, red_x2)
                or min(red_x1, red_x2) <= green_x2 <= max(red_x1, red_x2)
            ):
                green_line_inside = True
                break

        else:
            raise Exception(f"Your green line {green_p1, green_p2} is not a straight line")

    if not green_line_inside:
        print(f"Largest area {area}")
        break
