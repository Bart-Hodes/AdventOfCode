from aocd import data
from aocd.models import Puzzle


# TODO WORK OUT What exactly is happening in the code and make it more nice


def findCycle(graph, start):
    visited = set()
    while True:
        if start not in graph:
            return False
        if start in visited:
            return True
        visited.add(start)

        start = graph[start][0]


def loopDetector(obstacleList, pos, direction):
    visited = set()
    visited.add((pos, direction))
    while True:
        # Check if the next step is an obstacle
        nextStep = (pos[0] + direction[0], pos[1] + direction[1])

        if (
            nextStep[0] >= len(data[0])
            or nextStep[1] >= len(data)
            or nextStep[0] < 0
            or nextStep[1] < 0
        ):
            break

        if (nextStep, direction) in visited:
            return True

        if nextStep in obstacleList:
            direction = (-direction[1], direction[0])
        else:
            pos = nextStep
            visited.add((pos, direction))
    return False


def findGuardPath(data, pos, direction, obstacleList):
    visited = set()
    while True:
        # Check if the next step is an obstacle
        nextStep = (pos[0] + direction[0], pos[1] + direction[1])

        if (
            nextStep[0] >= len(data[0])
            or nextStep[1] >= len(data)
            or nextStep[0] < 0
            or nextStep[1] < 0
        ):
            break

        if nextStep in obstacleList:
            # Turn right
            direction = (-direction[1], direction[0])
        else:
            pos = nextStep
            visited.add(pos)

    return visited


def part_a(data):
    data = data.split("\n")

    obstacleList = []
    start = None
    direction = None
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                obstacleList.append((x, y))
            elif char == "^":
                start = (x, y)
                direction = (0, -1)
            elif char == "v":
                start = (x, y)
                direction = (0, 1)
            elif char == ">":
                start = (x, y)
                direction = (1, 0)
            elif char == "<":
                start = (x, y)
                direction = (-1, 0)

    pos = start

    debugCount = 0
    visited = set()
    visited.add(pos)
    while True:
        debugCount += 1
        # Check if the next step is an obstacle
        nextStep = (pos[0] + direction[0], pos[1] + direction[1])

        if (
            nextStep[0] >= len(data[0])
            or nextStep[1] >= len(data)
            or nextStep[0] < 0
            or nextStep[1] < 0
        ):
            break

        if nextStep in obstacleList:
            # Turn right
            direction = (-direction[1], direction[0])
        else:
            pos = nextStep
            visited.add(pos)

    return len(visited)


def parse_maze(data):
    # Split the input data into lines
    lines = data.split("\n")

    # Create a dictionary mapping each position (x, y) to its corresponding character
    maze = {(x, y): c for y, r in enumerate(lines) for x, c in enumerate(r.strip())}

    # Determine the width and height of the maze
    width, height = max((x + 1, y + 1) for x, y in maze.keys())

    # Find the starting position '^'
    start = next(k for k, v in maze.items() if v == "^")

    return maze, width, height, start


def find_loops(maze, width, height, start):

    # Initialize variables
    position, direction, guardPath = start, complex(0, -1), set()

    # Find the original path of the guard without extra obstacles
    while position in maze:
        guardPath.add(position)
        next_position = position[0] + direction.real, position[1] + direction.imag

        if maze.get(next_position) == "#":
            direction *= 1j
        else:
            position = next_position

    # Build the jump table for handling boundary conditions
    jump_table = {}
    for y in range(height):
        left_to_right = ((-1, y), 0)
        for x in range(width):
            if maze.get((x, y)) == "#":
                left_to_right = ((x + 1, y), 0)
            jump_table[(x, y, 3)] = left_to_right

        right_to_left = ((width, y), 2)
        for x in range(width - 1, -1, -1):
            if maze.get((x, y)) == "#":
                right_to_left = ((x - 1, y), 2)
            jump_table[(x, y, 1)] = right_to_left

    for x in range(width):
        top_to_bottom = ((x, -1), 1)
        for y in range(height):
            if maze.get((x, y)) == "#":
                top_to_bottom = ((x, y + 1), 1)
            jump_table[(x, y, 0)] = top_to_bottom

        bottom_to_top = ((x, height), 3)
        for y in range(height - 1, -1, -1):
            if maze.get((x, y)) == "#":
                bottom_to_top = ((x, y - 1), 3)
            jump_table[(x, y, 2)] = bottom_to_top

    # Count the number of cells that can act as a starting point for loops
    loop_count = 0
    for cell in guardPath:
        if maze[cell] != ".":
            continue

        position, direction, v = start, 0, set()

        while position in maze and (position, direction) not in v:
            v.add((position, direction))

            # Check if the current position is different from the target cell
            if position[0] != cell[0] and position[1] != cell[1]:
                position, direction = jump_table.get((*position, direction), (start, 0))
            else:
                next_position = (
                    position[0] + (0, 1, 0, -1)[direction],
                    position[1] + (-1, 0, 1, 0)[direction],
                )

                if maze.get(next_position) == "#" or next_position == cell:
                    direction = (direction + 1) % 4
                else:
                    position = next_position

        loop_count += (position, direction) in v
    return loop_count


def part_b(data):
    # Parse the maze and find the number of loops
    maze, width, height, start = parse_maze(data)
    result = find_loops(maze, width, height, start)
    return result


if __name__ == "__main__":
    puzzle = Puzzle(2024, 6)
    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
