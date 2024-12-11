from aocd import data
from aocd.models import Puzzle


def part_a(data):
    data = data.split("\n")

    feetOfWrappingPaper = 0
    for input in data:
        dimensions = input.split("x")

        side1 = 2 * int(dimensions[0]) * int(dimensions[1])
        side2 = 2 * int(dimensions[1]) * int(dimensions[2])
        side3 = 2 * int(dimensions[2]) * int(dimensions[0])

        feetOfWrappingPaper += side1 + side2 + side3 + min(side1, side2, side3) // 2

    return feetOfWrappingPaper


def part_b(data):
    data = data.split("\n")

    feetOfRibbon = 0
    for input in data:
        dimensions = input.split("x")

        dimensions = [int(dimension) for dimension in dimensions]
        dimensions.sort()

        feetOfRibbon += (
            dimensions[0] * dimensions[1] * dimensions[2]
            + 2 * dimensions[0]
            + 2 * dimensions[1]
        )

    return feetOfRibbon


if __name__ == "__main__":
    puzzle = Puzzle(2015, 2)
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
