fresh_ranges = []
fresh_id_count = 0
with open("inputs/day5-data.txt", "r") as fp:
    line = fp.readline()
    while line != "\n":
        beginning, end = line.split("-")
        fresh_ranges.append((int(beginning), int(end)))
        line = fp.readline()

    line = fp.readline()
    while line:
        fresh = False
        for range in fresh_ranges:
            if int(line) <= range[1] and int(line) >= range[0]:
                fresh = True
                break

        if fresh:
            fresh_id_count += 1
        line = fp.readline()

print(fresh_id_count)
