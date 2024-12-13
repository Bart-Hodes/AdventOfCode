from aocd.models import Puzzle


def findCycle(graph, start):
    visited = set()
    print(graph)
    while True:
        print(start)
        if start not in graph:
            return False
        if start in visited:
            print("Cycle detected")
            print(visited)
            return True
        visited.add(start)

        start = graph[start][0]


# Initialize variables
puzzle = Puzzle(2024, 6)
data = puzzle.input_data
obstacleList = set()
start = None
directions = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}

input = data.split("\n")

# Parse the input to find obstacles and start position with direction
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "#":
            obstacleList.add((x, y))
        elif char in directions:
            start = (x, y)
            direction = directions[char]

# Initialize the graph
graph = {}

# Add edges for these positions based on the direction of movement
for x1, y1 in obstacleList:
    # print(f"Checking for position {(x1, y1), dx1, dy1}")
    for x2, y2 in obstacleList:
        if (x1, y1) == (x2, y2):
            continue
        for dx1, dy1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # Check if the two positions are adjacent
            if dx1 == 1:
                if x1 + dx1 == x2 and y1 > y2:
                    graph[(x1 + dx1, y1)] = []
                    graph[(x1 + dx1, y1)].append((x2, y2 + 1))
            elif dx1 == -1:
                if x1 + dx1 == x2 and y1 < y2:
                    graph[(x1 + dx1, y1)] = []
                    graph[(x1 + dx1, y1)].append((x2, y2 - 1))
            elif dy1 == 1:
                if y1 + dy1 == y2 and x1 < x2:
                    graph[(x1, y1 + dy1)] = []
                    graph[(x1, y1 + dy1)].append((x2 - 1, y2))
            elif dy1 == -1:
                if y1 + dy1 == y2 and x1 > x2:
                    graph[(x1, y1 + dy1)] = []
                    graph[(x1, y1 + dy1)].append((x2 + 1, y2))


# Print the graph to verify
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")

print(len(obstacleList))
print(len(graph))

print(findCycle(graph, (4, 1)))
