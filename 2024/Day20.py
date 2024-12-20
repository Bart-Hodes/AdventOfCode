from aocd.models import Puzzle

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

import time


def printMaze(walls, start, end, visited, cheatingSpot=None):
    time.sleep(0.5)
    print(cheatingSpot)
    print(start)
    for y in range(15):
        for x in range(15):
            if (x, y) == start:
                print("S", end="")
            elif (x, y) == end:
                print("E", end="")
            elif (x, y) == cheatingSpot:
                print("C", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif (x, y) in visited:
                print("X", end="")
            else:
                print(" ", end="")
        print()


def BFS(walls, start, end):

    visited = [start]
    pathLength = 0
    position = start

    queue = [(pathLength, position, visited)]

    while queue:
        pathLength, position, visited = queue.pop(0)

        # printMaze(walls, start, end, visited)

        if position == end:
            return visited

        for direction in directions:
            newPosition = (position[0] + direction[0], position[1] + direction[1])
            if newPosition in walls:
                continue
            if newPosition in visited:
                continue

            visited.append(newPosition)
            queue.append((pathLength + 1, newPosition, visited))

    return False


def part_a(data):
    maze = data.split("\n")

    walls = set()
    start = None
    end = None

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            if cell == "S":
                start = (x, y)
            if cell == "E":
                end = (x, y)

    nonCheatedPath = BFS(walls, start, end)

    shortcutLenght = {}

    for i in range(len(nonCheatedPath)):
        for j in range(i + 1, len(nonCheatedPath)):
            if (
                (abs(nonCheatedPath[j][0] - nonCheatedPath[i][0]) == 2)
                and (abs(nonCheatedPath[j][1] - nonCheatedPath[i][1]) == 0)
            ) ^ (
                (abs(nonCheatedPath[j][0] - nonCheatedPath[i][0]) == 0)
                and (abs(nonCheatedPath[j][1] - nonCheatedPath[i][1]) == 2)
            ):

                cheatingSpot = (
                    (nonCheatedPath[i][0] + nonCheatedPath[j][0]) // 2,
                    (nonCheatedPath[i][1] + nonCheatedPath[j][1]) // 2,
                )

                if cheatingSpot not in nonCheatedPath:
                    if (j - 1) - (i) - 1 not in shortcutLenght:
                        shortcutLenght[(j - 1) - (i) - 1] = 1
                    else:
                        shortcutLenght[(j - 1) - (i) - 1] += 1

    threshold = 100
    numberOfShortcuts = 0
    for key in shortcutLenght:
        if key >= threshold:
            numberOfShortcuts += shortcutLenght[key]
    return numberOfShortcuts


def part_b(data):
    maze = data.split("\n")

    walls = set()
    start = None
    end = None

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            if cell == "S":
                start = (x, y)
            if cell == "E":
                end = (x, y)

    nonCheatedPath = BFS(walls, start, end)

    shortcutPathLenght = {}
    maxCheatingLenght = 20

    for i in range(len(nonCheatedPath)):
        for j in range(i + 1, len(nonCheatedPath)):
            distance = abs(nonCheatedPath[j][0] - nonCheatedPath[i][0]) + abs(
                nonCheatedPath[j][1] - nonCheatedPath[i][1]
            )

            if 1 < distance <= maxCheatingLenght:
                # Check if we save time by cheating
                if distance < j - i:
                    shortcut_length = distance
                    if (j - i) - shortcut_length not in shortcutPathLenght:
                        shortcutPathLenght[(j) - (i) - shortcut_length] = 1
                    else:
                        shortcutPathLenght[(j) - (i) - shortcut_length] += 1

    threshold = 100
    numberOfShortcuts = 0
    for key in shortcutPathLenght:
        if key >= threshold:
            print(f"Shortcut of length {key} was used {shortcutPathLenght[key]} times")
            numberOfShortcuts += shortcutPathLenght[key]

    return numberOfShortcuts


if __name__ == "__main__":
    puzzle = Puzzle(2024, 20)
    # examples = puzzle.examples
    # for example in examples:
    # print(part_b(example.input_data))
    # puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
