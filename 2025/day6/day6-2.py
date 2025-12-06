import os

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day6-data.txt"
file_path = os.path.join(parent_dir, inputs)
with open(file_path, "r") as fp:
    lines = fp.readlines()

column_to_digits = []
operators = []
row = lines[-1]
operator = row[0]
column_length = 0
for i in range(1, len(row)):
    if row[i] in ["*", "+"] and column_length > 0:
        column_to_digits.append(column_length)
        operators.append(operator)
        operator = row[i]
        column_length = 0
    else:
        column_length += 1

# Input doesn't end on an operator so we have to add last grouping
# +1 for the column length because last char is EOF so we don't iterate on it
column_to_digits.append(column_length + 1)
operators.append(operator)

ROWS = len(lines)
total = 0
pointer = 0
for digits, operator in zip(column_to_digits, operators):
    current_total = 0
    for _ in range(digits):
        cephalopod_num = ""
        for row in range(ROWS):
            if lines[row][pointer].isdigit():
                cephalopod_num += lines[row][pointer]
        print(f"cephalopod num {cephalopod_num}")
        if current_total == 0:
            current_total = int(cephalopod_num)
        elif operator == "*":
            current_total *= int(cephalopod_num)
        elif operator == "+":
            current_total += int(cephalopod_num)
        else:
            raise ValueError()

        pointer += 1
    # Whitespace between each grouping of cephalopod numbers
    pointer += 1
    total += current_total

print(total)
