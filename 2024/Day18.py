from aocd.models import Puzzle


def printMaze(fallenBytes, bfsPath):
    for i in range(rows):
        for j in range(cols):
            if (i, j) in fallenBytes:
                print("X", end="")
            elif (i, j) in bfsPath:
                print("O", end="")
            else:
                print(".", end="")
        print()


def BFS(start, end, fallenBytes):
    # Return number of steps of the shortest path from start to end
    queue = []
    visited = set()

    score = 0
    queue.append((score, start))

    while queue:
        # printMaze(fallenBytes, visited)
        score, current = queue.pop(0)

        if current == end:
            return score

        if current in fallenBytes:
            continue

        if current in visited:
            continue

        visited.add(current)

        # Add the neighbors of the current node
        # Up
        if current[0] > 0:
            queue.append((score + 1, (current[0] - 1, current[1])))
        # Down
        if current[0] < cols - 1:
            queue.append((score + 1, (current[0] + 1, current[1])))
        # Left
        if current[1] > 0:
            queue.append((score + 1, (current[0], current[1] - 1)))
        # Right
        if current[1] < rows - 1:
            queue.append((score + 1, (current[0], current[1] + 1)))


def BFS_partB(start, end, fallenBytes):
    # Return number of steps of the shortest path from start to end
    queue = []
    visited = set()

    score = 0
    path = set()
    path.add(start)
    queue.append((score, start, path))

    while queue:
        score, current, path = queue.pop(0)

        if current == end:
            return path

        if current in fallenBytes:
            continue

        if current in visited:
            continue

        visited.add(current)

        # Add the neighbors of the current node
        # Up
        if current[0] > 0:
            upPath = path.copy()
            upPath.add((current[0] - 1, current[1]))
            queue.append((score + 1, (current[0] - 1, current[1]), upPath))
        # Down
        if current[0] < cols - 1:
            downPath = path.copy()
            downPath.add((current[0] + 1, current[1]))
            queue.append(
                (
                    score + 1,
                    (current[0] + 1, current[1]),
                    downPath,
                )
            )
        # Left
        if current[1] > 0:
            leftPath = path.copy()
            leftPath.add((current[0], current[1] - 1))
            queue.append(
                (
                    score + 1,
                    (current[0], current[1] - 1),
                    leftPath,
                )
            )
        # Right
        if current[1] < rows - 1:
            rightPath = path.copy()
            rightPath.add((current[0], current[1] + 1))
            queue.append(
                (
                    score + 1,
                    (current[0], current[1] + 1),
                    rightPath,
                )
            )

    return False


def part_a(data):
    byteLocations = data.split("\n")

    global rows, cols
    rows = 71
    cols = 71

    numberOfFallenBytes = 1024

    fallenBytes = set()

    for idx in range(numberOfFallenBytes):
        fallenBytesInstance = byteLocations[idx].split(",")
        fallenBytes.add((int(fallenBytesInstance[0]), int(fallenBytesInstance[1])))

    # We need to find the shortest path from top left to bottom right while avoiding fallen bytes

    start = (0, 0)
    end = (rows - 1, cols - 1)

    return BFS(start, end, fallenBytes)


def part_b(data):
    byteLocations = data.split("\n")

    global rows, cols
    rows = 71
    cols = 71

    fallenBytes = set()

    # Start adding falling bytes into the set of fallen bytes while checking if they are on the path. If they are check if there is still a valid path and update the path. Do this until there is no valid path.

    start = (0, 0)
    end = (rows - 1, cols - 1)

    path = BFS_partB(start, end, fallenBytes)

    for idx in range(len(byteLocations)):
        fallenBytesInstance = byteLocations[idx].split(",")
        fallenBytes.add((int(fallenBytesInstance[0]), int(fallenBytesInstance[1])))

        if (int(fallenBytesInstance[0]), int(fallenBytesInstance[1])) in path:
            path = BFS_partB(start, end, fallenBytes)
        if path == False:
            break

    return byteLocations[idx]


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=18)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
