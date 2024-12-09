with open("2015/Day6/input.txt") as f:
    data = [line.strip("\n") for line in f.readlines()]

grid = [[0 for i in range(1000)] for j in range(1000)]

for instruction in data:
    if instruction.startswith("turn on"):
        instruction = instruction[8:]
        instruction = instruction.replace(" through ", ",")
        instruction = instruction.split(",")
        x1, y1, x2, y2 = map(int, instruction)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = grid[i][j] + 1
    elif instruction.startswith("turn off"):
        instruction = instruction[9:]
        instruction = instruction.replace(" through ", ",")
        instruction = instruction.split(",")
        x1, y1, x2, y2 = map(int, instruction)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = max(0, grid[i][j] - 1)
    elif instruction.startswith("toggle"):
        instruction = instruction[7:]
        instruction = instruction.replace(" through ", ",")
        instruction = instruction.split(",")
        x1, y1, x2, y2 = map(int, instruction)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] =  grid[i][j] +2

print(sum([sum(row) for row in grid]))