from aocd import data
from aocd.models import Puzzle

import itertools

operators = ["*", "+", "||"]


def part_a(data):
    lines = data.split("\n")

    count = 0
    for line in lines:
        contents = line.split(":")
        result = contents[0]
        values = contents[1].split(" ")[1:]

        permutations = list(itertools.product([0, 1], repeat=len(values) - 1))
        for perm in permutations:
            product = values[0]
            for idx in range(len(perm)):
                product = eval(f"{product} {operators[perm[idx]]} {values[idx+1]}")

            if int(product) == int(result):
                count += int(result)
                break

    return count


def part_b(data):
    lines = data.split("\n")

    count = 0
    for line in lines:
        contents = line.split(":")
        result = contents[0]
        values = contents[1].split(" ")[1:]

        permutations = list(itertools.product([0, 1, 2], repeat=len(values) - 1))
        for perm in permutations:
            workingSet = values.copy()
            product = workingSet[0]
            for idx in range(len(perm)):
                if perm[idx] == 0:
                    product = int(product) * int(workingSet[idx + 1])
                elif perm[idx] == 1:
                    product = int(product) + int(workingSet[idx + 1])
                elif perm[idx] == 2:
                    product = str(product) + workingSet[idx + 1]

            if int(product) == int(result):
                count += int(result)
                break

    return count


if __name__ == "__main__":
    puzzle = Puzzle(2024, 7)
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
