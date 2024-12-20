from aocd.models import Puzzle

import re


def part_a(data):
    data = data.split("\n")

    counter = 0
    for line in data:
        matches = re.finditer("mul\((\d{1,3},\d{1,3})\)", line)
        for match_obj in matches:
            values = match_obj.group(1).split(",")
            counter += int(values[0]) * int(values[1])

    return counter


def part_b(data):
    data = data.split("\n")

    counter = 0
    enable = True

    for line in data:
        matches = re.finditer("mul\((\d{1,3},\d{1,3})\)|do\(\)|don't\(\)", line)
        for match_obj in matches:
            if match_obj.group() == "do()":
                enable = True
                continue
            if match_obj.group() == "don't()":
                enable = False
                continue
            if enable:
                values = match_obj.group(1).split(",")
                counter += int(values[0]) * int(values[1])

    return counter


if __name__ == "__main__":
    puzzle = Puzzle(2024, 3)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
