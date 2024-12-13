from aocd import data
from aocd.models import Puzzle

import math
import re


def part_a(data):
    lines = data.split("\n")

    count = 0
    adjecent = set()
    for row, line in enumerate(lines):
        for symbol in re.finditer(r"[^\d\.\n]", line):
            col = symbol.start()
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    adjecent.add((r, c))

    for row, line in enumerate(lines):
        for number in re.finditer(r"\d+", line):
            span = number.span()
            for c in range(*span):
                if (row, c) in adjecent:
                    count += int(number.group())
                    break

    return count


def part_b(data):
    lines = data.split("\n")

    count = 0
    gears = {}
    for row, line in enumerate(lines):
        for symbol in re.finditer(r"\*", line):
            col = symbol.start()
            gears[(row, col)] = []

    for row, line in enumerate(lines):
        for num in re.finditer(r"\d+", line):
            for r in range(row - 1, row + 2):
                for c in range(num.start() - 1, num.end() + 1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(num.group()))

    for g, nums in gears.items():
        if len(nums) == 2:
            count += math.prod(nums)

    return count


if __name__ == "__main__":
    puzzle = Puzzle(2023, 3)
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
