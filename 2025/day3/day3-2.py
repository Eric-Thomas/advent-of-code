from typing import List

BATTERY_LIMIT = 12

with open("/Users/eric/Projects/advent-of-code/2025/inputs/day3-data.txt", "r") as fp:
    lines = [line.strip() for line in fp.readlines()]

batteries: List[List[str]] = []
for line in lines:
    battery = []
    for joltage in line:
        battery.append(int(joltage))
    batteries.append(battery)

max_joltage = 0
for battery in batteries:
    left = 0
    right = len(battery) - BATTERY_LIMIT + 1
    current_joltage = ""
    while len(current_joltage) < BATTERY_LIMIT:
        current_subarray = battery[left : right + 1]
        current_max = max(battery[left:right])
        left += current_subarray.index(current_max) + 1
        right += 1
        current_joltage += str(current_max)
    print(f"current joltage {current_joltage}")
    max_joltage += int(current_joltage)

print(max_joltage)
