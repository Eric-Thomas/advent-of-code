import os

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day12-data.txt"
file_path = os.path.join(parent_dir, inputs)

with open(file_path, "r") as fp:
    lines = [line.strip() for line in fp.readlines()]


valid_regions = 0
for line in lines:
    if "x" in line:
        region = line.split(":")[0]
        region_area = int(region.split("x")[0]) * int(region.split("x")[1])
        boxes = sum([int(boxes) for boxes in line.split(":")[1].strip().split()])
        boxes_area = 9 * boxes
        if region_area >= boxes_area:
            valid_regions += 1

print(valid_regions)
