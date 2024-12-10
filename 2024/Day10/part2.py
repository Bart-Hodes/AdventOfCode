with open("2024/Day10/input.txt", "r") as f:
    topography = [line.strip() for line in f.readlines()]


def findNumberOfTrails(topography, x, y):
    return findTrail(topography, x, y, 0, 0)


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def findTrail(topography, x, y, level, numberOfTrails):

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
                topography, x + d[0], y + d[1], level + 1, numberOfTrails
            )
    return numberOfTrails


totalNumberOfTrails = 0
for y, line in enumerate(topography):
    for x, char in enumerate(line):
        if char == "0":
            totalNumberOfTrails += findNumberOfTrails(topography, x, y)

print(totalNumberOfTrails)
