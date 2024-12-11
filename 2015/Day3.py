from aocd import data
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
    for example in puzzle.examples:
        if example.answer_a:
            if int(example.answer_a) != part_a(example.input_data):
                print("Example part A failed!")
                print(f"Expected: {example.answer_a}")
                print(f"Got: {part_a(example.input_data)}")
                exit()
        if example.answer_b:
            if int(example.answer_b) != part_b(example.input_data):
                print("Example part B failed!")
                print(f"Expected: {example.answer_b}")
                print(f"Got: {part_b(example.input_data)}")

    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
