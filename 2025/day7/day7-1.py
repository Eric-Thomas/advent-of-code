import os

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day7-data.txt"
file_path = os.path.join(parent_dir, inputs)

grid = []
with open(file_path, "r") as fp:
    for line in fp:
        grid.append(list(line.strip()))

ROWS = len(grid)
tachyons_indicies = set([grid[0].index("S")])

splits = 0
for row in range(1, ROWS):
    for tachyon in tachyons_indicies.copy():
        if grid[row][tachyon] == "^":
            tachyons_indicies.remove(tachyon)
            tachyons_indicies.add(tachyon - 1)
            tachyons_indicies.add(tachyon + 1)
            splits += 1


print(splits)
