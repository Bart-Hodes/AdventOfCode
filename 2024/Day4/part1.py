def checkIfValidXMAS(input, x, y):
    directions = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]

    subcount = 0
    for d in directions:
        if checkDir(input, x, y, d):
            subcount += 1
            print(f"Found a valid XMAS at {x}, {y} in direction {d}")
    return subcount


def checkDir(input, x, y, d):
    for letter in ["M", "A", "S"]:
        x += d[0]
        y += d[1]

        if x < 0 or y < 0 or x >= len(input[0]) or y >= len(input):
            return False
        if input[y][x] != letter:
            return False
    return True


with open("input.txt", "r") as f:
    input = []
    for line in f:
        input.append(line.strip("\n"))

# Search for X
# Search around X for M
# Keep looking in that direction for A and S

count = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "X":
            count += checkIfValidXMAS(input, x, y)
print(count)
