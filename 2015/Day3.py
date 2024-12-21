from aocd.models import Puzzle


def part_a(data):
    data = data.split("\n")

    for sequence in data:
        x = 0
        y = 0
        visited = set()
        visited.add((x, y))
        for char in sequence:
            if char == "^":
                y += 1
            elif char == "v":
                y -= 1
            elif char == ">":
                x += 1
            elif char == "<":
                x -= 1
            visited.add((x, y))
    return len(visited)


def part_b(data):
    data = data.split("\n")

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
    return len(visited)


if __name__ == "__main__":
    puzzle = Puzzle(2015, 3)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
