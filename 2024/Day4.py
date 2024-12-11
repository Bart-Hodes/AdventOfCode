from aocd import data
from aocd.models import Puzzle


def checkIfValidXMAS(input, x, y):
    directions = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]

    subcount = 0
    for d in directions:
        if checkDir(input, x, y, d):
            subcount += 1
    return subcount


def checkDir(input, x, y, d):
    for letter in ["M", "A", "S"]:
        x += d[0]
        y += d[1]

        if x < 0 or y < 0 or x >= len(input[0]) or y >= len(input):
            return False
        if input[y][x] != letter:
            return False
    return True


def checkIfValidX_MAS(input, x, y):
    directions = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
    letters = []

    for direction in directions:
        if (
            x + direction[0] < 0
            or y + direction[1] < 0
            or x + direction[0] >= len(input[0])
            or y + direction[1] >= len(input)
        ):
            return False
        letters.append(input[y + direction[1]][x + direction[0]])
    if "".join(letters) not in ["MMSS", "MSSM", "SSMM", "SMMS"]:
        return False
    return True


def part_a(data):
    data = data.split("\n")

    # Search for X
    # Search around X for M
    # Keep looking in that direction for A and S

    count = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "X":
                count += checkIfValidXMAS(data, x, y)
    return count


def part_b(data):
    data = data.split("\n")

    count = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "A":
                count += checkIfValidX_MAS(data, x, y)
    return count


if __name__ == "__main__":
    puzzle = Puzzle(2024, 4)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         if int(example.answer_a) != part_a(example.input_data):
    #             print("Example part A failed!")
    #             print(f"Expected: {example.answer_a}")
    #             print(f"Got: {part_a(example.input_data)}")
    # if example.answer_b:
    #     if int(example.answer_b) != part_b(example.input_data):
    #         print("Example part B failed!")
    #         print(example)
    #         print(f"Expected: {example.answer_b}")
    #         print(f"Got: {part_b(example.input_data)}")
    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
