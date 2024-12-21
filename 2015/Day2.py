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
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
