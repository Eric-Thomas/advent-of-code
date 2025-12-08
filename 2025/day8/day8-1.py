import math
import os
from collections import defaultdict

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day8-data.txt"
file_path = os.path.join(parent_dir, inputs)
with open(file_path, "r") as fp:
    boxes = [tuple(map(int, line.strip().split(","))) for line in fp.readlines()]

NUM_CONNECTIONS = 1000
connections = defaultdict(list)
for _ in range(NUM_CONNECTIONS):
    print(f"checking connection {_}")
    min_distance = float("inf")
    box1, box2 = None, None
    for i in range(len(boxes)):
        x1, y1, z1 = boxes[i]
        for j in range(i + 1, len(boxes)):
            # Checking both might not be necessary
            if boxes[i] in connections[boxes[j]] or boxes[j] in connections[boxes[i]]:
                continue
            x2, y2, z2 = boxes[j]
            distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))
            if distance < min_distance:
                min_distance = distance
                box1 = boxes[i]
                box2 = boxes[j]

    connections[box1].append(box2)
    connections[box2].append(box1)


def build_circuit(circuit: set, current_box: tuple):
    for box in connections[current_box]:
        if box not in circuit:
            circuit.add(box)
            build_circuit(circuit, box)


circuits: list[set] = []
for box in connections:
    already_added_to_circuit = False
    for circuit in circuits:
        if box in circuit:
            already_added_to_circuit = True
            break

    circuit = set()
    if not already_added_to_circuit:
        build_circuit(circuit, box)
        circuits.append(circuit)
circuits.sort(key=lambda x: len(x))
circuits.reverse()

total = 1
for i in range(3):
    print(len(circuits[i]))
    total *= len(circuits[i])
print(total)
