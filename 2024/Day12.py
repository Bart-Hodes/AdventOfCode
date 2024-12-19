from aocd.models import Puzzle


def conv1d(input, kernel):
    kernel_size = len(kernel)
    return [
        sum(input[i + j] * kernel[j] for j in range(kernel_size))
        for i in range(len(input) - kernel_size + 1)
    ]


def conv2d(input, kernel):
    kernel_height, kernel_width = len(kernel), len(kernel[0])
    return [
        [
            sum(
                input[i + k][j + l] * kernel[k][l]
                for l in range(kernel_width)
                for k in range(kernel_height)
            )
            for j in range(len(input[0]) - kernel_width + 1)
        ]
        for i in range(len(input) - kernel_height + 1)
    ]


def flood_fill_and_extract_area(grid, visited, x, y, target_value):
    stack = [(x, y)]
    region_coords = []
    min_x, max_x, min_y, max_y = x, x, y, y

    while stack:
        cx, cy = stack.pop()
        if (
            0 <= cx < len(grid)
            and 0 <= cy < len(grid[0])
            and grid[cx][cy] == target_value
            and not visited[cx][cy]
        ):
            visited[cx][cy] = True
            region_coords.append((cx, cy))
            min_x, max_x = min(min_x, cx), max(max_x, cx)
            min_y, max_y = min(min_y, cy), max(max_y, cy)
            stack.extend([(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)])

    # Extract the region with zero-padding
    region_height = max_x - min_x + 3  # +2 for padding, +1 for inclusive range
    region_width = max_y - min_y + 3
    extracted_region = [[0] * region_width for _ in range(region_height)]

    for rx, ry in region_coords:
        extracted_region[rx - min_x + 1][ry - min_y + 1] = 1

    return extracted_region, len(region_coords)


def calculate_perimeter(region, kernel):
    perimeter = 0

    # Horizontal edges
    for row in region:
        edges = conv1d(row, kernel)
        perimeter += sum(abs(edge) for edge in edges)

    # Vertical edges
    transposed_region = list(zip(*region))
    for row in transposed_region:
        edges = conv1d(row, kernel)
        perimeter += sum(abs(edge) for edge in edges)

    return perimeter


def calculate_sides(region, kernel):
    sides = 0

    # Horizontal edges
    corners = conv2d(region, kernel)

    sides += sum(sum(abs(corner) for corner in sublist) for sublist in corners)
    return sides


def part_a(data):
    lines = data.strip().split("\n")

    # Convert input lines to integers
    grid = [[ord(x) - 64 for x in line.strip()] for line in lines if line.strip()]
    grid_height, grid_width = len(grid), len(grid[0])

    visited = [[False] * grid_width for _ in range(grid_height)]
    unique_values = set(value for row in grid for value in row)

    kernel = [1, -1]
    total_count = 0

    for value in unique_values:
        for x in range(grid_height):
            for y in range(grid_width):
                if grid[x][y] == value and not visited[x][y]:
                    # Extract region and calculate area
                    region, area = flood_fill_and_extract_area(
                        grid, visited, x, y, value
                    )

                    # Calculate perimeter
                    perimeter = calculate_perimeter(region, kernel)

                    # Update the total count
                    total_count += area * perimeter

    return str(total_count)


def part_b(data):
    lines = data.strip().split("\n")

    # Convert input lines to integers
    grid = [[ord(x) - 64 for x in line.strip()] for line in lines if line.strip()]
    grid_height, grid_width = len(grid), len(grid[0])

    visited = [[False] * grid_width for _ in range(grid_height)]
    unique_values = set(value for row in grid for value in row)

    kernel = [[-1, 1], [1, -1]]
    total_count = 0

    for value in unique_values:
        for x in range(grid_height):
            for y in range(grid_width):
                if grid[x][y] == value and not visited[x][y]:
                    # Extract region and calculate area
                    region, area = flood_fill_and_extract_area(
                        grid, visited, x, y, value
                    )

                    # Calculate perimeter
                    sides = calculate_sides(region, kernel)

                    # Update the total count
                    total_count += area * sides

    return str(total_count)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=12)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
