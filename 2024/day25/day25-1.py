keys = []
locks = []

# !!!! NEED TO SET THIS T/F BASED ON FIRST SCHEMATIC INPUT MANUALLY
schematic_is_key = True
prev_line = None
with open("inputs/day25-data.txt", "r") as fp:
    current_schematic = []
    for line in fp:
        if line == "\n":
            prev_line = line
            continue
        if prev_line == "\n":
            if schematic_is_key:
                keys.append(current_schematic)
            else:
                locks.append(current_schematic)
            current_schematic = []
            if line[0] == "#":
                schematic_is_key = False
            elif line[0] == ".":
                schematic_is_key = True

        current_schematic.append(list(line.strip()))
        prev_line = line

    if schematic_is_key:
        keys.append(current_schematic)
    else:
        locks.append(current_schematic)

lock_to_pin_height_needed = {}

for i in range(len(locks)):
    pin_heights = []
    for pin in range(len(locks[i][0])):
        pin_height = 0
        for height in range(len(locks[i]) - 1, 0, -1):
            if locks[i][height][pin] == ".":
                pin_height += 1
        pin_heights.append(pin_height)
    lock_to_pin_height_needed[i] = tuple(pin_heights)


keys_to_pin_heights = {}
for i in range(len(keys)):
    pin_heights = []
    for pin in range(len(keys[i][0])):
        pin_height = 0
        for height in range(len(keys[i])):
            if keys[i][height][pin] == "#":
                pin_height += 1
        pin_heights.append(pin_height)
    keys_to_pin_heights[i] = tuple(pin_heights)


fits = 0
for key_pin_heights in keys_to_pin_heights.values():
    for lock_pin_heights in lock_to_pin_height_needed.values():
        fit = True
        for i in range(len(key_pin_heights)):
            if lock_pin_heights[i] < key_pin_heights[i]:
                fit = False
                break
        if fit:
            print(f"{key_pin_heights} fits in {lock_pin_heights}")
            fits += 1

print(fits)
