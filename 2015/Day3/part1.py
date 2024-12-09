with open("input.txt") as f:
    data = [line.strip("\n") for line in f.readlines()]

for sequence in data:
    x = 0
    y = 0
    visited = set()
    visited.add((x, y))
    for char in sequence:
        if char == "^":
            y += 1
        elif char == "v":
            y -= 1
        elif char == ">":
            x += 1
        elif char == "<":
            x -= 1
        visited.add((x, y))
    print(len(visited))
