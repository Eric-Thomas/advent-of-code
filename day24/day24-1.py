from collections import deque

wires = {}

parsing_wires = True
gates_queue = deque()
with open("inputs/day24-data.txt", "r") as fp:
    for line in fp:
        if line == "\n":
            parsing_wires = False
            continue
        if parsing_wires:
            wires[line.strip().split(":")[0]] = int(line.strip()[-1])
        else:
            split_line = line.split()
            gates_queue.append((split_line[0], split_line[1], split_line[2], line.strip().split("-> ")[-1]))


while len(gates_queue) > 0:
    in1, gate, in2, out = gates_queue.popleft()
    try:
        if gate == "AND":
            wires[out] = int(wires[in1] and wires[in2])
        elif gate == "OR":
            wires[out] = int(wires[in1] or wires[in2])
        elif gate == "XOR":
            wires[out] = int(wires[in1] != wires[in2])
    except KeyError:
        gates_queue.append((in1, gate, in2, out))

z_wires = [(wire, val) for wire, val in wires.items() if wire.startswith("z")]
z_wires.sort()
z_wires = z_wires[::-1]

number = [str(val) for _, val in z_wires]

print(int("".join(number), 2))
