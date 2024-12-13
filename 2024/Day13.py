from aocd import data
from aocd.models import Puzzle

import re


def part_a(data):
    games = re.finditer(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
        data,
    )

    tokens = 0
    for game in games:

        # Coefficients of the equations
        # Modify these as needed
        a1, b1, c1 = (
            int(game.group(1)),
            int(game.group(3)),
            int(game.group(5)),
        )  # First equation: a1*A + b1*B = c1
        a2, b2, c2 = (
            int(game.group(2)),
            int(game.group(4)),
            int(game.group(6)),
        )  # Second equation: a2*A + b2*B = c2

        # Calculate determinants
        det_main = a1 * b2 - a2 * b1
        if det_main == 0:
            raise ValueError("The system of equations has no unique solution.")

        # Determinants for A and B
        det_a = c1 * b2 - c2 * b1
        det_b = a1 * c2 - a2 * c1

        # Solutions
        A = det_a / det_main
        B = det_b / det_main

        # Only valid if A and B are integers
        if A.is_integer() and B.is_integer():
            tokens += 3 * A + B

    return int(tokens)


def part_b(data):

    games = re.finditer(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
        data,
    )

    tokens = 0
    for game in games:

        # Coefficients of the equations
        # Modify these as needed
        a1, b1, c1 = (
            int(game.group(1)),
            int(game.group(3)),
            int(game.group(5)) + 10000000000000,
        )  # First equation: a1*A + b1*B = c1
        a2, b2, c2 = (
            int(game.group(2)),
            int(game.group(4)),
            int(game.group(6)) + 10000000000000,
        )  # Second equation: a2*A + b2*B = c2

        # Calculate determinants
        det_main = a1 * b2 - a2 * b1
        if det_main == 0:
            raise ValueError("The system of equations has no unique solution.")

        # Determinants for A and B
        det_a = c1 * b2 - c2 * b1
        det_b = a1 * c2 - a2 * c1

        # Solutions
        A = det_a / det_main
        B = det_b / det_main

        # Only valid if A and B are integers
        if A.is_integer() and B.is_integer():
            tokens += 3 * A + B

    return int(tokens)


if __name__ == "__main__":
    puzzle = Puzzle(2024, 13)
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
