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
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
