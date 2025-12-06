import os

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day6-data.txt"
file_path = os.path.join(parent_dir, inputs)
with open(file_path, "r") as fp:
    lines = [line.strip().split() for line in fp.readlines()]

ROWS = len(lines)
COLUMNS = len(lines[0])

total = 0
for col in range(COLUMNS):
    current_total = int(lines[0][col])
    for row in range(1, ROWS - 1):
        operator = lines[-1][col]
        if operator == "+":
            current_total += int(lines[row][col])
        elif operator == "*":
            current_total *= int(lines[row][col])
        else:
            raise ValueError()
    total += current_total

print(total)
