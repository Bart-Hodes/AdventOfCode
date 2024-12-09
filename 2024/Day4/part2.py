def checkIfValidX_MAS(input, x, y):
    directions = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
    letters = []

    for direction in directions:
        if (
            x + direction[0] < 0
            or y + direction[1] < 0
            or x + direction[0] >= len(input[0])
            or y + direction[1] >= len(input)
        ):
            return False
        letters.append(input[y + direction[1]][x + direction[0]])
    if "".join(letters) not in ["MMSS", "MSSM", "SSMM", "SMMS"]:
        return False
    return True


with open("input.txt", "r") as f:
    input = []
    for line in f:
        input.append(line.strip("\n"))

count = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "A":
            count += checkIfValidX_MAS(input, x, y)
print(count)
