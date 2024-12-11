from aocd import data
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
