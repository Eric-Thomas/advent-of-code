grid = []
with open("inputs/day4-data.txt", "r") as fp:
    for line in fp:
        grid.append(list(line.strip()))

ROWS = len(grid)
COLUMNS = len(grid[0])


DIRECTIONS = [(-1, -1), (-1, 0), (1, 0), (1, 1), (-1, 1), (1, -1), (0, 1), (0, -1)]


total_rolls = 0
while True:
    prev_total = total_rolls
    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == "@":
                adjacent = 0
                for direction in DIRECTIONS:
                    row_change, column_change = direction
                    new_row = row + row_change
                    new_column = column + column_change
                    if 0 <= new_row < ROWS and 0 <= new_column < COLUMNS and grid[new_row][new_column] == "@":
                        adjacent += 1
                        if adjacent >= 4:
                            break
                if adjacent < 4:
                    total_rolls += 1
                    grid[row][column] = "."
    if total_rolls == prev_total:
        break

print(total_rolls)
