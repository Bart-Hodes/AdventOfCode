from aocd import data
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
