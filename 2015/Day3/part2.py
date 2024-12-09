with open("2015/Day3/input.txt") as f:
    data = [line.strip("\n") for line in f.readlines()]

for sequence in data:
    xSanta = 0
    ySanta = 0
    xRobot = 0
    yRobot = 0
    visited = set()
    visited.add((xSanta, ySanta))
    for idx, char in enumerate(sequence):
        if char == "^":
            if idx % 2 == 0:
                ySanta += 1
            else:
                yRobot += 1
        if char == "v":
            if idx % 2 == 0:
                ySanta -= 1
            else:
                yRobot -= 1
        if char == ">":
            if idx % 2 == 0:
                xSanta += 1
            else:
                xRobot += 1
        if char == "<":
            if idx % 2 == 0:
                xSanta -= 1
            else:
                xRobot -= 1
        if idx % 2 == 0:
            visited.add((xSanta, ySanta))
        else:
            visited.add((xRobot, yRobot))
    print(len(visited))
