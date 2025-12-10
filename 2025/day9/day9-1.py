import os

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day9-data.txt"
file_path = os.path.join(parent_dir, inputs)
points = []
with open(file_path, "r") as fp:
    for line in fp.readlines():
        points.append(tuple(list(map(int, line.strip().split(",")))))

largest_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
        largest_area = max(largest_area, area)

print(largest_area)
