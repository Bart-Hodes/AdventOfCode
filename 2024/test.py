def calculate_correct_sides(grid):
    # Convert the input string into a 2D grid
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    sides = []

    # Directions for neighbors (top, bottom, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def flood_fill(x, y):
        # Perform flood fill and calculate the perimeter correctly
        stack = [(x, y)]
        visited[x][y] = True
        char = grid[x][y]
        perimeter = 0

        while stack:
            cx, cy = stack.pop()

            # Check neighbors
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != char:
                    # Edge of the grid or neighboring cell is different
                    perimeter += 1
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

        return perimeter

    # Iterate over the grid
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                # Start a new field and calculate its perimeter
                field_sides = flood_fill(i, j)
                sides.append((grid[i][j], field_sides))

    return sides


# Example input
data = """AAAA
BBCD
BBCC
EEEC"""

# Convert input to a grid
grid = [list(row) for row in data.splitlines()]

# Calculate sides for each field
result = calculate_correct_sides(grid)

# Print results
for char, sides in result:
    print(f"Field '{char}' has {sides} sides")
