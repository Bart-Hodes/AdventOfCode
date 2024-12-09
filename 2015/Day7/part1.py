with open("input.txt") as f:
    data = [line.strip("\n") for line in f.readlines()]

wires = {}
for instruction in data:
    print(instruction)
    if instruction[0].isdigit():
        operants = instruction.split("-> ")
        wires[operants[1]] = int(operants[0])
        continue
    if instruction.startswith("NOT"):
        operants = instruction[4:].split(" -> ")
        wires[operants[1]] = ~wires[operants[0]]
        continue
    if "AND" in instruction:
        operants = instruction.split(" -> ")
        operants[0] = operants[0].split(" AND ")
        wires[operants[1]] = wires[operants[0][0]] & wires[operants[0][1]]
        continue
    if "OR" in instruction:
        operants = instruction.split(" -> ")
        operants[0] = operants[0].split(" OR ")
        wires[operants[1]] = wires[operants[0][0]] | wires[operants[0][1]]
        continue
    if "LSHIFT" in instruction:
        operants = instruction.split(" -> ")
        operants[0] = operants[0].split(" LSHIFT ")
        wires[operants[1]] = wires[operants[0][0]] << int(operants[0][1])
        continue
    if "RSHIFT" in instruction:
        operants = instruction.split(" -> ")
        operants[0] = operants[0].split(" RSHIFT ")
        wires[operants[1]] = wires[operants[0][0]] >> int(operants[0][1])
        continue

print(wires)
for wire in wires:
    print(wire[0])
    if wires[wire] < 0:
        wires[wire] = 65536 + wires[wire]

print(wires)