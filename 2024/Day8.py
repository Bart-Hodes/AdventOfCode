from aocd import data
from aocd.models import Puzzle


def part_a(data):
    lines = data.split("\n")

    antennaDict = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                if char not in antennaDict:
                    antennaDict[char] = []
                antennaDict[char].append((x, y))

    rows = len(lines)
    cols = len(lines[0])

    antiNodes = set()

    for frequency in antennaDict:
        # print(f"{frequency}: {antennaDict[frequency]}")
        for idx, antenna1 in enumerate(antennaDict[frequency]):
            for antenna2 in antennaDict[frequency][idx + 1 :]:
                # print(f"Checking {antenna1} and {antenna2}")
                dx = antenna2[0] - antenna1[0]
                dy = antenna2[1] - antenna1[1]
                if (
                    antenna1[0] - dx >= 0
                    and antenna1[1] - dy >= 0
                    and antenna1[0] - dx < cols
                    and antenna1[1] - dy < rows
                ):
                    # print(f"Adding antinode at {(antenna1[0] - dx, antenna1[1] - dy)}")
                    antiNodes.add((antenna1[0] - dx, antenna1[1] - dy))
                if (
                    antenna2[0] + dx >= 0
                    and antenna2[1] + dy >= 0
                    and antenna2[0] + dx < cols
                    and antenna2[1] + dy < rows
                ):
                    # print(f"Adding antinode at {(antenna2[0] + dx, antenna2[1] + dy)}")
                    antiNodes.add((antenna2[0] + dx, antenna2[1] + dy))

    return len(antiNodes)


def part_b(data):
    lines = data.split("\n")

    antennaDict = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                if char not in antennaDict:
                    antennaDict[char] = []
                antennaDict[char].append((x, y))

    rows = len(lines)
    cols = len(lines[0])

    antiNodes = set()

    for frequency in antennaDict:
        # print(f"{frequency}: {antennaDict[frequency]}")
        for idx, antenna1 in enumerate(antennaDict[frequency]):
            for antenna2 in antennaDict[frequency][idx + 1 :]:
                # print(f"Checking {antenna1} and {antenna2}")
                dx = antenna2[0] - antenna1[0]
                dy = antenna2[1] - antenna1[1]

                if len(antennaDict[frequency]) > 2:
                    antiNodes.add(antenna1)
                    antiNodes.add(antenna2)
                while (
                    antenna1[0] - dx >= 0
                    and antenna1[1] - dy >= 0
                    and antenna1[0] - dx < cols
                    and antenna1[1] - dy < rows
                ):
                    # print(f"Adding antinode at {(antenna1[0] - dx, antenna1[1] - dy)}")
                    antiNodes.add((antenna1[0] - dx, antenna1[1] - dy))
                    dx += antenna2[0] - antenna1[0]
                    dy += antenna2[1] - antenna1[1]

                dx = antenna2[0] - antenna1[0]
                dy = antenna2[1] - antenna1[1]
                while (
                    antenna2[0] + dx >= 0
                    and antenna2[1] + dy >= 0
                    and antenna2[0] + dx < cols
                    and antenna2[1] + dy < rows
                ):
                    # print(f"Adding antinode at {(antenna2[0] + dx, antenna2[1] + dy)}")
                    antiNodes.add((antenna2[0] + dx, antenna2[1] + dy))
                    dx += antenna2[0] - antenna1[0]
                    dy += antenna2[1] - antenna1[1]

    # # print lines with antenna nodes
    # for y, line in enumerate(lines):
    #     for x, char in enumerate(line):
    #         if char != ".":
    #             print(char, end="")
    #         elif (x, y) in antiNodes:
    #             print("#", end="")
    #         else:
    #             print(char, end="")
    #     print()

    return len(antiNodes)


if __name__ == "__main__":
    puzzle = Puzzle(2024, 8)
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
