from aocd.models import Puzzle

import re
import math


def part_a(data):
    data = data.split("\n")

    TimeMatch = re.finditer(r"(\d+)", data[0])
    DistanceMatch = re.finditer(r"(\d+)", data[1])

    recordList = []
    for time, distance in zip(TimeMatch, DistanceMatch):
        time = int(time.group())
        distance = int(distance.group())
        records = 0

        for i in range(time):
            distanceAttempt = i * (time - i)
            if distance < distanceAttempt:
                records += 1
        recordList.append(records)

    count = 1
    for val in recordList:
        count *= val
    return count


def part_b(data):
    data = data.split("\n")

    time = int(data[0][5:].replace(" ", ""))
    distance = int(data[1][9:].replace(" ", ""))

    # Given distance = (time - i) * i
    # distance = time * i - i^2
    # i^2 - time * i + distance = 0
    # i = (time +- sqrt(time^2 - 4 * distance)) / 2

    firstZero = (time + (time**2 - 4 * distance) ** 0.5) / 2
    secondZero = (time - (time**2 - 4 * distance) ** 0.5) / 2

    return math.floor(firstZero) - math.ceil(secondZero) + 1


if __name__ == "__main__":
    puzzle = Puzzle(2023, 6)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
