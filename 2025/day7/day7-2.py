import os
from functools import lru_cache

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day7-data.txt"
file_path = os.path.join(parent_dir, inputs)

grid = []
with open(file_path, "r") as fp:
    for line in fp:
        grid.append(list(line.strip()))

ROWS = len(grid)


@lru_cache(maxsize=None)
def calculate_splits(tachyon, starting_row):
    for row in range(starting_row, ROWS):
        if grid[row][tachyon] == "^":
            return calculate_splits(tachyon - 1, row + 1) + calculate_splits(tachyon + 1, row + 1)

    return 1


print(calculate_splits(grid[0].index("S"), 1))
