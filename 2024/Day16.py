from aocd.models import Puzzle

import time
import heapq


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


def findScoreDijkstra(start, end, orientation, walls):

    # Priority queue for Dijkstra's algorithm: (score, position, orientation)
    pq = [(0, start, orientation)]

    # Visited set to track visited positions and orientations
    visited = set()

    while pq:
        score, current, current_orientation = heapq.heappop(pq)

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
            heapq.heappush(pq, (score + 1, forward_pos, current_orientation))

        # Turn left
        left_orientation = (-dy, dx)
        left_pos = (x + left_orientation[0], y + left_orientation[1])
        if left_pos not in walls and (left_pos, left_orientation) not in visited:
            heapq.heappush(pq, (score + 1001, left_pos, left_orientation))

        # Turn right
        right_orientation = (dy, -dx)
        right_pos = (x + right_orientation[0], y + right_orientation[1])
        if right_pos not in walls and (right_pos, right_orientation) not in visited:
            heapq.heappush(pq, (score + 1001, right_pos, right_orientation))

    # If we exhaust the queue without finding the end, return infinity
    return float("inf")


def findScoreDijkstraPartB(start, end, orientation, walls):

    # Priority queue for Dijkstra's algorithm: (score, position, orientation)
    pq = [(0, start, orientation)]

    # Visited set to track visited positions and orientations
    visited = set()

    while pq:
        score, current, current_orientation = heapq.heappop(pq)
        printMaze(walls, current, end)

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
            heapq.heappush(pq, (score + 1, forward_pos, current_orientation))

        # Turn left
        left_orientation = (-dy, dx)
        left_pos = (x + left_orientation[0], y + left_orientation[1])
        if left_pos not in walls and (left_pos, left_orientation) not in visited:
            heapq.heappush(pq, (score + 1001, left_pos, left_orientation))

        # Turn right
        right_orientation = (dy, -dx)
        right_pos = (x + right_orientation[0], y + right_orientation[1])
        if right_pos not in walls and (right_pos, right_orientation) not in visited:
            heapq.heappush(pq, (score + 1001, right_pos, right_orientation))

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

    print(score)

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
    score = findScoreDijkstraPartB(start, end, orientation, walls)

    print(score)

    return score

    return None


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=16)
    # data = puzzle.input_data
    examples = puzzle.examples
    for example in examples:
        part_b(example.input_data)
    # print(part_a(data))
    # print(part_b(data))
    # puzzle.answer_a = part_a(puzzle.input_data)
