with open("inputs/day1-data.txt", "r") as fp:
    rotations = [line.strip() for line in fp.readlines()]

current_number = 50
password = 0

for rotation in rotations:
    direction = rotation[0]
    amount = int(rotation[1:])
    if direction == "R":
        current_number = (current_number + amount) % 100
    else:
        current_number = (current_number - amount) % 100

    if current_number == 0:
        password += 1

print(f"password: {password}")
