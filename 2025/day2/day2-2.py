ranges = []
with open("/Users/eric/Projects/advent-of-code/2025/inputs/day2-data.txt", "r") as fp:
    line = fp.readline()
    for range_id in line.split(","):
        ranges.append([int(range_id.split("-")[0]), int(range_id.split("-")[1])])

ans = 0
invalids = set()
for start, end in ranges:
    for num in range(start, end + 1):
        if num == 1188511885:
            x = 7
        length = len(str(num))
        for i in range(1, 1 + length // 2):
            if length % i == 0:
                invalid = True
                for j in range(1, length // i):
                    start = j * i
                    end = (j * i) + i
                    if str(num)[:i] != str(num)[start:end]:
                        invalid = False
                        break
                if invalid and num not in invalids:
                    print(f"{num} is invalid")
                    ans += num
                    invalids.add(num)
print(ans)
