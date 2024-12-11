from aocd import data
from aocd.models import Puzzle


def findCycle(graph, start):
    visited = set()
    print(graph)
    while True:
        print(start)
        if start not in graph:
            return False
        if start in visited:
            print("Cycle detected")
            print(visited)
            return True
        visited.add(start)

        start = graph[start][0]


def loopDetector(obstacleList, pos, direction):
    visited = set()
    visited.add((pos, direction))
    while True:
        # Check if the next step is an obstacle
        nextStep = (pos[0] + direction[0], pos[1] + direction[1])

        if (
            nextStep[0] >= len(data[0])
            or nextStep[1] >= len(data)
            or nextStep[0] < 0
            or nextStep[1] < 0
        ):
            break

        if (nextStep, direction) in visited:
            return True

        if nextStep in obstacleList:
            direction = (-direction[1], direction[0])
        else:
            pos = nextStep
            visited.add((pos, direction))
    return False


def findGuardPath(data, pos, direction, obstacleList):
    visited = set()
    while True:
        # Check if the next step is an obstacle
        nextStep = (pos[0] + direction[0], pos[1] + direction[1])

        if (
            nextStep[0] >= len(data[0])
            or nextStep[1] >= len(data)
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


def part_a(data):
    data = data.split("\n")

    obstacleList = []
    start = None
    direction = None
    for y, line in enumerate(data):
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

    debugCount = 0
    visited = set()
    visited.add(pos)
    while True:
        debugCount += 1
        # Check if the next step is an obstacle
        nextStep = (pos[0] + direction[0], pos[1] + direction[1])

        if (
            nextStep[0] >= len(data[0])
            or nextStep[1] >= len(data)
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

    return len(visited)


def part_b(data):
    data = data.split("\n")

    obstacleList = []
    start = None
    direction = None
    for y, line in enumerate(data):
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
    guardPath = findGuardPath(data, pos, direction, obstacleList)

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


if __name__ == "__main__":
    puzzle = Puzzle(2024, 6)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         if int(example.answer_a) != part_a(example.input_data):
    #             print("Example part A failed!")
    #             print(f"Expected: {example.answer_a}")
    #             print(f"Got: {part_a(example.input_data)}")
    # if example.answer_b:
    #     if int(example.answer_b) != part_b(example.input_data):
    #         print("Example part B failed!")
    #         print(example)
    #         print(f"Expected: {example.answer_b}")
    #         print(f"Got: {part_b(example.input_data)}")
    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
