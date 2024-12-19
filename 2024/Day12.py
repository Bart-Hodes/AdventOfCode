from aocd.models import Puzzle
from aocd import data


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def getLatticePoints(grid, char, start):
    latticePoints = set()
    visited = set()

    queue = [start]

    while queue:
        current = queue.pop(0)

        if current in visited:
            continue

        if grid[current[0]][current[1]] != char:
            continue

        i, j = current

        visited.add(current)

        latticePoints.append((i, j))
        latticePoints.append((i + 1, j))
        latticePoints.append((i, j + 1))
        latticePoints.append((i + 1, j + 1))
    return latticePoints


def calculate_disconnected_perimeters_and_area(grid):

    disconnected_perimeters = []
    disconnected_areas = []

    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                latticePoints = getLatticePoints(grid, "#", (i, j))
                visited.update(latticePoints)

    return disconnected_perimeters, disconnected_areas


def part_a(data):
    data = data.split("\n")


if __name__ == "__main__":
    puzzle = Puzzle(2024, 12)
    for example in puzzle.examples:
        print(part_a(example.input_data))
