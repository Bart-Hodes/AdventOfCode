def calculate_disconnected_sides_and_area(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pattern = [(0, 1), (1, 0), (1, 1), (2, 2)]
    patterns = [pattern]
    for _ in range(3):
        pattern = [(dy, -dx) for dx, dy in pattern]
        patterns.append(pattern)

    def flood_fill(x, y):
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
                    if grid[nx][ny] == char and not visited[nx][ny]:
                        for d1, d2, d3, d4 in patterns:
                            dx1, dy1 = d1
                            dx2, dy2 = d2
                            dx3, dy3 = d3
                            dx4, dy4 = d4
                            nx1, ny1, nx2, ny2, nx3, ny3, nx4, ny4 = (
                                nx + dx1,
                                ny + dy1,
                                nx + dx2,
                                ny + dy2,
                                nx + dx3,
                                ny + dy3,
                                nx + dx4,
                                ny + dy4,
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
                                ):
                                    if 0 <= nx4 < rows and 0 <= ny4 < cols:
                                        if grid[nx4][ny4] == char:
                                            print(d4)
                                            print("nx: ", nx, "ny: ", ny)
                                            print("nx1 ", nx1, "ny1 ", ny1)
                                            print("nx2 ", nx2, "ny2 ", ny2)
                                            print("nx3 ", nx3, "ny3 ", ny3)
                                            if d4 == (2, 2):
                                                sides += 4
                                                print("Inner sides", sides)
                                        else:
                                            sides += 2
                                            print("Outer sides", sides)
                    if not visited[nx][ny] and grid[nx][ny] == char:
                        area += 1
                        visited[nx][ny] = True
                        stack.append((nx, ny))
        print(sides, area)
        return sides, area

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                region_perimeter = flood_fill(i, j)
                # perimeters.append(
                #     (grid[i][j], region_perimeter[0] * region_perimeter[1])
                # )

    return None


data = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
data = data.split("\n")
calculate_disconnected_sides_and_area(data)
