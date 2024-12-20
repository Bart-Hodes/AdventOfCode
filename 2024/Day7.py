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
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
