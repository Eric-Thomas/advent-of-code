from collections import deque

wires = {}

parsing_wires = True
gates = []
with open("inputs/day24-data.txt", "r") as fp:
    for line in fp:
        if line == "\n":
            parsing_wires = False
            continue
        if parsing_wires:
            wires[line.strip().split(":")[0]] = int(line.strip()[-1])
        else:
            split_line = line.split()
            gates.append((split_line[0], split_line[1], split_line[2], line.strip().split("-> ")[-1]))


queue = deque()
for in1, gate, in2, out in gates:
    try:
        if gate == "AND":
            wires[out] = int(wires[in1] and wires[in2])
        elif gate == "OR":
            wires[out] = int(wires[in1] or wires[in2])
        elif gate == "XOR":
            wires[out] = int(wires[in1] != wires[in2])
    except KeyError:
        queue.append((in1, gate, in2, out))

while len(queue) > 0:
    in1, gate, in2, out = queue.popleft()
    try:
        if gate == "AND":
            wires[out] = int(wires[in1] and wires[in2])
        elif gate == "OR":
            wires[out] = int(wires[in1] or wires[in2])
        elif gate == "XOR":
            wires[out] = int(wires[in1] != wires[in2])
    except KeyError:
        queue.append((in1, gate, in2, out))

z_wires = [(wire, val) for wire, val in wires.items() if wire.startswith("z")]
z_wires.sort()
z_wires = z_wires[::-1]

number = [str(val) for _, val in z_wires]
print(number)

print(int("".join(number), 2))
