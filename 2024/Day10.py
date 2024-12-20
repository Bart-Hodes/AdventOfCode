from aocd.models import Puzzle


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def findNumberOfTrails(topography, x, y):
    visited = set()
    return findTrail(topography, x, y, 0, 0, visited)


def findTrail(topography, x, y, level, numberOfTrails, visited):
    if (x, y) in visited:
        return numberOfTrails
    visited.add((x, y))

    if level == 9:
        return numberOfTrails + 1

    for d in directions:
        if (
            x + d[0] < 0
            or x + d[0] >= len(topography[0])
            or y + d[1] < 0
            or y + d[1] >= len(topography)
        ):
            continue

        if int(topography[y + d[1]][x + d[0]]) == level + 1:

            numberOfTrails = findTrail(
                topography, x + d[0], y + d[1], level + 1, numberOfTrails, visited
            )
    return numberOfTrails


def findTrailAllowMultiplePaths(topography, x, y, level, numberOfTrails, visited=set()):

    if level == 9:
        return numberOfTrails + 1

    for d in directions:
        if (
            x + d[0] < 0
            or x + d[0] >= len(topography[0])
            or y + d[1] < 0
            or y + d[1] >= len(topography)
        ):
            continue

        if int(topography[y + d[1]][x + d[0]]) == level + 1:
            numberOfTrails = findTrailAllowMultiplePaths(
                topography, x + d[0], y + d[1], level + 1, numberOfTrails
            )
    return numberOfTrails


def part_a(data):
    topography = data.split("\n")
    totalNumberOfTrails = 0
    for y, line in enumerate(topography):
        for x, char in enumerate(line):
            if char == "0":
                totalNumberOfTrails += findNumberOfTrails(topography, x, y)
    return totalNumberOfTrails


def part_b(data):
    topography = data.split("\n")
    totalNumberOfTrails = 0
    for y, line in enumerate(topography):
        for x, char in enumerate(line):
            if char == "0":
                totalNumberOfTrails += findTrailAllowMultiplePaths(
                    topography,
                    x,
                    y,
                    0,
                    0,
                )
    return totalNumberOfTrails


if __name__ == "__main__":
    puzzle = Puzzle(2024, 10)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
