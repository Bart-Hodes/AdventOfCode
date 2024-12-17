from aocd.models import Puzzle

import time


def printMaze(walls, start, end):
    time.sleep(0.1)
    for y in range(15):
        for x in range(15):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) == start:
                print("S", end="")
            elif (x, y) == end:
                print("E", end="")
            else:
                print(".", end="")
        print("")
    print("")


def printPath(path, walls, start, end):
    time.sleep(0.1)
    for y in range(140):
        for x in range(140):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) == start:
                print("S", end="")
            elif (x, y) == end:
                print("E", end="")
            elif (x, y) in path:
                print("X", end="")
            else:
                print(".", end="")
        print("")
    print("")


def findScoreDijkstra(start, end, orientation, walls):
    # Priority queue for Dijkstra's algorithm: (score, position, orientation)
    priorityQueue = [(0, start, orientation)]

    # Visited set to track visited positions and orientations
    visited = set()

    while priorityQueue:
        # Sort the priority queue based on score (smallest first)
        priorityQueue.sort(key=lambda x: x[0])

        # Pop the element with the smallest score
        score, current, current_orientation = priorityQueue.pop(0)

        # If we reach the end, return the score
        if current == end:
            return score

        if (current, current_orientation) in visited:
            continue

        visited.add((current, current_orientation))

        x, y = current
        dx, dy = current_orientation

        # Move forward
        forward_pos = (x + dx, y + dy)
        if (
            forward_pos not in walls
            and (forward_pos, current_orientation) not in visited
        ):
            priorityQueue.append((score + 1, forward_pos, current_orientation))

        # Turn left
        left_orientation = (-dy, dx)
        left_pos = (x + left_orientation[0], y + left_orientation[1])
        if left_pos not in walls and (left_pos, left_orientation) not in visited:
            priorityQueue.append((score + 1001, left_pos, left_orientation))

        # Turn right
        right_orientation = (dy, -dx)
        right_pos = (x + right_orientation[0], y + right_orientation[1])
        if right_pos not in walls and (right_pos, right_orientation) not in visited:
            priorityQueue.append((score + 1001, right_pos, right_orientation))

    # If we exhaust the queue without finding the end, return infinity
    return float("inf")


def findScoreDijkstraWithPathTracking(start, end, orientation, walls):
    # Priority queue for Dijkstra's algorithm: (score, position, orientation)

    path = set()
    path.add(start)
    priorityQueue = [(0, start, orientation, path)]

    # Visited set to track visited positions and orientations
    visited = set()

    while priorityQueue:

        # Sort the priority queue based on score (smallest first)
        priorityQueue.sort(key=lambda x: x[0])

        # Pop the element with the smallest score
        score, current, current_orientation, path = priorityQueue.pop(0)

        # If the two lowest scores are the same, we have multiple paths to the end
        # We need to keep track of all of them so we merge them into one path
        if (
            priorityQueue
            and priorityQueue[0][0] == score
            and priorityQueue[0][1] == current
        ):
            path.update(priorityQueue[0][3])
            priorityQueue.pop(0)

        # If we reach the end, return the score
        if current == end:
            return path

        visited.add((current, current_orientation))

        x, y = current
        dx, dy = current_orientation

        # Move forward
        forward_pos = (x + dx, y + dy)
        if (
            forward_pos not in walls
            and (forward_pos, current_orientation) not in visited
        ):
            forwardPath = path.copy()
            forwardPath.add(forward_pos)
            priorityQueue.append(
                (score + 1, forward_pos, current_orientation, forwardPath)
            )

        # Turn left
        left_orientation = (-dy, dx)
        left_pos = (x + left_orientation[0], y + left_orientation[1])
        if left_pos not in walls and (left_pos, left_orientation) not in visited:
            leftPath = path.copy()
            leftPath.add(left_pos)
            priorityQueue.append((score + 1001, left_pos, left_orientation, leftPath))

        # Turn right
        right_orientation = (dy, -dx)
        right_pos = (x + right_orientation[0], y + right_orientation[1])
        if right_pos not in walls and (right_pos, right_orientation) not in visited:
            rightPath = path.copy()
            rightPath.add(right_pos)
            priorityQueue.append(
                (score + 1001, right_pos, right_orientation, rightPath)
            )

    # If we exhaust the queue without finding the end, return infinity
    return float("inf")


def part_a(data):

    data = data.split("\n")

    walls = set()
    start = None
    end = None

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            if cell == "S":
                start = (x, y)
            if cell == "E":
                end = (x, y)

    orientation = (1, 0)  # Initial orientation is to the right
    score = findScoreDijkstra(start, end, orientation, walls)

    # print(score)

    return score


def part_b(data):
    data = data.split("\n")

    walls = set()
    start = None
    end = None

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            if cell == "S":
                start = (x, y)
            if cell == "E":
                end = (x, y)

    orientation = (1, 0)  # Initial orientation is to the right
    path = findScoreDijkstraWithPathTracking(start, end, orientation, walls)

    # printPath(path, walls, start, end)

    return len(path)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=16)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
