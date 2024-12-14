from aocd.models import Puzzle

import re


def debugPrintGuardLocations(guardLocations, rows, cols):
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    for x, y in guardLocations:
        if grid[y][x] == ".":
            grid[y][x] = 1
        else:
            grid[y][x] += 1

    for row in grid:
        for cell in row:
            print(cell, end="")
        print()


def part_a(data):

    rows = 103
    cols = 101

    matches = re.finditer(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", data)

    simulationTime = 100
    guardLocations = []
    for match in matches:
        x, y, dx, dy = map(int, match.groups())

        # Add position after 100 seconds
        guardLocations.append(
            ((x + simulationTime * dx) % cols, (y + simulationTime * dy) % rows)
        )

    # debugPrintGuardLocations(guardLocations)

    # Count robots in each quadrant
    quadrants = [0, 0, 0, 0]
    for x, y in guardLocations:
        if x < cols // 2 and y < rows // 2:
            quadrants[0] += 1
        elif x >= cols // 2 + 1 and y < rows // 2:
            quadrants[1] += 1
        elif x < cols // 2 and y >= rows // 2 + 1:
            quadrants[2] += 1
        elif x >= cols // 2 + 1 and y >= rows // 2 + 1:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part_b(data):

    rows = 103
    cols = 101

    matches = list(re.finditer(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", data))

    for simulationTime in range(9999999):
        guardLocations = []
        for match in matches:
            x, y, dx, dy = map(int, match.groups())

            guardLocations.append(
                ((x + simulationTime * dx) % cols, (y + simulationTime * dy) % rows)
            )

        if len(guardLocations) == len(set(guardLocations)):
            # debugPrintGuardLocations(guardLocations, rows, cols)
            break

    return simulationTime


if __name__ == "__main__":
    puzzle = Puzzle(2024, 14)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
