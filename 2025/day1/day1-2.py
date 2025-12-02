with open("inputs/day1-data.txt", "r") as fp:
    rotations = [line.strip() for line in fp.readlines()]

current_number = 50
points_at_0_count = 0

for rotation in rotations:
    # print(f"Pointing at {current_number}")
    # print(f"rotation {rotation}")
    if rotation[0] == "R":
        for i in range(int(rotation[1:])):
            current_number += 1
            if current_number == 100:
                current_number = 0
                points_at_0_count += 1
    else:
        for i in range(int(rotation[1:])):
            current_number -= 1
            if current_number == 0:
                # print("pointing at 0 going left")
                points_at_0_count += 1
            if current_number == -1:
                current_number = 99

print(f"password: {points_at_0_count}")
