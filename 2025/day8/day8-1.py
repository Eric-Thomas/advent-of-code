import heapq
import math
import os

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day8-data.txt"
file_path = os.path.join(parent_dir, inputs)
with open(file_path, "r") as fp:
    boxes = [tuple(map(int, line.strip().split(","))) for line in fp.readlines()]

NUM_CONNECTIONS = 1000
connection_distances = []
for i in range(len(boxes)):
    x1, y1, z1 = boxes[i]
    for j in range(i + 1, len(boxes)):
        x2, y2, z2 = boxes[j]
        distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))
        connection_distances.append((distance, (boxes[i], boxes[j])))

heapq.heapify(connection_distances)

circuits: list[set] = []
for i in range(NUM_CONNECTIONS):
    print(f"on iteration {i}")
    if circuits and len(circuits[0]) == len(boxes):
        print("All boxes in same circuit")
        print(box1[0] * box2[0])
        break

    distance, connected_boxes = heapq.heappop(connection_distances)
    # Union circuit of box1 (if exists) and circuit of box2 (if exists)
    box1, box2 = connected_boxes
    circuit1 = set([box1])
    circuit2 = set([box2])
    for i in range(len(circuits)):
        if box1 in circuits[i]:
            circuit1 = circuit1.union(circuits[i])
            circuits.pop(i)
            break

    for i in range(len(circuits)):
        if box2 in circuits[i]:
            circuit2 = circuit2.union(circuits[i])
            circuits.pop(i)
            break

    circuits.append(circuit1.union(circuit2))

circuits.sort(key=lambda x: len(x))
circuits.reverse()

total = 1
for i in range(3):
    print(len(circuits[i]))
    total *= len(circuits[i])
print(total)
