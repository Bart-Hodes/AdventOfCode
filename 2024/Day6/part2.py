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


def loopDetector(obstacleList, pos, direction):
    visited = set()
    visited.add((pos, direction))
    while True:
        # Check if the next step is an obstacle
        nextStep = (pos[0] + direction[0], pos[1] + direction[1])

        if (
            nextStep[0] >= len(input[0])
            or nextStep[1] >= len(input)
            or nextStep[0] < 0
            or nextStep[1] < 0
        ):
            break

        if (nextStep, direction) in visited:
            # print("Loop detected")
            # debugPrint(input, pos, [x[0] for x in visited])
            return True

        if nextStep in obstacleList:
            # Turn right
            direction = (-direction[1], direction[0])
        else:
            pos = nextStep
            visited.add((pos, direction))
    # debugPrint(input, pos, [x[0] for x in visited])
    return False


def findGuardPath(input, pos, direction):
    visited = set()
    while True:
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

    return visited


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

# It only makes sense to check obstables placed in the guards path
guardPath = findGuardPath(input, pos, direction)

count = 0
previousPos = pos
# iterativly search the guards path for loops
for newObstacle in guardPath:
    obstacleListAppended = obstacleList.copy()
    obstacleListAppended.append(newObstacle)

    if loopDetector(obstacleListAppended, pos, direction):
        count += 1
    previousPos = newObstacle

print(count)
