ranges = []
with open("inputs/day2-data.txt", "r") as fp:
    line = fp.readline()
    for range_id in line.split(","):
        ranges.append([int(range_id.split("-")[0]), int(range_id.split("-")[1])])

ans = 0
for start, end in ranges:
    for num in range(start, end + 1):
        length = len(str(num))
        if str(num)[: length // 2] == str(num)[length // 2 :]:
            print(f"{num} is invalid")
            ans += num
print(ans)
