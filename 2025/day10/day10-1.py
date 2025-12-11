import os
from collections import deque

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day10-data.txt"
file_path = os.path.join(parent_dir, inputs)

with open(file_path, "r") as fp:
    machines = [line.strip().split() for line in fp.readlines()]

for machine in machines:
    indicator_lights_str = machine[0]
    indicator_lights_str = indicator_lights_str.replace("[", "")
    indicator_lights_str = indicator_lights_str.replace("]", "")
    indicator_lights = []
    for i in range(len(indicator_lights_str)):
        indicator_lights.append(indicator_lights_str[i] == "#")
    machine[0] = indicator_lights
    for i in range(1, len(machine) - 1):
        buttons_str = machine[i]
        buttons_str = buttons_str.replace("(", "")
        buttons_str = buttons_str.replace(")", "")
        buttons = tuple(map(int, buttons_str.split(",")))
        machine[i] = buttons


def bfs(current_lights, target_lights, buttons: set):
    queue = deque([(current_lights, set(), 0)])
    while len(queue) > 0:
        current_lights, visited, button_presses = queue.popleft()
        if current_lights == target_lights:
            return button_presses

        for button in buttons:
            # Pressing a button twice is the same as pressing it 0
            if button in visited:
                continue
            new_lights = current_lights.copy()
            new_visited = visited.copy()
            for light_index in button:
                new_lights[light_index] = not new_lights[light_index]
            new_visited.add(button)
            queue.append([new_lights, new_visited, button_presses + 1])


total = 0
for i in range(len(machines)):
    current = bfs([False for _ in range(len(machines[i][0]))], machines[i][0], machines[i][1:-1])
    total += current

print(total)
