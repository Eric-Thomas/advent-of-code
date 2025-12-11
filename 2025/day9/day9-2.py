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

    red_x_min = min(red_x1, red_x2)
    red_x_max = max(red_x1, red_x2)
    red_y_min = min(red_y1, red_y2)
    red_y_max = max(red_y1, red_y2)

    for green_p1, green_p2 in green_lines:
        green_x1, green_y1 = green_p1
        green_x2, green_y2 = green_p2

        green_x_min = min(green_x1, green_x2)
        green_x_max = max(green_x1, green_x2)
        green_y_min = min(green_y1, green_y2)
        green_y_max = max(green_y1, green_y2)

        # Vertical line
        if green_x1 == green_x2:
            if red_x_min < green_x1 < red_x_max:
                if green_y_min < red_y_max and red_y_min < green_y_max:
                    green_line_inside = True
                    break

        # Horizontal line
        elif green_y1 == green_y2:
            if red_y_min < green_y1 < red_y_max:
                if green_x_min < red_x_max and red_x_min < green_x_max:
                    green_line_inside = True
                    break

        else:
            raise Exception(f"Your green line {green_p1, green_p2} is not a straight line")

    if not green_line_inside:
        # Ray cast and check if our rectangle is fully inside or fully outside
        # Check against L shaped green lines
        cast_point = (min(red_x1, red_x2) + 0.5, min(red_y1, red_y2) + 0.5)
        x, y = cast_point
        # Shoot directly up and count how many intersections
        intersections = 0
        for green_p1, green_p2 in green_lines:
            green_x1, green_y1 = green_p1
            green_x2, green_y2 = green_p2

            # We only care about horizontal lines because we are shooting a ray straight up
            # and we offset the point by 0.5 and vertical lines are on whole integer numbers
            if green_y1 == green_y2:
                if min(green_x1, green_x2) <= x <= max(green_x1, green_x2) and y < green_y1:
                    intersections += 1

        # Rectangle fully inside shape
        if intersections % 2 == 1:
            print(f"Largest area {area}")
            break
