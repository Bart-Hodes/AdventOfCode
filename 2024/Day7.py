from aocd.models import Puzzle

import itertools

operators = ["*", "+", "||"]


def PlaceOperator(values, result, concat=False):
    *values, last = values

    if result < 0:
        return False

    if not values:
        return last == result

    quotient, remainder = divmod(result, last)

    if remainder == 0 and PlaceOperator(values, quotient, concat):
        return True

    prefix = str(result)[: -len(str(last))]
    if (
        concat
        and str(result).endswith(str(last))
        and prefix != ""
        and PlaceOperator(values, int(prefix), concat)
    ):
        return True

    return PlaceOperator(values, result - last, concat)


def part_a(data):
    lines = data.split("\n")

    count = 0
    for line in lines:
        contents = line.split(":")
        result = contents[0]
        values = contents[1].strip().split(" ")
        values = [int(x) for x in values]

        if PlaceOperator(values, int(result)):
            count += int(result)

    return count


def part_b(data):
    lines = data.split("\n")

    count = 0
    for line in lines:
        contents = line.split(":")
        result = contents[0]
        values = contents[1].strip().split(" ")
        values = [int(x) for x in values]

        if PlaceOperator(values, int(result), concat=True):
            count += int(result)

    return count


if __name__ == "__main__":
    puzzle = Puzzle(2024, 7)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
