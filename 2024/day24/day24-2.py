import math
import sys
from collections import deque
from copy import copy

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
            gates_queue.append([split_line[0], split_line[1], split_line[2], line.strip().split("-> ")[-1]])


"""I'm applying the rules of a full adder https://www.gsnetwork.com/wp-content/uploads/2023/01/full-adder-xor-gate-circuit-diagram.jpg

1. The sum of a full adder is XOR gate, so if there is a Z that doesn't come from an XOR gate it has been swapped. 
This is not true for the last digit of Z since that comes from the carry of the n-1 digit

2. If the 2 inputs to a gate are and X/Y wires, then it must go to a XOR/AND but not an OR gate
3. If the 2 inputs to a gate are not X/Y wires, and the output is not z, then it must go to an AND/OR but not XOR"""


LAST_Z_GATE = "z45"
swapped_gates_output = []

for in1, gate, in2, out in gates_queue:
    # rule 1
    if out.startswith("z") and gate != "XOR":
        if out != LAST_Z_GATE:
            print("rule 1 violated")
            swapped_gates_output.append(out)
    # rule 2
    # After running, this rule is never violated
    elif (
        (in1.startswith("x") and in2.startswith("y")) or (in1.startswith("y") and in2.startswith("x"))
    ) and gate == "OR":
        print("rule 2 violated")
        swapped_gates_output.append(out)
    # # rule 3
    elif not (in1[0] in ["x", "y"] or in2[0] in ["x", "y"]) and not out.startswith("z") and gate == "XOR":
        print("rule 3 violated")
        swapped_gates_output.append(out)


print(swapped_gates_output)

# I traversed non z swapped gates to the first z that it hits in the circut and
# Manually  made a map bc I couldn't get the recursive funciton to work
# Removing this to not post answers

# mqh -> z39
# tfb -> z28
# vvr -> z08
gates_to_swap = {"vvr": "z08", "tfb": "z28", "mqh": "z39", "z39": "mqh", "z28": "tfb", "z08": "vvr"}

for i in range(len(gates_queue)):
    in1, gate, in2, out = gates_queue[i]
    if out in gates_to_swap:
        print(f"swapping {gates_queue[i][-1]} with {gates_to_swap[out]}")
        gates_queue[i][-1] = gates_to_swap[out]


x_wires = [(wire, val) for wire, val in wires.items() if wire.startswith("x")]
x_wires.sort()
x_wires = x_wires[::-1]
x_number = "".join([str(val) for _, val in x_wires])

y_wires = [(wire, val) for wire, val in wires.items() if wire.startswith("y")]
y_wires.sort()
y_wires = x_wires[::-1]
y_number = "".join([str(val) for _, val in y_wires])


expected_z = int(bin(int(x_number, 2) + int(y_number, 2)), 2)
# expected_z_digits = list(expected_z)[2:]
# expected_z = int("".join(expected_z_digits), 2)


def actual_z(gates_queue):
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

    digits = [str(val) for _, val in z_wires]
    return int("".join(digits), 2)


# min_diff = float("inf")
# for i in range(len(gates_queue)):
#     for j in range(i, len(gates_queue)):
#         gates_queue[i][-1], gates_queue[j][-1] = gates_queue[j][-1], gates_queue[i][-1]
#         actual_z_after_swap = actual_z(copy(gates_queue))
#         min_diff = min(min_diff, abs(actual_z_after_swap - expected_z))
#         if actual_z_after_swap == expected_z:
#             swapped_gates = set(gates_to_swap.keys()).union(set([gates_queue[i][-1], gates_queue[j][-1]]))
#             print(",".join(sorted(swapped_gates)))
#             sys.exit()
#         gates_queue[i][-1], gates_queue[j][-1] = gates_queue[j][-1], gates_queue[i][-1]

# print("not found :(")
# print(min_diff)


print(bin(actual_z(gates_queue) ^ expected_z))
