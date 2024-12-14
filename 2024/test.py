def count_regions_and_calculate_prices(map_data):
    def find_neighbors(x, y, map_data):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(map_data) and 0 <= ny < len(map_data[0]):
                neighbors.append((nx, ny))
        return neighbors

    def bfs_find_region(x, y, map_data):
        visited = set()
        queue = [(x, y)]
        while queue:
            cx, cy = queue.pop(0)
            if (cx, cy) not in visited and map_data[cx][cy] == current_region_type:
                visited.add((cx, cy))
                for nx, ny in find_neighbors(cx, cy, map_data):
                    if map_data[nx][ny] == current_region_type:
                        queue.append((nx, ny))
        return visited

    def calculate_perimeter(region):
        perimeter = 0
        for x, y in region:
            neighbors = find_neighbors(x, y, map_data)
            # Count the number of None or non-region neighbors (i.e., perimeter)
            for nx, ny in neighbors + [
                (None, None)
            ]:  # Add a dummy pair to handle len 0 or 1
                if nx is None or ny is None or (nx, ny) not in region:
                    perimeter += 1
        return perimeter

    def calculate_sides(region):
        sides = 0
        for x, y in region:
            neighbors = find_neighbors(x, y, map_data)
            # Count the number of None neighbors (i.e., sides)
            for nx, ny in neighbors + [
                (None, None)
            ]:  # Add a dummy pair to handle len 0 or 1
                if nx is None or ny is None:
                    sides += 1
        return sides

    regions = []
    visited_cells = set()
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if (i, j) not in visited_cells and map_data[i][
                j
            ] != " ":  # Assuming spaces are empty cells
                current_region_type = map_data[i][j]
                region = bfs_find_region(i, j, map_data)
                regions.append(region)
                visited_cells.update(region)

    total_price_part1 = 0
    total_price_part2 = 0

    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region)
        sides = calculate_sides(region)
        print(area, perimeter, sides)

        # Assuming price calculation based on some criteria (replace with actual logic)
        total_price_part1 += area * perimeter
        total_price_part2 += area * sides

    return total_price_part1, total_price_part2


# Example usage
map_data = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",
]

part1, part2 = count_regions_and_calculate_prices(map_data)
print(f"Part 1 total price: {part1}")
print(f"Part 2 total price: {part2}")
