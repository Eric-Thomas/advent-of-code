fresh_ranges = []
with open("inputs/day5-data.txt", "r") as fp:
    line = fp.readline()
    while line != "\n":
        beginning, end = line.split("-")
        fresh_ranges.append((int(beginning), int(end)))
        line = fp.readline()

fresh_ranges.sort(key=lambda x: x[0])
fresh_total = 0

left, right = fresh_ranges[0]
for new_left, new_right in fresh_ranges[1:]:
    if new_left <= right:
        right = max(right, new_right)
    else:
        fresh_total += (right - left) + 1
        left = new_left
        right = new_right

fresh_total += (right - left) + 1

print(fresh_total)
