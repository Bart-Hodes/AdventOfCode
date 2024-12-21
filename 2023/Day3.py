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
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
