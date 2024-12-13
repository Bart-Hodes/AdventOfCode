from aocd.models import Puzzle
from aocd import data


def calculate_disconnected_perimeters_and_area(grid):
    # Convert the input string into a 2D grid
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    perimeters = []

    # Directions for neighbors (top, bottom, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def flood_fill(x, y):
        # Perform flood fill and calculate perimeter
        stack = [(x, y)]
        visited[x][y] = True
        char = grid[x][y]
        perimeter = 0
        area = 0

        while stack:
            cx, cy = stack.pop()
            area += 1
            interior_edges = 0

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == char:
                        interior_edges += 1

                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))

        perimeter = 2 * area - 2 * interior_edges + 2
        return perimeter, area

    # Iterate over the grid
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                # Start a new region
                region_perimeter = flood_fill(i, j)
                perimeters.append(
                    (grid[i][j], region_perimeter[0] * region_perimeter[1])
                )

    return perimeters


def calculate_disconnected_sides_and_area(grid):
    # Convert the input string into a 2D grid
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    perimeters = []

    # Directions for neighbors (top, bottom, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Search for pattern
    # AX
    # AA
    # In all orientations

    pattern = [(0, 1), (1, 0), (1, 1), (2, 2)]
    # Create all orientations of the pattern
    patterns = [pattern]
    for _ in range(3):
        pattern = [(dy, -dx) for dx, dy in pattern]
        patterns.append(pattern)

    def flood_fill(x, y):
        # Perform flood fill and calculate perimeter
        stack = [(x, y)]
        visited[x][y] = True
        char = grid[x][y]
        sides = 4
        area = 1

        while stack:
            cx, cy = stack.pop()

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == char:

                        # it breaks when it finds a pattern like
                        # AAA
                        # AXA
                        # AAA

                        # Check neighbors
                        for d1, d2, d3, d4 in patterns:
                            dx1, dy1 = d1
                            dx2, dy2 = d2
                            dx3, dy3 = d3
                            dx4, dy4 = d4
                            nx1, ny1, nx2, ny2, nx3, ny3, nx4, ny4 = (
                                cx + dx1,
                                cy + dy1,
                                cx + dx2,
                                cy + dy2,
                                cx + dx3,
                                cy + dy3,
                                cx + dx4,
                                cy + dy4,
                            )
                            if (
                                0 <= nx1 < rows
                                and 0 <= ny1 < cols
                                and 0 <= nx2 < rows
                                and 0 <= ny2 < cols
                                and 0 <= nx3 < rows
                                and 0 <= ny3 < cols
                            ):
                                if (
                                    grid[nx1][ny1] == char
                                    and grid[nx2][ny2] == char
                                    and grid[nx3][ny3] != char
                                    and not visited[nx][ny]
                                ):
                                    if 0 <= nx4 < rows and 0 <= ny4 < cols:
                                        if grid[nx4][ny4] == char:
                                            sides += 1
                                            print(f"nx: {nx}, ny: {ny}")
                                            print(d1, d2, d3, d4)
                                            print(
                                                grid[nx][ny],
                                                grid[nx1][ny1],
                                                grid[nx2][ny2],
                                                grid[nx3][ny3],
                                                grid[nx4][ny4],
                                            )
                                            print(
                                                nx,
                                                ny,
                                            )
                                            print(
                                                nx1,
                                                ny1,
                                            )
                                            print(
                                                nx2,
                                                ny2,
                                            )
                                            print(
                                                nx3,
                                                ny3,
                                            )
                                            print(
                                                nx4,
                                                ny4,
                                            )
                                        else:

                                            sides += 2
                                    else:
                                        sides += 2

                        if not visited[nx][ny]:
                            area += 1
                            visited[nx][ny] = True
                            stack.append((nx, ny))

        # print(f"area: {area}")
        # print(f"sides: {sides}")
        return sides, area

    # Iterate over the grid
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                # Start a new region
                region_perimeter = flood_fill(i, j)
                perimeters.append(
                    (grid[i][j], region_perimeter[0] * region_perimeter[1])
                )
                # print(visited)

    return perimeters


def part_a(data):

    data = data.split("\n")

    fenceLenght = 0
    for item in calculate_disconnected_perimeters_and_area(data):
        fenceLenght += item[1]

    return fenceLenght


# def part_b(data):

#     data = """OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO"""

#     data = data.split("\n")

#     fenceLenght = 0

#     for item in calculate_disconnected_sides_and_area(data):
#         fenceLenght += item[1]

#     print(fenceLenght)

#     return fenceLenght


if __name__ == "__main__":
    puzzle = Puzzle(2024, 12)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         if int(example.answer_a) != part_a(example.input_data):
    #             print("Example part A failed!")
    #             print(f"Expected: {example.answer_a}")
    #             print(f"Got: {part_a(example.input_data)}")
    # if example.answer_b:
    #     if int(example.answer_b) != part_b(example.input_data):
    #         print("Example part B failed!")
    #         print(f"Expected: {example.answer_b}")
    #         print(f"Got: {part_b(example.input_data)}")

    # part_a(data)
    part_b(data)
    # puzzle.answer_a = part_a(data)
    # puzzle.answer_b = part_b(data)
