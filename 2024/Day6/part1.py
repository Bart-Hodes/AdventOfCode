def debugPrint(input, pos, visited):
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if (x, y) == pos:
                print("Y", end="")
            elif (x, y) in visited:
                print("X", end="")
            else:
                print(char, end="")
        print()
    print("\n")


with open("input.txt", "r") as f:
    input = []
    for line in f:
        input.append(line.strip("\n"))


obstacleList = []
start = None
direction = None
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "#":
            obstacleList.append((x, y))
        elif char == "^":
            start = (x, y)
            direction = (0, -1)
        elif char == "v":
            start = (x, y)
            direction = (0, 1)
        elif char == ">":
            start = (x, y)
            direction = (1, 0)
        elif char == "<":
            start = (x, y)
            direction = (-1, 0)


pos = start
print(obstacleList)

debugCount = 0
visited = set()
visited.add(pos)
while True:
    debugCount += 1
    # Check if the next step is an obstacle
    nextStep = (pos[0] + direction[0], pos[1] + direction[1])

    if (
        nextStep[0] >= len(input[0])
        or nextStep[1] >= len(input)
        or nextStep[0] < 0
        or nextStep[1] < 0
    ):
        break

    if nextStep in obstacleList:
        # Turn right
        direction = (-direction[1], direction[0])
    else:
        pos = nextStep
        visited.add(pos)

debugPrint(input, pos, visited)

# print(visited)
print(len(visited))
