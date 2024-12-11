from aocd import data
from aocd.models import Puzzle


def part_a(data):
    data = data.split("\n")

    count = 0
    historianOneLocationList = []
    historianTwoLocationList = []
    for line in data:
        split = line.strip("\n").split("   ")

        historianOneLocationList.append(int(split[0]))
        historianTwoLocationList.append(int(split[1]))

    historianOneLocationList.sort()
    historianTwoLocationList.sort()

    for idx in range(len(historianOneLocationList)):
        count += abs(historianOneLocationList[idx] - historianTwoLocationList[idx])

    return count


def part_b(data):
    data = data.split("\n")

    count = 0
    historianOneLocationList = []
    historianTwoLocationList = []
    for line in data:
        split = line.strip("\n").split("   ")

        historianOneLocationList.append(int(split[0]))
        historianTwoLocationList.append(int(split[1]))

    for idx in range(len(historianOneLocationList)):
        multipier = historianTwoLocationList.count(historianOneLocationList[idx])
        count += multipier * historianOneLocationList[idx]
    return count


if __name__ == "__main__":
    puzzle = Puzzle(2024, 1)
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
