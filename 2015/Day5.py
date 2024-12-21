from aocd.models import Puzzle

import re


def part_a(data):
    data = data.split("\n")
    niceCounter = 0
    for string in data:
        match = re.findall("[aeiou]", string)
        if len(match) < 3:
            continue
        match = re.findall(r"(.)\1", string)
        if not match:
            continue
        match = re.findall(r"(ab|cd|pq|xy)", string)
        if match:
            continue
        niceCounter += 1
    return niceCounter


def part_b(data):
    data = data.split("\n")

    niceCounter = 0
    for string in data:
        match = re.findall(r"(.).\1", string)
        if not match:
            continue
        match = re.findall(r"(..).*\1", string)
        if not match:
            continue
        niceCounter += 1
    return niceCounter


if __name__ == "__main__":
    puzzle = Puzzle(2015, 5)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
