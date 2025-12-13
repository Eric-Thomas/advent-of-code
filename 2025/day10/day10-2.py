import os

from z3 import Ints, Optimize, sat

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day10-data.txt"
file_path = os.path.join(parent_dir, inputs)

with open(file_path, "r") as fp:
    machines = [line.strip().split()[1:] for line in fp.readlines()]

for machine in machines:
    joltage_levels = machine[-1].replace("{", "")
    joltage_levels = joltage_levels.replace("}", "")
    joltage_levels = list(map(int, joltage_levels.split(",")))
    machine[-1] = joltage_levels
    for i in range(len(machine) - 1):
        lights = [0 for _ in range(len(joltage_levels))]
        buttons_str = machine[i]
        buttons_str = buttons_str.replace("(", "")
        buttons_str = buttons_str.replace(")", "")
        buttons = tuple(map(int, buttons_str.split(",")))
        for light_index in buttons:
            lights[light_index] = 1
        machine[i] = lights

total_presses = 0
for machine in machines:
    num_buttons = len(machine) - 1
    coefficients_str = [f"x{i}" for i in range(num_buttons)]
    coefficients = Ints(" ".join(coefficients_str))
    opt = Optimize()
    target_joltage = machine[-1]
    current_target = 0
    for i, coefficient in enumerate(coefficients):
        opt.add(coefficient >= 0)
        current_target += coefficient

    for row in range(len(target_joltage)):
        left_side = 0
        for col in range(num_buttons):
            left_side += coefficients[col] * machine[col][row]

        right_side = target_joltage[row]
        opt.add(left_side == right_side)

    print(machine)
    opt.minimize(current_target)
    opt.check()
    model = opt.model()
    ans = model.evaluate(current_target).as_long()
    print(ans)
    total_presses += int(ans)

print(total_presses)
