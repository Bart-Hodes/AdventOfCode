from aocd.models import Puzzle

import sys

sys.setrecursionlimit(10000)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def printMaze(walls, start, end, visited, cheatingSpot=None):
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


def parse_maze(maze):

    walls = set()
    start = None
    end = None

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            elif cell == "S":
                start = (x, y)
            elif cell == "E":
                end = (x, y)

    return maze, walls, start, end


def find_path(walls, start, end):
    path = [start]
    visited = set([start])

    # We know that there is only one path to the end
    def dfs(position):
        if position == end:
            return True

        for direction in directions:
            newPosition = (position[0] + direction[0], position[1] + direction[1])
            if newPosition not in walls and newPosition not in visited:
                visited.add(newPosition)
                path.append(newPosition)
                if dfs(newPosition):
                    return True
                path.pop()

        return False

    dfs(start)
    return path


def find_shortcuts(nonCheatedPath, max_cheating_length=20):
    shortcutLenght = {}

    for i in range(len(nonCheatedPath)):
        for j in range(i + 1, len(nonCheatedPath)):
            distance = abs(nonCheatedPath[j][0] - nonCheatedPath[i][0]) + abs(
                nonCheatedPath[j][1] - nonCheatedPath[i][1]
            )

            if 1 < distance <= max_cheating_length:
                # Check if we save time by cheating
                if distance < j - i:
                    shortcut_length = distance
                    key = (j) - (i) - shortcut_length
                    if key not in shortcutLenght:
                        shortcutLenght[key] = 0
                    shortcutLenght[key] += 1

    threshold = 100
    numberOfShortcuts = sum(
        count for key, count in shortcutLenght.items() if key >= threshold
    )

    return numberOfShortcuts


import time


def part_a(data):
    maze = data.split("\n")

    __, walls, start, end = parse_maze(maze)

    nonCheatedPath = find_path(walls, start, end)

    return find_shortcuts(nonCheatedPath, 2)


def part_b(data):
    maze = data.split("\n")

    __, walls, start, end = parse_maze(maze)

    nonCheatedPath = find_path(walls, start, end)

    return find_shortcuts(nonCheatedPath, 20)


if __name__ == "__main__":
    puzzle = Puzzle(2024, 20)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
